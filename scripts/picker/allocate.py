#!/usr/bin/env python3
"""Deterministic, picker-faithful allocator: order our best-20 to maximise the
published Adaptyv selection rubric, on the picker's OWN screens (bare design + WT
GLP1R, ipSAE/ipTM co-fold, ESMFold monomer pLDDT, mean Kyte-Doolittle gravy),
with novelty + family/epitope diversity, and a few honest long shots.

FIREWALL: ranking uses only the picker's MEASURABLE proxies (binding + expression
+ on-epitope + novelty + diversity). Agonism is NEVER scored or ranked; the
vestibule/R299 epitope is a stated binding-site, and pre-organized staples enter
only as labelled long shots. Weights are disclosed below and printed to the report.

Usage: uv run python -I scripts/picker/allocate.py <scores_boltz.csv> <plddt.json> <out_prefix>
"""
import csv, json, sys, math
from collections import defaultdict

# ---- disclosed composite weights (binding-led, expression-gated) ----
W_IPSAE, W_IPTM, W_EXPRESS, W_EPITOPE = 0.55, 0.20, 0.15, 0.10
GRAVY_HI = 0.5          # above this = hydrophobic/aggregation risk (expression penalty)
TOP10_FAMILY_CAP = 3    # diversity: <=3 of any method family in the top 10
OVERALL_FAMILY_CAP = 4  # <=4 of any family across the 20 (rubric rewards family diversity)

def plddt_class_ok(plddt, length):
    # single-seq predictors score short peptides low -> read within class (rubric)
    if plddt is None: return 0.5
    thr = 50 if length <= 25 else (62 if length <= 45 else 70)
    return 1.0 if plddt >= thr else max(0.0, plddt / thr)

def norm(x, lo, hi):
    if x is None: return 0.0
    return max(0.0, min(1.0, (x - lo) / (hi - lo)))

def load(scores_csv, plddt_json):
    plddt = json.load(open(plddt_json)) if plddt_json and plddt_json != "-" else {}
    rows = []
    for r in csv.DictReader(open(scores_csv)):
        for k in ("ipsae_best", "ipsae_med", "iptm_best", "ipae_best", "gravy"):
            r[k] = float(r[k]) if r.get(k) not in ("", None, "None") else None
        for k in ("length", "n_cys", "r299_n", "n_seeds", "nterm_in7TM_n", "graft_max"):
            r[k] = int(r[k]) if r.get(k) not in ("", None) else 0
        r["plddt"] = plddt.get(r["name"])
        rows.append(r)
    return rows

def composite(r):
    bind = W_IPSAE * norm(r["ipsae_best"], 0.2, 0.9) + W_IPTM * norm(r["iptm_best"], 0.5, 0.95)
    express = W_EXPRESS * (plddt_class_ok(r["plddt"], r["length"])
                           * (1.0 if (r["gravy"] is None or r["gravy"] <= GRAVY_HI) else 0.5)
                           * (0.6 if r["n_cys"] % 2 == 1 else 1.0))
    vest = r.get("vestibule", "").split("|") if r.get("vestibule") else []
    epi = W_EPITOPE * (1.0 if (r["r299_n"] >= 1 or len([v for v in vest if v]) >= 2) else 0.3)
    return round(bind + express + epi, 4)

def pclass(length):
    return "peptide" if length <= 30 else ("miniprotein" if length <= 100 else "small_protein")

def main(scores_csv, plddt_json, outpre):
    rows = load(scores_csv, plddt_json)
    for r in rows:
        r["composite"] = composite(r)
        r["pclass"] = pclass(r["length"])
        # hard eligibility gate (rubric): length, graft, (odd-Cys is a soft penalty not a gate)
        r["eligible"] = (10 <= r["length"] <= 250) and (r["graft_max"] <= 3)
    elig = [r for r in rows if r["eligible"]]
    elig.sort(key=lambda r: -r["composite"])

    # greedy diversity-aware selection of 20, enforcing family caps + >=1 long-shot staple
    chosen, famc = [], defaultdict(int)
    def pick(r):
        chosen.append(r); famc[r["family"]] += 1
    # pass 1: fill top-10 respecting TOP10 family cap
    for r in elig:
        if len(chosen) >= 10: break
        if famc[r["family"]] < TOP10_FAMILY_CAP: pick(r)
    # ensure >=1 staple long-shot in the set (agonism-prior modality) if any forms a disulfide
    staples = [r for r in elig if r["family"] == "DiffPep-SS" and r not in chosen]
    # pass 2: fill 11-20 respecting OVERALL cap, maximising remaining composite + family spread
    for r in elig:
        if len(chosen) >= 20: break
        if r in chosen: continue
        if famc[r["family"]] < OVERALL_FAMILY_CAP: pick(r)
    # swap in one staple long-shot at slot ~ last if none present
    if not any(r["family"] == "DiffPep-SS" for r in chosen) and staples:
        chosen[-1] = staples[0]
    chosen = chosen[:20]

    # write ranked submission + full screen table
    with open(f"{outpre}_submission.csv", "w", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n"); w.writerow(["name", "sequence", "molecule_class"])
        for i, r in enumerate(chosen, 1):
            w.writerow([r["name"], r["sequence"], "single_chain"])
    cols = ["rank", "name", "family", "pclass", "length", "composite", "ipsae_best", "iptm_best",
            "ipae_best", "r299_n", "n_seeds", "epitope", "vestibule", "plddt", "gravy", "n_cys", "in_v10", "sequence"]
    with open(f"{outpre}_screens.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, lineterminator="\n", extrasaction="ignore"); w.writeheader()
        for i, r in enumerate(chosen, 1):
            w.writerow({"rank": i, **r})
    # also dump the full ranked pool for the report/reserve
    with open(f"{outpre}_ranked_pool.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, lineterminator="\n", extrasaction="ignore"); w.writeheader()
        for i, r in enumerate(elig, 1): w.writerow({"rank": i, **r})

    v10_in = sum(1 for r in chosen if r["in_v10"])
    print(f"weights: ipSAE {W_IPSAE} iptm {W_IPTM} express {W_EXPRESS} epitope {W_EPITOPE}; gravy_hi {GRAVY_HI}; fam caps {TOP10_FAMILY_CAP}/{OVERALL_FAMILY_CAP}")
    print(f"chosen 20: from v10 = {v10_in}, NEW = {20 - v10_in}")
    print("family mix:", dict(famc))
    print(f"{'rk':>2} {'name':22s} {'fam':11s} {'comp':>5s} {'ipSAE':>6s} {'iptm':>5s} {'r299':>5s} {'epi':>9s} {'pLDDT':>5s} v10")
    for i, r in enumerate(chosen, 1):
        print(f"{i:2d} {r['name']:22s} {r['family']:11s} {r['composite']:5.3f} {str(r['ipsae_best']):>6s} {str(r['iptm_best']):>5s} {r['r299_n']}/{r['n_seeds']:<3d} {r['epitope']:>9s} {str(r['plddt']):>5s} {'Y' if r['in_v10'] else ''}")
    print(f"wrote {outpre}_submission.csv + _screens.csv + _ranked_pool.csv")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "-", sys.argv[3])
