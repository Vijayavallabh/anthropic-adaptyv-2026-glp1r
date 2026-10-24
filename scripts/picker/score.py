#!/usr/bin/env python3
"""Picker-faithful screen scorer for a bare-design + WT-receptor Boltz fold dir.
Per design (aggregated across seeds): ipSAE (canonical, min of both directions -
the picker's interface metric), ipTM, iPAE_min, R299/vestibule epitope, N-term
insertion. Merges the cheap screens (gravy/length/family/graft) from pool_screened.csv.

Usage: uv run python -I scripts/picker/score.py <fold_workdir> <out.csv>
Binding/geometry necessary-condition only; never an agonism claim.
"""
import csv, glob, json, os, sys
import numpy as np
from Bio.PDB import MMCIFParser

REPO = "/home/prachh/v/anthropic-adaptyv-2026-glp1r"
sys.path.insert(0, f"{REPO}/third_party/boltzgen/src/boltzgen/task/esmfold2")
import ipsae  # noqa: E402

OFFSET = 23
VESTIBULE = {145, 190, 197, 299, 363, 364, 388, 392, 394}
CENTRAL_POLAR = {190, 240, 363, 364, 394}
CONTACT_A = 5.0

def heavy(res): return [a for a in res if a.element not in ("H", "D")]

def load_pae(npz):
    try:
        d = np.load(npz)
        for k in d.files:
            a = d[k]
            if a.ndim == 2 and a.shape[0] == a.shape[1]:
                return a
    except Exception:
        return None
    return None

def score_cif(cif, pae_npz, conf_json):
    st = MMCIFParser(QUIET=True).get_structure("x", cif)
    model = next(iter(st))
    chains = {c.id: [r for r in c if r.id[0] == " "] for c in model}
    ids = sorted(chains, key=lambda c: len(chains[c]))
    A, B = chains[ids[0]], chains[ids[-1]]           # A=design(short) B=receptor(long)
    na, nb = len(A), len(B)
    # epitope contacts
    Bheavy = {r.id[1]: np.array([at.coord for at in heavy(r)]) for r in B}
    contacted, nmin_u, nmin_d = set(), None, 1e9
    for i, ra in enumerate(A):
        aco = np.array([at.coord for at in heavy(ra)])
        if not len(aco): continue
        for bnum, bco in Bheavy.items():
            if not len(bco): continue
            d = np.sqrt(((aco[:, None] - bco[None]) ** 2).sum(-1)).min()
            if d <= CONTACT_A: contacted.add(bnum + OFFSET)
            if i == 0 and d < nmin_d: nmin_d, nmin_u = d, bnum + OFFSET
    conf = json.load(open(conf_json))
    pae = load_pae(pae_npz)
    ipsae_min = iPAE = None
    if pae is not None and pae.shape[0] >= na + nb:
        try:
            ipsae_min = ipsae.score_interface(pae, list(range(na)), list(range(na, na + nb)))["esmfold2_ipsae_min"]
        except Exception:
            ipsae_min = None
        ab = pae[:na, na:na + nb]; ba = pae[na:na + nb, :na]
        iPAE = float((ab.min(1).mean() + ba.min(1).mean()) / 2)
    return {
        "ipsae": round(ipsae_min, 4) if ipsae_min is not None else None,
        "iptm": round(float(conf.get("iptm", 0)), 3),
        "ipae": round(iPAE, 2) if iPAE is not None else None,
        "vest": sorted(contacted & VESTIBULE),
        "cp": sorted(contacted & CENTRAL_POLAR),
        "r299": 299 in contacted,
        "nterm_in7TM": bool(nmin_u is not None and nmin_u >= 140 and nmin_d <= CONTACT_A),
    }

def main(work, out):
    cifs = sorted(glob.glob(os.path.join(work, "boltz", "**", "*_model_0.cif"), recursive=True))
    per = {}  # name -> list of seed dicts
    for cif in cifs:
        base = os.path.basename(cif).replace("_model_0.cif", "")
        d = os.path.dirname(cif)
        pae = os.path.join(d, f"pae_{base}_model_0.npz")
        conf = os.path.join(d, f"confidence_{base}_model_0.json")
        if not (os.path.exists(pae) and os.path.exists(conf)): continue
        try:
            per.setdefault(base, []).append(score_cif(cif, pae, conf))
        except Exception as e:
            print("skip", base, e, file=sys.stderr)
    # cheap screens
    cheap = {r["name"]: r for r in csv.DictReader(open(f"{REPO}/runs/picker/pool_screened.csv"))}
    rows = []
    for name, seeds in per.items():
        ips = [s["ipsae"] for s in seeds if s["ipsae"] is not None]
        ipt = [s["iptm"] for s in seeds]
        ipa = [s["ipae"] for s in seeds if s["ipae"] is not None]
        r299 = sum(1 for s in seeds if s["r299"])
        vest_union = sorted(set().union(*[set(s["vest"]) for s in seeds])) if seeds else []
        cp_union = sorted(set().union(*[set(s["cp"]) for s in seeds])) if seeds else []
        nterm = sum(1 for s in seeds if s["nterm_in7TM"])
        c = cheap.get(name, {})
        rows.append({
            "name": name, "sequence": c.get("sequence", ""), "family": c.get("family", "?"),
            "length": c.get("length", ""), "n_cys": c.get("n_cys", ""), "gravy": c.get("gravy", ""),
            "graft_max": c.get("graft_max", ""), "in_v10": c.get("in_v10", ""),
            "ipsae_best": round(max(ips), 4) if ips else None,
            "ipsae_med": round(float(np.median(ips)), 4) if ips else None,
            "iptm_best": round(max(ipt), 3) if ipt else None,
            "ipae_best": round(min(ipa), 2) if ipa else None,
            "n_seeds": len(seeds), "r299_n": r299,
            "vestibule": "|".join(map(str, vest_union)), "central_polar": "|".join(map(str, cp_union)),
            "nterm_in7TM_n": nterm,
            "epitope": "vestibule" if (299 in vest_union or len(vest_union) >= 2) else ("ECD/other" if vest_union == [] else "weak-vest"),
        })
    rows.sort(key=lambda r: (-(r["ipsae_best"] or 0)))
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), lineterminator="\n")
        w.writeheader(); w.writerows(rows)
    print(f"scored {len(rows)} designs -> {out}")
    print("top-8 by ipsae_best:")
    for r in rows[:8]:
        print(f"  {r['name']:22s} {r['family']:11s} ipSAE {r['ipsae_best']} iptm {r['iptm_best']} r299 {r['r299_n']}/{r['n_seeds']} epi {r['epitope']} in_v10={r['in_v10']}")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
