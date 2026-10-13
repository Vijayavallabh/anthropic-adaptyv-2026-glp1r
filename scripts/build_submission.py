"""F9 - project the ranked portfolio (data/candidates/ranked.csv) into the Track-3 submission CSV
`submissions/glp1r_track3.csv` (columns name,sequence,molecule_class), rows in rank order (best-first,
row order = our disclosed ranking). Published-safe names: glp1r_<rank>_<ago|bind> (unique, no PII,
method-tag only). Prints the submission_name <-> internal_name mapping for the dossier. Does NOT upload.

Usage: uv run python scripts/build_submission.py
Then gate: uv run python scripts/validate_submission.py submissions/glp1r_track3.csv --track 3
"""
from __future__ import annotations
import csv, os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RANKED = os.path.join(REPO, "data/candidates/ranked.csv")
OUT = os.path.join(REPO, "submissions/glp1r_track3.csv")
MAP = os.path.join(REPO, "submissions/glp1r_track3_mapping.csv")


def main():
    ranked = list(csv.DictReader(open(RANKED)))
    sub, mapping = [], []
    for r in ranked:
        arm = "ago" if r["arm"] == "agonism-peptide" else "bind"
        name = f"glp1r_{int(r['rank']):02d}_{arm}"
        sub.append((name, r["sequence"], r["molecule_class"]))
        mapping.append((r["rank"], name, r["name"], r["arm"], r["binding_metric"],
                        r["binding_value"], r.get("struct_nov_maxTM", ""), r["composite"]))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["name", "sequence", "molecule_class"]); w.writerows(sub)
    with open(MAP, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["rank", "submission_name", "internal_name", "arm", "binding_metric", "binding_value", "struct_nov_maxTM", "composite"])
        w.writerows(mapping)

    # Incretin-resemblance audit, GENERATED from candidates.csv (root fix: the pre-upload portal
    # watchlist must be DERIVED, never hand-picked - a hand-picked '3' silently omitted higher-id
    # peptides). Flag any agonism peptide with raw local id >=50% to a known incretin for portal re-check.
    cand = {r["name"]: r for r in csv.DictReader(open(os.path.join(REPO, "data/candidates/candidates.csv")))}
    ELIG = os.path.join(REPO, "submissions/glp1r_track3_eligibility.csv")
    erows = []
    for rk, name, internal, arm, *_ in mapping:
        if arm != "agonism-peptide":
            continue
        c = cand[internal]
        pid = float(c["elig_id_pct"]); cov = float(c["elig_cov"])
        concern = pid if cov >= 0.50 else pid * cov / 0.50   # same cov-gating as eligibility_check
        erows.append((name, internal, f"{pid:.1f}", f"{cov:.2f}", c["elig_nearest"], f"{concern:.1f}",
                      "recheck" if pid >= 50.0 else "ok"))
    erows.sort(key=lambda r: -float(r[2]))
    with open(ELIG, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["submission_name", "internal_name", "raw_id_pct", "coverage", "nearest_incretin", "cov_gated_concern", "portal_recheck"])
        w.writerows(erows)
    nrc = sum(1 for e in erows if e[6] == "recheck")
    print(f"wrote {OUT} ({len(sub)} designs, rank order) + mapping {MAP}")
    print(f"wrote {ELIG}: {len(erows)} agonism peptides, {nrc} flagged portal_recheck (raw id>=50%)")
    print(f"{'rank':>4} {'submission_name':<16}{'internal':<14}{'arm':<16}{'metric':<22}comp")
    for rk, nm, intn, arm, bm, bv, nov, comp in mapping:
        print(f"{rk:>4} {nm:<16}{intn:<14}{arm:<16}{bm+'='+bv:<22}{comp}")


if __name__ == "__main__":
    main()
