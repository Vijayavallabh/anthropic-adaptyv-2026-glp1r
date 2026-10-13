#!/bin/bash
# EvoBind predict_only: fold ONE given peptide sequence against the GLP1R construct receptor and
# report if_dist + plddt + a clean (non-MC) pose. Used to (a) harden the message-reader-engagement
# evidence on a FRESH fixed-seed fold, and (b) score disulfide-stapled variants. Reuses conda env
# 'evobind' + the ColabFold receptor MSA. Fresh output_dir is REQUIRED (a pre-existing metrics.csv
# makes predict_only skip the fold -> NameError on save). Needs a GENUINELY FREE GPU.
#
# Usage: eval_evobind_predict.sh <outsub> <sequence> <gpu> [ifres] [seed=42] [recyc=8]
set -uo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
EB="$REPO/third_party/EvoBind"
OUTSUB=${1:?outsub}; SEQ=${2:?sequence}; GPU=${3:?gpu}
DEEP="167,171,174,178,181,182,187,188,191,192,198,207,210,211,214,218,272,275,276,277,283,286,287,290"
IFRES=${4:-$DEEP}; SEED=${5:-42}; RECYC=${6:-8}
PLEN=${#SEQ}
FASTA="$EB/data/glp1r/glp1r_construct.fasta"
MSA="$EB/data/glp1r/glp1r_construct.a3m"
[ -s "$FASTA" ] || { echo "no receptor fasta $FASTA" >&2; exit 2; }
[ -s "$MSA" ]   || { echo "no receptor MSA $MSA" >&2; exit 2; }
OUT="$REPO/runs/evobind_predict/$OUTSUB"
mkdir -p "$OUT"; rm -f "$OUT/metrics.csv"      # predict_only needs NO pre-existing metrics.csv
# shellcheck disable=SC1091
source /home/prachh/miniconda3/etc/profile.d/conda.sh
conda activate evobind
export CUDA_VISIBLE_DEVICES=$GPU
export XLA_PYTHON_CLIENT_PREALLOCATE=false
export JAX_COMPILATION_CACHE_DIR="$REPO/runs/.jax_cache"   # reuse XLA compiles across same-length folds
echo "[predict] $OUTSUB plen=$PLEN gpu=$GPU seed=$SEED seq=$SEQ $(date -u +%FT%TZ)"
cd "$EB"
python3 src/mc_design.py \
  --receptor_fasta_path="$FASTA" \
  --receptor_if_residues="$IFRES" \
  --peptide_length="$PLEN" \
  --peptide_sequence="$SEQ" \
  --msas="$MSA" \
  --output_dir="$OUT/" \
  --model_names=model_1_ptm \
  --data_dir="$EB/src/AF2/" \
  --max_recycles="$RECYC" \
  --num_iterations=1 \
  --predict_only=True \
  --random_seed="$SEED"
echo "PREDICT_${OUTSUB}_DONE rc=$? seq=$SEQ $(date -u +%FT%TZ)"
