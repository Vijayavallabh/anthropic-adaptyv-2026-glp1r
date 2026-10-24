#!/usr/bin/env python3
"""Merge all picker-screen score shards into one Boltz csv, one Chai csv, one pLDDT json
for the final 2-folder allocation. Dedup by design name (first occurrence wins).
Run with -I from repo root. Missing optional shards are skipped gracefully.
"""
import csv, json, os
REPO = "/home/prachh/v/anthropic-adaptyv-2026-glp1r"
R = f"{REPO}/runs/picker"

def merge_csv(paths, out):
    seen, rows, hdr = set(), [], None
    for p in paths:
        if not os.path.exists(p): continue
        for r in csv.DictReader(open(p)):
            hdr = hdr or list(r.keys())
            if r["name"] in seen: continue
            seen.add(r["name"]); rows.append(r)
    if hdr:
        w = csv.DictWriter(open(out, "w", newline=""), fieldnames=hdr, lineterminator="\n", extrasaction="ignore")
        w.writeheader(); w.writerows(rows)
    return len(rows)

def merge_json(paths, out):
    d = {}
    for p in paths:
        if os.path.exists(p):
            d.update(json.load(open(p)))
    json.dump(d, open(out, "w"), indent=1)
    return len(d)

nb = merge_csv([f"{R}/scores_boltz.csv", f"{R}/scores_exp.csv"], f"{R}/scores_boltz_all.csv")
nc = merge_csv([f"{R}/scores_chai.csv", f"{R}/scores_chai2.csv", f"{R}/scores_chai3.csv"], f"{R}/scores_chai_all.csv")
npl = merge_json([f"{R}/plddt/plddt.json", f"{R}/plddt_exp/plddt.json"], f"{R}/plddt_all.json")
print(f"merged: boltz {nb} | chai {nc} | plddt {npl}")
print("wrote scores_boltz_all.csv scores_chai_all.csv plddt_all.json")
