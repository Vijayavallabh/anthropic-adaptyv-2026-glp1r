"""Stage 0 — target preparation for the GLP1R agonist campaign.

Produces the design/scoring inputs (CPU/light; no generation GPU):
  * data/raw/6X18.cif                 — the clean human ACTIVE-state complex (download; gitignored)
  * data/raw/6X18_receptorR.pdb       — receptor chain R = active-state design/scoring target
  * data/raw/6X18_peptideP.pdb        — GLP-1 chain P = positive-control "message" geometry
  * data/target/construct_24_432.fasta— WT P43220 24-432 (binding-assay construct model; thermostab. muts unknown)
  * data/target/hotspots.json         — ECD-groove + 7TM-vestibule hotspot residues (resolved from target.yaml)
  * data/controls/positive_agonists.fasta — GLP-1(7-36), exendin-4 (CALIBRATION ONLY — never design seeds)
  * data/target/manifest.json         — provenance + md5 checksums + modeled-range/gap notes

Run:  uv run python src/adaptyv_glp1r/stage0_target_prep.py
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
from pathlib import Path

import requests
import yaml

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "raw"
TGT = ROOT / "data" / "target"
CTL = ROOT / "data" / "controls"

PDB_ID = "6X18"
UNIPROT = "P43220"
CONSTRUCT_RANGE = (24, 432)  # Sino 13944-H18H-DD expressed range (inclusive, UniProt numbering)

# Known control agonists — CALIBRATION ONLY (positive controls for scoring); NEVER design seeds.
POSITIVE_CONTROLS = {
    "GLP1_7_36_NH2": "HAEGTFTSDVSSYLEGQAAKEFIAWLVKGR",
    "exendin_4": "HGEGTFTSDLSKQMEEEAVRLFIEWLKNGGPSSGAPPPS",
}


def _md5(p: Path) -> str:
    h = hashlib.md5()
    h.update(p.read_bytes())
    return h.hexdigest()


def _get(url: str) -> bytes:
    r = requests.get(url, timeout=120, headers={"User-Agent": "adaptyv-glp1r/0.1"})
    r.raise_for_status()
    return r.content


def fetch_structure() -> Path:
    RAW.mkdir(parents=True, exist_ok=True)
    cif = RAW / f"{PDB_ID}.cif"
    if not cif.exists():
        cif.write_bytes(_get(f"https://files.rcsb.org/download/{PDB_ID}.cif"))
    return cif


def extract_chain(structure, chain_id: str, out: Path):
    """Write one chain's standard+hetero residues to a PDB; return (resnums, gaps)."""
    from Bio.PDB import PDBIO, Select

    model = next(iter(structure))
    if chain_id not in {c.id for c in model}:
        raise KeyError(f"chain {chain_id} not in {PDB_ID} (have {[c.id for c in model]})")

    class _Keep(Select):
        def accept_chain(self, c):
            return c.id == chain_id

    io = PDBIO()
    io.set_structure(structure)
    out.parent.mkdir(parents=True, exist_ok=True)
    io.save(str(out), _Keep())

    resnums = sorted(r.id[1] for r in model[chain_id] if r.id[0] == " ")
    gaps = [(a, b) for a, b in zip(resnums, resnums[1:]) if b - a > 1]
    return resnums, gaps


def construct_sequence() -> str:
    fa = _get(f"https://rest.uniprot.org/uniprotkb/{UNIPROT}.fasta").decode()
    seq = "".join(l.strip() for l in fa.splitlines() if not l.startswith(">"))
    lo, hi = CONSTRUCT_RANGE
    sub = seq[lo - 1 : hi]  # 1-based inclusive -> slice
    assert len(seq) == 463, f"unexpected P43220 length {len(seq)}"
    assert sub[0] == "R", f"construct must start at Arg24, got {sub[0]}"
    assert len(sub) == hi - lo + 1 == 409, f"construct length {len(sub)} != 409"
    return sub


def write_fasta(path: Path, records: dict[str, str]):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(f">{k}\n{v}\n" for k, v in records.items()))


def run() -> dict:
    from Bio.PDB import MMCIFParser

    cif = fetch_structure()
    structure = MMCIFParser(QUIET=True).get_structure(PDB_ID, str(cif))

    r_res, r_gaps = extract_chain(structure, "R", RAW / f"{PDB_ID}_receptorR.pdb")
    p_res, _ = extract_chain(structure, "P", RAW / f"{PDB_ID}_peptideP.pdb")

    construct = construct_sequence()
    write_fasta(TGT / "construct_24_432.fasta", {"GLP1R_P43220_24_432_WTmodel": construct})
    write_fasta(CTL / "positive_agonists.fasta", POSITIVE_CONTROLS)

    hotspots = yaml.safe_load((ROOT / "configs" / "target.yaml").read_text())["hotspots"]
    (TGT / "hotspots.json").write_text(json.dumps(hotspots, indent=2))

    manifest = {
        "stage": "S0_target_prep",
        "date": _dt.date.today().isoformat(),
        "active_state_reference": {
            "pdb": PDB_ID,
            "receptor_chain": "R",
            "receptor_modeled_range": [r_res[0], r_res[-1]] if r_res else None,
            "receptor_gaps": r_gaps,
            "peptide_chain_P_range": [p_res[0], p_res[-1]] if p_res else None,
            "note": "clean human active-state (DN-Gs + Nb35); NO thermostabilizing mutations, NO BRIL/T4L.",
        },
        "binding_construct_model": {
            "uniprot": UNIPROT,
            "range": list(CONSTRUCT_RANGE),
            "length": len(construct),
            "note": "WT 24-432; the vendor construct's thermostabilizing mutations are PROPRIETARY/unknown "
                    "(not applied). Use for binding-assay passage scoring; score AGONISM against 6X18.",
        },
        "controls": {"positive": list(POSITIVE_CONTROLS), "negative": "scramble (generated at scoring, fixed seed)"},
        "files": {},
    }
    for p in [RAW / f"{PDB_ID}.cif", RAW / f"{PDB_ID}_receptorR.pdb", RAW / f"{PDB_ID}_peptideP.pdb",
              TGT / "construct_24_432.fasta", CTL / "positive_agonists.fasta", TGT / "hotspots.json"]:
        manifest["files"][str(p.relative_to(ROOT))] = {"md5": _md5(p), "bytes": p.stat().st_size}

    (TGT / "manifest.json").write_text(json.dumps(manifest, indent=2))
    return manifest


if __name__ == "__main__":
    m = run()
    print(json.dumps(m, indent=2))
