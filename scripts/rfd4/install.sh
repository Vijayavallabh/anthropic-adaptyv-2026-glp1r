#!/usr/bin/env bash
# RFD4-Proteina (Baker/IPD + NVIDIA GenAIR) install — OWNER-RUN via `!`
#   (environment-setup change = owner-gated per CLAUDE.md; the harness also blocks the assistant
#    from first-running freshly-cloned external code — same handoff as the BindCraft2 install.)
#
# ELIGIBILITY: BSD-3-Clause for code AND the Hugging Face weights bundle (Institute for Protein
# Design / University of Washington copyright) — on the clean/explicit license list, same as
# RFdiffusion/RFd3. NO NGC account, NO gating, NO license click-through. ODC-BY output release clean.
# The OPTIONAL AF2 / AlphaFold3 / OpenFold3 reward+metric images carry their own upstream terms, so we
# SKIP them (--skip-search-envs): base generation runs with no folder in the loop; designs are judged
# ONLY by our own independent Boltz∧Chai 2-folder bar (firewall: never an agonism claim).
#
# Run:   ! bash scripts/rfd4/install.sh
set -euo pipefail
cd "$(dirname "$0")/../.."                         # repo root
DEST=third_party/RFD4-Proteina                     # gitignored
mkdir -p third_party

if [ ! -d "$DEST/.git" ]; then
  echo "=== clone RFD4-Proteina ==="
  git clone https://github.com/RosettaCommons/RFD4-Proteina.git "$DEST"
fi
cd "$DEST"
echo "=== repo HEAD ==="; git log -1 --oneline 2>/dev/null || true
echo "=== LICENSE (expect BSD-3-Clause, IPD/UW) ==="; sed -n '1,8p' LICENSE 2>/dev/null || true

echo "=== setup: uv venv py3.12 + deps + cache the BSD-3 HF weights (~1.7GB), SKIP AF2/AF3/OF3 search envs ==="
echo "    (--skip-search-envs keeps AlphaFold3 out of the loop for eligibility AND shrinks the install;"
echo "     if the build dies, paste the error back and I'll patch — same iterate-from-output loop as BC2.)"
if [ -f setup.sh ]; then
  bash setup.sh --skip-search-envs
else
  make setup
fi

echo "=== activate + smoke test ==="
# shellcheck disable=SC1091
source .venv/bin/activate
rfd4-generate --help 2>/dev/null | head -40 || python -c "import rfd4; print('rfd4 import OK', getattr(rfd4,'__version__','?'))"

echo "=== DONE: RFD4-Proteina at $DEST — base-generation ready, no AF3 in the loop ==="
echo "Hand back to the assistant: build the GLP1R active-state (6X18) target YAML (contig + vestibule"
echo "range + R299/reader hotspots + burial/H-bond conditions, 0-Cys, natural AAs), generate on free"
echo "GPUs (1-7; compare fold keeps GPU 0), then run the Boltz∧Chai 2-folder construct funnel."
