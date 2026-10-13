"""Write the control-calibration CSV (positive agonists + a deterministic scramble negative)
and a bare target-sequence file for co-folding. CPU; no fabrication (controls are known peptides)."""
from __future__ import annotations

import csv
import random
from pathlib import Path

R = Path(__file__).resolve().parents[1]

GLP1_7_36 = "HAEGTFTSDVSSYLEGQAAKEFIAWLVKGR"          # positive control (native agonist)
EXENDIN_4 = "HGEGTFTSDLSKQMEEEAVRLFIEWLKNGGPSSGAPPPS"  # positive control (exendin-4)

scr = list(GLP1_7_36)
random.Random(0).shuffle(scr)
GLP1_SCRAMBLE = "".join(scr)                            # negative control (same composition, shuffled)

rows = [
    ("GLP1_7_36", GLP1_7_36, "protein"),
    ("exendin_4", EXENDIN_4, "protein"),
    ("GLP1_scramble_s0", GLP1_SCRAMBLE, "protein"),
]

(R / "data" / "controls").mkdir(parents=True, exist_ok=True)
with (R / "data" / "controls" / "calibration.csv").open("w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["name", "sequence", "molecule_class"])
    w.writerows(rows)

fa = (R / "data" / "target" / "construct_24_432.fasta").read_text().splitlines()
seq = "".join(l.strip() for l in fa if not l.startswith(">"))
(R / "data" / "target" / "construct_24_432.seq").write_text(seq + "\n")

print(f"calibration.csv rows={len(rows)} (2 positive + 1 scramble) | target construct len={len(seq)}")
print("negative scramble:", GLP1_SCRAMBLE)
