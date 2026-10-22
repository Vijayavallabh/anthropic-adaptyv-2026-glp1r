#!/usr/bin/env bash
# Wave-3c (FINAL BC2 wave): ordinary targeting + termini_accessible, to test construct-robustness
# (both termini away so the Met+GFP11/TwinStrep tag sits clear). I=peptide, J=miniprotein. 4 GPUs each.
set -uo pipefail
REPO=/home/prachh/v/anthropic-adaptyv-2026-glp1r
BIN=$REPO/third_party/BindCraft2/.venv/bin/bindcraft
CFG=$REPO/runs/bc2; LOGS=$CFG/logs; mkdir -p "$LOGS"
[ -x "$BIN" ] || { echo "ERR: $BIN missing"; exit 1; }
run_arm () { local name="$1" json="$2" gpus="$3"
  echo "[$(date +%T)] launch $name on GPU[$gpus] -> $LOGS/$name.log"
  CUDA_VISIBLE_DEVICES="$gpus" setsid "$BIN" design "$json" > "$LOGS/$name.log" 2>&1 < /dev/null &
  echo $! > "$LOGS/$name.pid"; }
run_arm I_pep_termaway  "$CFG/armI_pep_termaway.json"  "0,1,2,3"
run_arm J_mini_termaway "$CFG/armJ_mini_termaway.json" "4,5,6,7"
echo "Wave-3c: 2 arms launched (I peptides GPUs 0-3, J miniproteins GPUs 4-7)"
