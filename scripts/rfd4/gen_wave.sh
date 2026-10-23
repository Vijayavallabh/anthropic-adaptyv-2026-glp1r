#!/usr/bin/env bash
# RFD4-Proteina GLP1R vestibule generation wave.
#   pep (8-20) GPU 0-3 @ PEP_BSZ; mini (50-90, 0-Cys) GPU 4-7 @ MINI_BSZ. Base gen ('~metrics' => no oracle).
#   NOTE (measured 2026-10-22): RFD4 is COMPUTE-BOUND on this ~485-token target — throughput is flat
#   across batch (mini ~0.04 designs/s/GPU at any batch). Batch only sets VRAM use, not speed; we fill
#   ~70GB/card (safe margin below the 80GB OOM edge) with expandable_segments. Real throughput = 8 GPUs
#   in parallel x replicates. compile_lengths=null (eager). Firewall: candidate geometries only.
# Usage: bash scripts/rfd4/gen_wave.sh [replicates_per_proc=256] [pep_bsz=36] [mini_bsz=28]
set -uo pipefail
REPO=/home/prachh/v/anthropic-adaptyv-2026-glp1r
GEN="$REPO/third_party/RFD4-Proteina/.venv/bin/rfd4-generate"
export HF_HOME=/home/prachh/work/cache/huggingface
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
OUT="$REPO/runs/rfd4/wave"; mkdir -p "$OUT"
REPL=${1:-256}; PEP_BSZ=${2:-36}; MINI_BSZ=${3:-28}
PEP="$REPO/runs/rfd4/specs/pep.yaml"; MINI="$REPO/runs/rfd4/specs/mini.yaml"
launch(){ local spec=$1 gpu=$2 seed=$3 bsz=$4 tag=$5
  CUDA_VISIBLE_DEVICES=$gpu "$GEN" inputs="$spec" '~metrics' compile_lengths=null \
    num_replicates="$REPL" batch_size="$bsz" seed="$seed" out_dir="$OUT/$tag" > "$OUT/$tag.log" 2>&1 & }
launch "$PEP"  0 101 "$PEP_BSZ" pep_g0;  launch "$PEP"  1 102 "$PEP_BSZ" pep_g1
launch "$PEP"  2 103 "$PEP_BSZ" pep_g2;  launch "$PEP"  3 104 "$PEP_BSZ" pep_g3
launch "$MINI" 4 201 "$MINI_BSZ" mini_g4; launch "$MINI" 5 202 "$MINI_BSZ" mini_g5
launch "$MINI" 6 203 "$MINI_BSZ" mini_g6; launch "$MINI" 7 204 "$MINI_BSZ" mini_g7
echo "wave: 4xpep(bsz $PEP_BSZ) + 4xmini(bsz $MINI_BSZ), $REPL repl each = $((8*REPL)) designs; waiting..."
wait
echo "WAVE_DONE $(date -u +%FT%TZ)"
