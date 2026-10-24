#!/usr/bin/env bash
# Picker-faithful co-fold: BARE design (chain A) + WT GLP1R 24-432 tags-removed (chain B),
# Boltz-2, sharded across a GPU LIST (default idle 7, skipping foreign GPU 1). Boltz only
# (one co-folder, picker-style); Chai-confirm the top set separately. Geometry/binding
# necessary-condition only; never an agonism claim.
# Usage: fold_pool.sh <shortlist.csv:name,sequence> <workdir> [seeds=0,1,2,3] [gpus="0 2 3 4 5 6 7"]
set -uo pipefail
REPO=/home/prachh/v/anthropic-adaptyv-2026-glp1r
TGT=$REPO/data/target/construct_24_432.seq
SURV=${1:?shortlist csv}; WORK=${2:?workdir}; SEEDS=${3:-0,1,2,3}; GPUS=${4:-0 2 3 4 5 6 7}
read -ra GA <<< "$GPUS"; N=${#GA[@]}
mkdir -p "$WORK/shards" "$WORK/boltz" "$WORK/score"
# preflight: never clobber a foreign GPU job (override FORCE_GPU=1)
for g in "${GA[@]}"; do
  u=$(nvidia-smi -i "$g" --query-gpu=memory.used --format=csv,noheader,nounits 2>/dev/null | tr -d ' '); u=${u:-0}
  [ "$u" -gt 2000 ] && { echo "ABORT: GPU $g busy (${u} MiB) — refusing to clobber (FORCE_GPU=1 to override)"; [ "${FORCE_GPU:-0}" = 1 ] || exit 3; }
done
# shard round-robin across the GPU list
/home/prachh/v/sepiq-2026-challenge/.venv-boltz/bin/python - "$SURV" "$WORK/shards" "$N" <<'PY'
import sys, csv, os
surv, sh, n = sys.argv[1], sys.argv[2], int(sys.argv[3])
rows = list(csv.DictReader(open(surv)))
ws = [csv.writer(open(os.path.join(sh, f"s{i}.csv"), "w", newline=""), lineterminator="\n") for i in range(n)]
for w in ws: w.writerow(["name", "sequence"])
for i, r in enumerate(rows): ws[i % n].writerow([r["name"], r["sequence"]])
print("sharded", len(rows), "designs into", n, "shards")
PY
echo "=== PICKER CO-FOLD: $(wc -l < "$SURV") rows, seeds $SEEDS, gpus [$GPUS] ==="
pids=()
for idx in "${!GA[@]}"; do
  g=${GA[$idx]}
  bash "$REPO/scripts/bc2/fold_boltz.sh" "$WORK/shards/s$idx.csv" "$TGT" "$WORK/boltz/s$idx" "$g" "$SEEDS" > "$WORK/boltz_s$idx.log" 2>&1 &
  pids+=($!)
done
echo "launched ${#pids[@]} shard procs: ${pids[*]}"
wait
echo "PICKER_FOLD_DONE $(date -u +%FT%TZ)"
