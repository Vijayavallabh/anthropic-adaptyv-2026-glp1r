#!/bin/bash
# EvoBind2 de-novo LINEAR peptide binder design to the GLP1R 7TM VESTIBULE — the agonism
# bet (only direct de-novo GLP1R-agonist precedent: Li/Bryant 2025, cyclic EC50 31.9 nM).
# Reuses conda env 'evobind' + the ColabFold receptor MSA. Peptide is steered to the deep
# message site via receptor_if_residues (1-indexed fasta positions = UniProt-23).
# LINEAR (no --cyclic_offset) = gene-encodable/submittable. PROVENANCE: EvoBind2 is CC-BY-NC
# (flag on any final-20 pick); AF2 params CC-BY. NOTE: needs a GENUINELY FREE GPU (full AF2
# on ~430 residues); do NOT launch onto a GPU the TNF job is using.
#
# Usage: gen_evobind.sh <outsub> <peptide_length> <niter> <gpu> [max_recycles=8]
set -uo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
EB="$REPO/third_party/EvoBind"
OUTSUB=${1:?outsub}; PLEN=${2:?peptide_length}; NITER=${3:?niter}; GPU=${4:?gpu}; RECYC=${5:-8}
# IFRES (fasta index = UniProt-23) default = deep vestibule message site. Override with $6 to
# target the ACCESSIBLE upper vestibule (orforglipron agonist site) which a peptide can reach
# (a mean-distance loss floors on unreachable buried residues). See lesson-denovo-binder-cant-reach-buried-pocket.
DEEP_IFRES="167,171,174,178,181,182,187,188,191,192,198,207,210,211,214,218,272,275,276,277,283,286,287,290"
IFRES=${6:-$DEEP_IFRES}
FASTA="$EB/data/glp1r/glp1r_construct.fasta"
MSA="$EB/data/glp1r/glp1r_construct.a3m"
[ -s "$FASTA" ] || { echo "no receptor fasta $FASTA" >&2; exit 2; }
[ -s "$MSA" ]   || { echo "no receptor MSA $MSA" >&2; exit 2; }
OUT="$REPO/runs/evobind/$OUTSUB"; mkdir -p "$OUT"
# shellcheck disable=SC1091
source /home/prachh/miniconda3/etc/profile.d/conda.sh
conda activate evobind
export CUDA_VISIBLE_DEVICES=$GPU
export XLA_PYTHON_CLIENT_PREALLOCATE=false   # allocate on demand (do not grab the whole GPU)
echo "[evobind] $OUTSUB plen=$PLEN niter=$NITER gpu=$GPU recyc=$RECYC ifres=$IFRES $(date -u +%FT%TZ)"
cd "$EB"
python3 src/mc_design.py \
  --receptor_fasta_path="$FASTA" \
  --receptor_if_residues="$IFRES" \
  --peptide_length="$PLEN" \
  --msas="$MSA" \
  --output_dir="$OUT/" \
  --model_names=model_1_ptm \
  --data_dir="$EB/src/AF2/" \
  --max_recycles="$RECYC" \
  --num_iterations="$NITER" \
  --predict_only=False
echo "EVOBIND_${OUTSUB}_DONE rc=$? $(date -u +%FT%TZ)"
