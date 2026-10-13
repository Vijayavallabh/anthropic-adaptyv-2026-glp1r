# Shared-tool wiring. The heavy uplifting kits + per-tool venvs + weights are installed ONCE in the
# sibling TNF repo (disk is tight; kits are repo-agnostic). GLP1R inputs/outputs stay in THIS repo.
export TOOLS="${TOOLS:-/home/prachh/v/anthropic-adaptyv-2026-tnf}"
export GLP1R_REPO="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")/.." && pwd)"
# Cache env vars (BOLTZ_CACHE, CHAI_DOWNLOADS_DIR, RFD_ROOT, WEIGHTS_RFD, AF2_PARAMS, MPNN_DIR, ...)
[ -f "$TOOLS/envs/uplifting.env" ] && { set -a; . "$TOOLS/envs/uplifting.env"; set +a; }
# Boltz weight fallback to the stock $HOME/.boltz cache if the kit cache dir isn't populated.
if [ ! -s "${BOLTZ_CACHE:-}/boltz2_conf.ckpt" ] && [ -s "$HOME/.boltz/boltz2_conf.ckpt" ]; then
  export BOLTZ_CACHE="$HOME/.boltz"
fi
# Persistent JIT/kernel cache so concurrent GPU shards reuse a warmed cache (avoids the
# first-compile self-check race that refuses the mode when many procs launch at once).
export MODEL_OPT_JIT_ROOT="${MODEL_OPT_JIT_ROOT:-$GLP1R_REPO/.jit}"
mkdir -p "$MODEL_OPT_JIT_ROOT" 2>/dev/null || true
