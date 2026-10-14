"""Brutal per-design liability stress test (CPU, deterministic).

Extends scripts/developability.analyze + scripts/eligibility_check.score_design with the
metrics the existing flags MISS, which matter for a submission-quality audit:
  - longest CONTIGUOUS single-residue run (catches poly-Ala extensions that maxfrac dilutes)
  - Shannon entropy (bits) over AA composition (global low-complexity)
  - longest common substring vs EACH incretin (graft detector; the audit's "<=3 identical run")
  - oxidation-prone Met/Trp count + fraction
  - deamidation (NG/NS/NT) and isomerization (DG/DP) motif counts
  - N-terminal pyroGlu risk (Q/E), C-terminal
  - theoretical pI (ProtParam)
Everything here RANKS RELATIVE RISK; nothing is a wet-lab truth. Portal is the novelty authority.

Usage: uv run python stress_liab.py <submission.csv>   (cols name,sequence[,molecule_class])
Writes <out>.json + prints a table. Paths are resolved to the repo so it is run-location agnostic.
"""
from __future__ import annotations
import csv, sys, json, math, collections, os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import developability as dev          # noqa: E402
import eligibility_check as elig      # noqa: E402


def longest_run(s: str):
    best_c, best_n = "-", 0
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        if j - i > best_n:
            best_c, best_n = s[i], j - i
        i = j
    return best_c, best_n


def shannon_bits(s: str) -> float:
    n = len(s)
    if not n:
        return 0.0
    c = collections.Counter(s)
    return -sum((v / n) * math.log2(v / n) for v in c.values())


def lcs_substr(a: str, b: str) -> int:
    """Longest common CONTIGUOUS substring length (graft detector)."""
    if not a or not b:
        return 0
    prev = [0] * (len(b) + 1)
    best = 0
    for i in range(1, len(a) + 1):
        cur = [0] * (len(b) + 1)
        ai = a[i - 1]
        for j in range(1, len(b) + 1):
            if ai == b[j - 1]:
                cur[j] = prev[j - 1] + 1
                if cur[j] > best:
                    best = cur[j]
        prev = cur
    return best


def pI(s: str):
    try:
        from Bio.SeqUtils.ProtParam import ProteinAnalysis
        return ProteinAnalysis(s).isoelectric_point()
    except Exception:
        return float("nan")


def count_motifs(s: str, motifs):
    return {m: sum(1 for i in range(len(s) - 1) if s[i:i + 2] == m) for m in motifs}


def main():
    sub = sys.argv[1]
    rows = [(r["name"], r["sequence"].strip().upper()) for r in csv.DictReader(open(sub)) if r.get("sequence")]
    refs, aligner = elig.build_scorer()
    out = []
    for name, s in rows:
        a = dev.analyze(s)
        e = elig.score_design(s, refs, aligner)
        run_c, run_n = longest_run(s)
        lcs = {rn: lcs_substr(s, rs) for rn, rs in refs.items()}
        lcs_max_ref = max(lcs, key=lcs.get)
        deam = count_motifs(s, ["NG", "NS", "NT"])
        isom = count_motifs(s, ["DG", "DP"])
        rec = {
            "name": name, "len": a["len"], "seq": s,
            "cys": a["cys"], "cys_parity": "odd(free-thiol)" if a["cys"] % 2 else ("even" if a["cys"] else "none"),
            "longest_run_res": run_c, "longest_run_len": run_n,
            "maxfrac": round(a["maxfrac"], 3), "entropy_bits": round(shannon_bits(s), 2),
            "gravy": round(a["gravy"], 2), "arom_frac": round(a["arom"], 3),
            "net_charge": a["charge"], "pI": round(pI(s), 1), "instab": round(a["instab"], 1),
            "met": s.count("M"), "trp": s.count("W"), "ox_frac": round((s.count("M") + s.count("W")) / len(s), 3),
            "deamid_NG_NS_NT": sum(deam.values()), "isom_DG_DP": sum(isom.values()),
            "nterm": s[0], "cterm": s[-1], "pyroglu_risk": s[0] in "QE",
            "elig_pid": round(e["pid"], 1), "elig_cov": round(e["cov"], 2), "elig_nearest": e["nearest"], "elig_flag": e["flag"],
            "lcs_max": lcs[lcs_max_ref], "lcs_max_ref": lcs_max_ref,
            "dev_flags": a["flags"],
        }
        # composite liability flags (surfacing, not a hard gate)
        liab = []
        if a["cys"] % 2 == 1:
            liab.append(f"FREE-THIOL(C{a['cys']})")
        if run_n >= 6:
            liab.append(f"POLYRUN({run_c}x{run_n})")
        elif a["maxfrac"] > 0.30:
            liab.append(f"LOWCPLX({a['maxaa_res']}{a['maxfrac']:.0%})")
        if a["instab"] == a["instab"] and a["instab"] > 60:
            liab.append(f"INSTAB++({a['instab']:.0f})")
        elif a["instab"] == a["instab"] and a["instab"] > 40:
            liab.append(f"instab({a['instab']:.0f})")
        if a["gravy"] > 0.5:
            liab.append(f"HYDROPHOBIC({a['gravy']:.2f})")
        if e["flag"]:
            liab.append(f"ELIG-ID({e['pid']:.0f}%/{e['cov']:.2f}→{e['nearest']})")
        if rec["lcs_max"] >= 6:
            liab.append(f"GRAFT(lcs{rec['lcs_max']}→{lcs_max_ref})")
        if (s.count("M") + s.count("W")) / len(s) > 0.12:
            liab.append(f"OXID({s.count('M')}M{s.count('W')}W)")
        rec["liabilities"] = liab
        rec["n_liab"] = len(liab)
        out.append(rec)

    outp = sys.argv[2] if len(sys.argv) > 2 else "stress_liab.json"
    json.dump(out, open(outp, "w"), indent=2)
    # table
    hdr = f"{'name':<14}{'len':>4}{'Cys':>4}{'run':>7}{'ent':>5}{'gravy':>6}{'instab':>7}{'ox':>5}{'pI':>5}{'elig':>14}{'lcs':>5}  LIABILITIES"
    print(hdr)
    print("-" * len(hdr))
    for r in sorted(out, key=lambda x: -x["n_liab"]):
        print(f"{r['name']:<14}{r['len']:>4}{r['cys']:>4}{r['longest_run_res']+str(r['longest_run_len']):>7}"
              f"{r['entropy_bits']:>5.1f}{r['gravy']:>6.2f}{r['instab']:>7.1f}{r['ox_frac']*100:>4.0f}%{r['pI']:>5.1f}"
              f"{r['elig_pid']:>6.0f}%/{r['elig_cov']:<3.2f}{r['elig_nearest'][:6]:>7}{r['lcs_max']:>5}  {', '.join(r['liabilities']) or 'CLEAN'}")
    print(f"\n# {len(out)} designs | wrote {outp}")
    print(f"# n_liab distribution: " + ", ".join(f"{k}→{v}" for k, v in sorted(collections.Counter(r['n_liab'] for r in out).items())))


if __name__ == "__main__":
    main()
