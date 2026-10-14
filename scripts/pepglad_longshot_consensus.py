#!/usr/bin/env python3
"""NEW driver (does NOT modify any scorer): build the Boltz-first / 2-folder engagement
consensus for the PepGLAD long-shot survivors pglad_### by REUSING scripts/chai_consensus.py's
EXACT agg()/classify()/consensus()/VEST_HI -- the SAME bands that produced
data/candidates/chai_consensus.csv -- plus the published control panel for calibration.

Per-seed metrics were produced by the UNCHANGED scripts/iface_score.py for both folders:
  boltz designs : runs/boltz_pepglad_longshot_iface.json   (NEW; from runs/boltz_pepglad_longshot)
  boltz controls: runs/panel_iface.json                    (published)
  chai  designs : runs/pepglad_longshot_chai_iface.json    (NEW; only if Chai was run)
  chai  controls: runs/chai_winpath_iface.json             (published)

Boltz-first logic (per task):
  * classify every survivor by Boltz under BOTH band sets:
      - primary: chai_consensus.classify (ipae<=5.0, nterm_frac>=0.999 AND vest>=6)
      - note   : task parenthetical (ipae<=5.0 junk-cut; nterm_frac>=2/3 AND vest>=3 AND ipae<=4.5
                 => agonist; nterm_frac<0.5 OR vest<2 => antagonist; else weak)
  * Chai is run ONLY if some survivor is Boltz-agonist-like under EITHER band set.
  * If Chai present  -> any_agonist_like_consensus = some survivor agonist-like in BOTH folders.
  * If Chai absent   -> only valid when NO survivor is Boltz-agonist-like; then
                        any_agonist_like_consensus = FALSE (the AND-bar cannot be met).
"""
import csv, json, sys, os
from pathlib import Path

REPO = Path("/home/prachh/v/anthropic-adaptyv-2026-glp1r")
sys.path.insert(0, str(REPO / "scripts"))
import chai_consensus as C  # reuse the EXACT scorer/classifier -- no rewrite

IPAE_CUT = 5.0


def classify_note(a, agon_ipae=4.5, ipae_cut=5.0):
    if a["ipae"] is None or a["ipae"] > ipae_cut:
        return "scramble-like"
    if a["nterm_frac"] >= (2.0 / 3.0 - 1e-9) and a["vest"] >= 3 and a["ipae"] <= agon_ipae:
        return "agonist-like"
    if a["nterm_frac"] < 0.5 or a["vest"] < 2:
        return "antagonist-like"
    return "weak"


