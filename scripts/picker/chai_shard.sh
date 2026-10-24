#!/usr/bin/env bash
# Chai bare-design + WT co-fold sharded across a GPU LIST (one proc per GPU, proven pattern).
# Usage: chai_shard.sh <csv:name,sequence> <workdir> [seeds=0,1,2] [gpus="0 1"]
set -uo pipefail
REPO=/home/prachh/v/anthropic-adaptyv-2026-glp1r
CHAI=/home/prachh/v/sepiq-2026-challenge/.venv-chai/bin/python
TGT=$REPO/data/target/construct_24_432.seq
CSV=${1:?csv}; WORK=${2:?workdir}; SEEDS=${3:-0,1,2}; GPUS=${4:-0 1}
read -ra GA <<< "$GPUS"; N=${#GA[@]}
mkdir -p "$WORK/shards"
for g in "${GA[@]}"; do
  u=$(nvidia-smi -i "$g" --query-gpu=memory.used --format=csv,noheader,nounits 2>/dev/null | tr -d ' '); u=${u:-0}
  [ "$u" -gt 2000 ] && { echo "ABORT: GPU $g busy (${u} MiB) — refusing to clobber"; [ "${FORCE_GPU:-0}" = 1 ] || exit 3; }
done
"$CHAI" - "$CSV" "$WORK/shards" "$N" <<'PY'
import sys, csv, os
csvf, sh, n = sys.argv[1], sys.argv[2], int(sys.argv[3])
rows = list(csv.DictReader(open(csvf)))
ws = [csv.writer(open(os.path.join(sh, f"s{i}.csv"), "w", newline=""), lineterminator="\n") for i in range(n)]
for w in ws: w.writerow(["name", "sequence"])
for i, r in enumerate(rows): ws[i % n].writerow([r["name"], r["sequence"]])
print("sharded", len(rows), "into", n)
PY
for idx in "${!GA[@]}"; do
  g=${GA[$idx]}
  CHAI_DOWNLOADS_DIR=/home/prachh/v/chai_downloads CUDA_VISIBLE_DEVICES="$g" OMP_NUM_THREADS=4 MKL_NUM_THREADS=4 \
    "$CHAI" "$REPO/scripts/chai_fold_adapt.py" "$WORK/shards/s$idx.csv" "$TGT" "$WORK/chai/s$idx" --seeds "$SEEDS" > "$WORK/chai_s$idx.log" 2>&1 &
  sleep 20   # stagger model load to avoid the shared-cache lock race
done
wait
echo "CHAI_SHARD_DONE $(date -u +%FT%TZ)"
