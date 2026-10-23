#!/usr/bin/env python3
# Harvest ALL RFD4-Proteina designs under a base dir (wave / wave_crop / ramp / smoke): extract the
# designed binder sequence from each *_generated.cif (binder = shortest chain), enforce natural-AA + 0-Cys
# (post-filter the soft C_SEQ_PROB_CYS exclusion), dedup by sequence -> CSV (name,sequence).
# Run with the RFD4 venv python (gemmi):  .venv/bin/python scripts/rfd4/harvest_rfd4.py <base_dir> <out.csv>
import sys, glob, csv, os, gemmi
BASE = sys.argv[1]; OUT = sys.argv[2]
NAT = set("ACDEFGHIKLMNPQRSTVWY")
cifs = set()
for pat in ("*/*/inference_samples/*/*_generated.cif", "*/inference_samples/*/*_generated.cif"):
    cifs.update(glob.glob(os.path.join(BASE, pat)))
rows = {}; n_seen = n_cys = n_nonnat = 0
for cif in sorted(cifs):
    parts = os.path.relpath(cif, BASE).split(os.sep)
    i = parts.index("inference_samples")
    tag = "_".join(parts[:i]); sample = parts[i + 1]
    try:
        m = gemmi.read_structure(cif)[0]
        chains = sorted(m, key=lambda c: len(c))
        # binder = shortest chain; require a strictly-longer receptor chain or skip (guards a
        # degenerate cif where a short context fragment could be mistaken for the design)
        if len(chains) < 2 or len(chains[-1]) <= len(chains[0]):
            continue
        binder = chains[0]
        seq = "".join((gemmi.find_tabulated_residue(r.name).one_letter_code.upper()
                       if gemmi.find_tabulated_residue(r.name) else 'X') for r in binder)
    except Exception:
        continue
    n_seen += 1
    if not seq or any(a not in NAT for a in seq): n_nonnat += 1; continue
    if 'C' in seq: n_cys += 1; continue
    if seq in rows: continue
    rows[seq] = ("rfd4_" + tag + "_" + sample).replace(os.sep, "_")
with open(OUT, "w", newline="") as f:
    w = csv.writer(f, lineterminator="\n"); w.writerow(["name", "sequence"])
    for seq, name in rows.items(): w.writerow([name, seq])
print(f"scanned {n_seen} designs; dropped {n_cys} Cys-containing, {n_nonnat} non-natural; "
      f"wrote {len(rows)} unique 0-Cys natural -> {OUT}")