def main():
    boltz_designs = REPO / "runs/boltz_pepglad_longshot_iface.json"
    chai_designs = REPO / "runs/pepglad_longshot_chai_iface.json"
    assert boltz_designs.exists(), f"missing {boltz_designs}"

    bd = C.agg(str(boltz_designs))
    bc = C.agg(str(REPO / "runs/panel_iface.json"))
    boltz = {**bd, **bc}

    have_chai = chai_designs.exists()
    chai = {}
    if have_chai:
        cd = C.agg(str(chai_designs))
        cx = C.agg(str(REPO / "runs/chai_winpath_iface.json"))
        chai = {**cd, **cx}

    # dynamic survivor list from the gated candidates CSV
    cand = REPO / "data/candidates/pepglad_longshot.csv"
    designs = [r["name"] for r in csv.DictReader(open(cand))] if cand.exists() else []
    designs = [d for d in designs if d in boltz]

    rolemap = {"GLP1_7_36": "positive", "exendin_4": "positive",
               "exendin_9_39": "antagonist", "GLP1_15_36_addr": "antagonist", "scr_s3": "scramble"}
    controls = [c for c in rolemap if c in boltz]

    hdr = ["name", "role", "boltz_class", "chai_class", "consensus",
           "boltz_nterm_frac", "boltz_vest", "boltz_frac7TM", "boltz_iPAE", "boltz_iptm",
           "chai_nterm_frac", "chai_vest", "chai_frac7TM", "chai_iPAE", "chai_iptm", "n_seeds",
           "boltz_class_note", "chai_class_note", "consensus_note"]
    rows = []
    any_agon_primary = False
    any_agon_note = False
    boltz_trigger = False  # any survivor Boltz-agonist-like under EITHER band set
    for n in designs + controls:
        role = "design" if n in designs else f"control-{rolemap[n]}"
        b = boltz[n]
        cb = C.classify(b, IPAE_CUT)
        nb = classify_note(b)
        if n in designs and ("agonist-like" in (cb, nb)):
            boltz_trigger = True
        if have_chai and n in chai:
            c = chai[n]
            cc = C.classify(c, IPAE_CUT); con = C.consensus(cb, cc)
            nc = classify_note(c); ncon = C.consensus(nb, nc)
            crow = [c["nterm_frac"], c["vest"], c["f7"], c["ipae"], c["iptm"], c["n"]]
            if n in designs:
                if cb == "agonist-like" and cc == "agonist-like":
                    any_agon_primary = True
                if nb == "agonist-like" and nc == "agonist-like":
                    any_agon_note = True
        else:
            cc = "SKIPPED" if not have_chai else "NA"
            con = f"BOLTZ-ONLY:{cb}"
            nc = "SKIPPED" if not have_chai else "NA"
            ncon = f"BOLTZ-ONLY:{nb}"
            crow = ["", "", "", "", "", b["n"]]
        rows.append([n, role, cb, cc, con,
                     b["nterm_frac"], b["vest"], b["f7"], b["ipae"], b["iptm"],
                     *crow[:5], crow[5], nb, nc, ncon])

    out = REPO / "data/candidates/pepglad_longshot_consensus.csv"
    with open(out, "w", newline="") as f:
        w = csv.writer(f, lineterminator="\n"); w.writerow(hdr); w.writerows(rows)

    # ---- final boolean per task logic ----
    if have_chai:
        any_agonist_like_consensus = any_agon_primary or any_agon_note
        basis = "2-folder AND (primary OR note bands)"
    else:
        # valid skip only if no survivor is Boltz-agonist-like
        any_agonist_like_consensus = False
        basis = "Boltz-only; Chai skipped (no Boltz-agonist-like survivor => AND-bar unmeetable)"

    print("=== BOLTZ control calibration (panel_iface.json; exact + note bands) ===")
    print(f"{'name':<16}{'role':<12}{'nt_frac':>8}{'vest':>5}{'f7':>6}{'iPAE':>7}{'iptm':>7}  primary / note")
    for n in controls:
        b = boltz[n]
        print(f"{n:<16}{rolemap[n]:<12}{b['nterm_frac']:>8}{b['vest']:>5}{b['f7']:>6}{str(b['ipae']):>7}{b['iptm']:>7}  {C.classify(b, IPAE_CUT)} / {classify_note(b)}")

    print(f"\n=== PepGLAD survivors: Boltz{' + Chai' if have_chai else ' (Chai skipped)'} ===")
    print(f"{'name':<12}{'BOLTZ(prim)':<16}{'BOLTZ(note)':<16}{'CHAI(prim)':<14}{'consensus'}")
    for r in rows:
        if r[1] == "design":
            print(f"{r[0]:<12}{r[2]:<16}{r[16]:<16}{str(r[3]):<14}{r[4]}")

    print(f"\nHAVE_CHAI: {have_chai}")
    print(f"ANY_BOLTZ_AGONIST_LIKE (trigger, either band): {boltz_trigger}")
    if have_chai:
        print(f"ANY_AGONIST_LIKE_CONSENSUS (primary bands): {any_agon_primary}")
        print(f"ANY_AGONIST_LIKE_CONSENSUS (note bands): {any_agon_note}")
    print(f"ANY_AGONIST_LIKE_CONSENSUS [{basis}]: {any_agonist_like_consensus}")
    if (not have_chai) and boltz_trigger:
        print("WARNING: a survivor IS Boltz-agonist-like but Chai is MISSING -> run Chai before concluding.")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
