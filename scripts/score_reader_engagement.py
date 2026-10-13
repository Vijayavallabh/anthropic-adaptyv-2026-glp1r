#!/usr/bin/env python3
"""Mechanism-grounded AGONISM-plausibility evidence for the 12 EvoBind agonism peptides.

if_dist (EvoBind's proxy) is a MEAN distance to the whole GLP-1 interface and does not say whether a
peptide reaches the activation-critical MESSAGE-READER residues. This script measures, from the actual
predicted bound poses, how many of the 24 6X18-derived message-reader residues each peptide contacts,
and its distance to R299 (ECL2 Arg that reads GLP-1 His7), across TWO independent folds:
  (A) the mid-MC EvoBind design pose (min-if_dist iteration), and
  (B) a fresh fixed-seed predict_only fold (runs/evobind_predict/pp_<run>/unrelaxed_true.pdb).
It also reports self-disulfide formation (Cys Sgamma-Sgamma) in the fresh fold.

Robustness: a contact claim counts only if it holds in BOTH folds. Still LOW-confidence, single-engine
(AF2), inactive-biased receptor -> NO in-silico score proves agonism; this ranks mechanism plausibility.

Regenerate poses first: scripts/gen_evobind.sh (design) + scripts/eval_evobind_predict.sh (fresh folds).
Writes: data/candidates/agonism_reader_engagement.csv
"""
import os, csv, math

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUNS = f"{REPO}/runs/evobind"
PRED = f"{REPO}/runs/evobind_predict"
OUT_CSV = f"{REPO}/data/candidates/agonism_reader_engagement.csv"

# 6X18 GLP-1 message-contact residues (fasta idx = UniProt-23; receptor PDB is fasta-numbered 1..409)
READERS = [167,171,174,178,181,182,187,188,191,192,198,207,210,211,214,218,
           272,275,276,277,283,286,287,290]
R299 = 276  # ECL2 Arg that reads GLP-1 His7 (UniProt 299)

mp = {r['internal_name']: r for r in csv.DictReader(open(f"{REPO}/submissions/glp1r_track3_mapping.csv"))}
cand = {r['name']: r for r in csv.DictReader(open(f"{REPO}/data/candidates/candidates.csv"))}
AGO = sorted((k for k, v in mp.items() if v['arm'] == 'agonism-peptide'), key=lambda k: int(mp[k]['rank']))

def parse(path):
    order, res = [], {}
    for ln in open(path):
        if ln.startswith(("ATOM", "HETATM")):
            key = (ln[21], int(ln[22:26])); atom = ln[12:16].strip()
            res.setdefault(key, {})
            if key not in order: order.append(key)
            res[key][atom] = (float(ln[30:38]), float(ln[38:46]), float(ln[46:54]))
    return order, res

def dd(a, b): return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)
def heavy(d): return [c for a, c in d.items() if not a.startswith("H")]

def engage(pdb, L, seq):
    """Return (readers_contacted_<4.5, R299_min_dist, mean_reader_dist, [(i,j,SgSg) for Cys pairs])."""
    order, res = parse(pdb)
    pep = order[-L:]
    pep_h = [c for k in pep for c in heavy(res[k])]
    rec = {}
    for k in order[:-L]:
        rec.setdefault(k[1], []).extend(heavy(res[k]))
    def mind(rs):
        return min((dd(p, a) for p in pep_h for a in rec.get(rs, [])), default=999)
    per = [mind(r) for r in READERS]
    n45 = sum(1 for x in per if x <= 4.5)
    r299d = mind(R299)
    meanD = sum(per)/len(per)
    # self-disulfide among peptide Cys (SG-SG)
    cys = [(i+1, res[pep[i]].get('SG')) for i in range(L) if seq[i] == 'C' and res[pep[i]].get('SG')]
    ss = []
    for a in range(len(cys)):
        for b in range(a+1, len(cys)):
            ss.append((cys[a][0], cys[b][0], dd(cys[a][1], cys[b][1])))
    return n45, r299d, meanD, ss

rows_out = []
print(f"{'rk':>2s} {'pep':12s} {'midR299':>7s} {'frshR299':>8s} {'midRd':>5s} {'frshRd':>6s} "
      f"{'plddt':>5s} {'robustR299':>10s} {'self-SS(A)':>10s}")
print("-"*86)
for name in AGO:
    run = name.replace("eb_", ""); L = int(cand[name]['length']); cand_seq = cand[name]['sequence']
    rank = int(mp[name]['rank'])
    # mid-MC pose
    rows = list(csv.DictReader(open(f"{RUNS}/{run}/metrics.csv")))
    bi = min(range(len(rows)), key=lambda i: float(rows[i]['if_dist_peptide']))
    mid_pdb = f"{RUNS}/{run}/unrelaxed_{rows[bi]['iteration']}.pdb"
    m_n45, m_r299, m_mean, _ = engage(mid_pdb, L, cand_seq)
    # fresh predict_only pose
    fr_dir = f"{PRED}/pp_{run}"; fr_pdb = f"{fr_dir}/unrelaxed_true.pdb"
    plddt = float('nan'); f_n45 = f_r299 = f_mean = float('nan'); ss = []
    if os.path.exists(fr_pdb):
        f_n45, f_r299, f_mean, ss = engage(fr_pdb, L, cand_seq)
        mc = f"{fr_dir}/metrics.csv"
        if os.path.exists(mc):
            plddt = float(list(csv.DictReader(open(mc)))[-1]['plddt'])
    robust = (m_r299 <= 4.5 and f_r299 <= 4.5)
    ss_clean = [(i, j, d) for i, j, d in ss if d <= 2.6]
    ss_txt = ";".join(f"{i}-{j}:{d:.1f}" for i, j, d in ss_clean) if ss_clean else "-"
    n_cys = cand_seq.count('C')
    rows_out.append({
        'rank': rank, 'name': name, 'length': L, 'n_cys': n_cys,
        'midmc_R299': f"{m_r299:.2f}", 'fresh_R299': f"{f_r299:.2f}",
        'midmc_readers45': m_n45, 'fresh_readers45': f_n45,
        'robust_reaches_R299': robust, 'fresh_plddt': f"{plddt:.1f}",
        'self_disulfide': bool(ss_clean), 'ss_sg_dist': ss_txt, 'sequence': cand_seq,
    })
    print(f"{rank:2d} {name:12s} {m_r299:7.2f} {f_r299:8.2f} {m_n45:5d} {f_n45:6d} "
          f"{plddt:5.1f} {str(robust):>10s} {ss_txt:>10s}")

os.makedirs(os.path.dirname(OUT_CSV), exist_ok=True)
with open(OUT_CSV, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows_out[0].keys()))
    w.writeheader(); w.writerows(rows_out)

n_robust = sum(1 for r in rows_out if r['robust_reaches_R299'])
n_ss = sum(1 for r in rows_out if r['self_disulfide'])
n_any = sum(1 for r in rows_out if float(r['fresh_R299']) <= 4.5 or float(r['midmc_R299']) <= 4.5)
print(f"\nSummary: {n_robust}/12 robustly reach R299 (<4.5A BOTH folds); "
      f"{n_any}/12 reach R299 in at least one fold; {n_ss}/12 form a clean self-disulfide (Sg-Sg<=2.6A).")
print(f"Wrote {OUT_CSV}")
