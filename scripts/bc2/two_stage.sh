#!/usr/bin/env bash
# Two-stage 2-folder CONSTRUCT funnel. Boltz-screen all (cheap, over-optimistic) -> keep R299
# reachers (>=2/4 seeds) -> Chai-confirm only those (expensive discriminator) -> GLP-1-calibrated
# 2-folder bar. NECESSARY-CONDITION geometry only; never an agonism claim. Run on FREE GPUs.
# Usage: two_stage.sh <designs_csv:name,sequence> <workdir> [gpu=0] [seeds=0,1,2,3]
set -uo pipefail
REPO=/home/prachh/v/anthropic-adaptyv-2026-glp1r
CHAI=/home/prachh/v/sepiq-2026-challenge/.venv-chai/bin/python
TGT=$REPO/data/target/construct_24_432.seq
DESIGNS=${1:?designs csv}; WORK=${2:?workdir}; GPU=${3:-0}; SEEDS=${4:-0,1,2,3}
mkdir -p "$WORK/score"
cp "$DESIGNS" "$WORK/designs.csv"
env -C "$REPO" uv run python -I scripts/bc2/build_construct_csv.py "$WORK/designs.csv"   # -> construct.csv + bare.csv

echo "=== STAGE 1: Boltz screen (construct, all designs, seeds $SEEDS) ==="
bash "$REPO/scripts/bc2/fold_boltz.sh" "$WORK/construct.csv" "$TGT" "$WORK/boltz_cons" "$GPU" "$SEEDS"
IFS=',' read -ra SS <<< "$SEEDS"
for s in "${SS[@]}"; do
  env -C "$REPO" uv run python -I scripts/iface_score.py "$WORK/boltz_cons/seed$s" > "$WORK/score/boltz_cons_seed$s.json" 2>/dev/null
done
env -C "$REPO" uv run python -I scripts/bc2/apply_bar.py --boltz "$WORK"/score/boltz_cons_seed*.json \
  --min-r299-seeds 2 --boltz-cut 6.0 --label boltz_screen --out "$WORK/boltz_screen.csv" || true

env -C "$REPO" uv run python -I - "$WORK" <<'PY'
import csv, sys, os
work = sys.argv[1]
surv = []
for r in csv.DictReader(open(os.path.join(work, "boltz_screen.csv"))):
    num = int(str(r.get("boltz_R299_n", "0/0")).split("/")[0] or 0)
    if num >= 2:
        surv.append(r["name"])
cons = {row["name"]: row["sequence"] for row in csv.DictReader(open(os.path.join(work, "construct.csv")))}
with open(os.path.join(work, "survivors_construct.csv"), "w", newline="") as fh:
    w = csv.writer(fh, lineterminator="\n"); w.writerow(["name", "sequence"])
    for nm in surv:
        if nm in cons:
            w.writerow([nm, cons[nm]])
print(f"Boltz R299 survivors (>=2/4 seeds): {len(surv)}")
PY

NS=$(( $(wc -l < "$WORK/survivors_construct.csv") - 1 ))
if [ "$NS" -le 0 ]; then echo "NO Boltz R299 survivors -> 2-folder NEGATIVE (nothing to Chai-confirm)"; echo "TWO_STAGE_DONE $(date -u +%FT%TZ)"; exit 0; fi

echo "=== STAGE 2: Chai confirm ($NS survivors, construct, SEQUENTIAL gpu$GPU) ==="
CHAI_DOWNLOADS_DIR=/home/prachh/v/chai_downloads CUDA_VISIBLE_DEVICES="$GPU" \
  "$CHAI" "$REPO/scripts/chai_fold_adapt.py" "$WORK/survivors_construct.csv" "$TGT" "$WORK/chai_cons" --seeds "$SEEDS" > "$WORK/chai_cons.log" 2>&1
env -C "$REPO" uv run python -I scripts/iface_score.py "$WORK/chai_cons" > "$WORK/score/chai_cons_all.json" 2>/dev/null

echo "=== 2-FOLDER CONSTRUCT BAR (the BoltzGen-0/21 gate) ==="
env -C "$REPO" uv run python -I scripts/bc2/apply_bar.py \
  --boltz "$WORK"/score/boltz_cons_seed*.json --chai "$WORK/score/chai_cons_all.json" \
  --min-r299-seeds 2 --boltz-cut 6.0 --chai-cut 5.5 --label construct --out "$WORK/scorecard_2folder.csv"
echo "TWO_STAGE_DONE $(date -u +%FT%TZ)"
