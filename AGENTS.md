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
  **Linear or intramolecular-disulfide only** (gene-encodable; no head-to-tail macrocycles); natural AAs only.
  **Do NOT depend on a disulfide forming** — Adaptyv cell-free expression is "linear only" with redox UNCONFIRMED
  (organizer-clarified 2026-10-19); treat a disulfide as a bonus topology, never a load-bearing assumption.
- **Production reality (organizer-clarified 2026-10-19).** Adaptyv **cell-free expresses** Track-3 designs (not
  chemically synthesized): an initiator **(f)Met is added and NOT removed**, and the C-terminus carries a
  **linker–GFP11–linker–Twin-Strep tag that stays ON during the activation assay**. ⇒ the activating "message" must be
  **internal** (not a free N-terminal tip); **both termini are disposable/compromised**; **no design may depend on a
  disulfide** (redox unconfirmed). Fold the REAL construct (±Met, +tag) before trusting any reach number; reach is a
  **positive indicator, never a disqualifier**. No self wet-lab; the ranked ≤20 go to a Claude selection workflow.
- **uv only** for env work; heavy tools in isolated `envs/` venvs (reuse sibling repos' venvs + the Anthropic
  `third_party/uplifting-biomolecular-modeling` kit; `--det 1` for byte-reproducible submitted artifacts). See `configs/tools.yaml`.
- **Local multi-GPU**, run CUDA directly (no SSH). One process per GPU; shard sweeps; **up to 8 GPUs (owner-authorized 2026-10-14, +500 GB),
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
- `bash scripts/novelty_check.sh <csv>`: sequence+structure novelty pre-screen (FoldSeek/MMseqs2). The **Challenge-3 upload portal has NO novelty score** (format/parse "Single chain / Passed" only) — lock novelty up-front with these local screens; there is no portal recheck to defer to.

## Definition of done

A change is done only when its criteria are met, its tests pass, `validate_submission.py` exits `0`
for Track 3, and the command + key output are recorded as evidence. Never claim done without evidence.

## Submission contract (Challenge 3 — ≤20 designs; deadline 2026-10-25 23:59 AoE)

- CSV `name,sequence,molecule_class`, **rows best-first** (row order = ranking). Natural AAs; Fab = `VH:VL` (heavy first).
- `molecule_class` **RESOLVED (2026-10-13; re-confirmed on v2 2026-10-14)**: the live GLP1R /submit portal parsed
  all submitted designs as **"Single chain"** and accepted our emitted `protein` ("0 needing fixes" — for the 19-row
  v1 on 2026-10-13 and again for the 20-row v2 incl. slot-20 on 2026-10-14). Builders/validator now emit `single_chain` (owner directive 2026-10-14; portal accepts both values). Low-risk.
- **The upload portal has NO novelty score** — it only runs a format/parse gate returning per-row "Single chain /
  Passed". Novelty is locked up-front with the local screens (coverage-gated id, FoldSeek structural TM, graft LCS);
  there is no portal recheck. Current pick **v6b** (md5 `32819e6f`, owner-approved 2026-10-19) = **v6** with its lone staple-dependent slot
  (glp1r_13 = dpbss_010, Cys9–Cys13) swapped for the clean linear peptide `pglad_053` (`GHGKIAAYPWNYTA`, 0 Cys) —
  Adaptyv cell-free "linear only" expression likely won't form the staple (leaving 2 free thiols), per the
  Production-reality invariant. **v6** (md5 `398bfb30`, owner-adopted 2026-10-16; 2-folder Boltz+Chai
  reach-validated 2026-10-19) is the byte-frozen fallback; **v5c** (`61c2d9e4`) + **v5b** (`b10571b4`) + **v1**
  (`1ce4e943`) deeper fallbacks. No GPU work pending; the in-silico frontier is exhausted (the agonist proxy
  cannot separate agonists — firewall); the win now rides on the wet-lab cAMP/SEAP assay. A later **BoltzGen
  active-state generation arm (2026-10-19)** produced deep-vestibule inserters that passed Boltz multi-pose but
  **FAILED the 2-folder Boltz∧Chai bar GLP-1(7-36) clears (0/21)** → a Boltz-specific artifact; the proposed v7 was
  **REJECTED, v6 UNCHANGED** (see `reports/GLP1R active-state generation and construct probes 2026-10-19.md`).
- Names published verbatim → no PII/prompt-like text. Unique names + sequences. De-novo + zero-shot (hard gate).
- Candidate CSVs live in `runs/` (gitignored). **Upload is USER-GATED** (portal account) — never auto-upload.

## Commits

Stage only source, docs, configs, harness. Never stage `results/ runs/ envs/ third_party/ weights/ data/raw/`.
Repo-local identity **Vijayavallabh** + noreply (id 88388452). Descriptive message, **no AI attribution**; push to `origin`.

## Open questions / must re-verify before upload

- ~~`molecule_class` live value (`protein` vs `single_chain`)~~ — RESOLVED 2026-10-13 (live portal = "Single chain", accepts both; owner chose to emit `single_chain` 2026-10-14).
- Macrocycle / non-canonical policy (working assumption: linear/disulfide, natural-AA only).
- Whether de-novo *motif scaffolding* of a novel (non-GLP-1) message is permitted (a sibling Adaptyv comp forbade motif scaffolding) — prefer fully-generated/blind-search designs.
- Organizer-unspecified: EC50/affinity/agonism thresholds, the reference agonist, the selection-prompt weighting.
