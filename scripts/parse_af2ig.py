"""Parse an af2ig (dl_binder_design) SCORE file into a ranked binder table.
af2ig is the Baker de-novo-binder standard (more reliable than Boltz co-fold, which
over-docks this vestibule). Key metric = pae_interaction (lower=better; community
'binds' ~<10, strong <~7); supported by plddt_binder (>80) and binder_aligned_rmsd
(<2 = AF2 agrees with the designed backbone pose).

Usage: uv run python scripts/parse_af2ig.py <af2ig_out_dir_or_scorefile> [pae_cut=10] [plddt_cut=80] [rmsd_cut=2.0]
"""
from __future__ import annotations
import glob, os, sys

def find_sc(p):
    if os.path.isfile(p):
        return [p]
    return glob.glob(os.path.join(p, "**", "*.sc"), recursive=True) + glob.glob(os.path.join(p, "*.sc"))

def main():
    p = sys.argv[1]
    pae_cut = float(sys.argv[2]) if len(sys.argv) > 2 else 10.0
    plddt_cut = float(sys.argv[3]) if len(sys.argv) > 3 else 80.0
    rmsd_cut = float(sys.argv[4]) if len(sys.argv) > 4 else 2.0
    scs = find_sc(p)
    if not scs:
        print(f"no scorefile under {p}"); return
    rows, hdr = [], None
    for sc in scs:
        for ln in open(sc):
            if not ln.startswith("SCORE:"):
                continue
            parts = ln.split()[1:]
            if parts and parts[0] == "binder_aligned_rmsd":
                hdr = parts; continue
            if hdr is None:
                continue
            d = dict(zip(hdr, parts))
            try:
                rows.append({
                    "desc": d.get("description", "?"),
                    "pae_i": float(d["pae_interaction"]),
                    "plddt_b": float(d["plddt_binder"]),
                    "rmsd": float(d["binder_aligned_rmsd"]),
                })
            except (KeyError, ValueError):
                continue
    if not rows:
        print("no SCORE rows parsed"); return
    rows.sort(key=lambda r: r["pae_i"])
    npass = 0
    print(f"{'design':<42}{'pae_int':>8}{'plddt_b':>9}{'rmsd':>7}  gate")
    for r in rows:
        ok = r["pae_i"] <= pae_cut and r["plddt_b"] >= plddt_cut and r["rmsd"] <= rmsd_cut
        npass += ok
        print(f"{r['desc']:<42}{r['pae_i']:>8.2f}{r['plddt_b']:>9.1f}{r['rmsd']:>7.2f}  {'PASS' if ok else '.'}")
    print(f"# {len(rows)} designs | PASS(pae<={pae_cut},plddt>={plddt_cut},rmsd<={rmsd_cut}) = {npass}")
    best = rows[0]
    print(f"# BEST pae_interaction={best['pae_i']:.2f} ({best['desc']}) "
          f"| min over all = {'strong' if best['pae_i']<7 else 'weak/none' if best['pae_i']>12 else 'marginal'}")

if __name__ == "__main__":
    main()
