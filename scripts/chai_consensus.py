#!/usr/bin/env python3
"""Aggregate per-seed iface_score outputs (Boltz + Chai) -> per-design medians + nterm_in_7TM
fraction, classify by the SAME scheme used for the published Boltz calibration, and emit the
2-folder consensus table. NO change to the scoring science (iface_score.py produced the per-seed
metrics); this only aggregates across seeds + applies the published classification bands.

Classification (folder-agnostic geometry; only the iPAE 'junk' cut is folder-calibrated):
  scramble-like : median iPAE_min > IPAE_CUT  (no confident interface)
  agonist-like  : nterm_in_7TM in ALL seeds (frac==1.0) AND median vestibule_hits >= VEST_HI
  weak          : nterm_in_7TM frac >= 0.5 but not strong enough for agonist-like
  antagonist-like: nterm_in_7TM frac <= 0.333 (binds, but N-term 'message' not inserted)
"""
import csv, json, statistics as st, sys, argparse
from pathlib import Path

REPO = Path("/home/prachh/v/anthropic-adaptyv-2026-glp1r")
VEST_HI = 6


def agg(path):
    d = json.load(open(path))
    byb = {}
    for k, v in d.items():
        byb.setdefault(k.split("@")[0], []).append(v)
    out = {}
    for base, rows in byb.items():
        nt = [1 if r.get("nterm_in_7TM") else 0 for r in rows]
        vh = [len(r.get("vestibule_hits", [])) for r in rows]
        f7 = [r.get("frac_7TM", 0) for r in rows]
        ip = [r.get("iPAE_min") for r in rows if r.get("iPAE_min") is not None]
        it = [r.get("iptm", 0) for r in rows]
        out[base] = dict(n=len(rows), nterm_frac=round(sum(nt) / len(nt), 3),
                         vest=st.median(vh), f7=round(st.median(f7), 2),
                         ipae=round(st.median(ip), 2) if ip else None,
                         iptm=round(st.median(it), 3))
    return out


def classify(a, ipae_cut):
    if a["ipae"] is None or a["ipae"] > ipae_cut:
        return "scramble-like"
    if a["nterm_frac"] >= 0.999 and a["vest"] >= VEST_HI:
        return "agonist-like"
    if a["nterm_frac"] >= 0.5:
        return "weak"
    return "antagonist-like"


def consensus(cb, cc):
    if cb == cc:
        return f"AGREE:{cb}"
    return f"SPLIT:boltz={cb}/chai={cc}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chai", default=str(REPO / "runs/chai_winpath_iface.json"))
    ap.add_argument("--boltz-designs", default=str(REPO / "runs/boltz_winpath_iface.json"))
    ap.add_argument("--boltz-controls", default=str(REPO / "runs/panel_iface.json"))
    ap.add_argument("--boltz-ipae-cut", type=float, default=5.0)
    ap.add_argument("--chai-ipae-cut", type=float, default=5.0)
    ap.add_argument("--out", default=str(REPO / "data/candidates/chai_consensus.csv"))
    ap.add_argument("--controls-csv", default=str(REPO / "runs/chai_winpath/control_classes.csv"))
    a = ap.parse_args()

    bd = agg(a.boltz_designs)
    bc = agg(a.boltz_controls)
    cc = agg(a.chai)
    boltz = {**bd, **bc}

    roles = {r["name"]: r["class"] for r in csv.DictReader(open(a.controls_csv))}
    designs = ["dpbv2_030", "dpbv2_048", "dpbv2_049", "dpbv2_040", "eb_prod_l26"]
    controls = ["GLP1_7_36", "exendin_4", "exendin_9_39", "GLP1_15_36_addr", "scr_s3"]

    print("=== CHAI control calibration (its own controls) ===")
    print(f"{'name':<16}{'role':<11}{'nt_frac':>8}{'vest':>5}{'f7TM':>6}{'iPAE':>6}{'iptm':>7}")
    for n in controls:
        if n in cc:
            r = cc[n]
            print(f"{n:<16}{roles.get(n,'?'):<11}{r['nterm_frac']:>8}{r['vest']:>5}{r['f7']:>6}{str(r['ipae']):>6}{r['iptm']:>7}")

    rows = []
    hdr = ["name", "role", "boltz_class", "chai_class", "consensus",
           "boltz_nterm_frac", "boltz_vest", "boltz_frac7TM", "boltz_iPAE", "boltz_iptm",
           "chai_nterm_frac", "chai_vest", "chai_frac7TM", "chai_iPAE", "chai_iptm", "n_seeds"]
    for n in designs + controls:
        role = "design" if n in designs else f"control-{roles.get(n,'?')}"
        b = boltz.get(n); c = cc.get(n)
        cb = classify(b, a.boltz_ipae_cut) if b else "NA"
        cch = classify(c, a.chai_ipae_cut) if c else "NA"
        con = consensus(cb, cch) if (b and c) else "NA"
        rows.append([n, role, cb, cch, con,
                     b["nterm_frac"] if b else "", b["vest"] if b else "", b["f7"] if b else "",
                     b["ipae"] if b else "", b["iptm"] if b else "",
                     c["nterm_frac"] if c else "", c["vest"] if c else "", c["f7"] if c else "",
                     c["ipae"] if c else "", c["iptm"] if c else "", (c or b or {}).get("n", "")])

    with open(a.out, "w", newline="") as f:
        w = csv.writer(f, lineterminator="\n"); w.writerow(hdr); w.writerows(rows)

    print(f"\n=== 2-FOLDER CONSENSUS (boltz_ipae_cut={a.boltz_ipae_cut} chai_ipae_cut={a.chai_ipae_cut}) ===")
    print(f"{'name':<16}{'role':<20}{'BOLTZ':<16}{'CHAI':<16}{'consensus'}")
    for r in rows:
        print(f"{r[0]:<16}{r[1]:<20}{r[2]:<16}{r[3]:<16}{r[4]}")
    print(f"\nwrote {a.out}")


if __name__ == "__main__":
    main()
