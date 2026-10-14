#!/usr/bin/env python3
"""Compare DiffPepBuilder vest2 keepers to the EvoBind agonism arm on IDENTICAL footing:
full-receptor AF2 (EvoBind predict_only) pose -> R299 (construct res 276) + message-reader engagement
+ self-disulfide. Removes the DiffPepBuilder 12-residue-crop artifact. Writes
data/candidates/diffpep_vest2_fullfold.csv."""
import os, csv, math
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRED = os.path.join(REPO, "runs/evobind_predict")
OUT = os.path.join(REPO, "data/candidates/diffpep_vest2_fullfold.csv")
READERS = [167,171,174,178,181,182,187,188,191,192,198,207,210,211,214,218,
           272,275,276,277,283,286,287,290]
R299 = 276  # construct fasta residue == UniProt 299 (His7 reader), receptor numbered 1..409

def parse(path):
    order, res = [], {}
    for ln in open(path):
        if ln.startswith("ATOM"):
            key = (ln[21], int(ln[22:26])); atom = ln[12:16].strip()
            res.setdefault(key, {})
            if key not in order: order.append(key)
            res[key][atom] = (float(ln[30:38]), float(ln[38:46]), float(ln[46:54]))
    return order, res

def dd(a, b): return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)
def heavy(d): return [c for a, c in d.items() if not a.startswith("H")]

cand = {r["name"]: r for r in csv.DictReader(open(os.path.join(REPO, "data/candidates/diffpep_vest2_eval.csv")))}
keep = [r for r in cand.values() if r["keep"] == "True"]

rows = []
for r in keep:
    name = r["name"]; seq = r["sequence"]; L = len(seq)
    pdb = f"{PRED}/ppv2_{name}/unrelaxed_true.pdb"
    if not os.path.exists(pdb):
        continue
    order, res = parse(pdb)
    pep = order[-L:]
    pep_h = [c for k in pep for c in heavy(res[k])]
    rec = {}
    for k in order[:-L]:
        rec.setdefault(k[1], []).extend(heavy(res[k]))
    def mind(rs): return min((dd(p, a) for p in pep_h for a in rec.get(rs, [])), default=999)
    per = [mind(x) for x in READERS]
    n45 = sum(1 for x in per if x <= 4.5)
    r299 = mind(R299)
    m = f"{PRED}/ppv2_{name}/metrics.csv"
    plddt = ifd = float("nan")
    if os.path.exists(m):
        row = list(csv.DictReader(open(m)))[-1]; plddt = float(row["plddt"]); ifd = float(row["if_dist_peptide"])
    # self-disulfide in this fold
    cys = [(i+1, res[pep[i]].get("SG")) for i in range(L) if seq[i] == "C" and res[pep[i]].get("SG")]
    ss = [dd(cys[a][1], cys[b][1]) for a in range(len(cys)) for b in range(a+1, len(cys)) if cys[a][1] and cys[b][1]]
    self_ss = any(d <= 2.6 for d in ss)
    rows.append({"name": name, "length": L, "n_cys": seq.count("C"),
                 "fullfold_R299": round(r299, 2), "reaches_R299": r299 <= 4.5, "readers45": n45,
                 "plddt": round(plddt, 1), "if_dist": round(ifd, 2),
                 "dpb_pose_R299": r["minD_R299"], "elig_pid": r["elig_pid"], "elig_cov": r["elig_cov"],
                 "self_ss": self_ss, "dev_flags": r["dev_flags"], "sequence": seq})

rows.sort(key=lambda r: r["fullfold_R299"])
cols = ["name", "length", "n_cys", "fullfold_R299", "reaches_R299", "readers45", "plddt", "if_dist",
        "dpb_pose_R299", "elig_pid", "elig_cov", "self_ss", "dev_flags", "sequence"]
with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
    for r in rows: w.writerow(r)

reach = sum(1 for r in rows if r["reaches_R299"])
print(f"=== DiffPepBuilder vest2 keepers, full-receptor AF2 fold (n={len(rows)}) ===")
print(f"{reach}/{len(rows)} reach R299 <4.5A (vs EvoBind arm: 7/12 in >=1 fold).")
print(f"{'name':10s}{'L':>3s}{'Cys':>4s}{'ffR299':>7s}{'rd45':>5s}{'plddt':>6s}{'ifd':>6s}{'id%':>6s}  dev  seq")
for r in rows[:14]:
    print(f"{r['name']:10s}{r['length']:>3d}{r['n_cys']:>4d}{r['fullfold_R299']:>7.2f}{r['readers45']:>5d}"
          f"{r['plddt']:>6.1f}{r['if_dist']:>6.2f}{r['elig_pid']:>6.1f}  {r['dev_flags'][:16]:16s} {r['sequence']}")
print(f"Wrote {OUT}")
