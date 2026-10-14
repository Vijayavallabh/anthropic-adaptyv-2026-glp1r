#!/usr/bin/env python3
"""Gate DiffPepBuilder peptides through the project's OWN eligibility + developability filters.
Keep = eligible (not incretin-similar) AND no odd-Cys/low-complexity liability.
Writes data/candidates/diffpep_gated.csv."""
import csv, sys, os
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "scripts"))
from eligibility_check import build_scorer, score_design
from developability import analyze

RAW = os.path.join(REPO, "data/candidates/diffpep_raw.csv")
OUT = os.path.join(REPO, "data/candidates/diffpep_gated.csv")

refs, aligner = build_scorer()
rows = list(csv.DictReader(open(RAW)))
out = []
for r in rows:
    seq = r["sequence"]
    e = score_design(seq, refs, aligner)
    d = analyze(seq)
    hard_dev = [f for f in d["flags"] if f.startswith("oddCys") or f.startswith("lowcplx")]
    keep = (not e["flag"]) and (len(hard_dev) == 0)
    out.append({
        "name": r["name"], "target": r["target"], "length": r["length"], "n_cys": r["n_cys"],
        "elig_pid": round(e["pid"], 1), "elig_cov": round(e["cov"], 2), "elig_nearest": e["nearest"],
        "elig_flag": e["flag"], "dev_flags": ",".join(d["flags"]) or "clean",
        "instab": round(d["instab"], 1) if d["instab"] == d["instab"] else "nan",
        "gravy": round(d["gravy"], 2), "charge": d["charge"], "keep": keep, "sequence": seq,
    })

cols = ["name", "target", "length", "n_cys", "elig_pid", "elig_cov", "elig_nearest", "elig_flag",
        "dev_flags", "instab", "gravy", "charge", "keep", "sequence"]
with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(out)

keeps = [r for r in out if r["keep"]]
kv = [r for r in keeps if r["target"] == "glp1rvest"]
ke = [r for r in keeps if r["target"] == "glp1recd"]
kss = [r for r in keeps if int(r["n_cys"]) >= 2]
print(f"Gated {len(out)} -> KEEP {len(keeps)} (vest={len(kv)}, ecd={len(ke)}); of keeps, {len(kss)} have >=2 Cys (disulfide-capable).")
print(f"dropped: elig_flag={sum(1 for r in out if r['elig_flag'])}, "
      f"low-complexity/oddCys={sum(1 for r in out if not r['keep'] and not r['elig_flag'])}")
print(f"Wrote {OUT}")
