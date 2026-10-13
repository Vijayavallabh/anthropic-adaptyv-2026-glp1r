#!/bin/bash
# LigandMPNN binder-interface sequence design for RFd backbones (reuses the TNF-installed
# LigandMPNN + proteinmpnn_v_48_020 weights). Receptor chain R is held FIXED; the binder
# chain A is redesigned. 0 Cys (--omit_AA C) to avoid unpaired-Cys liability (filters.yaml).
# Concurrency capped at one proc/GPU (LigandMPNN ~2 GB each; coexists with a busy box).
#
# Usage: seq_mpnn.sh <indir_with_des_pdbs> <outsub> [nseq=8] [gpus=0-3] [temp=0.2]
# Output: runs/mpnn/<outsub>/<design>/seqs/*.fa  + runs/mpnn/<outsub>/variants.csv (name,sequence)
set -uo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"; cd "$REPO"; . "$REPO/scripts/env.sh" >/dev/null 2>&1 || true
INDIR=${1:?indir}; OUTSUB=${2:?outsub}; NSEQ=${3:-8}; GPUS=${4:-0-3}; TEMP=${5:-0.2}
LM=/home/prachh/v/anthropic-adaptyv-2026-tnf/third_party/LigandMPNN
CKPT="$LM/model_params/proteinmpnn_v_48_020.pt"
[ -x "$LM/.venv/bin/python" ] || { echo "no LigandMPNN venv at $LM" >&2; exit 2; }
[ -s "$CKPT" ] || { echo "no ckpt $CKPT" >&2; exit 2; }
OUT="$REPO/runs/mpnn/$OUTSUB"; mkdir -p "$OUT"
IFS='-' read -r g0 g1 <<< "$GPUS"; gpus=($(seq "$g0" "$g1")); ng=${#gpus[@]}
nb=$(( NSEQ/4 > 0 ? NSEQ/4 : 1 )); bs=$(( NSEQ/nb ))
echo "[mpnn] $OUTSUB indir=$INDIR nseq=$NSEQ (nb=$nb bs=$bs) gpus=${gpus[*]} temp=$TEMP $(date -u +%FT%TZ)"
pids=(); i=0
for pdb in "$INDIR"/des_*.pdb; do
  [ -s "$pdb" ] || continue
  name=$(basename "$pdb" .pdb)
  g=${gpus[$(( i % ng ))]}
  CUDA_VISIBLE_DEVICES=$g OMP_NUM_THREADS=2 nohup "$LM/.venv/bin/python" "$LM/run.py" \
    --model_type protein_mpnn --checkpoint_protein_mpnn "$CKPT" \
    --pdb_path "$pdb" --chains_to_design "A" --omit_AA "C" \
    --temperature "$TEMP" --number_of_batches "$nb" --batch_size "$bs" \
    --out_folder "$OUT/$name" --seed 17 > "$OUT/${name}.log" 2>&1 &
  pids+=($!); i=$((i+1))
  if (( ${#pids[@]} >= ng )); then wait "${pids[0]}" 2>/dev/null || true; pids=("${pids[@]:1}"); fi
done
for p in "${pids[@]}"; do wait "$p" 2>/dev/null || true; done
# extract binder (chain A = first colon field) sequences -> variants.csv
"$REPO/.venv/bin/python" -I - "$OUT" <<'PY'
import glob, csv, os, sys
OUT=sys.argv[1]; rows=[]; seen=set()
for fa in sorted(glob.glob(f"{OUT}/*/seqs/*.fa")):
    design=os.path.basename(os.path.dirname(os.path.dirname(fa)))
    lines=[l for l in open(fa).read().splitlines() if l.strip()]
    recs=[(lines[j],lines[j+1]) for j in range(0,len(lines)-1,2) if lines[j].startswith(">")]
    for k,(hdr,seq) in enumerate(recs):
        if k==0: continue   # record 0 = the input (RFd poly-Gly placeholder), not a design
        binder=seq.split(":")[0].strip().replace("/","")
        nm=f"{design}_m{k}"
        if binder and nm not in seen and "X" not in binder:
            seen.add(nm); rows.append((nm,binder,len(binder)))
with open(f"{OUT}/variants.csv","w",newline="") as fh:
    w=csv.writer(fh); w.writerow(["name","sequence","length"])
    for r in rows: w.writerow(r)
print(f"[mpnn] {len(rows)} binder seqs -> {OUT}/variants.csv")
PY
echo "MPNN_${OUTSUB}_DONE $(date -u +%FT%TZ)"
