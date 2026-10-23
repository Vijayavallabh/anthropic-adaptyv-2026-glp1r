#!/usr/bin/env bash
# Stage-2 parallel 2-folder CONFIRM across 8 GPUs for the Boltz R299 survivors (+ anchors).
# Phase A: Boltz re-seed (8 shards GPU0-7, all seeds) ; Phase B: Chai (8 shards GPU0-7, all seeds).
# Then per-seed merge (Boltz keys are bare <name> -> keep seeds in separate files; Chai keys are
# <name>@s<seed> -> merge freely) and apply the tag-on 2-folder bar: R299 in BOTH folders.
# NO hard Chai cut (--chai-cut 99): the bare-calibrated 5.5 is wrong tag-ON; rank by chai_ipae_reach
# and compare to the v9 anchors folded in the SAME run. Geometry only; never an agonism claim.
# Usage: confirm_stage2.sh <survivors_construct_csv> <workdir> [seeds=0,1,2,3]
set -uo pipefail
REPO=/home/prachh/v/anthropic-adaptyv-2026-glp1r
CHAI=/home/prachh/v/sepiq-2026-challenge/.venv-chai/bin/python
TGT=$REPO/data/target/construct_24_432.seq
SURV=${1:?survivors csv}; WORK=${2:?workdir}; SEEDS=${3:-0,1,2,3}
mkdir -p "$WORK/score" "$WORK/shards" "$WORK/boltz" "$WORK/chai"
cp "$SURV" "$WORK/survivors.csv"
# preflight: never clobber a foreign GPU job (CLAUDE.md/AGENTS.md); override with FORCE_GPU=1
for g in 0 1 2 3 4 5 6 7; do
  u=$(nvidia-smi -i "$g" --query-gpu=memory.used --format=csv,noheader,nounits 2>/dev/null | tr -d ' '); u=${u:-0}
  [ "$u" -gt 2000 ] && { echo "ABORT: GPU $g busy (${u} MiB) — refusing to clobber (FORCE_GPU=1 to override)"; [ "${FORCE_GPU:-0}" = 1 ] || exit 3; }
done
env -C "$REPO" uv run python -I - "$WORK" <<'PY'
import csv, sys, os
work = sys.argv[1]; rows = list(csv.DictReader(open(os.path.join(work, "survivors.csv")))); N = 8
ws = [csv.writer(open(os.path.join(work, "shards", f"s{i}.csv"), "w", newline="")) for i in range(N)]
for w in ws: w.writerow(["name", "sequence"])
for i, r in enumerate(rows): ws[i % N].writerow([r["name"], r["sequence"]])
print("sharded", len(rows), "rows into", N)
PY
NS=$(( $(wc -l < "$WORK/survivors.csv") - 1 ))
echo "=== STAGE 2: $NS rows (survivors + anchors), seeds $SEEDS ==="
if [ "$NS" -le 0 ]; then echo "NO rows to fold (empty input) -> NEGATIVE, nothing to confirm"; echo "CONFIRM_STAGE2_DONE $(date -u +%FT%TZ)"; exit 0; fi

echo "--- Phase A: Boltz re-seed, 8 shards GPU0-7 ---"
for i in 0 1 2 3 4 5 6 7; do
  bash "$REPO/scripts/bc2/fold_boltz.sh" "$WORK/shards/s$i.csv" "$TGT" "$WORK/boltz/s$i" "$i" "$SEEDS" > "$WORK/boltz_s$i.log" 2>&1 &
done
wait
echo "--- Phase B: Chai, 8 shards GPU0-7 (one Chai process per GPU) ---"
for i in 0 1 2 3 4 5 6 7; do
  CHAI_DOWNLOADS_DIR=/home/prachh/v/chai_downloads CUDA_VISIBLE_DEVICES="$i" OMP_NUM_THREADS=4 MKL_NUM_THREADS=4 \
    "$CHAI" "$REPO/scripts/chai_fold_adapt.py" "$WORK/shards/s$i.csv" "$TGT" "$WORK/chai/s$i" --seeds "$SEEDS" > "$WORK/chai_s$i.log" 2>&1 &
done
wait

echo "--- scoring + merge ---"
IFS=',' read -ra SS <<< "$SEEDS"
for s in "${SS[@]}"; do
  for i in 0 1 2 3 4 5 6 7; do
    env -C "$REPO" uv run python -I scripts/iface_score.py "$WORK/boltz/s$i/seed$s" > "$WORK/score/boltz_s${i}_seed$s.json" 2>/dev/null || true
  done
done
for i in 0 1 2 3 4 5 6 7; do
  env -C "$REPO" uv run python -I scripts/iface_score.py "$WORK/chai/s$i" > "$WORK/score/chai_s$i.json" 2>/dev/null || true
done
env -C "$REPO" uv run python -I - "$WORK" "$SEEDS" <<'PY'
import json, glob, os, sys
work, seeds = sys.argv[1], sys.argv[2].split(",")
for s in seeds:
    merged = {}
    for jf in sorted(glob.glob(os.path.join(work, "score", f"boltz_s*_seed{s}.json"))):
        try: merged.update(json.load(open(jf)))
        except Exception: pass
    json.dump(merged, open(os.path.join(work, "score", f"boltz_seed{s}.json"), "w"))
cm = {}
for jf in sorted(glob.glob(os.path.join(work, "score", "chai_s*.json"))):
    try: cm.update(json.load(open(jf)))
    except Exception: pass
json.dump(cm, open(os.path.join(work, "score", "chai_all.json"), "w"))
print("merged boltz per-seed + chai; chai seed-entries:", len(cm))
PY

echo "=== 2-FOLDER CONSTRUCT BAR (tag-on; R299 both, no hard Chai cut -> rank vs anchors) ==="
env -C "$REPO" uv run python -I scripts/bc2/apply_bar.py \
  --boltz "$WORK"/score/boltz_seed*.json --chai "$WORK/score/chai_all.json" \
  --min-r299-seeds 2 --boltz-cut 6.0 --chai-cut 99 --label construct_tagon --out "$WORK/scorecard_2folder.csv"
echo "CONFIRM_STAGE2_DONE $(date -u +%FT%TZ)"
