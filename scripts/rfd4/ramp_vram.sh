#!/usr/bin/env bash
# Find the max feasible batch_size for RFD4 on the FULL 6X18 receptor (n~485; pair-rep ~ batch*n^2).
# Low ramp + expandable_segments; capture peak VRAM, completion, and wall-time (=> designs/sec vs batch).
# Designs produced are real (kept in runs/rfd4/ramp) and harvestable.
set -uo pipefail
REPO=/home/prachh/v/anthropic-adaptyv-2026-glp1r
GEN="$REPO/third_party/RFD4-Proteina/.venv/bin/rfd4-generate"
export HF_HOME=/home/prachh/work/cache/huggingface
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
OUT="$REPO/runs/rfd4/ramp"; mkdir -p "$OUT"
PEP="$REPO/runs/rfd4/specs/pep.yaml"; MINI="$REPO/runs/rfd4/specs/mini.yaml"
JOBS=( "0:$MINI:8" "1:$MINI:16" "2:$MINI:24" "3:$MINI:32" "4:$PEP:32" "5:$PEP:48" "6:$PEP:64" "7:$PEP:96" )
declare -A B SP
for j in "${JOBS[@]}"; do IFS=: read -r g s b <<<"$j"; B[$g]=$b; SP[$g]=$s
  : > "$OUT/g${g}.log"
  CUDA_VISIBLE_DEVICES=$g "$GEN" inputs="$s" '~metrics' compile_lengths=null \
    num_replicates="$b" batch_size="$b" seed=99 out_dir="$OUT/g${g}_b${b}" >> "$OUT/g${g}.log" 2>&1 &
done
declare -A PEAK DONET; for g in 0 1 2 3 4 5 6 7; do PEAK[$g]=0; done
start=$SECONDS; finished=0
while [ "$finished" -lt 8 ] && [ $((SECONDS-start)) -lt 1200 ]; do
  finished=0
  for g in 0 1 2 3 4 5 6 7; do
    L="$OUT/g${g}.log"
    if [ -z "${DONET[$g]:-}" ] && grep -qiE "Generation complete" "$L" 2>/dev/null; then DONET[$g]=$((SECONDS-start)); fi
    if [ -n "${DONET[$g]:-}" ] || grep -qiE "out of memory|CUDA error|Traceback|RuntimeError" "$L" 2>/dev/null; then finished=$((finished+1)); fi
    u=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits -i "$g" 2>/dev/null | tr -d ' ')
    [ -n "$u" ] && [ "$u" -gt "${PEAK[$g]}" ] && PEAK[$g]=$u
  done
  sleep 5
done
echo "=== RAMP2 RESULTS (peak MiB / 81920) ==="
for g in 0 1 2 3 4 5 6 7; do
  tag=$([ "${SP[$g]}" = "$PEP" ] && echo pep || echo mini)
  ok=$(grep -ciE "Generation complete" "$OUT/g${g}.log" 2>/dev/null)
  oom=$(grep -ciE "out of memory|CUDA error" "$OUT/g${g}.log" 2>/dev/null)
  el="${DONET[$g]:-NA}"; tp="NA"; [ "$el" != "NA" ] && [ "$el" -gt 0 ] && tp=$(awk "BEGIN{printf \"%.2f\", ${B[$g]}/$el}")
  echo "gpu$g $tag batch=${B[$g]} peak=${PEAK[$g]}MiB complete=$ok oom=$oom elapsed=${el}s designs_per_s=$tp"
done
echo "RAMP2_DONE $(date -u +%FT%TZ)"
