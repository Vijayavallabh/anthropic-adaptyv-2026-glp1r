#!/usr/bin/env python3
"""Assemble the deduplicated, firewall-clean eligible candidate pool for the
picker-rubric re-score. Schema-agnostic: pulls any peptide-like column from every
data/candidates/*.csv + the current submission, dedups by sequence, tags method
family, and applies the hard eligibility + firewall (graft) filters.

Output: runs/picker/pool.csv  (name, sequence, length, n_cys, family, in_v10, graft_max, graft_ref, elig_ok, flags)
Run with -I from repo root.
"""
import csv, glob, os, re, sys

REPO = "/home/prachh/v/anthropic-adaptyv-2026-glp1r"
AA = set("ACDEFGHIKLMNPQRSTVWY")
INCRETIN = {
    "GLP1_7_36": "HAEGTFTSDVSSYLEGQAAKEFIAWLVKGR",
    "GLP1_7_37": "HAEGTFTSDVSSYLEGQAAKEFIAWLVKGRG",
    "exendin_4": "HGEGTFTSDLSKQMEEEAVRLFIEWLKNGGPSSGAPPPS",
    "glucagon":  "HSQGTFTSDYSKYLDSRRAQDFVQWLMNT",
    "GIP_1_42":  "YAEGTFISDYSIAMDKIHQQDFVNWLLAQKGKKNDWKHNITQ",
    "lira":      "HAEGTFTSDVSSYLEGQAAKEFIAWLVRGRG",
}
TAILMOTIF = "WSHPQFEK"           # TwinStrep tag motif -> exclude tagged/construct seqs
RECEPTOR = open(f"{REPO}/data/target/construct_24_432.seq").read().strip().replace("\n", "")

def lccs(a, b):
    best = 0
    for i in range(len(a)):
        for j in range(len(b)):
            k = 0
            while i + k < len(a) and j + k < len(b) and a[i + k] == b[j + k]:
                k += 1
            best = max(best, k)
    return best

def graft(seq):
    mx, ref = 0, ""
    for n, r in INCRETIN.items():
        l = lccs(seq, r)
        if l > mx:
            mx, ref = l, n
    return mx, ref

def family(fname, name):
    f = fname.lower(); n = (name or "").lower()
    if "diffpep_ss" in f or "dpbss" in n: return "DiffPep-SS"
    if "diffpep" in f or n.startswith(("dpb", "diffpep")): return "DiffPep"
    if "boltzgen" in f or n.startswith("bg"): return "BoltzGen"
    if "pepglad" in f or n.startswith("pglad") or "pglad" in n: return "PepGLAD"
    if "pepmlm" in f or n.startswith("pepmlm"): return "PepMLM"
    if "pepgen" in f or n.startswith("pepgen"): return "PepGen"
    if "msgaddr" in f or n.startswith(("des_", "msg")): return "RFd3"
    if "evobind" in f or n.startswith(("eb_", "prod_", "accv")): return "EvoBind"
    if n.startswith("ecd") or "ecd_des" in n: return "ECD"
    if n.startswith("rm_"): return "PepGLAD"
    return "other"

def is_seqcol(vals):
    ok = 0; tot = 0
    for v in vals[:40]:
        v = (v or "").strip().upper()
        if not v: continue
        tot += 1
        if 8 <= len(v) <= 260 and set(v) <= AA: ok += 1
    return tot >= 3 and ok / max(tot, 1) >= 0.6

# v10 sequences (membership tag)
v10 = {}
with open(f"{REPO}/submissions/glp1r_track3_v10.csv") as fh:
    for r in csv.DictReader(fh):
        v10[r["sequence"]] = r["name"]

pool = {}   # sequence -> dict
def add(name, seq, fam, fromfile):
    seq = seq.strip().upper()
    if seq in pool:
        pool[seq]["families"].add(fam); return
    pool[seq] = {"name": name or f"cand_{len(pool)}", "seq": seq, "families": {fam}, "src": os.path.basename(fromfile)}

files = sorted(glob.glob(f"{REPO}/data/candidates/*.csv")) + [f"{REPO}/submissions/glp1r_track3_v10.csv"]
for fp in files:
    try:
        rows = list(csv.DictReader(open(fp)))
    except Exception:
        continue
    if not rows: continue
    cols = rows[0].keys()
    seqcols = [c for c in cols if c and is_seqcol([r.get(c, "") for r in rows])]
    namecol = next((c for c in ("name", "design", "id") if c in cols), None)
    for sc in seqcols:
        for r in rows:
            v = (r.get(sc) or "").strip().upper()
            if not v or set(v) - AA: continue
            nm = (r.get(namecol) or "").strip() if namecol else ""
            if nm.lower().startswith(("ctrl", "scram", "neg", "target", "receptor")): continue
            add(nm, v, family(fp, nm), fp)

# filter + annotate
out = []
for seq, d in pool.items():
    L = len(seq); ncys = seq.count("C")
    flags = []
    elig = True
    if not (10 <= L <= 250): elig = False; flags.append("len")
    if set(seq) - AA: elig = False; flags.append("nonstd")
    if TAILMOTIF in seq or seq in RECEPTOR or RECEPTOR in seq: elig = False; flags.append("tagged/target")
    if seq in INCRETIN.values(): elig = False; flags.append("is_incretin_ctrl")
    gmax, gref = graft(seq)
    if gmax > 3: elig = False; flags.append(f"graft{gmax}:{gref}")
    if ncys % 2 == 1: flags.append("odd_Cys(unpaired)")
    fam = sorted(d["families"] - {"other"}) or ["other"]
    out.append({
        "name": d["name"], "sequence": seq, "length": L, "n_cys": ncys,
        "family": fam[0], "all_families": "|".join(sorted(d["families"])),
        "in_v10": v10.get(seq, ""), "graft_max": gmax, "graft_ref": gref,
        "elig_ok": elig, "flags": "|".join(flags), "src": d["src"],
    })

out.sort(key=lambda x: (not x["in_v10"], x["family"], -x["length"]))
os.makedirs(f"{REPO}/runs/picker", exist_ok=True)
with open(f"{REPO}/runs/picker/pool.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(out[0].keys()), lineterminator="\n")
    w.writeheader(); w.writerows(out)

elig = [x for x in out if x["elig_ok"]]
from collections import Counter
print(f"total unique seqs: {len(out)}  eligible: {len(elig)}")
print(f"v10 members found: {sum(1 for x in out if x['in_v10'])}/20")
print("eligible by family:", dict(Counter(x["family"] for x in elig)))
print("ineligible reasons:", dict(Counter(x['flags'].split('|')[0] for x in out if not x['elig_ok'])))
print("len distribution (eligible): min %d max %d" % (min(x['length'] for x in elig), max(x['length'] for x in elig)))
print("wrote runs/picker/pool.csv")
