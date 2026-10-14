#!/usr/bin/env python3
"""Evaluate corrected-vestibule (R299) DiffPepBuilder designs on agonism relevance, orthogonally.

For each glp1rvest2 design, measure peptide(chainA)->R299(chainB res 299) min heavy-atom distance in
DiffPepBuilder's OWN docked pose (orthogonal to AF2/EvoBind), plus pocket-contact count, and run the
project's eligibility + developability gates. Ranks gated keepers by R299 proximity.

Writes data/candidates/diffpep_vest2_eval.csv
"""
import os, glob, csv, math, sys
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "scripts"))
from eligibility_check import build_scorer, score_design
from developability import analyze

RUNS = os.path.join(REPO, "third_party/DiffPepBuilder/runs/inference")
OUT = os.path.join(REPO, "data/candidates/diffpep_vest2_eval.csv")
T3 = {'ALA':'A','ARG':'R','ASN':'N','ASP':'D','CYS':'C','GLN':'Q','GLU':'E','GLY':'G','HIS':'H',
      'ILE':'I','LEU':'L','LYS':'K','MET':'M','PHE':'F','PRO':'P','SER':'S','THR':'T','TRP':'W','TYR':'Y','VAL':'V'}

def dd(a, b): return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)

def parse(pdb):
    """chain A peptide (seq + heavy atoms), chain B R299 heavy atoms, chain B per-residue heavy atoms."""
    pepseq = {}; pep_atoms = []; r299 = []; bres = {}
    for ln in open(pdb):
        if not ln.startswith("ATOM"): continue
        ch = ln[21]; atom = ln[12:16].strip(); rs = int(ln[22:26]); rn = ln[17:20].strip()
        c = (float(ln[30:38]), float(ln[38:46]), float(ln[46:54]))
        if ch == "A":
            if atom == "CA": pepseq[rs] = T3.get(rn, "X")
            if not atom.startswith("H"): pep_atoms.append(c)
        elif ch == "B":
            if not atom.startswith("H"):
                bres.setdefault(rs, []).append(c)
                if rn == "ARG": r299.append(c)   # R299 is the unique Arg in this pocket (renumbered in output)
    seq = "".join(pepseq[k] for k in sorted(pepseq))
    return seq, pep_atoms, r299, bres

refs, aligner = build_scorer()
rows = []
seen = set()
for pdb in sorted(glob.glob(f"{RUNS}/*/glp1rvest2/length_*/*.pdb")):
    seq, pep, r299, bres = parse(pdb)
    if not seq or seq in seen: continue
    seen.add(seq)
    minR299 = min((dd(p, a) for p in pep for a in r299), default=999) if r299 else 999
    ncontact = sum(1 for rs, atoms in bres.items()
                   if min((dd(p, a) for p in pep for a in atoms), default=999) <= 4.5)
    e = score_design(seq, refs, aligner); d = analyze(seq)
    hard = [f for f in d["flags"] if f.startswith("oddCys") or f.startswith("lowcplx")]
    keep = (not e["flag"]) and not hard
    rows.append({"length": len(seq), "n_cys": seq.count("C"), "minD_R299": round(minR299, 2),
                 "reaches_R299": minR299 <= 4.5, "pocket_contacts": ncontact,
                 "elig_pid": round(e["pid"], 1), "elig_cov": round(e["cov"], 2), "elig_nearest": e["nearest"],
                 "dev_flags": ",".join(d["flags"]) or "clean", "keep": keep, "has_ss": "_ss" in pdb,
                 "sequence": seq})

rows.sort(key=lambda r: r["minD_R299"])
for i, r in enumerate(rows): r["name"] = f"dpbv2_{i:03d}"
cols = ["name", "length", "n_cys", "minD_R299", "reaches_R299", "pocket_contacts",
        "elig_pid", "elig_cov", "elig_nearest", "dev_flags", "keep", "has_ss", "sequence"]
with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
    for r in rows: w.writerow({k: r[k] for k in cols})

keeps = [r for r in rows if r["keep"]]
reach = [r for r in keeps if r["reaches_R299"]]
print(f"{len(rows)} unique vest2 designs; KEEP(elig+dev)={len(keeps)}; "
      f"of keeps {len(reach)} reach R299 (<4.5A in DiffPepBuilder pose).")
print(f"{'name':10s}{'L':>3s}{'Cys':>4s}{'R299d':>7s}{'contacts':>9s}{'id%':>6s}{'cov':>6s}  dev  seq")
for r in keeps[:12]:
    print(f"{r['name']:10s}{r['length']:>3d}{r['n_cys']:>4d}{r['minD_R299']:>7.2f}{r['pocket_contacts']:>9d}"
          f"{r['elig_pid']:>6.1f}{r['elig_cov']:>6.2f}  {r['dev_flags'][:18]:18s} {r['sequence']}")
print(f"Wrote {OUT}")
