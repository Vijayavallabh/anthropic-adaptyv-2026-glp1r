#!/usr/bin/env bash
# Proteina-Complexa (NVIDIA) install — OWNER-RUN via `!` (the harness blocks the assistant from
# executing freshly-cloned external code; same handoff as the BindCraft2 install).
#
# ELIGIBILITY (owner-ruled 2026-10-22; confirmed from primary license text):
#   code = Apache-2.0; weights = NVIDIA Open Model License (output-permissive —
#   §2.4 "NVIDIA claims no ownership rights in outputs"; §1.1 "An output is not a Derivative Model";
#   no field-of-use / non-commercial clause). ODC-BY output release OK. Cite NVIDIA-OML in methods;
#   do NOT redistribute the weights (§3 NOTICE duty attaches to the MODEL, not the designs).
#
# PREREQUISITE (owner-only, gated): an NGC account + API key, with the Proteina-Complexa model
# license ACCEPTED on its NGC model page (catalog.ngc.nvidia.com/.../proteina_complexa). Then set:
#   ngc config set            # paste API key   (or:  export NGC_CLI_API_KEY=<key>)
# Without NGC creds + license-acceptance, `complexa download` cannot fetch the generator weights.
#
# Run:   ! bash scripts/complexa/install.sh
set -euo pipefail
cd "$(dirname "$0")/../.."                        # repo root
DEST=third_party/Proteina-Complexa                # gitignored
mkdir -p third_party

if [ ! -d "$DEST/.git" ]; then
  echo "=== clone Proteina-Complexa ==="
  git clone https://github.com/NVIDIA-Digital-Bio/Proteina-Complexa "$DEST"
fi
cd "$DEST"
echo "=== repo HEAD ==="; git log -1 --oneline 2>/dev/null || true
echo "=== LICENSE / licenses/ (honor terms) ==="; sed -n '1,30p' LICENSE 2>/dev/null; echo "--- licenses/ ---"; ls licenses/ 2>/dev/null || true

echo "=== build uv env (README: Python 3.12, torch 2.7.0+cu126; ~10-20 min) ==="
echo "    NOTE: tmol can fail on py3.12 (llvmlite/numba pins). If the build dies on tmol,"
echo "    paste the error back — the README documents a workaround to add before the tmol line,"
echo "    and I'll patch env/build_uv_env.sh from your output (same iterate-from-output loop as BC2)."
./env/build_uv_env.sh

echo "=== activate + init (.env with AF2_DIR / ESM_DIR / RF3_* placeholders) ==="
# shellcheck disable=SC1091
source .venv/bin/activate
complexa init || true

echo "=== download weights from NGC (needs NGC creds + accepted model license) ==="
if ! complexa download --all; then
  echo "!! weights download failed — almost certainly NGC auth / license-acceptance."
  echo "   Fix: create NGC API key, accept the model license on its NGC page, then:"
  echo "        ngc config set   (or export NGC_CLI_API_KEY=<key>)   and re-run this script."
  exit 3
fi

echo "=== DONE: Proteina-Complexa installed at $DEST ==="
echo "Hand back to the assistant: wire the AF2-Multimer reward (eligible) or run base sampling"
echo "(no folder in the loop), point it at the active-state 6X18 GLP1R vestibule + R299 hotspots,"
echo "then judge every design through OUR independent Boltz∧Chai 2-folder construct bar on free GPUs."
