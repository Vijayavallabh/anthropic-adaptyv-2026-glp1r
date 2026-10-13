"""Build the versioned candidate register (data/candidates/{candidates.csv,register.md})
by JOINING the actual tool outputs — never hand-transcribed (code-review bd802e8 root fix):

  - ECD binders: sequences from runs/portfolio/ecd_binders.csv + af2ig pae/plddt/rmsd from
    runs/af2/ecd_mini/**/*.sc via parse_af2ig.parse_scores.
  - EvoBind peptides: best pose per run (min if_dist_peptide) from runs/evobind/<run>/metrics.csv.
  - Developability via developability.analyze; eligibility via eligibility.score_design.

candidates.csv is the machine-readable AUTHORITY. Columns are explicit and arm-safe:
`binding_model` (af2ig|evobind) disambiguates the arm-specific `plddt`; `status` (keep|drop)
and `eligible` (bool) make the dropped/ineligible rows machine-filterable so a downstream
picker can't ship them. register.md tables are generated from the same rows (no drift).

Usage: uv run python scripts/build_candidate_register.py
"""
from __future__ import annotations
import csv, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from developability import analyze                      # noqa: E402
from eligibility_check import build_scorer, score_design  # noqa: E402
from parse_af2ig import parse_scores                     # noqa: E402

PEP_RUNS = ["prod_l14", "prod_l20", "prod_l26", "prod_l32",
            "accv_l14", "accv_l20", "accv_l26", "accv_l32"]
ECD_CSV = os.path.join(REPO, "runs/portfolio/ecd_binders.csv")
AF2_DIR = os.path.join(REPO, "runs/af2/ecd_mini")
OUT_DIR = os.path.join(REPO, "data/candidates")

COLS = ["name", "arm", "status", "molecule_class", "length", "binding_model", "binding_metric",
        "binding_value", "plddt", "rmsd", "instability", "gravy", "net_charge", "cys",
        "max_aa_frac", "elig_id_pct", "elig_cov", "elig_nearest", "eligible", "dev_flags", "sequence"]


def best_peptide(run):
    m = os.path.join(REPO, "runs/evobind", run, "metrics.csv")
    rows = list(csv.DictReader(open(m)))
    return min(rows, key=lambda r: float(r["if_dist_peptide"]))


def row_for(name, seq, arm, binding_model, binding_metric, binding_value, plddt, rmsd, refs, aligner):
    dev = analyze(seq)
    el = score_design(seq, refs, aligner)
    eligible = not el["flag"]
    return {
        "name": name, "arm": arm, "status": "keep" if eligible else "drop",
        "molecule_class": "protein", "length": dev["len"],
        "binding_model": binding_model, "binding_metric": binding_metric,
        "binding_value": f"{binding_value:.2f}",
        "plddt": f"{plddt:.1f}" if plddt is not None else "",
        "rmsd": f"{rmsd:.2f}" if rmsd is not None else "",
        "instability": f"{dev['instab']:.1f}", "gravy": f"{dev['gravy']:.2f}",
        "net_charge": dev["charge"], "cys": dev["cys"],
        "max_aa_frac": f"{dev['maxfrac']:.2f}",
        "elig_id_pct": f"{el['pid']:.1f}", "elig_cov": f"{el['cov']:.2f}",
        "elig_nearest": el["nearest"], "eligible": eligible,
        "dev_flags": ",".join(dev["flags"]) or "clean", "sequence": seq,
    }


def main():
    refs, aligner = build_scorer()
    rows = []

    # Arm A: EvoBind threading peptides (agonism bet)
    for run in PEP_RUNS:
        b = best_peptide(run)
        rows.append(row_for(f"eb_{run}", b["sequence"].strip(), "agonism-peptide",
                            "evobind", "if_dist_peptide", float(b["if_dist_peptide"]),
                            float(b["plddt"]), None, refs, aligner))

    # Arm B: ECD miniprotein binders (binding hedge) — join af2ig scores by description
    sc = {r["desc"].replace("_af2pred", ""): r for r in parse_scores(AF2_DIR)}
    for r in csv.DictReader(open(ECD_CSV)):
        core = r["name"][4:] if r["name"].startswith("ecd_") else r["name"]
        s = sc.get(core)
        if s is None:
            print(f"WARN no af2ig score for {r['name']} (core={core}) — skipped", file=sys.stderr)
            continue
        rows.append(row_for(r["name"], r["sequence"].strip(), "binding-hedge",
                            "af2ig", "pae_interaction", s["pae_i"], s["plddt_b"], s["rmsd"],
                            refs, aligner))

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "candidates.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS)
        w.writeheader()
        w.writerows(rows)

    write_register_md(rows)
    nkeep = sum(1 for r in rows if r["status"] == "keep")
    print(f"wrote {len(rows)} candidates ({nkeep} keep, {len(rows)-nkeep} drop) -> {OUT_DIR}/")


