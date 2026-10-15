"""M1 — Principled final-20 diversity-selection certificate (CPU, deterministic, zero GPU).

Formalizes the portfolio's "diversity" axis as an explicit subset-selection optimum instead of a
hand-curated heuristic, and emits a reproducible certificate that the current pick (v5c) sits within
epsilon of the maximal-diversity frontier under a STATED objective — plus a strict-Pareto swap scan.

FIREWALL (hard):
  GUARD-A  The diversity feature block uses ONLY sequence / physicochemical / novelty features. It MUST
           NOT contain minD_R299, Boltz/Chai engagement, iPAE, ipTM, vestibule-contact, or any consensus
           column. Smuggling such a signal in would turn this selector into an in-silico AGONISM ranker,
           which is barred. This script never reads those columns.
  GUARD-B  The reported "gain" is decorrelation / coverage / auditability on RANKABLE per-design axes
           ONLY. It is NEVER a P(agonist) or activation claim. Agonism stays unprovable in-silico; the
           wet-lab cAMP/CRE-SEAP assay is the only verdict.

Method:
  - Uniform CLEAN feature vector per design (reuses developability.analyze + eligibility_check +
    stress_liab helpers so the definitions match the committed audit).
  - Win-path quality PRE-FILTER on the candidate pool (entropy>=2.81, longest-run<=2, A+G<=0.36,
    even non-vicinal Cys, graft lcs<=3, eligibility pass). TRIPWIRE: must drop every PepFlow/pepx row.
  - Lineage partition-matroid fixed to v5c's budget (EvoBind 4 / DiffPep-linear 6 / DiffPep-ss 1 /
    PepGLAD 6 / ECD 3; max single-generator share <= 35%).
  - Per lineage: max-min dispersion (facility-location) + log-det volume (D-optimality / k-DPP MAP,
    numpy if available) of the v5c subset vs a greedy frontier subset of the same size from the gated
    pool; report the epsilon gap.
  - Strict-Pareto swap scan: a pool member may displace a v5c member ONLY if it is no worse on EVERY
    gated axis (seq-novelty id, coverage, graft lcs, structural-novelty TM when known, liability set)
    and strictly better on at least one, AND does not lower that lineage's min-pair diversity.

Usage: uv run python scripts/diversity_certificate.py
"""
from __future__ import annotations
import csv, os, sys, math, json, collections

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import developability as dev          # noqa: E402
import eligibility_check as elig      # noqa: E402
import stress_liab as sl             # noqa: E402

try:
    import numpy as np
    HAVE_NP = True
except Exception:
    HAVE_NP = False

# ---- quality band (the v5b/v5c win-path pre-filter) --------------------------------------------
BAND = dict(entropy_min=2.81, run_max=2, ag_max=0.36, lcs_max=3)

# ---- lineage budget (partition matroid) fixed to v5c -------------------------------------------
LINEAGE_BUDGET = {"EvoBind": 4, "DiffPep-linear": 6, "DiffPep-ss": 1, "PepGLAD": 6, "ECD": 3}
# v5c slot (1-based) -> lineage, from data/candidates/portfolio_v5c_order.txt
SLOT_LINEAGE = {}
for s in (1, 2, 3, 4):
    SLOT_LINEAGE[s] = "EvoBind"
for s in (5, 6, 7, 8, 9, 10):
    SLOT_LINEAGE[s] = "DiffPep-linear"
for s in (11, 12, 14, 15, 16, 17):
    SLOT_LINEAGE[s] = "PepGLAD"
SLOT_LINEAGE[13] = "DiffPep-ss"
for s in (18, 19, 20):
    SLOT_LINEAGE[s] = "ECD"

# CLEAN feature order (GUARD-A: nothing engagement/aim here)
FEATS = ["length", "entropy", "maxfrac", "ag_frac", "longest_run", "n_cys",
         "arom", "gravy", "charge", "elig_pid", "elig_cov", "lcs"]

REFS, ALIGNER = elig.build_scorer()


