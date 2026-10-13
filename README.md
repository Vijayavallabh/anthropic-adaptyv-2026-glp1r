# anthropic-adaptyv-2026-glp1r

De-novo **GLP1R agonist** design for the Anthropic × Adaptyv 2026 Protein Design
Competition, **Challenge 3 (Track 3)**. Target: human GLP1R (UniProt **P43220**).

## The problem in one line

Design novel molecules that **bind *and activate*** human GLP1R. **Binding alone loses** —
and because the receptor is a class B GPCR, binding and activation come apart harder than
for almost any other target (see `AGENTS.md`).

## Objective priority (this IS the design priority)

1. **Activation (agonism)** — cell-surface GLP1R → Gαs → cAMP → CRE-SEAP. The win condition.
2. **Binding** to the detergent `24–432` construct — the gate that precedes the functional assay.
3. **Design + method novelty** — Track 3 rewards both (and novelty is an eligibility gate).

> **Feasibility, stated honestly:** no standalone designed protein/antibody has ever agonized a
> class B GPCR. This is a frontier/moonshot; the portfolio is a mechanism-hedged bet, and **no
> in-silico score proves agonism** — only the functional assay does.

## Startup

1. `./init.sh` — build the core env and run the verification gate (uv sync + compile + pytest + validator self-check).
2. Read `AGENTS.md` (invariants), `progress.md` (status), `configs/target.yaml` (the target + activation contract), and `docs/PLAN_GLP1R.md` (the plan).
3. Research evidence: `reports/GLP1R de novo agonist design.md` + `research_notes/`.

## Verification

```bash
./init.sh
uv run pytest -q
uv run python scripts/validate_submission.py <designs.csv> --track 3   # submission gate
```

## Layout

- `AGENTS.md` / `CLAUDE.md` — working contract + invariants (start here)
- `configs/` — `target.yaml` (target, hotspots, controls), `filters.yaml` (thresholds), `tools.yaml` (stack + licenses)
- `src/adaptyv_glp1r/` — stage skeleton + the submission contract/validator
- `scripts/` — pipeline + `validate_submission.py` (the gate) + `novelty_check.sh`
- `docs/` — `PLAN_GLP1R.md` (the 10-deliverable dossier), `METHODS.md`, `TOOLS.md`
- `reports/` + `research_notes/` — the cited research synthesis + per-topic notes
- `runs/`, `results/`, `envs/`, `weights/`, `third_party/` — local-only (gitignored)

Submission CSVs are **USER-GATED**; nothing uploads automatically.
