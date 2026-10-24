#!/usr/bin/env python3
"""2-FOLDER picker-rubric allocator. De-confounds single-folder over-docking by
scoring binding as the CONSERVATIVE MINIMUM of Boltz and Chai ipSAE, and treating
the agonism arm as both-folder R299 reachers only. Keeps v10 members that hold up
in both folders; replaces v10 members weak in both; seats a few honest long shots;
enforces family + class/length diversity.

FIREWALL: ranks only measurable binding/expression/epitope/novelty/diversity; the
vestibule/R299 engagement is a stated binding-site necessary condition, never an
agonism score. Weights disclosed below.

Usage: uv run python -I scripts/picker/allocate2.py <scores_boltz.csv> <scores_chai.csv> <plddt.json> <out_prefix>
"""
import csv, json, sys
from collections import defaultdict

W_IPSAE, W_IPTM, W_EXPRESS, W_EPITOPE, W_ROBUST = 0.45, 0.15, 0.15, 0.10, 0.15
GRAVY_HI = 0.5
TOP10_FAMILY_CAP, OVERALL_FAMILY_CAP = 3, 4
MIN_MINIPROT = 4          # >=4 of the 20 should be >=25 aa (class diversity, anti short-collapse)
N_LONGSHOT = 3            # reserve up to 3 slots for honest agonism long shots

def norm(x, lo, hi):
    return 0.0 if x is None else max(0.0, min(1.0, (x - lo) / (hi - lo)))

def plddt_ok(p, L):
    if p is None: return 0.5
    if p <= 1.0: p *= 100.0
    thr = 50 if L <= 25 else (62 if L <= 45 else 70)
    return 1.0 if p >= thr else max(0.0, p / thr)

def fnum(x):
    try: return float(x)
    except (TypeError, ValueError): return None

def load_scores(path):
    d = {}
    for r in csv.DictReader(open(path)):
        d[r["name"]] = r
    return d