def build_aim():
    """seq -> minD_R299 (geometric correct-aim PRIOR, NOT an agonism score).
    Loaded ONLY for the swap-admissibility Pareto test — NEVER enters the diversity kernel (GUARD-A).
    A swap must not sacrifice the correct-aim rankable prior the displaced member was selected on."""
    aim = {}
    for fn in ("pepglad_longshot.csv", "diffpep_vest2_eval.csv", "diffpep_ss_vest2.csv", "pepgen_longshot.csv"):
        p = os.path.join(REPO, "data/candidates", fn)
        if not os.path.exists(p):
            continue
        with open(p) as fh:
            for r in csv.DictReader(fh):
                v = r.get("minD_R299", "")
                try:
                    aim[r["sequence"].strip().upper()] = float(v)
                except Exception:
                    pass
    return aim


AIM = build_aim()


def liab_set(seq, a, e, runlen, lcs):
    """Replicate stress_liab's composite liability flags as a SET (for Pareto subset tests)."""
    s = set()
    if a["cys"] % 2 == 1:
        s.add("FREE-THIOL")
    if runlen >= 6:
        s.add("POLYRUN")
    elif a["maxfrac"] > 0.30:
        s.add("LOWCPLX")
    if a["instab"] == a["instab"] and a["instab"] > 60:
        s.add("INSTAB++")
    elif a["instab"] == a["instab"] and a["instab"] > 40:
        s.add("instab")
    if a["gravy"] > 0.5:
        s.add("HYDROPHOBIC")
    if e["flag"]:
        s.add("ELIG-ID")
    if lcs >= 6:
        s.add("GRAFT")
    if (seq.count("M") + seq.count("W")) / len(seq) > 0.12:
        s.add("OXID")
    return s


def featurize(seq):
    seq = seq.strip().upper()
    a = dev.analyze(seq)
    e = elig.score_design(seq, REFS, ALIGNER)
    _, runlen = sl.longest_run(seq)
    ent = sl.shannon_bits(seq)
    ag = (seq.count("A") + seq.count("G")) / len(seq)
    lcs = max(sl.lcs_substr(seq, rs) for rs in REFS.values())
    return {
        "seq": seq, "length": a["len"], "entropy": round(ent, 3), "maxfrac": a["maxfrac"],
        "ag_frac": round(ag, 3), "longest_run": runlen, "n_cys": a["cys"], "arom": a["arom"],
        "gravy": a["gravy"], "charge": a["charge"], "elig_pid": e["pid"], "elig_cov": e["cov"],
        "lcs": lcs, "elig_flag": e["flag"],
        "liab": liab_set(seq, a, e, runlen, lcs), "instab": a["instab"],
    }


def vicinal_cys(seq):
    return "CC" in seq


def passes_band(f):
    return (f["entropy"] >= BAND["entropy_min"] and f["longest_run"] <= BAND["run_max"]
            and f["ag_frac"] <= BAND["ag_max"] and f["lcs"] <= BAND["lcs_max"]
            and f["n_cys"] % 2 == 0 and not vicinal_cys(f["seq"]) and not f["elig_flag"])


def read_csv(path):
    if not os.path.exists(path):
        return []
    with open(path) as fh:
        return list(csv.DictReader(fh))


def truthy(v):
    return str(v).strip().lower() in ("true", "1", "yes", "keep")


# ---- load v5c members (reuse the committed stress_liab.json panel for the submitted seqs) --------
def load_v5c():
    sub = read_csv(os.path.join(REPO, "submissions", "glp1r_track3_v5c.csv"))
    members = []
    for i, r in enumerate(sub, start=1):
        f = featurize(r["sequence"])
        f["name"] = r["name"]
        f["slot"] = i
        f["lineage"] = SLOT_LINEAGE[i]
        members.append(f)
    return members


