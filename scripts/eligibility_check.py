"""Eligibility hard-avoid gate: for each design, max % sequence identity to the known
GLP1R agonists / incretin peptides (data/novelty/known_agonists.fasta). The challenge
forbids modifying GLP-1 / exendin-4 / semaglutide / known binders into candidates; a
de-novo design (esp. an EvoBind vestibule peptide) must NOT accidentally resemble them.
MMseqs is insensitive for short peptides, so this uses exact local (Smith-Waterman)
pairwise identity. Flag if max identity > 30% (configs/filters.yaml known_agonist_id_max_pct)
AND the alignment covers >= COV_MIN of the design (a short spurious high-id patch must NOT
flag; a GLP-1-derived design must).

Importable: `build_scorer()` + `score_design(seq, refs, aligner)` are the single source of
truth for the eligibility verdict (reused by scripts/build_candidate_register.py).
The Proteinbase portal remains the authority; re-check before any upload.

Usage: uv run python scripts/eligibility_check.py <designs.csv|designs.fasta> [id_cut=30]
CSV must have columns name,sequence.
"""
from __future__ import annotations
import csv, sys, os
from Bio import Align
from Bio.Align import substitution_matrices

REF = os.path.join(os.path.dirname(__file__), "..", "data", "novelty", "known_agonists.fasta")
COV_MIN = 0.50
ID_CUT = 30.0


def read_fasta(p):
    out, name, seq = {}, None, []
    for ln in open(p):
        ln = ln.strip()
        if ln.startswith(">"):
            if name:
                out[name] = "".join(seq)
            name, seq = ln[1:].split()[0], []
        elif ln:
            seq.append(ln)
    if name:
        out[name] = "".join(seq)
    return out


def read_designs(p):
    if p.endswith(".fasta") or p.endswith(".fa"):
        return list(read_fasta(p).items())
    rows = []
    for r in csv.DictReader(open(p)):
        if r.get("sequence"):
            rows.append((r["name"], r["sequence"].strip()))
    return rows


def build_scorer():
    """Return (refs, aligner) for score_design; load once, reuse across designs."""
    refs = read_fasta(REF)
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = "local"
    return refs, aligner


def score_design(seq, refs, aligner, id_cut=ID_CUT, cov_min=COV_MIN) -> dict:
    """Single source of truth for the eligibility verdict of one sequence.
    FLAG = a SUBSTANTIAL match: local identity > id_cut AND coverage >= cov_min."""
    best = (0.0, 0.0, 0.0, "-")  # (concern_score, pid, cov, nearest)
    for rn, rs in refs.items():
        aln = aligner.align(seq, rs)[0]
        a, b = aln[0], aln[1]
        idn = sum(1 for x, y in zip(a, b) if x == y and x != "-")
        allen = sum(1 for x, y in zip(a, b) if x != "-" and y != "-")
        pid = 100.0 * idn / allen if allen else 0.0
        cov = allen / len(seq) if len(seq) else 0.0
        score = pid if cov >= cov_min else pid * cov / cov_min
        if score > best[0]:
            best = (score, pid, cov, rn)
    _, pid, cov, rn = best
    flag = pid > id_cut and cov >= cov_min
    return {"pid": pid, "cov": cov, "nearest": rn, "flag": flag}


def main():
    designs = read_designs(sys.argv[1])
    id_cut = float(sys.argv[2]) if len(sys.argv) > 2 else ID_CUT
    refs, aligner = build_scorer()
    print(f"{'design':<24}{'len':>4}{'id%':>6}{'cov':>6}{'nearest':>16}  eligible")
    n_flag = 0
    for name, seq in designs:
        r = score_design(seq, refs, aligner, id_cut)
        n_flag += r["flag"]
        print(f"{name:<24}{len(seq):>4}{r['pid']:>6.1f}{r['cov']:>6.2f}{r['nearest']:>16}  {'FLAG' if r['flag'] else 'OK'}")
    print(f"# {len(designs)} designs | FLAG(id>{id_cut}% AND cov>={COV_MIN}) = {n_flag}  (portal is authority; re-check pre-upload)")


if __name__ == "__main__":
    main()
