#!/usr/bin/env bash
# Wave-3b launcher: ordinary-targeted peptides (E,F) + miniproteins (G,H) across GPUs 0-7.
# Rationale: forced-deep lone peptides folded to 0 confident designs (reachability wall); these
# configs CAN yield confident vestibule engagement, which the 2-folder funnel then tests for R299.
set -uo pipefail
REPO=/home/prachh/v/anthropic-adaptyv-2026-glp1r
BIN=$REPO/third_party/BindCraft2/.venv/bin/bindcraft
CFG=$REPO/runs/bc2; LOGS=$CFG/logs; mkdir -p "$LOGS"
[ -x "$BIN" ] || { echo "ERR: $BIN missing"; exit 1; }
run_arm () { # name json gpuset
  local name="$1" json="$2" gpus="$3"
  echo "[$(date +%T)] launch $name on GPU[$gpus] -> $LOGS/$name.log"
  CUDA_VISIBLE_DEVICES="$gpus" setsid "$BIN" design "$json" > "$LOGS/$name.log" 2>&1 < /dev/null &
  echo $! > "$LOGS/$name.pid"
}
run_arm E_pep_reader   "$CFG/armE_pep_reader.json"   "0,1"
run_arm F_pep_deepord  "$CFG/armF_pep_deepord.json"  "2,3"
run_arm G_mini_forced  "$CFG/armG_mini_forced.json"  "4,5"
run_arm H_mini_ord     "$CFG/armH_mini_ord.json"     "6,7"
echo "Wave-3b: 4 arms launched across GPUs 0-7"
