"""Parse Boltz/Chai confidence JSONs under an out dir -> a ranked table (CSV to stdout).
Usage: python scripts/parse_cofold.py <out_dir>"""
from __future__ import annotations

import csv
import glob
import json
import os
import sys

out = sys.argv[1]
rows = []
for jf in glob.glob(os.path.join(out, "**", "confidence_*.json"), recursive=True):
    try:
        d = json.load(open(jf))
    except Exception:
        continue
    nm = os.path.basename(jf).replace("confidence_", "").split("_model")[0]
    rows.append({
        "name": nm,
        "iptm": d.get("iptm"),
        "ptm": d.get("ptm"),
        "complex_plddt": d.get("complex_plddt"),
        "complex_iplddt": d.get("complex_iplddt"),
        "confidence_score": d.get("confidence_score"),
    })
rows.sort(key=lambda r: -(r["iptm"] or 0))
w = csv.DictWriter(sys.stdout, fieldnames=["name", "iptm", "ptm", "complex_plddt", "complex_iplddt", "confidence_score"])
w.writeheader()
for r in rows:
    w.writerow(r)
if not rows:
    print("# no confidence_*.json found under", out, file=sys.stderr)