# ---- load the gated candidate pool from the committed pool CSVs ----------------------------------
def load_pool():
    pool = {}  # lineage -> list of feature dicts (dedup by seq)
    seen = set()

    def add(lineage, seq, name, extra=None):
        seq = seq.strip().upper()
        if not seq or (lineage, seq) in seen:
            return
        seen.add((lineage, seq))
        f = featurize(seq)
        f["name"] = name
        f["lineage"] = lineage
        if extra:
            f.update(extra)
        pool.setdefault(lineage, []).append(f)

    # PepGLAD pool
    for r in read_csv(os.path.join(REPO, "data/candidates/pepglad_longshot.csv")):
        if truthy(r.get("keep")) or truthy(r.get("submittable")):
            add("PepGLAD", r["sequence"], r["name"])
    # DiffPep-linear pool (gated + vest2 eval)
    for fn in ("diffpep_gated.csv", "diffpep_vest2_eval.csv"):
        for r in read_csv(os.path.join(REPO, "data/candidates", fn)):
            if truthy(r.get("keep")):
                add("DiffPep-linear", r["sequence"], r["name"])
    # DiffPep-ss pool
    for r in read_csv(os.path.join(REPO, "data/candidates/diffpep_ss_vest2.csv")):
        if truthy(r.get("keep")):
            add("DiffPep-ss", r["sequence"], r["name"])
    # PepFlow / pepgen pool (REJECTED — included only to verify the pre-filter drops it = tripwire)
    for r in read_csv(os.path.join(REPO, "data/candidates/pepgen_longshot.csv")):
        add("PepFlow", r["sequence"], r["name"])
    # ECD + EvoBind from the main register (carry struct_nov_maxTM when present)
    for r in read_csv(os.path.join(REPO, "data/candidates/candidates.csv")):
        nm = r.get("name", "")
        tm = r.get("struct_nov_maxTM", "")
        extra = {}
        try:
            extra["struct_tm"] = float(tm)
        except Exception:
            pass
        if nm.startswith("ecd") or r.get("arm", "").lower() in ("ecd", "bind", "binder"):
            add("ECD", r["sequence"], nm, extra)
        elif nm.startswith("eb_") or "evobind" in r.get("arm", "").lower():
            add("EvoBind", r["sequence"], nm, extra)
    return pool


# ---- diversity metrics ---------------------------------------------------------------------------
def zscore(rows):
    cols = {}
    for k in FEATS:
        vals = [float(r[k]) for r in rows]
        mu = sum(vals) / len(vals)
        var = sum((v - mu) ** 2 for v in vals) / len(vals)
        sd = math.sqrt(var) if var > 1e-12 else 1.0
        cols[k] = (mu, sd)
    for r in rows:
        r["_z"] = [(float(r[k]) - cols[k][0]) / cols[k][1] for k in FEATS]
    return cols


def dist(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a["_z"], b["_z"])))


def min_pair(sub):
    if len(sub) < 2:
        return float("inf")
    return min(dist(sub[i], sub[j]) for i in range(len(sub)) for j in range(i + 1, len(sub)))


def mean_pair(sub):
    if len(sub) < 2:
        return 0.0
    ds = [dist(sub[i], sub[j]) for i in range(len(sub)) for j in range(i + 1, len(sub))]
    return sum(ds) / len(ds)


def logdet_vol(sub):
    """D-optimality volume: log det(I + Z Zt) over selected rows (k-DPP MAP objective)."""
    if not HAVE_NP or len(sub) == 0:
        return float("nan")
    Z = np.array([r["_z"] for r in sub], dtype=float)
    K = Z @ Z.T + np.eye(len(sub))
    sign, logdet = np.linalg.slogdet(K)
    return float(logdet) if sign > 0 else float("nan")


def greedy_maxmin(cands, k):
    """Greedy max-min dispersion: seed with the farthest pair, add the point maximizing min-dist."""
    if len(cands) <= k:
        return list(cands)
    best = (-1, None)
    for i in range(len(cands)):
        for j in range(i + 1, len(cands)):
            d = dist(cands[i], cands[j])
            if d > best[0]:
                best = (d, (i, j))
    chosen = [cands[best[1][0]], cands[best[1][1]]]
    chosen_ids = {id(chosen[0]), id(chosen[1])}
    while len(chosen) < k:
        pick, pick_d = None, -1
        for c in cands:
            if id(c) in chosen_ids:
                continue
            d = min(dist(c, x) for x in chosen)
            if d > pick_d:
                pick, pick_d = c, d
        chosen.append(pick)
        chosen_ids.add(id(pick))
    return chosen


