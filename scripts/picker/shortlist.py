#!/usr/bin/env python3
"""Cheap-screen the eligible pool and select the co-fold shortlist of real
contenders for our 20 slots. Cheap screens (no GPU): mean Kyte-Doolittle gravy,
length preference, graft-clean, family. Always keep the current 20 + all
disulfide-staples; cap confounded families to a diverse subset.

In:  runs/picker/pool.csv   Out: runs/picker/shortlist.csv (name,sequence) + runs/picker/pool_screened.csv
Run with -I from repo root.
"""
import csv, os
REPO = "/home/prachh/v/anthropic-adaptyv-2026-glp1r"
KD = {  # Kyte-Doolittle hydropathy
 'A':1.8,'R':-4.5,'N':-3.5,'D':-3.5,'C':2.5,'Q':-3.5,'E':-3.5,'G':-0.4,'H':-3.2,'I':4.5,
 'L':3.8,'K':-3.9,'M':1.9,'F':2.8,'P':-1.6,'S':-0.8,'T':-0.7,'W':-0.9,'Y':-1.3,'V':4.2}
def gravy(s): return round(sum(KD[a] for a in s)/len(s), 3)

CAP = {"BoltzGen":45,"DiffPep":45,"PepMLM":30,"PepGLAD":35,"RFd3":20,"EvoBind":14,"PepGen":8,"ECD":7,"DiffPep-SS":16,"other":2}

rows = [r for r in csv.DictReader(open(f"{REPO}/runs/picker/pool.csv")) if r["elig_ok"] == "True"]
for r in rows:
    r["length"] = int(r["length"]); r["n_cys"] = int(r["n_cys"]); r["graft_max"] = int(r["graft_max"])
    r["gravy"] = gravy(r["sequence"])
    # cheap-screen priority (higher=better): wettable gravy, reasonable peptide length, graft-clean, few unpaired Cys
    g = r["gravy"]
    s = 0.0
    s += 2.0 if -1.0 <= g <= 0.3 else (1.0 if -1.6 <= g <= 0.6 else 0.0)   # solubility/expression band
    s += 1.5 if 12 <= r["length"] <= 45 else (0.8 if 10 <= r["length"] <= 65 else 0.2)
    s += 0.5 if r["graft_max"] <= 2 else 0.2
    s += -0.5 if (r["n_cys"] % 2 == 1) else 0.0                            # unpaired-Cys penalty
    r["cheap_score"] = round(s, 3)

# selection
keep = []
seen = set()
def take(r):
    if r["sequence"] in seen: return
    seen.add(r["sequence"]); keep.append(r)
# 1) always: current 20 + all staples
for r in rows:
    if r["in_v10"] or r["family"] == "DiffPep-SS": take(r)
# 2) top-K per family by cheap_score
from collections import defaultdict
byfam = defaultdict(list)
for r in rows: byfam[r["family"]].append(r)
for fam, lst in byfam.items():
    lst.sort(key=lambda r: (-r["cheap_score"], r["length"]))
    n = sum(1 for r in keep if r["family"] == fam)
    for r in lst:
        if n >= CAP.get(fam, 10): break
        if r["sequence"] not in seen: take(r); n += 1

# write screened pool (all eligible, annotated) + shortlist
allcols = list(rows[0].keys())
with open(f"{REPO}/runs/picker/pool_screened.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=allcols, lineterminator="\n"); w.writeheader(); w.writerows(rows)
with open(f"{REPO}/runs/picker/shortlist.csv", "w", newline="") as fh:
    w = csv.writer(fh, lineterminator="\n"); w.writerow(["name", "sequence"])
    for r in keep: w.writerow([r["name"], r["sequence"]])

from collections import Counter
print(f"shortlist: {len(keep)} designs for co-fold")
print("by family:", dict(Counter(r["family"] for r in keep)))
print("in_v10 kept:", sum(1 for r in keep if r["in_v10"]), "/20")
print("gravy range:", min(r["gravy"] for r in keep), "..", max(r["gravy"] for r in keep))
print("wrote runs/picker/shortlist.csv + pool_screened.csv")
