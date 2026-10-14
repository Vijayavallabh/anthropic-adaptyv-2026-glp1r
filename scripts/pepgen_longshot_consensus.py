#!/usr/bin/env python3
"""NEW driver (does NOT modify any scorer): build the 2-folder engagement consensus for the
pepgen long-shot peptides pepx_000..007 by REUSING scripts/chai_consensus.py's EXACT
agg()/classify()/consensus()/VEST_HI -- the same bands that produced
data/candidates/chai_consensus.csv -- plus the published control panel for calibration.

Per-seed metrics were produced by the UNCHANGED scripts/iface_score.py for both folders:
  boltz designs : runs/boltz_pepgen_longshot_iface.json   (NEW; from runs/boltz_pepgen_longshot)
  boltz controls: runs/panel_iface.json                   (published; chai_consensus --boltz-controls default)
  chai  designs : runs/pepgen_longshot_chai_iface.json     (NEW; from runs/pepgen_longshot_chai)
  chai  controls: runs/chai_winpath_iface.json            (published; chai_consensus --chai default)

Primary classification = chai_consensus.classify(a, 5.0)  (ipae_cut 5.0, VEST_HI 6).
Cross-check columns *_note use the task-note parenthetical thresholds
  (iPAE>5 => scramble; nterm_frac>=2/3 AND vest>=3 AND iPAE<=4.5 => agonist;
   nterm_frac<0.5 OR vest<2 => antagonist; else weak).

any_agonist_like_consensus = TRUE iff some pepx design is agonist-like in BOTH folders.
"""
import csv, json, sys
from pathlib import Path

REPO = Path("/home/prachh/v/anthropic-adaptyv-2026-glp1r")
sys.path.insert(0, str(REPO / "scripts"))
import chai_consensus as C  # reuse the EXACT scorer/classifier -- no rewrite

IPAE_CUT = 5.0  # chai_consensus default for BOTH folders


def classify_note(a, agon_ipae=4.5, ipae_cut=5.0):
    """Task-note parenthetical variant (reported as a cross-check only)."""
    if a["ipae"] is None or a["ipae"] > ipae_cut:
        return "scramble-like"
    if a["nterm_frac"] >= (2.0 / 3.0 - 1e-9) and a["vest"] >= 3 and a["ipae"] <= agon_ipae:
        return "agonist-like"
    if a["nterm_frac"] < 0.5 or a["vest"] < 2:
        return "antagonist-like"
    return "weak"


def main():
    bd = C.agg(str(REPO / "runs/boltz_pepgen_longshot_iface.json"))
    bc = C.agg(str(REPO / "runs/panel_iface.json"))
    cd = C.agg(str(REPO / "runs/pepgen_longshot_chai_iface.json"))
    cx = C.agg(str(REPO / "runs/chai_winpath_iface.json"))
    boltz = {**bd, **bc}
    chai = {**cd, **cx}

    designs = [f"pepx_00{i}" for i in range(8)]
    rolemap = {"GLP1_7_36": "positive", "exendin_4": "positive",
               "exendin_9_39": "antagonist", "GLP1_15_36_addr": "antagonist",
               "scr_s3": "scramble"}
    controls = list(rolemap)

    missing = [n for n in designs + controls if n not in boltz or n not in chai]
    assert not missing, f"missing folder entries for: {missing}"

    # self-validation: the 5 controls must reproduce the published chai_consensus.csv rows
    pub = {r["name"]: r for r in csv.DictReader(open(REPO / "data/candidates/chai_consensus.csv"))}
    repro_ok = True
    for n in controls:
        cb = C.classify(boltz[n], IPAE_CUT); cc = C.classify(chai[n], IPAE_CUT)
        con = C.consensus(cb, cc)
        if n in pub:
            same = (cb == pub[n]["boltz_class"] and cc == pub[n]["chai_class"] and con == pub[n]["consensus"])
            repro_ok &= same
            if not same:
                print(f"[REPRO MISMATCH] {n}: mine[{cb}/{cc}/{con}] pub[{pub[n]['boltz_class']}/{pub[n]['chai_class']}/{pub[n]['consensus']}]")

    hdr = ["name", "role", "boltz_class", "chai_class", "consensus",
           "boltz_nterm_frac", "boltz_vest", "boltz_frac7TM", "boltz_iPAE", "boltz_iptm",
           "chai_nterm_frac", "chai_vest", "chai_frac7TM", "chai_iPAE", "chai_iptm", "n_seeds",
           "boltz_class_note", "chai_class_note", "consensus_note"]
    rows = []
    any_agon_primary = False
    any_agon_note = False
    for n in designs + controls:
        role = "design" if n in designs else f"control-{rolemap[n]}"
        b, c = boltz[n], chai[n]
        cb = C.classify(b, IPAE_CUT); cc = C.classify(c, IPAE_CUT); con = C.consensus(cb, cc)
        nb = classify_note(b); nc = classify_note(c); ncon = C.consensus(nb, nc)
        if n in designs:
            if cb == "agonist-like" and cc == "agonist-like":
                any_agon_primary = True
            if nb == "agonist-like" and nc == "agonist-like":
                any_agon_note = True
        rows.append([n, role, cb, cc, con,
                     b["nterm_frac"], b["vest"], b["f7"], b["ipae"], b["iptm"],
                     c["nterm_frac"], c["vest"], c["f7"], c["ipae"], c["iptm"], c["n"],
                     nb, nc, ncon])

    out = REPO / "data/candidates/pepgen_longshot_consensus.csv"
    with open(out, "w", newline="") as f:
        w = csv.writer(f, lineterminator="\n"); w.writerow(hdr); w.writerows(rows)

    print("=== CHAI control calibration (its own controls, exact bands) ===")
    print(f"{'name':<16}{'role':<12}{'nt_frac':>8}{'vest':>5}{'f7':>6}{'iPAE':>7}{'iptm':>7}  class")
    for n in controls:
        c = chai[n]
        print(f"{n:<16}{rolemap[n]:<12}{c['nterm_frac']:>8}{c['vest']:>5}{c['f7']:>6}{str(c['ipae']):>7}{c['iptm']:>7}  {C.classify(c, IPAE_CUT)}")

    print("\n=== 2-FOLDER CONSENSUS (exact chai_consensus.py bands; ipae_cut=5.0, VEST_HI=6) ===")
    print(f"{'name':<16}{'role':<20}{'BOLTZ':<16}{'CHAI':<16}consensus")
    for r in rows:
        print(f"{r[0]:<16}{r[1]:<20}{r[2]:<16}{r[3]:<16}{r[4]}")

    print(f"\nCONTROLS_REPRODUCE_PUBLISHED: {repro_ok}")
    print(f"ANY_AGONIST_LIKE_CONSENSUS (exact bands): {any_agon_primary}")
    print(f"ANY_AGONIST_LIKE_CONSENSUS (task-note bands): {any_agon_note}")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
