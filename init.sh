#!/bin/bash
# adaptyv-glp1r harness bootstrap + verification (uv-only).
#   ./init.sh          core env + smoke tests (fast, CPU-only) -- the verification gate
#   ./init.sh --tools  additionally scaffold isolated uv venvs for heavy design tools + novelty gate
set -euo pipefail
unset VIRTUAL_ENV 2>/dev/null || true
cd "$(dirname "$0")"

echo "=== adaptyv-glp1r :: core environment (uv sync) ==="
uv sync

echo "=== compile check ==="
uv run python -m compileall -q src scripts

echo "=== tests (pytest) ==="
uv run pytest -q

echo "=== submission validator self-check (Track 3) ==="
uv run python scripts/validate_submission.py submissions/example_track3.csv --track 3

if [[ "${1:-}" == "--tools" ]]; then
  echo ""
  echo "=== heavy tool stacks (isolated; NOT part of the core gate) ==="
  mkdir -p envs third_party weights
  echo "Novelty gate (FoldSeek + MMseqs2): scripts/setup_tools.sh novelty"
  echo "Generators/folders reuse the sibling repos' venvs + Anthropic uplifting kit (configs/tools.yaml)."
  echo "(Weight installs are NOT auto-run: heavy and some are license/gated.)"
fi

echo ""
echo "=== Verification Complete -- environment is clean and restartable ==="
echo "Next: read AGENTS.md, progress.md, configs/target.yaml, docs/PLAN_GLP1R.md."
echo "Before every upload: uv run python scripts/validate_submission.py <csv> --track 3  (USER-GATED)"
