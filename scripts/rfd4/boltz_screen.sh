#!/usr/bin/env bash
# Stage-1 parallel Boltz R299 screen across 8 GPUs. harvest.csv -> construct.csv -> 8 shards ->
# fold_boltz.sh per shard on GPU 0-7 (1 seed; R299 reach is seed-stable) -> merge -> apply_bar ->
# R299 reachers -> survivors_construct.csv. NECESSARY-CONDITION geometry only; never an agonism claim.
# Usage: bash scripts/rfd4/boltz_screen.sh <designs_csv> <workdir> [seed=0]
set -uo pipefail
REPO=/home/prachh/v/anthropic-adaptyv-2026-glp1r
DESIGNS=${1:?designs csv}; WORK=${2:?workdir}; SEED=${3:-0}
TGT=$REPO/data/target/construct_24_432.seq
mkdir -p "$WORK/score" "$WORK/shards" "$WORK/boltz"
cp "$DESIGNS" "$WORK/designs.csv"
# preflight: never clobber a foreign GPU job (CLAUDE.md/AGENTS.md); override with FORCE_GPU=1
for g in 0 1 2 3 4 5 6 7; do
  u=$(nvidia-smi -i "$g" --query-gpu=memory.used --format=csv,noheader,nounits 2>/dev/null | tr -d ' '); u=${u:-0}
  [ "$u" -gt 2000 ] && { echo "ABORT: GPU $g busy (${u} MiB) — refusing to clobber (FORCE_GPU=1 to override)"; [ "${FORCE_GPU:-0}" = 1 ] || exit 3; }
done
env -C "$REPO" uv run python -I scripts/bc2/build_construct_csv.py "$WORK/designs.csv"   # -> construct.csv (+ bare.csv)
env -C "$REPO" uv run python -I - "$WORK" <<'PY'
import csv, sys, os
work = sys.argv[1]; rows = list(csv.DictReader(open(os.path.join(work, "construct.csv")))); N = 8
ws = [csv.writer(open(os.path.join(work, "shards", f"s{i}.csv"), "w", newline="")) for i in range(N)]
for w in ws: w.writerow(["name", "sequence"])
for i, r in enumerate(rows): ws[i % N].writerow([r["name"], r["sequence"]])
print("sharded", len(rows), "designs into", N)
PY
echo "=== STAGE 1: Boltz screen, 8 shards on GPU 0-7, seed $SEED ==="
for i in 0 1 2 3 4 5 6 7; do
  bash "$REPO/scripts/bc2/fold_boltz.sh" "$WORK/shards/s$i.csv" "$TGT" "$WORK/boltz/s$i" "$i" "$SEED" > "$WORK/boltz_s$i.log" 2>&1 &
done
wait
echo "=== scoring + merge ==="
for i in 0 1 2 3 4 5 6 7; do
  env -C "$REPO" uv run python -I scripts/iface_score.py "$WORK/boltz/s$i/seed$SEED" > "$WORK/score/boltz_s$i.json" 2>/dev/null || true
done
env -C "$REPO" uv run python -I - "$WORK" "$SEED" <<'PY'
import json, glob, os, sys
work, seed = sys.argv[1], sys.argv[2]
merged = {}
for jf in sorted(glob.glob(os.path.join(work, "score", "boltz_s*.json"))):
    try: merged.update(json.load(open(jf)))
    except Exception: pass
json.dump(merged, open(os.path.join(work, "score", f"boltz_screen_seed{seed}.json"), "w"))
print("merged designs scored:", len(merged))
PY
env -C "$REPO" uv run python -I scripts/bc2/apply_bar.py \
  --boltz "$WORK/score/boltz_screen_seed$SEED.json" --min-r299-seeds 1 --boltz-cut 99 \
  --label screen --out "$WORK/boltz_screen.csv" \
  || { echo "ABORT: apply_bar failed — not writing survivors"; exit 4; }
[ -s "$WORK/boltz_screen.csv" ] || { echo "ABORT: boltz_screen.csv missing/empty"; exit 4; }
env -C "$REPO" uv run python -I - "$WORK" <<'PY'
import csv, os, sys
work = sys.argv[1]
keep = []
for r in csv.DictReader(open(os.path.join(work, "boltz_screen.csv"))):
    n = int(str(r.get("boltz_R299_n", "0/0")).split("/")[0] or 0)
    if n >= 1: keep.append(r["name"])
cons = {r["name"]: r["sequence"] for r in csv.DictReader(open(os.path.join(work, "construct.csv")))}
with open(os.path.join(work, "survivors_construct.csv"), "w", newline="") as f:
    w = csv.writer(f, lineterminator="\n"); w.writerow(["name", "sequence"])
    for nm in keep:
        if nm in cons: w.writerow([nm, cons[nm]])
print(f"Boltz R299 reachers (seed, construct): {len(keep)} / survivors_construct.csv")
PY
echo "BOLTZ_SCREEN_DONE $(date -u +%FT%TZ)"
