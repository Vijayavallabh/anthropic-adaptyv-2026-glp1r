"""adaptyv_glp1r — de-novo GLP1R AGONIST design toolkit.

Anthropic x Adaptyv 2026 Protein Design Competition, Challenge 3 (Track 3).

The win condition is ACTIVATION (cell-surface GLP1R -> Gαs -> cAMP -> CRE-SEAP),
not binding. See AGENTS.md for the invariants and docs/PLAN_GLP1R.md for the plan.
"""
from __future__ import annotations

from .submission import format_report, validate_csv, write_submission  # noqa: F401

__all__ = ["validate_csv", "write_submission", "format_report", "main"]


def main() -> int:
    """Console entry point: a thin wrapper around the submission validator."""
    import sys
    from pathlib import Path

    if len(sys.argv) < 2:
        print("usage: adaptyv-glp1r <submission.csv>   # validates against the Track-3 contract")
        return 2
    rep = validate_csv(Path(sys.argv[1]), track=3)
    print(format_report(rep, sys.argv[1]))
    return 0 if rep.ok else 1
