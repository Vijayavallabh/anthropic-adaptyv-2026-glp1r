"""Calibration panel: native-agonist POSITIVES vs scramble NEGATIVES, to test whether the
mechanism-aware discriminator (N-term inserted into the 7TM + ECD-groove anchoring) separates
true agonists from decoys. Positives are known agonists (CALIBRATION ONLY, never design seeds)."""
from __future__ import annotations

import csv
import random
from pathlib import Path

R = Path(__file__).resolve().parents[1]

POSITIVES = {
    "GLP1_7_36": "HAEGTFTSDVSSYLEGQAAKEFIAWLVKGR",
    "GLP1_7_37": "HAEGTFTSDVSSYLEGQAAKEFIAWLVKGRG",
    "exendin_4": "HGEGTFTSDLSKQMEEEAVRLFIEWLKNGGPSSGAPPPS",
    "liraglutide_bb": "HAEGTFTSDVSSYLEGQAAKEFIAWLVRGRG",  # Arg34-GLP-1(7-37) backbone (no lipid)
}
BASE = POSITIVES["GLP1_7_36"]

rows = [(k, v, "protein") for k, v in POSITIVES.items()]
for s in range(8):
    chars = list(BASE)
    random.Random(s).shuffle(chars)
    rows.append((f"scr_s{s}", "".join(chars), "protein"))

(R / "data" / "controls").mkdir(parents=True, exist_ok=True)
with (R / "data" / "controls" / "panel.csv").open("w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["name", "sequence", "molecule_class"])
    w.writerows(rows)

print(f"panel.csv rows={len(rows)} ({len(POSITIVES)} positive agonists + {len(rows)-len(POSITIVES)} scrambles)")
