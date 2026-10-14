#!/bin/bash
# DiffPepBuilder (MIT; SE(3) diffusion + ESM; orthogonal to AF2/Boltz) de-novo peptide binder
# design against a GLP1R pocket, with native disulfide building. ORTHOGONAL-GENERATOR probe to
# diversify the win-path monoculture (owner-approved 2026-10-14). Surface-trained model -> deep
# vestibule threading is OUT OF DISTRIBUTION; most likely yields ECD/surface binders (hedge).
#
# Usage: run_diffpep.sh <metadata_csv> <min_len> <max_len> <samples_per_len> <gpu>
#   e.g. run_diffpep.sh data/glp1r_receptor/metadata_vest.csv 12 24 4 0
#
# REPRODUCIBILITY NOTES (third_party/DiffPepBuilder is gitignored; these setup steps were applied):
#   1. conda env create -f environment.yml  (env 'diffpepbuilder'; torch 2.1.0/cu118 works on H100/sm_90).
#   2. DO NOT `conda install -c conda-forge libstdcxx-ng` -> it cascades torch to CPU + MKL2025
#      (undefined symbol iJIT_NotifyEvent). Instead OpenMM's GLIBCXX_3.4.30 need is met at RUNTIME via
#      LD_PRELOAD of a saved GCC-12 libstdc++ (ldfix/libstdc++.so.6).
#   3. PyRosetta: pip install the wheel under its PEP-427 name (a renamed *.whl is rejected by pip).
#   4. Code edits applied to the clone (both needed to run on this box):
#      - experiments/run_inference.py: add `torch.multiprocessing.set_sharing_strategy('file_system')`.
#      - data/utils.py create_data_loader: `prefetch_factor = None if num_workers==0 else prefetch_factor`
#        (was buggy `=2`), so num_loader_workers=0 is usable (dodges the worker-collate
#        "resize storage that is not resizable" from read-only numpy ESM embeds).
#   5. ONE target per invocation: the length-batch sampler pools targets of equal peptide length,
#      and different receptor pocket sizes then fail to stack. Split metadata per target.
set -uo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
DPB="$REPO/third_party/DiffPepBuilder"
CSV=${1:?metadata_csv}; MINL=${2:-12}; MAXL=${3:-24}; SPL=${4:-4}; GPU=${5:-0}
source /home/prachh/miniconda3/etc/profile.d/conda.sh
conda activate diffpepbuilder
export BASE_PATH="$DPB"
export CUDA_VISIBLE_DEVICES=$GPU
export LD_PRELOAD="$DPB/ldfix/libstdc++.so.6"
cd "$DPB"
echo "[diffpep] csv=$CSV len=$MINL-$MAXL spl=$SPL gpu=$GPU $(date -u +%FT%TZ)"
python experiments/run_inference.py \
  data.val_csv_path="$CSV" \
  experiment.use_ddp=False experiment.num_gpus=1 experiment.num_loader_workers=0 \
  inference.sampling.min_length="$MINL" inference.sampling.max_length="$MAXL" \
  inference.sampling.samples_per_length="$SPL"
echo "DIFFPEP_DONE rc=$? $(date -u +%FT%TZ)"
