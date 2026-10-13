# Agent Guide (AGENTS.md)

Design de-novo **GLP1R AGONISTS** — Anthropic × Adaptyv 2026 **Challenge 3 (Track 3)**.
Target: human GLP1R (UniProt **P43220**). This file is routing + invariants; project facts
live in `configs/target.yaml`, the plan in `docs/PLAN_GLP1R.md`, status in `progress.md`,
the cited evidence in `reports/` + `research_notes/`. Keep it short.

## The one thing that makes this challenge different

**AGONISM ≠ BINDING, and for a class B GPCR the gap is maximal.** The win condition is
**activation** (cell-surface GLP1R → Gαs → cAMP → CRE-SEAP), not binding. A surface/ECD binder
is an **antagonist** by default (proven: Baker's de-novo GLP1R binders were antagonists). Activation
requires a **"message" that reaches the 7TM vestibule and drives the TM6 kink** (His7-imidazole-charge
logic). No standalone designed protein has ever agonized a class B GPCR — this is a **frontier moonshot**;
the portfolio is a mechanism-hedged bet.

**Objective priority (this IS the design priority):**
1. **Agonism** — plausibly drives the active state / TM6 opening (highest)
2. **Binding** to the detergent `24–432` construct — the gate before the functional assay
3. **Design + method novelty** (Track 3 reward; novelty is also an eligibility gate)

## Startup workflow

1. `./init.sh` — core env + verification gate (uv sync + compile + pytest + validator self-check).
2. Read `progress.md` (status), `session-handoff.md` (next steps), `configs/target.yaml` (target + hotspots + controls), `docs/PLAN_GLP1R.md` (plan).
3. Work one feature at a time (`feature_list.json`); finish it (tests + evidence) before the next.

## Invariants (do not violate)

- **AGONISM, not binding.** Score **agonism against the WT ACTIVE state (6X18)** — never the thermostabilized
  construct (it is likely inactive-biased and will reward off-state/antagonist binders). Score **binding-assay
  passage against the WT/apo `24–432` model**. Keep the two scores **separate**; **demerit off-state-only binders**.
- **No in-silico score proves agonism.** Co-folders default to inactive and ignore the membrane; there is no
  validated activation oracle. Computation gates a *credible active-state binder* only. **Only the functional
  cAMP/SEAP assay confirms an agonist** — never claim a design "is an agonist" from computation.
- **Calibrate against controls, not absolute cutoffs.** Per-folder positives (GLP-1(7-36), exendin-4, orforglipron,
  Boc5) + scrambled negatives. Controls are **calibration only — NEVER design seeds**.
- **De-novo / zero-shot only.** Never start from or modify a known binder or a native agonist–receptor complex.
  **No significant identity to GLP-1 / exendin-4 / glucagon / semaglutide**; generated-not-grafted scaffold.
  **Linear or disulfide-cyclized only** (gene-encodable; no head-to-tail macrocycles); natural AAs only.
- **uv only** for env work; heavy tools in isolated `envs/` venvs (reuse sibling repos' venvs + the Anthropic
  `third_party/uplifting-biomolecular-modeling` kit; `--det 1` for byte-reproducible submitted artifacts). See `configs/tools.yaml`.
- **Local multi-GPU**, run CUDA directly (no SSH). One process per GPU; shard sweeps; **default 4 GPUs, burst to 8
  only in idle windows**; verify idle with `nvidia-smi`; never clobber a foreign job; cap `OMP_NUM_THREADS`.
- **License hygiene for public release.** Submitted sequences are published under **ODC-BY**. Keep
  **AF3 / Protenix-v2 / ESM-3 / ESMC-600M OUT of submitted-design provenance**; use the permissive stack.
- **Latest SOTA, researched then adopted** (availability + license verified). **Never claim a tool ran unless it ran.**
- **Devil's-advocate, then revise.** For each design argue the strongest case *against* it (does the message truly
  reach the vestibule, or does it just bind the ECD → antagonist? is it de-novo? will it open TM6?).
- **Re-validate the exact submitted artifact end to end:** submit == folded == scored.

## Verification commands

- `./init.sh`: core env + smoke tests (fast, CPU-only) — the gate.
- `uv run pytest -q`: tests (schema, length, format, uniqueness, byte-repro).
- `uv run python -m compileall -q src scripts`: compile check.
- `uv run python scripts/validate_submission.py <csv> --track 3`: **submission gate** (rows/format/length/uniqueness/ANARCI). Record md5 + `rows=N errors=0`.
- `bash scripts/novelty_check.sh <csv>`: sequence+structure novelty pre-screen (FoldSeek/MMseqs2). The **Proteinbase portal is the novelty authority** — always re-check before upload.

## Definition of done

A change is done only when its criteria are met, its tests pass, `validate_submission.py` exits `0`
for Track 3, and the command + key output are recorded as evidence. Never claim done without evidence.

## Submission contract (Challenge 3 — ≤20 designs; deadline 2026-10-25 23:59 AoE)

- CSV `name,sequence,molecule_class`, **rows best-first** (row order = ranking). Natural AAs; Fab = `VH:VL` (heavy first).
- `molecule_class` **RESOLVED (2026-10-13)**: the live GLP1R /submit portal parsed all 19 submitted designs as
  **"Single chain"** and accepted our emitted `protein` (owner's live portal paste, "0 needing fixes"). Validator
  emits `protein`. Low-risk; glance at the dropdown once more at upload.
- Names published verbatim → no PII/prompt-like text. Unique names + sequences. De-novo + zero-shot (hard gate).
- Candidate CSVs live in `runs/` (gitignored). **Upload is USER-GATED** (portal account) — never auto-upload.

## Commits

Stage only source, docs, configs, harness. Never stage `results/ runs/ envs/ third_party/ weights/ data/raw/`.
Repo-local identity **Vijayavallabh** + noreply (id 88388452). Descriptive message, **no AI attribution**; push to `origin`.

## Open questions / must re-verify before upload

- ~~`molecule_class` live value (`protein` vs `single_chain`)~~ — RESOLVED 2026-10-13 (live portal = "Single chain", accepts `protein`).
- Macrocycle / non-canonical policy (working assumption: linear/disulfide, natural-AA only).
- Whether de-novo *motif scaffolding* of a novel (non-GLP-1) message is permitted (a sibling Adaptyv comp forbade motif scaffolding) — prefer fully-generated/blind-search designs.
- Organizer-unspecified: EC50/affinity/agonism thresholds, the reference agonist, the selection-prompt weighting.
