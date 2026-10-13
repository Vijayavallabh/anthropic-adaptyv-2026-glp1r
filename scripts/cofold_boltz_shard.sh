#!/bin/bash
# Sharded Boltz-2 single-seq cofold across GPUs (reusable scoring workhorse).
# Binder chain A : target chain B, msa empty. Usage:
#   cofold_boltz_shard.sh <csv:name|design,sequence> <target_seq_file> <tag> [gpus=0-3] [seeds=0]
set -uo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"; cd "$REPO"; . "$REPO/scripts/env.sh"
CSV=${1:?csv}; TGTF=${2:?target_seq_file}; TAG=${3:-run}; GPUS=${4:-0-3}; SEEDS=${5:-0}
MDPY="$TOOLS/envs/md/bin/python"
[ -s "$CSV" ] && [ -s "$TGTF" ] || { echo "missing csv/target" >&2; exit 2; }
TGT=$(tr -d '\n ' < "$TGTF")
IN="$REPO/runs/boltz_${TAG}/in"; OUT="$REPO/runs/boltz_${TAG}/out"; mkdir -p "$IN" "$OUT"
find "$IN" -name '*.yaml' -delete 2>/dev/null || true   # clear stale inputs from a prior same-TAG run
if [[ "$GPUS" == *-* ]]; then mapfile -t G < <(seq "${GPUS%-*}" "${GPUS#*-}"); else IFS=',' read -ra G <<< "$GPUS"; fi
# Cap CPU threads so concurrent shards don't oversubscribe the shared box (AGENTS.md invariant).
NG=${#G[@]}; CORES=$(nproc 2>/dev/null || echo 8)
export OMP_NUM_THREADS=$(( CORES/NG > 1 ? CORES/NG : 1 )); export MKL_NUM_THREADS=$OMP_NUM_THREADS
"$MDPY" - "$CSV" "$IN" "$TGT" "$NG" <<'PY'
import sys, csv, os
csvf, ind, tgt, ng = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
rows = []
for r in csv.DictReader(open(csvf)):
    nm = (r.get("name") or r.get("design") or "").strip()
    seq = (r.get("sequence") or "").split(":")[0].strip()
    if nm and seq:
        rows.append((nm, seq))
if not rows:
    sys.exit("cofold shard: no valid name+sequence rows in " + csvf)
for g in range(ng):
    os.makedirs(os.path.join(ind, f"g{g}"), exist_ok=True)
for i, (nm, seq) in enumerate(rows):
    open(os.path.join(ind, f"g{i % ng}", nm + ".yaml"), "w").write(
        "version: 1\nsequences:\n  - protein:\n      id: A\n      sequence: %s\n      msa: empty\n"
        "  - protein:\n      id: B\n      sequence: %s\n      msa: empty\n" % (seq, tgt))
print("sharded", len(rows), "designs across", ng, "gpus")
PY
[ $? -eq 0 ] || { echo "cofold shard: input generation FAILED" >&2; exit 2; }
unset VIRTUAL_ENV 2>/dev/null || true
source "$TOOLS/envs/uplifting-boltz2/bin/activate"
[ -s "${BOLTZ_CACHE:-}/boltz2_conf.ckpt" ] || { echo "boltz weights missing: ${BOLTZ_CACHE:-unset}" >&2; exit 2; }
cd "$TOOLS/third_party/uplifting-biomolecular-modeling/boltz2"
# Warm the shared JIT/kernel cache ONCE (serial) so concurrent shards don't race the first-compile
# self-check (which otherwise refuses the mode with rc=3 on all-but-one process).
if [ ! -f "$MODEL_OPT_JIT_ROOT/.glp1r_warmed" ]; then
  echo "[boltz] warming kernel cache on gpu ${G[0]} (one-time) ..."
  CUDA_VISIBLE_DEVICES=${G[0]} bash run.sh warm --config h100 --mode fast \
    --out "$REPO/runs/boltz_${TAG}/warm" > "$REPO/runs/boltz_${TAG}/warm.log" 2>&1 \
    && touch "$MODEL_OPT_JIT_ROOT/.glp1r_warmed" || echo "[boltz] warm rc=$? (continuing)"
fi
pids=()
for idx in "${!G[@]}"; do
  gpu=${G[$idx]}; sub="$IN/g$idx"
  [ -n "$(ls -A "$sub" 2>/dev/null)" ] || continue
  CUDA_VISIBLE_DEVICES=$gpu bash run.sh pred --config h100 --mode fast --seeds "$SEEDS" \
    --input "$sub" --out_dir "$OUT" > "$REPO/runs/boltz_${TAG}/g${gpu}.log" 2>&1 &
  pids+=($!); echo "[boltz] gpu=$gpu shard=g$idx seeds=$SEEDS omp=$OMP_NUM_THREADS"
done
[ "${#pids[@]}" -gt 0 ] || { echo "cofold shard: no non-empty shards to run" >&2; exit 2; }
rc=0; for p in "${pids[@]}"; do wait "$p" || rc=1; done
echo "BOLTZ_SHARD_${TAG}_DONE rc=$rc $(date -u +%FT%TZ) | confidence jsons: $(find "$OUT" -name 'confidence_*.json' 2>/dev/null | wc -l)"
