#!/usr/bin/env python3
"""harvest.csv -> bare.csv (design as-is) + construct.csv (production expressed chain).

Production chain = (M if design doesn't start with M else '') + design + TAIL, where
TAIL = GGSGG-GFP11-GGSGG-TwinStrep (scripts/prod_viability.py:16). GPU-free; geometry prep only.
Usage: uv run python -I scripts/bc2/build_construct_csv.py [harvest.csv]
"""
import csv, sys, os
TAIL = "GGSGGRDHMVLHEYVNAAGITGGSGGWSHPQFEKGGGSGGGSGGSAWSHPQFEK"
HARVEST = sys.argv[1] if len(sys.argv) > 1 else "/home/prachh/v/anthropic-adaptyv-2026-glp1r/runs/bc2/harvest.csv"
OUTDIR = os.path.dirname(HARVEST) or "."

def construct(seq):
    seq = seq.strip().upper()
    return (seq if seq[:1] == "M" else "M" + seq) + TAIL

rows = list(csv.DictReader(open(HARVEST)))
with open(os.path.join(OUTDIR, "bare.csv"), "w", newline="") as fb, \
     open(os.path.join(OUTDIR, "construct.csv"), "w", newline="") as fc:
    wb = csv.writer(fb, lineterminator="\n"); wc = csv.writer(fc, lineterminator="\n")
    wb.writerow(["name", "sequence"]); wc.writerow(["name", "sequence"])
    for r in rows:
        nm = r["name"]; seq = r["sequence"].strip().upper()
        if not seq:
            continue
        wb.writerow([nm, seq]); wc.writerow([nm, construct(seq)])
print(f"{len(rows)} designs -> bare.csv + construct.csv (TAIL {len(TAIL)}aa appended; Met prepended when absent)")
