#!/usr/bin/env bash
# Boltz-2 single-sequence co-fold (binder chain A : receptor chain B, msa empty), reusing the
# established sepiq .venv-boltz. NECESSARY-CONDITION binding/geometry only; never an agonism claim.
# Usage: fold_boltz.sh <designs_csv:name,sequence> <receptor_seq_file> <out_root> <gpu> <seeds_csv>
# Writes per-seed out dirs; score each with scripts/iface_score.py.
set -uo pipefail
BOLTZ=/home/prachh/v/sepiq-2026-challenge/.venv-boltz/bin/boltz
CSV=${1:?designs csv}; TGTF=${2:?receptor seq file}; OUT=${3:?out root}; GPU=${4:-0}; SEEDS=${5:-0}
[ -x "$BOLTZ" ] || { echo "ERR: boltz CLI not found at $BOLTZ" >&2; exit 2; }
TGT=$(tr -d '\n ' < "$TGTF")
IN="$OUT/in"; mkdir -p "$IN"
/home/prachh/v/sepiq-2026-challenge/.venv-boltz/bin/python - "$CSV" "$IN" "$TGT" <<'PY'
import sys, csv, os
csvf, ind, tgt = sys.argv[1], sys.argv[2], sys.argv[3]
n = 0
for r in csv.DictReader(open(csvf)):
    nm = (r.get("name") or r.get("design") or "").strip()
    seq = (r.get("sequence") or "").split(":")[0].strip().upper()
    if nm and seq:
        open(os.path.join(ind, nm + ".yaml"), "w").write(
            "version: 1\nsequences:\n  - protein:\n      id: A\n      sequence: %s\n      msa: empty\n"
            "  - protein:\n      id: B\n      sequence: %s\n      msa: empty\n" % (seq, tgt))
        n += 1
print("wrote", n, "yaml(s) to", ind)
PY
export OMP_NUM_THREADS=4 MKL_NUM_THREADS=4
IFS=',' read -ra SS <<< "$SEEDS"
rc=0
for s in "${SS[@]}"; do
  echo "[boltz] gpu=$GPU seed=$s -> $OUT/seed$s"
  # single-sequence: omit --use_msa_server (default False); the YAML carries msa: empty
  CUDA_VISIBLE_DEVICES="$GPU" "$BOLTZ" predict "$IN" --out_dir "$OUT/seed$s" --seed "$s" \
      --output_format mmcif --num_workers 1 > "$OUT/boltz_seed$s.log" 2>&1 || rc=1
done
echo "FOLD_BOLTZ_DONE rc=$rc cifs=$(find "$OUT" -name '*_model_0.cif' 2>/dev/null | wc -l) pae=$(find "$OUT" -name 'pae_*_model_0.npz' 2>/dev/null | wc -l)"
exit $rc
