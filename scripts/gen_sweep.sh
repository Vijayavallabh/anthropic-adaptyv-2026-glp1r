#!/bin/bash
# RFd production sweep: fan out gen_rfd.sh over the validated binding sites, with a
# concurrency cap + GPU rotation so RFd's ~4 GB coexists with the busy box (never clobber).
# Edit CONFIGS to extend (micro/large, more sites) after the first co-fold signal.
#   config = tag | "contig len" | hotspots_csv | ndes
# Usage: gen_sweep.sh ["g0 g1 ..."=1 3 5] [maxconcurrent=2]
set -uo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"; cd "$REPO"
CONFIGS=(
  "tm5tip_mini|R140-338/0 60-90|R298,R299,R300,R306|24"   # vestibule rim (agonism-relevant site)
  "ecl2_mini|R140-338/0 60-90|R210,R211,R214,R215|24"     # ECL2 broad accessible loop (strong-binder hedge)
  "ecd_mini|R29-129/0 60-90|R32,R35,R36,R39|24"           # ECD address groove (antagonist control + diversity)
)
read -r -a GPUS <<< "${1:-1 3 5}"
MAXC=${2:-2}
echo "[sweep] ${#CONFIGS[@]} configs, gpus=${GPUS[*]}, maxc=$MAXC $(date -u +%FT%TZ)"
pids=(); i=0
for cfg in "${CONFIGS[@]}"; do
  IFS='|' read -r tag contig hots ndes <<< "$cfg"
  g=${GPUS[$(( i % ${#GPUS[@]} ))]}
  echo "[sweep] launch $tag gpu$g [$contig] hots=$hots ndes=$ndes"
  nohup bash scripts/gen_rfd.sh "$tag" "$contig" "$hots" "$ndes" "$g" > "runs/rfd_${tag}.log" 2>&1 &
  pids+=($!); i=$((i+1))
  if (( ${#pids[@]} >= MAXC )); then wait "${pids[0]}" 2>/dev/null || true; pids=("${pids[@]:1}"); fi
done
for p in "${pids[@]}"; do wait "$p" 2>/dev/null || true; done
echo "SWEEP_DONE $(date -u +%FT%TZ)"
for cfg in "${CONFIGS[@]}"; do IFS='|' read -r tag _ _ _ <<< "$cfg"
  echo "  $tag: $(find "runs/rfd/$tag" -name 'des_*.pdb' 2>/dev/null | wc -l) pdbs"; done