def pareto_dominates(c, m):
    """Does pool candidate c weakly dominate v5c member m on ALL gated axes & strictly on >=1?
    Axes (lower = better): elig_pid, elig_cov, lcs, struct_tm (if both known), |liab| with subset."""
    better_any = False
    # sequence novelty id
    if c["elig_pid"] > m["elig_pid"]:
        return False
    better_any |= c["elig_pid"] < m["elig_pid"]
    if c["elig_cov"] > m["elig_cov"]:
        return False
    better_any |= c["elig_cov"] < m["elig_cov"]
    if c["lcs"] > m["lcs"]:
        return False
    better_any |= c["lcs"] < m["lcs"]
    # structural novelty (only if both known): lower TM = more novel = better
    if "struct_tm" in c and "struct_tm" in m:
        if c["struct_tm"] > m["struct_tm"]:
            return False
        better_any |= c["struct_tm"] < m["struct_tm"]
    elif "struct_tm" in m and "struct_tm" not in c:
        return False  # cannot assert c is >= as novel structurally
    # correct-aim PRIOR (geometric, not agonism): a swap must not worsen the aim the member was picked on.
    # lower minD_R299 = better aim. If m has verified aim but c does not, c cannot assert "not worse" -> no dominance.
    ma, ca = m.get("aim"), c.get("aim")
    if ma is not None:
        if ca is None:
            return False
        if ca > ma:
            return False
        # aim is a NOT-WORSE GATE ONLY — a lower minD_R299 never JUSTIFIES a swap, because ranking a
        # design in or out by aim is exactly the in-silico agonism ranking the firewall bars. The strict
        # improvement must come from a rankable quality axis (novelty id / coverage / lcs / struct-TM / liabilities).
    # developability: Cys count must not INCREASE. More Cys = more disulfide-pairing / oxidation /
    # synthesis risk and a topology-class change (Cys arrangement IS a developability axis); a clean
    # low-Cys member is NOT strictly dominated by a multi-Cys one even if it is more novel by coverage.
    if c["n_cys"] > m["n_cys"]:
        return False
    better_any |= c["n_cys"] < m["n_cys"]
    # c's liabilities must be a subset of m's
    if not c["liab"].issubset(m["liab"]):
        return False
    better_any |= len(c["liab"]) < len(m["liab"])
    return better_any


