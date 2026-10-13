#!/bin/bash
# Boltz-2 single-seq cofold (binder chain A : target chain B, msa empty), reusing the TNF-installed kit.
# Usage: cofold_boltz.sh <csv:name,sequence> <target_seq_file> <tag> <gpu>
set -uo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"; cd "$REPO"
. "$REPO/scripts/env.sh"
CSV=${1:?csv}; TGTF=${2:?target_seq_file}; TAG=${3:-cal}; GPU=${4:-0}
MDPY="$TOOLS/envs/md/bin/python"
[ -s "$CSV" ]  || { echo "csv missing/empty: $CSV" >&2; exit 2; }
[ -s "$TGTF" ] || { echo "target seq missing/empty: $TGTF" >&2; exit 2; }
TGT=$(tr -d '\n ' < "$TGTF"); [ -n "$TGT" ] || { echo "empty target seq" >&2; exit 2; }
IN="$REPO/runs/boltz_${TAG}/in"; OUT="$REPO/runs/boltz_${TAG}/out"; mkdir -p "$IN" "$OUT"
"$MDPY" - "$CSV" "$IN" "$TGT" <<'PY'
import sys, csv, os
csvf, ind, tgt = sys.argv[1], sys.argv[2], sys.argv[3]
n = 0
for r in csv.DictReader(open(csvf)):
    nm = (r.get("name") or r.get("design") or "").strip()
    seq = (r.get("sequence") or "").split(":")[0].strip()
    if not (nm and seq):
        continue
    open(os.path.join(ind, nm + ".yaml"), "w").write(
        "version: 1\nsequences:\n  - protein:\n      id: A\n      sequence: %s\n      msa: empty\n"
        "  - protein:\n      id: B\n      sequence: %s\n      msa: empty\n" % (seq, tgt))
    n += 1
print("wrote", n, "YAMLs ->", ind)
PY
export CUDA_VISIBLE_DEVICES=$GPU
unset VIRTUAL_ENV 2>/dev/null || true
source "$TOOLS/envs/uplifting-boltz2/bin/activate"
[ -s "${BOLTZ_CACHE:-}/boltz2_conf.ckpt" ] || { echo "BOLTZ weights missing at '${BOLTZ_CACHE:-unset}'" >&2; exit 2; }
cd "$TOOLS/third_party/uplifting-biomolecular-modeling/boltz2"
echo "[boltz] gpu=$GPU cache=$BOLTZ_CACHE in=$IN out=$OUT $(date -u +%FT%TZ)"
bash run.sh pred --config h100 --mode fast --input "$IN" --out_dir "$OUT"
echo "BOLTZ_${TAG}_DONE rc=$? $(date -u +%FT%TZ) | confidence jsons: $(find "$OUT" -name 'confidence_*.json' 2>/dev/null | wc -l)"