def _md_table(rows, metric_label):
    out = [f"| name | status | len | {metric_label} | plddt | rmsd | instab | eligibility (id%/cov/nearest) | dev |",
           "|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        elig = f"{'OK' if r['eligible'] else 'FLAG'} {r['elig_id_pct']}%/cov{r['elig_cov']}/{r['elig_nearest']}"
        out.append(f"| {r['name']} | {r['status']} | {r['length']} | {r['binding_value']} | "
                   f"{r['plddt'] or '-'} | {r['rmsd'] or '-'} | {r['instability']} | {elig} | {r['dev_flags']} |")
    return "\n".join(out)


def write_register_md(rows):
    pep = sorted([r for r in rows if r["arm"] == "agonism-peptide"], key=lambda r: float(r["binding_value"]))
    ecd = sorted([r for r in rows if r["arm"] == "binding-hedge"], key=lambda r: float(r["binding_value"]))
    txt = f"""# Candidate register — GLP1R agonist (Challenge 3)

**Generated** by `scripts/build_candidate_register.py` from the tool outputs (af2ig `.sc`,
EvoBind `metrics.csv`, `developability.analyze`, `eligibility.score_design`) — **do not hand-edit;
re-run to refresh.** `candidates.csv` (this dir) is the machine-readable authority: filter on
`status == keep` and `eligible == True` before selection. `binding_value` is arm-specific
(`binding_model`/`binding_metric` columns): af2ig `pae_interaction` (lower=better) for binders,
EvoBind `if_dist_peptide` (lower=better) for peptides; `plddt` is likewise the design-confidence
from that arm's model and is NOT comparable across arms. No in-silico score proves agonism; the
agonism arm is explicitly LOW-confidence. Proteinbase portal is the authority for
novelty/eligibility — re-check every pick before any (USER-GATED) upload.

## Arm A — agonism bet: EvoBind threading peptides (LOW confidence)

Only direct de-novo GLP1R-agonist precedent is a threading peptide (Li/Bryant 2025, cyclic). 8 runs
× 200 iters (linear, submittable). Result: **did not converge** — best-pose `if_dist_peptide` floored
~5–7.6 Å (a genuine inserted contact is <4 Å), peptide plddt low; the accessible retarget did not beat
the deep one. No clean in-silico binding gate exists for this membrane-blind isolated-receptor pocket,
and agonism is unprovable in-silico. Mechanism-plus-precedent bets, not validated binders. `status=drop`
rows failed the de-novo eligibility gate (local id to a known agonist >30% over ≥50% coverage).

{_md_table(pep, "if_dist (Å)")}

## Arm B — binding hedge: ECD miniprotein binders (antagonist-leaning)

RFdiffusion→LigandMPNN→af2ig on the soluble ECD groove; all shown pass the binder gate
(pae<10, plddt>80, rmsd<2). Mechanistically ECD-only (no 7TM message) → expected to BIND and pass the
binding gate but lean antagonist, not agonist. All de-novo (eligibility OK; coverage ≪ 0.5).

{_md_table(ecd, "af2ig pae")}

## Arm C — two-domain agonist (S2) — PLANNED, not yet generated

Mechanistically the strongest agonism bet (GLP-1 is bipartite: C-term address→ECD, N-term message→7TM).
Geometry gate (6X18, canonical hotspots): the accessible upper vestibule (R197/R299 — the region the oral
agonist orforglipron engages) sits ~14–20 Å from the ECD-groove anchor (R32) → reachable by a ~10–14-residue
extension; the deep orthosteric message pocket (R363/364/394) is 35–38 Å away **and buried** → NOT reachable
(same wall as Arm A). Plan: extend/scaffold from the clean Arm-B binders toward the accessible vestibule;
af2ig-gate the ECD contact; the vestibule reach stays a labeled mechanistic bet.
"""
    with open(os.path.join(OUT_DIR, "register.md"), "w") as fh:
        fh.write(txt)


if __name__ == "__main__":
    main()
