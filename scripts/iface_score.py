"""Interface discriminator for a Boltz co-fold dir: does the binder (chain A) make the
MECHANISM-relevant contacts (7TM vestibule message-reader hotspots), or only sit in the
promiscuous ECD groove? Plus interface-PAE. The point: find a metric that separates native
agonists from a scramble when global ipTM cannot.

Usage: uv run python scripts/iface_score.py runs/boltz_cal/out
Boltz chain B (receptor) is numbered 1..409 for the 24-432 construct -> UniProt = boltz_resnum + 23.
"""
from __future__ import annotations

import glob
import json
import os
import sys

import numpy as np
from Bio.PDB import MMCIFParser

OFFSET = 23  # boltz chain-B resnum + 23 = UniProt P43220 number (construct starts at 24)
VESTIBULE = {145, 190, 197, 299, 363, 364, 388, 392, 394}   # 7TM message-reader hotspots (UniProt)
ECD_GROOVE = {32, 69, 88, 89, 90, 121, 127, 128}            # ECD "address" groove hotspots (UniProt)
CONTACT_A = 5.0  # heavy-atom contact distance (Angstrom)


def heavy_atoms(res):
    return [a for a in res if a.element != "H" and a.element != "D"]


def load_pae(npz_path):
    try:
        d = np.load(npz_path)
        for k in d.files:
            a = d[k]
            if a.ndim == 2 and a.shape[0] == a.shape[1]:
                return a
    except Exception:
        return None  # corrupted/partial npz -> skip PAE, contacts still come from the .cif
    return None


def score_one(cif, pae_npz, conf_json):
    st = MMCIFParser(QUIET=True).get_structure("x", cif)
    model = next(iter(st))
    chains = {c.id: list(c) for c in model}
    # identify binder (shorter) vs receptor (longer) chain
    ids = sorted(chains, key=lambda c: len(chains[c]))
    bID, rID = ids[0], ids[-1]
    A = [r for r in chains[bID] if r.id[0] == " "]
    B = [r for r in chains[rID] if r.id[0] == " "]

    # heavy-atom contacts A<->B
    import numpy as _np
    Bres_heavy = {r.id[1]: _np.array([at.coord for at in heavy_atoms(r)]) for r in B}
    contacted_uni = set()
    nterm_min_uni, nterm_min_d = None, 1e9
    for i, ra in enumerate(A):
        aco = _np.array([at.coord for at in heavy_atoms(ra)])
        if len(aco) == 0:
            continue
        for bnum, bco in Bres_heavy.items():
            if len(bco) == 0:
                continue
            d = _np.sqrt(((aco[:, None, :] - bco[None, :, :]) ** 2).sum(-1)).min()
            if d <= CONTACT_A:
                contacted_uni.add(bnum + OFFSET)
            if i == 0 and d < nterm_min_d:  # peptide N-terminal residue (the "message" tip)
                nterm_min_d, nterm_min_uni = d, bnum + OFFSET

    n = len(contacted_uni)
    in7tm = sum(1 for u in contacted_uni if u >= 140)
    iPAE = None
    pae = load_pae(pae_npz)
    if pae is not None:
        na, nb = len(A), len(B)
        if pae.shape[0] >= na + nb:
            # inter-chain block mean (A rows vs B cols and vice versa), interface-focused = min over B per A then mean
            ab = pae[:na, na:na + nb]
            ba = pae[na:na + nb, :na]
            iPAE = float(round((ab.min(axis=1).mean() + ba.min(axis=1).mean()) / 2, 2))
    conf = json.load(open(conf_json))
    return {
        "iptm": round(conf.get("iptm", 0), 3),
        "n_contacts": n,
        "vestibule_hits": sorted(contacted_uni & VESTIBULE),
        "ecd_groove_hits": sorted(contacted_uni & ECD_GROOVE),
        "frac_7TM": round(in7tm / n, 2) if n else 0.0,
        "nterm_nearest_uni": nterm_min_uni,
        "nterm_in_7TM": (nterm_min_uni is not None and nterm_min_uni >= 140),
        "iPAE_min": iPAE,
    }


def main(outdir):
    results = {}
    for cif in sorted(glob.glob(os.path.join(outdir, "**", "*_model_0.cif"), recursive=True)):
        base = os.path.basename(cif).replace("_model_0.cif", "")
        d = os.path.dirname(cif)
        seeddir = os.path.basename(d)  # 's0','s1',... (multi-seed panels)
        pae = os.path.join(d, f"pae_{base}_model_0.npz")
        conf = os.path.join(d, f"confidence_{base}_model_0.json")
        if not (os.path.exists(pae) and os.path.exists(conf)):
            continue
        key = f"{base}@{seeddir}" if seeddir.startswith("s") else base
        results[key] = score_one(cif, pae, conf)
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main(sys.argv[1])
