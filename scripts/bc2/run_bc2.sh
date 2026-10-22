#!/usr/bin/env bash
# BindCraft2 v1.0.4 active-state GLP1R peptide campaign launcher.
# Usage:  bash scripts/bc2/run_bc2.sh [smoke|arms|all]   (default: all)
# Firewall: every design here is a NECESSARY-CONDITION geometry bet (deep-vestibule
# contact, construct-robust termini), never an agonism claim. The wet cAMP/SEAP assay is the judge.
set -uo pipefail
REPO=/home/prachh/v/anthropic-adaptyv-2026-glp1r
BC2=$REPO/third_party/BindCraft2
BIN=$BC2/.venv/bin/bindcraft
CFG=$REPO/runs/bc2
LOGS=$CFG/logs; mkdir -p "$LOGS"
mode="${1:-all}"

if [[ ! -x "$BIN" ]]; then
  echo "ERROR: $BIN not found. Install BC2 first:"
  echo "  cd $BC2 && env -u VIRTUAL_ENV -u CONDA_PREFIX bash install.sh cuda13"
  exit 1
fi

run_arm () { # name json gpuset
  local name="$1" json="$2" gpus="$3"
  echo "[$(date +%T)] launch $name on GPU[$gpus] -> $LOGS/$name.log"
  CUDA_VISIBLE_DEVICES="$gpus" \
    setsid "$BIN" design "$json" > "$LOGS/$name.log" 2>&1 < /dev/null &
  echo $! > "$LOGS/$name.pid"
}

if [[ $mode == smoke || $mode == all ]]; then
  echo "=== SMOKE TEST (GPU 0, 2 trajectories) ==="
  CUDA_VISIBLE_DEVICES=0 "$BIN" design "$CFG/smoke.json" 2>&1 | tail -60
  echo "=== smoke done ==="
fi

if [[ $mode == arms || $mode == all ]]; then
  # TfR1 + mva finished; all 8 GPUs free. 2 GPUs/arm, BC2 auto-packs ~2 workers/card.
  run_arm armA_deepcore        "$CFG/armA_deepcore.json"        "0,1"
  run_arm armB_constructrobust "$CFG/armB_constructrobust.json" "2,3"
  run_arm armC_polarnet        "$CFG/armC_polarnet.json"        "4,5"
  run_arm armD_deephelix       "$CFG/armD_deephelix.json"       "6,7"
  echo "all 4 arms launched across GPUs 0-7; tail e.g.:  tail -f $LOGS/armA_deepcore.log"
fi
