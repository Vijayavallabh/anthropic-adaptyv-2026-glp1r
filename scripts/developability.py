"""Developability quick-screen for the F7/F8 developability axis (consensus-drop only when
worst-tier on >=2 orthogonal axes — note 06 / TNF lesson; this just surfaces flags).
Metrics per sequence: length, unpaired Cys, max single-residue fraction (low-complexity /
poly-X, e.g. MPNN poly-Ala), GRAVY (hydrophobicity), aromatic fraction, net charge,
ProtParam instability index. Nothing here is a hard gate; it ranks relative risk.

Importable: `analyze(seq) -> dict` is the single source of truth for these metrics (reused by
scripts/build_candidate_register.py so the register is never hand-transcribed).

Usage: uv run python scripts/developability.py <designs.csv>   (columns name,sequence)
"""
from __future__ import annotations
import csv, sys, collections
from Bio.SeqUtils.ProtParam import ProteinAnalysis

KD = {'A':1.8,'R':-4.5,'N':-3.5,'D':-3.5,'C':2.5,'Q':-3.5,'E':-3.5,'G':-0.4,'H':-3.2,
      'I':4.5,'L':3.8,'K':-3.9,'M':1.9,'F':2.8,'P':-1.6,'S':-0.8,'T':-0.7,'W':-0.9,'Y':-1.3,'V':4.2}


def analyze(seq: str) -> dict:
    """Single source of truth for developability metrics + flags for one sequence."""
    s = seq.strip().upper()
    n = len(s)
    comp = collections.Counter(s)
    cys = comp.get("C", 0)
    maxaa, maxaa_res = max((v, k) for k, v in comp.items()) if n else (0, "-")
    maxfrac = maxaa / n if n else 0.0
    gravy = sum(KD.get(c, 0) for c in s) / n if n else 0.0
    arom = sum(comp.get(c, 0) for c in "FWY") / n if n else 0.0
    charge = (comp.get("K", 0) + comp.get("R", 0)) - (comp.get("D", 0) + comp.get("E", 0))
    try:
        instab = ProteinAnalysis(s).instability_index()
    except Exception:
        instab = float("nan")
    flags = []
    if cys % 2 == 1:
        flags.append(f"oddCys({cys})")
    if maxfrac > 0.30:
        flags.append(f"lowcplx({maxaa_res}{maxfrac:.0%})")
    if gravy > 0.5:
        flags.append("hydrophobic")
    if instab == instab and instab > 40:
        flags.append("instab>40")
    return {"len": n, "cys": cys, "maxaa_res": maxaa_res, "maxfrac": maxfrac,
            "gravy": gravy, "arom": arom, "charge": charge, "instab": instab, "flags": flags}


def main():
    rows = list(csv.DictReader(open(sys.argv[1])))
    print(f"{'name':<22}{'len':>4}{'Cys':>4}{'maxAA':>7}{'GRAVY':>7}{'arom%':>7}{'charge':>7}{'instab':>7}  flags")
    for r in rows:
        s = r["sequence"].strip().upper()
        if not s:
            continue
        a = analyze(s)
        print(f"{r['name']:<22}{a['len']:>4}{a['cys']:>4}{a['maxaa_res']}{a['maxfrac']:>5.0%}"
              f"{a['gravy']:>7.2f}{a['arom']:>7.0%}{a['charge']:>+7d}{a['instab']:>7.1f}  {','.join(a['flags']) or 'clean'}")


if __name__ == "__main__":
    main()
