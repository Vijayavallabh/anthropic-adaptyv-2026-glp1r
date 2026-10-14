#!/usr/bin/env python3
"""Harvest DiffPepBuilder-designed peptides (chain A) from generated complex PDBs.

Emits data/candidates/diffpep_raw.csv: name,target,length,n_cys,n_ssbond,ss_pairs,sequence,pdb_path
Chain A = designed peptide, chain B = cropped receptor pocket (confirmed from output format).
"""
import os, glob, csv, sys

RUNS = "/home/prachh/v/anthropic-adaptyv-2026-glp1r/third_party/DiffPepBuilder/runs/inference"
OUT = "/home/prachh/v/anthropic-adaptyv-2026-glp1r/data/candidates/diffpep_raw.csv"
T3 = {'ALA':'A','ARG':'R','ASN':'N','ASP':'D','CYS':'C','GLN':'Q','GLU':'E','GLY':'G',
      'HIS':'H','ILE':'I','LEU':'L','LYS':'K','MET':'M','PHE':'F','PRO':'P','SER':'S',
      'THR':'T','TRP':'W','TYR':'Y','VAL':'V'}

def parse(pdb):
    seq, ss = [], []
    for ln in open(pdb):
        if ln.startswith("SSBOND"):
            ss.append(ln.strip())
        elif ln.startswith("ATOM") and ln[12:16].strip() == "CA" and ln[21] == "A":
            seq.append(T3.get(ln[17:20].strip(), "X"))
    return "".join(seq), ss

rows = []
for pdb in sorted(glob.glob(f"{RUNS}/*/*/length_*/*.pdb")):
    parts = pdb.split("/")
    tgt = next((p for p in parts if p in ("glp1rvest", "glp1recd")), "unknown")
    # only the full probe run has lengths other than 14-only smokes; keep all, dedupe by seq below
    seq, ss = parse(pdb)
    if not seq:
        continue
    ncys = seq.count("C")
    # SSBOND pair residue numbers (cols 18-21 and 32-35 in standard SSBOND records)
    pairs = []
    for s in ss:
        try:
            pairs.append(f"{int(s[17:21])}-{int(s[31:35])}")
        except Exception:
            pairs.append("?")
    rows.append({
        "target": tgt, "length": len(seq), "n_cys": ncys,
        "n_ssbond": len(ss), "ss_pairs": ";".join(pairs) if pairs else "-",
        "sequence": seq, "pdb_path": pdb,
    })

# dedupe by sequence (keep first); drop the length-14 smoke singletons if an identical seq recurs
seen = set(); uniq = []
for r in rows:
    if r["sequence"] in seen:
        continue
    seen.add(r["sequence"]); uniq.append(r)

for i, r in enumerate(uniq):
    r["name"] = f"dpb_{r['target'].replace('glp1r','')}_{i:03d}"

os.makedirs(os.path.dirname(OUT), exist_ok=True)
cols = ["name", "target", "length", "n_cys", "n_ssbond", "ss_pairs", "sequence", "pdb_path"]
with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
    for r in uniq:
        w.writerow({k: r[k] for k in cols})

nvest = sum(1 for r in uniq if r["target"] == "glp1rvest")
necd = sum(1 for r in uniq if r["target"] == "glp1recd")
nss = sum(1 for r in uniq if r["n_ssbond"] > 0)
print(f"Harvested {len(uniq)} unique peptides (vest={nvest}, ecd={necd}); {nss} carry >=1 disulfide (SSBOND).")
print(f"Wrote {OUT}")
