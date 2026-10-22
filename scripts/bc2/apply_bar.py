#!/usr/bin/env python3
"""Apply the GLP-1-calibrated Boltz-and-Chai 2-folder construct bar to iface_score outputs.

This is the decisive NECESSARY-CONDITION gate the 2026-10-19 BoltzGen arm failed 0/21. It is
GEOMETRY + interface-confidence only; it does NOT rank or prove agonism (unprovable in-silico;
the wet cAMP/SEAP assay is the sole verdict).

PASS_2folder (per design) =
  reaches R299 (UniProt 299 in vestibule_hits) in BOTH Boltz AND Chai (best pose over seeds)
  AND best Boltz iPAE_min <= BOLTZ_CUT  AND best Chai iPAE_min <= CHAI_CUT.

Calibration (bare peptide vs construct_24_432, best-of-seeds): GLP-1(7-36) Boltz 2.23 / Chai 4.49,
glucagon 3.06/2.84, liraglutide 3.25/3.69 all reach R299 in both; exendin-4 3.81/3.73 reaches in
Chai only (Boltz misses R299). Boltz is systematically optimistic (floors ~2.4); Chai discriminates.

Usage:
  uv run python -I scripts/bc2/apply_bar.py --boltz b_s0.json b_s1.json ... --chai c_s0.json ... \
      [--out scorecard.csv] [--boltz-cut 4.5] [--chai-cut 5.5] [--label construct]
Each JSON is one iface_score run (one seed dir); pass several to aggregate best-of-seeds.
"""
import argparse, json, sys, csv

CENTRAL_POLAR = {190, 363, 364, 394}      # microswitch residues present in iface_score VESTIBULE set
R299 = 299

def load(paths):
    """Return {design_name: [per-seed metric dicts]} merged across the given JSON files."""
    agg = {}
    for p in paths:
        with open(p) as fh:
            d = json.load(fh)
        for k, v in d.items():
            name = k.split("@")[0]
            agg.setdefault(name, []).append(v)
    return agg

def fold_summary(seeds):
    """Aggregate one folder's per-seed dicts for a design: best iPAE, R299 reach count, polar, depth."""
    ipae = [s.get("iPAE_min") for s in seeds if isinstance(s.get("iPAE_min"), (int, float))]
    vhits = [set(s.get("vestibule_hits", [])) for s in seeds]
    nterm = [s.get("nterm_min_dist") for s in seeds if isinstance(s.get("nterm_min_dist"), (int, float))]
    # iPAE of the BEST R299-reaching pose (the calibration's notion of a real deep reacher),
    # falling back to overall best if none reach.
    reach_ipae = [s.get("iPAE_min") for s in seeds
                  if R299 in set(s.get("vestibule_hits", [])) and isinstance(s.get("iPAE_min"), (int, float))]
    return {
        "n_seed": len(seeds),
        "ipae_best": round(min(ipae), 2) if ipae else None,
        "ipae_best_reaching": round(min(reach_ipae), 2) if reach_ipae else None,
        "r299_count": sum(1 for h in vhits if R299 in h),
        "r299_any": any(R299 in h for h in vhits),
        "r299_all": all(R299 in h for h in vhits) if vhits else False,
        "cp_union": sorted(set().union(*vhits) & CENTRAL_POLAR) if vhits else [],
        "nterm_min": round(min(nterm), 2) if nterm else None,
        "nterm_in7TM_any": any(s.get("nterm_in_7TM") for s in seeds),
        "ecd_anchor_max": max((s.get("ecd_groove_anchor_count", 0) for s in seeds), default=0),
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--boltz", nargs="+", required=True)
    ap.add_argument("--chai", nargs="+", default=[])
    ap.add_argument("--boltz-cut", type=float, default=4.5)
    ap.add_argument("--chai-cut", type=float, default=5.5)
    ap.add_argument("--min-r299-seeds", type=int, default=1, help="min seeds docking R299 per folder to count as reaching")
    ap.add_argument("--label", default="construct")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    B = load(a.boltz)
    C = load(a.chai) if a.chai else {}
    names = sorted(set(B) | set(C))
    rows = []
    for nm in names:
        b = fold_summary(B.get(nm, []))
        c = fold_summary(C.get(nm, [])) if C else None
        mn = a.min_r299_seeds
        b_reach = b["r299_count"] >= mn
        b_ipae = b["ipae_best_reaching"] if b_reach else b["ipae_best"]
        boltz_ok = bool(b_reach and b_ipae is not None and b_ipae <= a.boltz_cut)
        if c is not None:
            c_reach = c["r299_count"] >= mn
            c_ipae = c["ipae_best_reaching"] if c_reach else c["ipae_best"]
            chai_ok = bool(c_reach and c_ipae is not None and c_ipae <= a.chai_cut)
            passed = boltz_ok and chai_ok
            r299_both = b_reach and c_reach
        else:
            c_ipae = None; chai_ok = None; passed = None; r299_both = None
        rows.append({
            "name": nm, "label": a.label,
            "boltz_ipae_reach": b["ipae_best_reaching"], "boltz_ipae_best": b["ipae_best"],
            "boltz_R299_n": f"{b['r299_count']}/{b['n_seed']}", "boltz_nterm_min": b["nterm_min"],
            "boltz_nterm_in7TM": b["nterm_in7TM_any"],
            "chai_ipae_reach": (c["ipae_best_reaching"] if c else None), "chai_ipae_best": (c["ipae_best"] if c else None),
            "chai_R299_n": (f"{c['r299_count']}/{c['n_seed']}" if c else None),
            "chai_nterm_min": (c["nterm_min"] if c else None),
            "R299_both": r299_both,
            "cp_union": "|".join(map(str, sorted(set(b["cp_union"]) | set(c["cp_union"] if c else [])))),
            "ecd_anchor_max": max(b["ecd_anchor_max"], (c["ecd_anchor_max"] if c else 0)),
            "PASS_2folder": passed,
        })
    rows.sort(key=lambda r: (r["PASS_2folder"] is not True, r["chai_ipae_reach"] if r["chai_ipae_reach"] is not None else 99))
    cols = list(rows[0].keys()) if rows else []
    if a.out:
        with open(a.out, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=cols, lineterminator="\n"); w.writeheader(); w.writerows(rows)
    print(f"# 2-folder {a.label} bar  (reaching-pose iPAE: Boltz<={a.boltz_cut}, Chai<={a.chai_cut}; R299 in >={a.min_r299_seeds} seed/folder, BOTH folders)")
    print(f"{'name':22s} {'bZ_reach':>8} {'bZ_R299':>7} {'cH_reach':>8} {'cH_R299':>7} {'both':>5} {'cp':>13} {'PASS':>5}")
    for r in rows:
        print(f"{r['name'][:22]:22s} {str(r['boltz_ipae_reach']):>8} {str(r['boltz_R299_n']):>7} "
              f"{str(r['chai_ipae_reach']):>8} {str(r['chai_R299_n']):>7} {str(r['R299_both']):>5} "
              f"{r['cp_union'][:13]:>13} {str(r['PASS_2folder']):>5}")
    npass = sum(1 for r in rows if r["PASS_2folder"])
    print(f"# {npass}/{len(rows)} PASS the 2-folder {a.label} bar" + (f"  -> {a.out}" if a.out else ""))

if __name__ == "__main__":
    main()
