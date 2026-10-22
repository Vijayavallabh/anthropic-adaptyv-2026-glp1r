#!/usr/bin/env python3
"""Harvest accepted BindCraft2 designs from the 4 active-state arms into one CSV.

Firewall: BC2 acceptance (AF2 confidence/geometry) is a GENERATION screen only. Nothing
here is an agonism claim; survivors must still clear the Boltz-and-Chai 2-folder construct
bar downstream, and only the wet cAMP/SEAP assay decides agonism.

Reads each arm's 3_Ranked/!_Ranked.csv (accepted) + 2_Refolded/!_Refolded.csv (scored),
detects the sequence column dynamically, dedups by sequence, writes runs/bc2/harvest.csv.
Usage: uv run python -I scripts/bc2/harvest_bc2.py [--stage ranked|refolded]
"""
import csv, glob, os, sys, re

ROOT = "/home/prachh/v/anthropic-adaptyv-2026-glp1r/runs/bc2/results"
OUT = "/home/prachh/v/anthropic-adaptyv-2026-glp1r/runs/bc2/harvest.csv"
# scan every campaign result folder present (Wave-3a _w2, Wave-3b E/F/G/H, etc.)
ARMS = sorted(d for d in os.listdir(ROOT) if os.path.isdir(os.path.join(ROOT, d))) if os.path.isdir(ROOT) else []
AA = set("ACDEFGHIKLMNPQRSTVWY")
stage = "ranked"
if "--stage" in sys.argv:
    stage = sys.argv[sys.argv.index("--stage") + 1]
REL = {"ranked": "3_Ranked/!_Ranked.csv", "refolded": "2_Refolded/!_Refolded.csv"}[stage]

def find_seq_col(header, rows):
    low = {h.lower(): h for h in header}
    for cand in ("binder_sequence", "sequence", "seq", "binder_seq"):
        if cand in low:
            return low[cand]
    # fallback: a column whose values look like protein AA strings (eligible range 10-250)
    for col in header:
        vals = [r.get(col, "") for r in rows[:5] if r.get(col)]
        if vals and all(isinstance(v, str) and 8 <= len(v) <= 250 and set(v.upper()) <= AA for v in vals):
            return col
    return None

def pick(row, *names):
    for n in names:
        if n in row and row[n] not in ("", None):
            return row[n]
    return ""

rows_out = []
seen = set()
per_arm = {}
for arm in ARMS:
    path = os.path.join(ROOT, arm, REL)
    n = 0
    if not os.path.isfile(path):
        per_arm[arm] = 0
        continue
    with open(path, newline="") as fh:
        rdr = list(csv.DictReader(fh))
    if not rdr:
        per_arm[arm] = 0
        continue
    header = rdr[0].keys()
    seqcol = find_seq_col(list(header), rdr)
    if not seqcol:
        per_arm[arm] = 0
        print(f"WARN {arm}: no sequence column found in {list(header)[:12]}", file=sys.stderr)
        continue
    for r in rdr:
        seq = (r.get(seqcol) or "").strip().upper()
        if not seq or set(seq) - AA:
            continue
        if seq in seen:
            continue
        seen.add(seq)
        rows_out.append({
            "name": pick(r, "name", "design", "id") or f"{arm}_{n}",
            "arm": arm,
            "sequence": seq,
            "length": len(seq),
            "n_cys": seq.count("C"),
            "i_pDAE": pick(r, "i_pDAE", "i_pdae"),
            "i_pTM": pick(r, "i_pTM", "i_ptm"),
            "pLDDT": pick(r, "pLDDT", "plddt", "Binder_pLDDT"),
            "Hotspot_Contact_Fraction": pick(r, "Hotspot_Contact_Fraction"),
        })
        n += 1
    per_arm[arm] = n

os.makedirs(os.path.dirname(OUT), exist_ok=True)
cols = ["name", "arm", "sequence", "length", "n_cys", "i_pDAE", "i_pTM", "pLDDT", "Hotspot_Contact_Fraction"]
with open(OUT, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=cols, lineterminator="\n")
    w.writeheader()
    w.writerows(rows_out)

print(f"stage={stage}  total unique designs={len(rows_out)}")
for a in ARMS:
    print(f"  {a}: {per_arm.get(a,0)}")
print(f"wrote {OUT}")