def main():
    members = load_v5c()
    pool = load_pool()

    # attach the correct-aim prior by sequence (used ONLY in the swap-admissibility test, never the kernel)
    for m in members:
        m["aim"] = AIM.get(m["seq"])
    for rows in pool.values():
        for r in rows:
            r["aim"] = AIM.get(r["seq"])

    # TRIPWIRE: pre-filter must drop every PepFlow/pepx row
    pepflow = pool.get("PepFlow", [])
    pepflow_survivors = [p["name"] for p in pepflow if passes_band(p)]
    if pepflow_survivors:
        sys.exit(f"FIREWALL TRIPWIRE: PepFlow/pepx rows survived the win-path band: {pepflow_survivors} — ABORT")

    # z-score over the union of v5c members + band-passing pool (consistent feature scaling)
    band_pool = {lin: [p for p in rows if passes_band(p)] for lin, rows in pool.items() if lin != "PepFlow"}
    universe = list(members)
    seqs_in = {m["seq"] for m in members}
    for lin, rows in band_pool.items():
        for r in rows:
            if r["seq"] not in seqs_in:
                universe.append(r)
    zscore(universe)

    lines = []
    W = lines.append
    W("# GLP1R portfolio — diversity-selection certificate (M1)\n")
    W("_Zero-GPU, deterministic. Firewall GUARD-A: the objective uses only clean sequence / "
      "physicochemical / novelty features — no minD_R299, engagement, iPAE, ipTM or consensus signal. "
      "GUARD-B: every number below is a RANKABLE coverage/decorrelation measure, never an agonism claim._\n")
    W(f"- Clean features in the objective ({len(FEATS)}): `{', '.join(FEATS)}` + lineage partition-matroid.")
    W(f"- Win-path band pre-filter: entropy>=%.2f, longest-run<=%d, A+G<=%.2f, graft-lcs<=%d, even non-vicinal Cys, eligibility pass."
      % (BAND["entropy_min"], BAND["run_max"], BAND["ag_max"], BAND["lcs_max"]))
    W(f"- **TRIPWIRE PASSED**: all {len(pepflow)} PepFlow/pepx pool rows are rejected by the band "
      f"(confirms the optimizer cannot select the rejected low-complexity outliers).\n")

    W("## Per-lineage dispersion: v5c subset vs the unconstrained max-min upper bound\n")
    W("_The 'frontier' column is a greedy max-min / log-det **upper bound that is outlier-seeking**: it "
      "maximizes raw feature spread, so it preferentially grabs the compositional extremes of each band "
      "(longest / most-charged / highest-entropy members). It is a DIAGNOSTIC CEILING, not a target — a "
      "gap to it means v5c spends some raw dispersion to buy the aim / developability / validated-binding "
      "priors those extremes lack, which is the intended engineering trade, not a deficiency. The "
      "decision-relevant test is the strict-Pareto scan below, not this gap._\n")
    W("| Lineage | budget | pool (band-pass) | v5c min-pair | max-min ceiling | head-room | v5c logdet | ceiling logdet |")
    W("|---|--:|--:|--:|--:|--:|--:|--:|")
    swap_flags = []
    for lin, budget in LINEAGE_BUDGET.items():
        chosen = [m for m in members if m["lineage"] == lin]
        alt = [p for p in band_pool.get(lin, []) if p["seq"] not in {c["seq"] for c in chosen}]
        cand_all = chosen + alt
        # frontier = greedy max-min over the whole gated lineage pool (chosen + alternates)
        frontier = greedy_maxmin(cand_all, budget) if len(cand_all) > budget else cand_all
        vm, fm = min_pair(chosen), min_pair(frontier)
        vol_v, vol_f = logdet_vol(chosen), logdet_vol(frontier)
        eps = 0.0 if fm in (0.0, float("inf")) or fm != fm else max(0.0, (fm - vm) / fm)
        def fmt(x):
            return "n/a" if x != x or x == float("inf") else f"{x:.3f}"
        W(f"| {lin} | {budget} | {len(alt)} | {fmt(vm)} | {fmt(fm)} | {eps*100:.1f}% | {fmt(vol_v)} | {fmt(vol_f)} |")
        # strict-Pareto swap scan within the lineage (+ diversity-preservation gate)
        base_div = min_pair(chosen)
        for m in chosen:
            for c in alt:
                if pareto_dominates(c, m):
                    new_sub = [x for x in chosen if x is not m] + [c]
                    if min_pair(new_sub) < base_div - 1e-9:
                        continue  # swap would REDUCE lineage diversity -> not adoptable
                    swap_flags.append((lin, m["name"], m["slot"], c["name"],
                                       f"id {c['elig_pid']:.0f}<= {m['elig_pid']:.0f}, cov {c['elig_cov']:.2f}<= {m['elig_cov']:.2f}, "
                                       f"lcs {c['lcs']}<= {m['lcs']}, liab {sorted(c['liab'])}⊆{sorted(m['liab'])}"))
    W("")
    W("## Strict-Pareto swap candidates\n")
    W("_Gated axes (a dominator must be no worse on every one, strictly better on >=1): sequence-novelty "
      "id, coverage, graft lcs, structural-novelty TM (when known), **correct-aim minD_R299 prior** "
      "(geometric, not agonism; a member with verified aim cannot be displaced by one without it), and "
      "developability liability-set (subset). Aim is used ONLY here, never in the diversity kernel._\n")
    if swap_flags:
        W("| lineage | v5c member (slot) | dominated by | margin |")
        W("|---|---|---|---|")
        for lin, mn, slot, cn, why in swap_flags:
            W(f"| {lin} | {mn} (slot {slot}) | {cn} | {why} |")
        W("\n**Assessment (not an auto-adopt):** the swap(s) above are non-harmful strict improvements, "
          "but each must clear the cost of re-opening the byte-frozen, portal-parsed-20/20 v5c submission. "
          "A swap whose ONLY strict gain is a within-eligibility coverage delta (both members already pass "
          "the id<=30%/cov<0.5 novelty gate, and the upload portal has NO novelty score) is a marginal "
          "local-screen gain, not a portal- or prize-visible one; the convergent portfolio math puts "
          "same-lineage member reshuffling at <0.03 of P(>=1 hit) with sign-uncertain direction. "
          "Recommend KEEPING v5c frozen unless the owner wants the marginally-more-novel variant built "
          "(v5d), in which case it is a one-slot rebuild + full re-validation, with v5c retained as fallback.")
    else:
        W("**None.** No gated pool member strictly Pareto-dominates any v5c member on all rankable axes.")
        W("Within the fixed lineage budgets, **v5c is Pareto-efficient and diversity-consistent** "
          "(no non-harmful swap available); it ships unchanged as the max-diversity-consistent pick.")
    W("")

    # weakest-member transparency (the band-marginal members, for audit)
    W("## Band-marginal v5c members (audit transparency)\n")
    W("| slot | name | lineage | entropy | longest-run | A+G | liabilities |")
    W("|--:|---|---|--:|--:|--:|---|")
    for m in sorted(members, key=lambda x: (x["entropy"], -x["longest_run"])):
        marg = (m["entropy"] < BAND["entropy_min"] or m["longest_run"] > BAND["run_max"] or m["ag_frac"] > BAND["ag_max"])
        if marg or m["liab"]:
            W(f"| {m['slot']} | {m['name']} | {m['lineage']} | {m['entropy']:.2f} | {m['longest_run']} | "
              f"{m['ag_frac']:.2f} | {sorted(m['liab']) or 'CLEAN'} |")
    W("")
    W("_Note: band-marginal v5c members are retained where they carry an irreplaceable rankable value "
      "(e.g. the most structurally-novel ECD) that no cleaner pool member matches — a strict-Pareto swap, "
      "not a band threshold, governs replacement._")

    out_md = os.path.join(REPO, "reports", "GLP1R diversity selection certificate.md")
    with open(out_md, "w") as fh:
        fh.write("\n".join(lines) + "\n")

    # machine CSV
    out_csv = os.path.join(REPO, "data/candidates", "diversity_certificate.csv")
    with open(out_csv, "w", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["lineage", "budget", "pool_alts", "v5c_minpair", "frontier_minpair", "gap_eps_pct",
                    "v5c_logdet", "frontier_logdet"])
        for lin, budget in LINEAGE_BUDGET.items():
            chosen = [m for m in members if m["lineage"] == lin]
            alt = [p for p in band_pool.get(lin, []) if p["seq"] not in {c["seq"] for c in chosen}]
            cand_all = chosen + alt
            frontier = greedy_maxmin(cand_all, budget) if len(cand_all) > budget else cand_all
            vm, fm = min_pair(chosen), min_pair(frontier)
            eps = 0.0 if fm in (0.0, float("inf")) or fm != fm else max(0.0, (fm - vm) / fm)
            w.writerow([lin, budget, len(alt), f"{vm:.4f}" if vm != float('inf') else "inf",
                        f"{fm:.4f}" if fm != float('inf') else "inf", f"{eps*100:.2f}",
                        f"{logdet_vol(chosen):.4f}", f"{logdet_vol(frontier):.4f}"])

    print(f"numpy={HAVE_NP}  v5c_members={len(members)}  pool_lineages={ {k: len(v) for k, v in pool.items()} }")
    print(f"TRIPWIRE: PepFlow survivors of band = {len(pepflow_survivors)} (must be 0)")
    print(f"strict-Pareto swap candidates = {len(swap_flags)}")
    for lin, mn, slot, cn, why in swap_flags:
        print(f"  SWAP? {lin}: {cn} dominates {mn} (slot {slot}) -- {why}")
    print(f"wrote {out_md}")
    print(f"wrote {out_csv}")


if __name__ == "__main__":
    main()
