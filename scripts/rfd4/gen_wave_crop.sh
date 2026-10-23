#!/usr/bin/env bash
# RFD4-Proteina CROPPED (7TM vestibule, contiguous F145-432) wave: pep_crop GPU0-3, mini_crop GPU4-7.
# ~1.7x faster than full receptor + vestibule-focused. Base gen ('~metrics' => no oracle). Firewall: geometry only.
# Every design is still judged against the FULL receptor in the Boltz/Chai bar (crop can't fake a pass).
# Usage: bash scripts/rfd4/gen_wave_crop.sh [replicates_per_proc=256] [pep_bsz=48] [mini_bsz=36]
set -uo pipefail
REPO=/home/prachh/v/anthropic-adaptyv-2026-glp1r
GEN="$REPO/third_party/RFD4-Proteina/.venv/bin/rfd4-generate"
export HF_HOME=/home/prachh/work/cache/huggingface
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
OUT="$REPO/runs/rfd4/wave_crop"; mkdir -p "$OUT"
REPL=${1:-256}; PEP_BSZ=${2:-48}; MINI_BSZ=${3:-36}
PEP="$REPO/runs/rfd4/specs/pep_crop.yaml"; MINI="$REPO/runs/rfd4/specs/mini_crop.yaml"
launch(){ local spec=$1 gpu=$2 seed=$3 bsz=$4 tag=$5
  CUDA_VISIBLE_DEVICES=$gpu "$GEN" inputs="$spec" '~metrics' compile_lengths=null \
    num_replicates="$REPL" batch_size="$bsz" seed="$seed" out_dir="$OUT/$tag" > "$OUT/$tag.log" 2>&1 & }
launch "$PEP"  0 301 "$PEP_BSZ" pepc_g0;  launch "$PEP"  1 302 "$PEP_BSZ" pepc_g1
launch "$PEP"  2 303 "$PEP_BSZ" pepc_g2;  launch "$PEP"  3 304 "$PEP_BSZ" pepc_g3
launch "$MINI" 4 401 "$MINI_BSZ" minic_g4; launch "$MINI" 5 402 "$MINI_BSZ" minic_g5
launch "$MINI" 6 403 "$MINI_BSZ" minic_g6; launch "$MINI" 7 404 "$MINI_BSZ" minic_g7
echo "crop wave: 4xpep_crop(bsz $PEP_BSZ)+4xmini_crop(bsz $MINI_BSZ), $REPL repl = $((8*REPL)) designs; waiting..."
wait
echo "CROP_WAVE_DONE $(date -u +%FT%TZ)"
