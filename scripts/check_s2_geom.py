"""Two-site geometry evaluator for the S2 two-domain agonist wave. A folded de-novo binder
CANNOT reach the deep/buried vestibule (lesson-denovo-binder-cant-reach-buried-pocket), and
af2ig/AF2 are membrane-blind so they cannot gate a vestibule contact — so after RFd generates
binders in the GLP-1 cleft, this script asks GEOMETRICALLY, per design: does the binder (chain A)
contact BOTH the ECD domain (the validated-anchorable address) AND the accessible upper vestibule
(the orforglipron-region message site)? A TWO_SITE design is an S2 agonism bet (the ECD contact
is then af2ig-validated separately; the vestibule reach stays a labeled mechanistic hypothesis).
An ecd_only design is just another ECD binder (hedge); vest_only/neither are discarded.

Usage: uv run python scripts/check_s2_geom.py runs/rfd/<sub>
"""
from __future__ import annotations
import glob, os, sys
import numpy as np
from Bio.PDB import PDBParser

ECD_RANGE = set(range(29, 130))                                  # the soluble ECD (anchor/address)
VEST_ACCESSIBLE = {145, 197, 211, 214, 215, 298, 299, 300, 306}  # accessible upper vestibule (orforglipron region)
CONTACT_A = 5.0
N_SITE_MIN = 3   # >=3 heavy-atom contacts to call a site engaged


def heavy(res):
    return [a for a in res if a.element not in ("H", "D")]


def ca_coords(chain):
    return {r.id[1]: r["CA"].coord for r in chain if r.id[0] == " " and "CA" in r}


def rg(coords):
    x = np.array(list(coords.values())); c = x.mean(0)
    return float(np.sqrt(((x - c) ** 2).sum(1).mean()))


def analyze(pdb):
    st = PDBParser(QUIET=True).get_structure("x", pdb)
    model = next(iter(st))
    chains = {c.id: c for c in model}
    if "A" not in chains or "R" not in chains:
        return None
    binder, recep = chains["A"], chains["R"]
    bca = ca_coords(binder)
    rca = ca_coords(recep)
    bheavy = np.array([a.coord for r in binder if r.id[0] == " " for a in heavy(r)])
    rres = {r.id[1]: np.array([a.coord for a in heavy(r)]) for r in recep if r.id[0] == " "}
    contacted = set()
    for num, rco in rres.items():
        if len(rco) and np.sqrt(((bheavy[:, None, :] - rco[None, :, :]) ** 2).sum(-1)).min() <= CONTACT_A:
            contacted.add(num)
    ecd_hits = sorted(contacted & ECD_RANGE)
    vest_hits = sorted(contacted & VEST_ACCESSIBLE)
    # span = max distance between any ECD-contacted CA and any vestibule-contacted CA (true two-site reach)
    span = 0.0
    if ecd_hits and vest_hits:
        e = np.array([rca[h] for h in ecd_hits if h in rca])
        v = np.array([rca[h] for h in vest_hits if h in rca])
        span = float(np.sqrt(((e[:, None, :] - v[None, :, :]) ** 2).sum(-1)).max())
    n_e, n_v = len(ecd_hits), len(vest_hits)
    if n_e >= N_SITE_MIN and n_v >= N_SITE_MIN:
        verdict = "TWO_SITE"
    elif n_e >= N_SITE_MIN:
        verdict = "ecd_only"
    elif n_v >= N_SITE_MIN:
        verdict = "vest_only"
    else:
        verdict = "neither"
    return {"nres": len(bca), "rg": round(rg(bca), 1), "n_ecd": n_e, "n_vest": n_v,
            "vest_hits": vest_hits, "span": round(span, 1), "verdict": verdict}


def main():
    d = sys.argv[1]
    pdbs = sorted(glob.glob(os.path.join(d, "des_*.pdb")))
    print(f"# {len(pdbs)} designs in {d} | ECD=29-129  VEST_accessible={sorted(VEST_ACCESSIBLE)}  contact<={CONTACT_A}A")
    print(f"{'design':<12}{'nres':>5}{'Rg':>6}{'nECD':>6}{'nVEST':>6}{'vestHits':>22}{'span':>7}  verdict")
    counts = {}
    for p in pdbs:
        r = analyze(p)
        if r is None:
            print(f"{os.path.basename(p):<12}  <no A/R chains>"); continue
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
        print(f"{os.path.basename(p).replace('.pdb',''):<12}{r['nres']:>5}{r['rg']:>6}{r['n_ecd']:>6}{r['n_vest']:>6}"
              f"{str(r['vest_hits']):>22}{r['span']:>7}  {r['verdict']}")
    print(f"# verdicts: {counts}")


if __name__ == "__main__":
    main()
