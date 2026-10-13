"""Validate an RFdiffusion binder-generation wave GEOMETRICALLY before spending
MPNN/co-fold compute on it. RFd is membrane-blind (research note 04): a binder
conditioned on the 7TM vestibule hotspots can still drift to the lipid-facing TM
surface or wrap the truncation edges of a cropped receptor. This script asks, per
design: is the binder (chain A) a compact fold whose contact footprint is centred
on the intended hotspot patch (chain R author numbering)?

Usage: uv run python scripts/check_rfd_geom.py runs/rfd/<sub> [hot1 hot2 ...]
Default hotspots = the calibrated vestibule generation cluster {190,194,233,234,237}.
Verdict per design (PASS needs all): >=2 hotspot contacts, footprint centroid
<=12A from hotspot-CA centroid, binder Rg in a compact band, helix-rich backbone.
"""
from __future__ import annotations

import glob
import os
import sys

import numpy as np
from Bio.PDB import PDBParser

DEF_HOTSPOTS = [190, 194, 233, 234, 237]
CONTACT_A = 5.0
RG_LO, RG_HI = 9.0, 20.0   # 60-90aa compact single-domain band (A); >HI => extended/unfolded
HELIX_MIN = 0.30           # fraction of CA in helical i,i+3 spacing; vestibule de-novo binders are helix-rich


def heavy(res):
    return [a for a in res if a.element not in ("H", "D")]


def ca_coords(chain):
    out = {}
    for r in chain:
        if r.id[0] != " ":
            continue
        if "CA" in r:
            out[r.id[1]] = r["CA"].coord
    return out


def rg(coords):
    x = np.array(list(coords.values()))
    c = x.mean(0)
    return float(np.sqrt(((x - c) ** 2).sum(1).mean()))


def helix_frac(ca):
    # helical if CA(i)-CA(i+3) ~5-6.3A (one turn); crude but discriminates helix vs strand/coil
    nums = sorted(ca)
    if len(nums) < 4:
        return 0.0
    hit = tot = 0
    for i in range(len(nums) - 3):
        if nums[i + 3] - nums[i] == 3:  # contiguous
            d = np.linalg.norm(ca[nums[i]] - ca[nums[i + 3]])
            tot += 1
            if 4.8 <= d <= 6.4:
                hit += 1
    return hit / tot if tot else 0.0


def analyze(pdb, hotspots):
    st = PDBParser(QUIET=True).get_structure("x", pdb)
    model = next(iter(st))
    chains = {c.id: c for c in model}
    if "A" not in chains or "R" not in chains:
        return None
    binder, recep = chains["A"], chains["R"]
    bca = ca_coords(binder)
    rca = ca_coords(recep)
    # binder heavy atoms
    bheavy = np.array([a.coord for r in binder if r.id[0] == " " for a in heavy(r)])
    # receptor residues -> heavy atom coords
    rres = {r.id[1]: np.array([a.coord for a in heavy(r)]) for r in recep if r.id[0] == " "}
    contacted = set()
    for num, rco in rres.items():
        if len(rco) == 0:
            continue
        d = np.sqrt(((bheavy[:, None, :] - rco[None, :, :]) ** 2).sum(-1)).min()
        if d <= CONTACT_A:
            contacted.add(num)
    hot_hits = sorted(contacted & set(hotspots))
    # footprint centroid distance to hotspot-CA centroid
    hot_ca = np.array([rca[h] for h in hotspots if h in rca])
    hot_cen = hot_ca.mean(0)
    foot = np.array([rca[c] for c in contacted if c in rca])
    foot_d = float(np.linalg.norm(foot.mean(0) - hot_cen)) if len(foot) else 999.0
    # trb plddt
    trb = pdb.replace(".pdb", ".trb")
    plddt = None
    if os.path.exists(trb):
        try:
            d = np.load(trb, allow_pickle=True)
            pl = d["plddt"]
            plddt = round(float(np.mean(pl)), 3)
        except Exception:
            pass
    rgv = rg(bca)
    hf = helix_frac(bca)
    ok = (len(hot_hits) >= 2 and foot_d <= 12.0 and RG_LO <= rgv <= RG_HI and hf >= HELIX_MIN)
    return {
        "nres": len(bca), "rg": round(rgv, 1), "helix_frac": round(hf, 2),
        "n_contacts": len(contacted), "hot_hits": hot_hits, "foot_d": round(foot_d, 1),
        "rfd_plddt": plddt, "PASS": ok,
    }


def main():
    d = sys.argv[1]
    hot = [int(x) for x in sys.argv[2:]] or DEF_HOTSPOTS
    pdbs = sorted(glob.glob(os.path.join(d, "des_*.pdb")))
    print(f"# {len(pdbs)} designs in {d} | hotspots={hot}")
    print(f"{'design':<10}{'nres':>5}{'Rg':>6}{'hlx':>6}{'nC':>5}{'hotHits':>18}{'footD':>7}{'plddt':>7}  verdict")
    npass = 0
    for p in pdbs:
        r = analyze(p, hot)
        if r is None:
            print(f"{os.path.basename(p):<10}  <no A/R chains>")
            continue
        npass += r["PASS"]
        print(f"{os.path.basename(p).replace('.pdb',''):<10}{r['nres']:>5}{r['rg']:>6}{r['helix_frac']:>6}"
              f"{r['n_contacts']:>5}{str(r['hot_hits']):>18}{r['foot_d']:>7}{str(r['rfd_plddt']):>7}  "
              f"{'PASS' if r['PASS'] else 'fail'}")
    print(f"# PASS {npass}/{len(pdbs)}")


if __name__ == "__main__":
    main()