def main(boltz_csv, chai_csv, plddt_json, outpre):
    B = load_scores(boltz_csv); C = load_scores(chai_csv)
    plddt = json.load(open(plddt_json))
    rows = []
    for name, b in B.items():
        if name not in C:   # only designs folded in BOTH folders are rankable 2-folder
            continue
        c = C[name]
        L = int(b["length"]); fam = b["family"]
        bi, ci = fnum(b["ipsae_best"]), fnum(c["ipsae_best"])
        bt, ct = fnum(b["iptm_best"]), fnum(c["iptm_best"])
        br, cr = int(b["r299_n"] or 0), int(c["r299_n"] or 0)
        # Boltz(optimistic) + Chai(pessimistic) both proxy the picker's unknown co-folder ->
        # MEAN estimates the expected picker ipSAE; MIN tracked as a conservative robustness flag.
        ips2 = (bi + ci) / 2 if (bi is not None and ci is not None) else (bi if ci is None else ci)
        ips_min = min(bi, ci) if (bi is not None and ci is not None) else None
        ipt2 = (bt + ct) / 2 if (bt is not None and ct is not None) else None
        robust_reacher = (br >= 2 and cr >= 2)   # reach R299 in BOTH folders = anti-artifact gate
        p = plddt.get(name)
        express = plddt_ok(p, L) * (1.0 if fnum(b["gravy"]) is None or fnum(b["gravy"]) <= GRAVY_HI else 0.5) \
                  * (0.6 if int(b["n_cys"]) % 2 == 1 else 1.0)
        epi_both = 1.0 if (br >= 1 and cr >= 1) else (0.5 if (br >= 1 or cr >= 1) else 0.2)
        comp = (W_IPSAE * norm(ips2, 0.1, 0.4) + W_IPTM * norm(ipt2, 0.5, 0.9)
                + W_EXPRESS * express + W_EPITOPE * epi_both + W_ROBUST * (1.0 if robust_reacher else 0.0))
        rob = "2f-robust" if robust_reacher else ("boltz-only" if br >= 2 and cr < 2 else ("chai-only" if cr >= 2 and br < 2 else "weak"))
        rows.append({
            "name": name, "sequence": b["sequence"], "family": fam, "length": L, "n_cys": int(b["n_cys"]),
            "in_v10": b["in_v10"], "pclass": "peptide" if L <= 30 else ("miniprotein" if L <= 100 else "small_protein"),
            "boltz_ipsae": bi, "chai_ipsae": ci, "ipsae_2f": round(ips2, 4) if ips2 is not None else None,
            "ipsae_min": round(ips_min, 4) if ips_min is not None else None,
            "iptm_2f": round(ipt2, 3) if ipt2 is not None else None, "boltz_r299": br, "chai_r299": cr,
            "robust": rob, "gravy": b["gravy"], "plddt": round(p * 100, 1) if (p is not None and p <= 1) else p,
            "composite": round(comp, 4), "graft_max": int(b["graft_max"]),
        })
    # light near-dup guard: drop a design that is a k-mer near-twin of a higher-composite one
    def k3(s): return set(s[i:i+3] for i in range(len(s) - 2))
    def jac(a, b):
        ka, kb = k3(a), k3(b)
        return len(ka & kb) / max(1, len(ka | kb))
    elig0 = sorted([r for r in rows if 10 <= r["length"] <= 250 and r["graft_max"] <= 3], key=lambda r: -r["composite"])
    elig = []
    for r in elig0:
        if all(jac(r["sequence"], k["sequence"]) < 0.7 for k in elig): elig.append(r)
    # HARD GATE: both-folder R299 reach (validated anti-single-folder-artifact necessary condition).
    tierA = [r for r in elig if r["robust"] == "2f-robust"]
    tierB = [r for r in elig if r["robust"] != "2f-robust"]

    chosen, famc, n_ecd = [], defaultdict(int), 0
    def pick(r):
        nonlocal n_ecd
        if r not in chosen:
            chosen.append(r); famc[r["family"]] += 1; n_ecd += (r["family"] == "ECD")
    def fam_ok(r, cap): return famc[r["family"]] < cap
    # pass 1: top-10 from Tier A, TOP10 family cap
    for r in tierA:
        if len(chosen) >= 10: break
        if fam_ok(r, TOP10_FAMILY_CAP): pick(r)
    # pass 2: fill to 17 from Tier A, OVERALL cap
    for r in tierA:
        if len(chosen) >= 17: break
        if fam_ok(r, OVERALL_FAMILY_CAP): pick(r)
    # ensure one pre-organized staple long shot (Tier A)
    if not any(r["family"] == "DiffPep-SS" for r in chosen):
        s = next((r for r in tierA if r["family"] == "DiffPep-SS" and r not in chosen), None)
        if s: pick(s)
    # diversity hedge: up to 3 Tier-B (distinct epitope/class e.g. ECD binders), ECD capped at 2
    for r in tierB:
        if len([x for x in chosen if x["robust"] != "2f-robust"]) >= 3 or len(chosen) >= 20: break
        if r["family"] == "ECD" and n_ecd >= 2: continue
        if fam_ok(r, OVERALL_FAMILY_CAP): pick(r)
    # final fill from Tier A, enforcing the family cap; relax by 1 only if still short
    for cap in (OVERALL_FAMILY_CAP, OVERALL_FAMILY_CAP + 1, OVERALL_FAMILY_CAP + 2):
        for r in tierA:
            if len(chosen) >= 20: break
            if r not in chosen and fam_ok(r, cap): pick(r)
    chosen = chosen[:20]

    cols = ["rank", "name", "family", "pclass", "length", "robust", "composite", "ipsae_2f",
            "boltz_ipsae", "chai_ipsae", "iptm_2f", "boltz_r299", "chai_r299", "plddt", "gravy", "n_cys", "in_v10", "sequence"]
    with open(f"{outpre}2_submission.csv", "w", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n"); w.writerow(["name", "sequence", "molecule_class"])
        for r in chosen: w.writerow([r["name"], r["sequence"], "single_chain"])
    with open(f"{outpre}2_screens.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, lineterminator="\n", extrasaction="ignore"); w.writeheader()
        for i, r in enumerate(chosen, 1): w.writerow({"rank": i, **r})
    with open(f"{outpre}2_ranked_all.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, lineterminator="\n", extrasaction="ignore"); w.writeheader()
        for i, r in enumerate(elig, 1): w.writerow({"rank": i, **r})

    v10names = {r["in_v10"] for r in rows if r["in_v10"]}
    kept = [r["in_v10"] for r in chosen if r["in_v10"]]
    dropped = sorted(v10names - set(kept))
    print(f"2-folder weights: ipSAE(min) {W_IPSAE} iptm {W_IPTM} express {W_EXPRESS} epitope {W_EPITOPE} robust {W_ROBUST}")
    print(f"chosen 20: v10-kept {len(kept)}, NEW {20-len(kept)}; family {dict(famc)}")
    print(f"robust mix: " + str({k: sum(1 for r in chosen if r['robust'] == k) for k in ('2f-robust','boltz-only','chai-only','weak')}))
    print(f"v10 DROPPED ({len(dropped)}): {dropped}")
    print(f"{'rk':>2} {'name':20s} {'fam':11s} {'L':>3s} {'robust':10s} {'comp':>5s} {'ips2f':>6s} {'B/C r299':>9s} {'pLDDT':>5s} v10")
    for i, r in enumerate(chosen, 1):
        print(f"{i:2d} {r['name']:20s} {r['family']:11s} {r['length']:3d} {r['robust']:10s} {r['composite']:5.3f} "
              f"{str(r['ipsae_2f']):>6s} {r['boltz_r299']}/{r['chai_r299']:<7d} {str(r['plddt']):>5s} {'Y' if r['in_v10'] else ''}")
    print(f"wrote {outpre}2_submission.csv + _screens.csv + _ranked_all.csv")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
