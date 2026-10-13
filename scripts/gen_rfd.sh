#!/bin/bash
# RFdiffusion-1 binder design to GLP1R (reuses the TNF-installed rfdiffusion1 kit + weights).
# Target = 6X18 receptor chain R (active state). Usage:
#   gen_rfd.sh <outsub> <contig> <hotspots_csv> <ndes> <gpu>
#   contig   : e.g. "R140-338/0 60-90"  (gap-free target range R140-338 + a 60-90aa binder)
#   hotspots : chain-R author numbering, e.g. "R190,R194,R233,R234,R237" (the compact vestibule cluster)
set -uo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"; cd "$REPO"; . "$REPO/scripts/env.sh"
OUTSUB=${1:?outsub}; CONTIG=${2:?contig}; HOTS=${3:?hotspots}; NDES=${4:-8}; GPU=${5:-1}
INP="${RFD_INPUT:-$REPO/data/raw/6X18_receptorR.pdb}"
[ -s "$INP" ] || { echo "RFd target pdb missing: $INP" >&2; exit 2; }
unset VIRTUAL_ENV 2>/dev/null || true
source "$TOOLS/envs/uplifting-rfdiffusion1/bin/activate"
export RFD_ROOT="${RFD_ROOT:-$TOOLS/third_party/RFdiffusion}"
export WEIGHTS="${WEIGHTS_RFD:-$TOOLS/weights/rfdiffusion1}"
export CUDA_VISIBLE_DEVICES=$GPU
export OMP_NUM_THREADS=$(( $(nproc 2>/dev/null||echo 8)/4 > 1 ? $(nproc)/4 : 1 ))
OUTDIR="$REPO/runs/rfd/$OUTSUB"; mkdir -p "$OUTDIR"
cd "$TOOLS/third_party/uplifting-biomolecular-modeling/rfdiffusion1"
echo "[rfd] gpu=$GPU contig=[$CONTIG] hotspots=[$HOTS] ndes=$NDES in=$INP -> $OUTDIR $(date -u +%FT%TZ)"
bash run.sh design --config h100 --mode fast \
  inference.input_pdb="$INP" \
  "contigmap.contigs=[$CONTIG]" \
  "ppi.hotspot_res=[$HOTS]" \
  denoiser.noise_scale_ca=0 denoiser.noise_scale_frame=0 \
  inference.num_designs="$NDES" \
  inference.output_prefix="$OUTDIR/des"
echo "RFD_${OUTSUB}_DONE rc=$? $(date -u +%FT%TZ) | pdbs: $(find "$OUTDIR" -name 'des_*.pdb' 2>/dev/null | wc -l)"
