#!/usr/bin/env bash
# End-to-end 2-folder construct-bar funnel for harvested BC2 designs.
# Folds the PRODUCTION CONSTRUCT ((M)+design+GFP11/TwinStrep tail) vs construct_24_432 in BOTH
# Boltz and Chai (multi-seed), scores with the unchanged iface_score.py, and applies the
# GLP-1-calibrated 2-folder bar. NECESSARY-CONDITION geometry only; never an agonism claim.
# Run AFTER the generation arms finish (free GPUs) to avoid CUDA-graph contention crashes.
#
# Usage: funnel_run.sh <designs_csv:name,sequence> <workdir> [gpu=0] [seeds=0,1,2,3] [variant=construct|bare|both]
set -uo pipefail
REPO=/home/prachh/v/anthropic-adaptyv-2026-glp1r
CHAI=/home/prachh/v/sepiq-2026-challenge/.venv-chai/bin/python
TGT=$REPO/data/target/construct_24_432.seq
CSV=${1:?designs csv}; WORK=${2:?workdir}; GPU=${3:-0}; SEEDS=${4:-0,1,2,3}; VARIANT=${5:-construct}
mkdir -p "$WORK/score"
cp "$CSV" "$WORK/designs.csv"
env -C "$REPO" uv run python -I scripts/bc2/build_construct_csv.py "$WORK/designs.csv"   # -> WORK/bare.csv + WORK/construct.csv

fold_and_score () { # variant
  local v="$1" vcsv="$WORK/$1.csv"
  [ -s "$vcsv" ] || { echo "no $vcsv"; return 1; }
  echo "=== [$v] Boltz fold (gpu $GPU, seeds $SEEDS) ==="
  bash "$REPO/scripts/bc2/fold_boltz.sh" "$vcsv" "$TGT" "$WORK/boltz_$v" "$GPU" "$SEEDS"
  IFS=',' read -ra SS <<< "$SEEDS"
  for s in "${SS[@]}"; do
    env -C "$REPO" uv run python -I scripts/iface_score.py "$WORK/boltz_$v/seed$s" > "$WORK/score/boltz_${v}_seed$s.json" 2>/dev/null
  done
  echo "=== [$v] Chai fold (gpu $GPU SEQUENTIAL, seeds $SEEDS) ==="
  CHAI_DOWNLOADS_DIR=/home/prachh/v/chai_downloads CUDA_VISIBLE_DEVICES="$GPU" \
    "$CHAI" "$REPO/scripts/chai_fold_adapt.py" "$vcsv" "$TGT" "$WORK/chai_$v" --seeds "$SEEDS" > "$WORK/chai_$v.log" 2>&1
  env -C "$REPO" uv run python -I scripts/iface_score.py "$WORK/chai_$v" > "$WORK/score/chai_${v}_all.json" 2>/dev/null
  echo "=== [$v] 2-folder bar ==="
  env -C "$REPO" uv run python -I scripts/bc2/apply_bar.py \
    --boltz "$WORK"/score/boltz_${v}_seed*.json --chai "$WORK/score/chai_${v}_all.json" \
    --min-r299-seeds 2 --boltz-cut 6.0 --chai-cut 5.5 --label "$v" --out "$WORK/scorecard_${v}.csv"
}

case "$VARIANT" in
  construct) fold_and_score construct ;;
  bare) fold_and_score bare ;;
  both) fold_and_score construct; fold_and_score bare ;;
  *) echo "variant must be construct|bare|both" >&2; exit 2 ;;
esac
echo "FUNNEL_DONE $(date -u +%FT%TZ)  scorecards in $WORK/"
