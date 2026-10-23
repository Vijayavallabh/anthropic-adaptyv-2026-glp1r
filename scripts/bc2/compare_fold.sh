#!/usr/bin/env bash
# Apples-to-apples re-scoring (side-agent critique fix): fold a design set BOTH bare (tag-off) and
# as the full expression construct (tag-on: (M)+design+GFP11/TwinStrep), both folders, SAME pipeline,
# so tag-on vs tag-off is never mixed. Tagged native references in the set give the tag-on threshold
# directly. NECESSARY-CONDITION geometry only; never an agonism claim.
# Usage: compare_fold.sh <set_csv:name,sequence> <workdir> [gpu=0] [seeds=0,1,2,3]
set -uo pipefail
REPO=/home/prachh/v/anthropic-adaptyv-2026-glp1r
CHAI=/home/prachh/v/sepiq-2026-challenge/.venv-chai/bin/python
TGT=$REPO/data/target/construct_24_432.seq
CSV=${1:?set csv}; WORK=${2:?workdir}; GPU=${3:-0}; SEEDS=${4:-0,1,2,3}
mkdir -p "$WORK/score"; cp "$CSV" "$WORK/designs.csv"
env -C "$REPO" uv run python -I scripts/bc2/build_construct_csv.py "$WORK/designs.csv"  # -> bare.csv + construct.csv
IFS=',' read -ra SS <<< "$SEEDS"
for mode in bare construct; do
  echo "=== [$mode] Boltz (gpu $GPU, seeds $SEEDS) ==="
  bash "$REPO/scripts/bc2/fold_boltz.sh" "$WORK/$mode.csv" "$TGT" "$WORK/boltz_$mode" "$GPU" "$SEEDS"
  for s in "${SS[@]}"; do
    env -C "$REPO" uv run python -I scripts/iface_score.py "$WORK/boltz_$mode/seed$s" > "$WORK/score/boltz_${mode}_seed$s.json" 2>/dev/null
  done
  echo "=== [$mode] Chai (SEQUENTIAL gpu $GPU) ==="
  CHAI_DOWNLOADS_DIR=/home/prachh/v/chai_downloads CUDA_VISIBLE_DEVICES="$GPU" \
    "$CHAI" "$REPO/scripts/chai_fold_adapt.py" "$WORK/$mode.csv" "$TGT" "$WORK/chai_$mode" --seeds "$SEEDS" > "$WORK/chai_$mode.log" 2>&1
  env -C "$REPO" uv run python -I scripts/iface_score.py "$WORK/chai_$mode" > "$WORK/score/chai_${mode}_all.json" 2>/dev/null
  # tag-OFF (bare) Chai cut 5.5; tag-ON (construct) inflates Chai ~+3.7 -> no absolute cut, rank vs tagged refs
  CC=5.5; [ "$mode" = construct ] && CC=99
  env -C "$REPO" uv run python -I scripts/bc2/apply_bar.py --boltz "$WORK"/score/boltz_${mode}_seed*.json \
    --chai "$WORK/score/chai_${mode}_all.json" --min-r299-seeds 2 --boltz-cut 6.0 --chai-cut "$CC" \
    --label "$mode" --out "$WORK/scorecard_$mode.csv"
done
echo "COMPARE_FOLD_DONE $(date -u +%FT%TZ)"
