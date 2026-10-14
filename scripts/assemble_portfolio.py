"""Assemble a revised Track-3 submission from an EXPLICIT ordered list of internal design names.

Resolves each internal name (rank order, best-first) to its sequence + arm + metrics from the
versioned candidate registers, emits the submission CSV (name,sequence,molecule_class) + a mapping
+ the DERIVED eligibility watchlist, and fails LOUD on any unresolved name or duplicate sequence.

Sources (single source of truth, no hand-transcription):
  - data/candidates/candidates.csv         (EvoBind eb_* peptides, ecd_des_* ECD binders)
  - data/candidates/diffpep_vest2_eval.csv  (DiffPepBuilder dpbv2_* orthogonal-method peptides)
  - data/candidates/pepglad_longshot.csv    (PepGLAD pglad_* orthogonal-method peptides; long-shot)

Usage: uv run python assemble_portfolio.py <order.txt> <out_dir> [version=v3]
  order.txt: one internal name per line (rank order); blank lines / # comments ignored.
  version:   output filename tag -> glp1r_track3_<version>.csv (default v3; pass v4 etc. so a new
             build never clobbers an existing submission).
"""
from __future__ import annotations
import csv, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import eligibility_check as elig      # noqa: E402
import developability as dev          # noqa: E402


def load_sources():
    cand = {r["name"]: r for r in csv.DictReader(open(os.path.join(REPO, "data/candidates/candidates.csv")))}
    dpb = {r["name"]: r for r in csv.DictReader(open(os.path.join(REPO, "data/candidates/diffpep_vest2_eval.csv")))}
    dpbg = {r["name"]: r for r in csv.DictReader(open(os.path.join(REPO, "data/candidates/diffpep_gated.csv")))}
    pglad_p = os.path.join(REPO, "data/candidates/pepglad_longshot.csv")
    pglad = {r["name"]: r for r in csv.DictReader(open(pglad_p))} if os.path.exists(pglad_p) else {}
    return cand, dpb, dpbg, pglad


def resolve(name, cand, dpb, dpbg, pglad):
    """Return (sequence, arm, source, metrics) or raise. DiffPepBuilder + PepGLAD peptides = agonism-peptide."""
    if name in cand:
        r = cand[name]
        return r["sequence"].strip().upper(), r["arm"], "candidates", r
    if name in dpb:
        r = dpb[name]
        return r["sequence"].strip().upper(), "agonism-peptide", "diffpep_vest2", r
    if name in dpbg:
        r = dpbg[name]
        return r["sequence"].strip().upper(), "agonism-peptide", "diffpep_vest", r
    if name in pglad:
        r = pglad[name]
        return r["sequence"].strip().upper(), "agonism-peptide", "pepglad_longshot", r
    raise SystemExit(f"FATAL: internal name '{name}' not found in candidates.csv / diffpep_vest2_eval.csv / diffpep_gated.csv / pepglad_longshot.csv")


def main():
    order_f, out_dir = sys.argv[1], sys.argv[2]
    ver = sys.argv[3] if len(sys.argv) > 3 else "v3"
    names = [ln.strip() for ln in open(order_f) if ln.strip() and not ln.startswith("#")]
    if len(names) != len(set(names)):
        raise SystemExit("FATAL: duplicate internal name in order file")
    if len(names) > 20:
        raise SystemExit(f"FATAL: {len(names)} designs > 20 cap")
    cand, dpb, dpbg, pglad = load_sources()
    refs, aligner = elig.build_scorer()
    os.makedirs(out_dir, exist_ok=True)

    sub, mapping, elig_rows, seqs = [], [], [], {}
    for rank, internal in enumerate(names, 1):
        seq, arm, src, r = resolve(internal, cand, dpb, dpbg, pglad)
        if seq in seqs:
            raise SystemExit(f"FATAL: duplicate sequence {internal} == {seqs[seq]}")
        seqs[seq] = internal
        tag = "ago" if arm == "agonism-peptide" else "bind"
        subname = f"glp1r_{rank:02d}_{tag}"
        sub.append((subname, seq, "protein"))
        a = dev.analyze(seq)
        e = elig.score_design(seq, refs, aligner)
        mapping.append((rank, subname, internal, arm, src, len(seq), ",".join(a["flags"]) or "clean",
                        f"{e['pid']:.1f}", f"{e['cov']:.2f}", e["nearest"]))
        if arm == "agonism-peptide":
            concern = e["pid"] if e["cov"] >= 0.50 else e["pid"] * e["cov"] / 0.50
            elig_rows.append((subname, internal, f"{e['pid']:.1f}", f"{e['cov']:.2f}", e["nearest"],
                              f"{concern:.1f}", "recheck" if e["pid"] >= 50.0 else "ok"))

    sub_p = os.path.join(out_dir, f"glp1r_track3_{ver}.csv")
    with open(sub_p, "w", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n"); w.writerow(["name", "sequence", "molecule_class"]); w.writerows(sub)
    with open(os.path.join(out_dir, f"glp1r_track3_{ver}_mapping.csv"), "w", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["rank", "submission_name", "internal_name", "arm", "source", "length", "dev_flags", "elig_id_pct", "elig_cov", "elig_nearest"])
        w.writerows(mapping)
    elig_rows.sort(key=lambda r: -float(r[2]))
    with open(os.path.join(out_dir, f"glp1r_track3_{ver}_eligibility.csv"), "w", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["submission_name", "internal_name", "raw_id_pct", "coverage", "nearest_incretin", "cov_gated_concern", "portal_recheck"])
        w.writerows(elig_rows)

    print(f"wrote {sub_p} ({len(sub)} designs)")
    n_ago = sum(1 for _, _, _, arm, *_ in mapping if arm == "agonism-peptide")
    print(f"  arms: {n_ago} agonism-peptide + {len(mapping)-n_ago} binding-hedge")
    print(f"  sources: candidates={sum(1 for m in mapping if m[4]=='candidates')} diffpep={sum(1 for m in mapping if m[4]=='diffpep')}")
    print(f"  portal_recheck (new/uncleared id>=50%): {sum(1 for e in elig_rows if e[6]=='recheck')}")
    print(f"{'rank':>4} {'subname':<16}{'internal':<14}{'arm':<16}{'src':<12}{'flags':<20}elig")
    for rk, sn, intn, arm, src, ln, fl, pid, cov, near in mapping:
        print(f"{rk:>4} {sn:<16}{intn:<14}{arm:<16}{src:<12}{fl:<20}{pid}%/{cov} {near}")


if __name__ == "__main__":
    main()
