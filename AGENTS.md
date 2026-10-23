# Agent Guide (AGENTS.md)

Design de-novo **GLP1R AGONISTS** — Anthropic × Adaptyv 2026 **Challenge 3 (Track 3)**.
Target: human GLP1R (UniProt **P43220**). This file is routing + invariants; project facts
live in `configs/target.yaml`, the plan in `docs/PLAN_GLP1R.md`, status in `progress.md`,
the cited evidence in `reports/` + `research_notes/`. Keep it short.

## The one thing that makes this challenge different

**AGONISM ≠ BINDING, and for a class B GPCR the gap is maximal.** The win condition is
**activation** (cell-surface GLP1R → Gαs → cAMP → CRE reporter; **INDIGO luciferase** as of Oct 22, was SEAP), not binding. A surface/ECD binder
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
  cAMP/CRE-reporter assay (INDIGO luciferase; was SEAP) confirms an agonist** — never claim a design "is an agonist" from computation.
- **Calibrate against controls, not absolute cutoffs.** Per-folder positives (GLP-1(7-36), exendin-4, orforglipron,
  Boc5) + scrambled negatives. Controls are **calibration only — NEVER design seeds**.
- **De-novo / zero-shot only.** Never start from or modify a known binder or a native agonist–receptor complex.
  **No significant identity to GLP-1 / exendin-4 / glucagon / semaglutide**; generated-not-grafted scaffold.
  **Linear-backbone only** (gene-encodable; no head-to-tail macrocycles); **20 standard AAs only** (no NCAAs); 10–250/chain.
  **PAIRED intramolecular disulfides ARE ELIGIBLE** (CORRECTED 2026-10-23, supersedes the 2026-10-19 "no disulfide
  dependence"): expression is **oxidizing** and paired Cys are explicitly acceptable (organizer Q&A Oct 22, consolidated
  in `docs/ORGANIZER_QA_2026-10-23.md`); **avoid UNPAIRED Cys**. A disulfide-stapled peptide IS "linear" (the "only linear"
  answer bans head-to-tail macrocycles, not side-chain staples). Caveat: §7 is a synthesis, not a verbatim quote — owner to
  confirm the paired-disulfide allowance in Slack before any staple design enters the submitted set.
- **Production reality (organizer-clarified 2026-10-19).** Adaptyv **cell-free expresses** Track-3 designs (not
  chemically synthesized): an initiator **(f)Met is added and NOT removed**, and the C-terminus carries a
  **linker–GFP11–linker–Twin-Strep tag that stays ON during the activation assay**. ⇒ the activating "message" must be
  **internal** (not a free N-terminal tip); **both termini are disposable/compromised**; **paired disulfides are now
  permitted** (oxidizing expression confirmed Oct 22 — supersedes the earlier "redox unconfirmed"; avoid unpaired Cys).
  Fold the REAL construct (±Met, +tag) before trusting any reach number; reach is a
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
  there is no portal recheck. **FINAL as of 2026-10-20 (superseded 2026-10-23 → v10; see the 2026-10-23 line at the end of this section) = `submissions/glp1r_track3_v9.csv`** (md5 `419c57ff`, PASS
  20/0/0; 2026-10-20 loaded into the portal + parsed clean [20 incl / 0 fixes / all "Single chain·Passed"], byte-verified
  portal==committed v9): the v6b composition with three owner-approved swaps (v7: glp1r_15 → rm_0079; v8: glp1r_22 → bg_0746;
  v9: glp1r_03 → bg_1170), seating the two wave-2 re-mined robust 2-folder R299 reachers from a new BoltzGen lineage
  (`glp1r_24_ago`/bg_0746 at rank 5, `glp1r_25_ago`/bg_1170 at rank 6 — two independent architectures) in a
  **cap-aware, ipSAE-informed row order** — the published selection prompt
  (`…/anthropic-adaptyv-2026/selection`) takes ≤10 designs/submission from the top of the row order, so the top 10
  front-loads all four 2-folder R299 reachers + all four agonism lineages (rank-1 = `glp1r_10`; binders 18–20 hedge),
  ordered by measured necessary conditions (R299 reach, then best-pose ipSAE) + diversity, **never agonism**
  ([[adaptyv-glp1r-selection-rubric]]; `data/candidates/v6b_necessary_conditions_2026-10-20.csv`).
  `v6b_ranked` (`1571a3d4`, prize-tier) is a fallback. The underlying v6b composition (md5 `32819e6f`,
  owner-approved 2026-10-19) = **v6** with its lone staple-dependent slot
  (glp1r_13 = dpbss_010, Cys9–Cys13) swapped for the clean linear peptide `pglad_053` (`GHGKIAAYPWNYTA`, 0 Cys) —
  Adaptyv cell-free "linear only" expression likely won't form the staple (leaving 2 free thiols), per the
  Production-reality invariant. **v6** (md5 `398bfb30`, owner-adopted 2026-10-16; 2-folder Boltz+Chai
  reach-validated 2026-10-19) is the byte-frozen fallback; **v5c** (`61c2d9e4`) + **v5b** (`b10571b4`) + **v1**
  (`1ce4e943`) deeper fallbacks. No GPU work pending; the in-silico frontier is exhausted (the agonist proxy
  cannot separate agonists — firewall); the win now rides on the wet-lab cAMP/SEAP assay. A later **BoltzGen
  active-state generation arm (2026-10-19)** produced deep-vestibule inserters that passed Boltz multi-pose but
  **FAILED the 2-folder Boltz∧Chai bar GLP-1(7-36) clears (0/21)** → a Boltz-specific artifact; the proposed v7 was
  **REJECTED, v6 UNCHANGED** (see `reports/GLP1R active-state generation and construct probes 2026-10-19.md`).
  Two further orthogonal-generator moonshots then also returned NEGATIVE → **HOLD v9, no v10**: **BindCraft2 v1.0.4**
  (AF2-based; wave-3, ~5,000 traj, 0 clear the bar) and **RFD4-Proteina** (BSD-3 flow-matching all-atom; wave-4, 2,520
  designs). A length-matched same-pipeline bake-off (2026-10-23) proved the 2-folder reach bar is **cheaply clearable by
  many generators AND agonism-blind** (the antagonist exendin(9-39) passes it; iPAE is length-biased) — so no in-silico
  result is an agonism-relevant reason to change v9. De-novo frontier exhausted across 7 generators; wet cAMP/SEAP is the
  only verdict. Detail: `progress.md` + `session-handoff.md` (2026-10-22/23) + [[lesson-cofold-reach-bar-cheaply-clearable-agonism-blind]].
- **2026-10-23 (ambition-lift moonshot → FINAL is now v10).** A 4-angle frontier sweep re-confirmed the firewall (no
  wet-validated class-B agonism ranker exists; the only demonstrated de-novo class-B agonists are **cyclic / noncanonical /
  disulfide-constrained** peptides — topologies this challenge forbids), and a deep-reader (Q234/V237 TM3, V237F −257×)
  discriminator was **refuted by its own matched controls** (the inactive metabolite GLP-1(9-36) passes it as strongly as
  agonists → reach ≠ efficacy). The organizers then **definitively confirmed the design space — linear peptides / 20 standard
  AAs only / 10–250 per chain, no cyclic macrocycle** (the "no load-bearing disulfide staple" I *inferred* here was
  **corrected 2026-10-23(b), next bullet** — paired disulfides ARE eligible) — and `molecule_class=single_chain` (NOT
  `protein`; a WebFetch paraphrase had misread it; see [[lesson-unverified-constraint-fenced-design-space]]). A compliance
  audit found 19/20 v9 designs clean; the lone flag was `glp1r_04` (the only 2-Cys / disulfide-capable design). A fold proved
  its 2 Cys are **not** load-bearing (its C9S/C29S mutant reaches R299 identically), so it was de-Cys'd at zero behavioural
  cost → **FINAL = `submissions/glp1r_track3_v10.csv` (md5 `6769ef67`, PASS 20/0/0, `single_chain`)**, = v9 with that one
  change (row order + 19 other sequences byte-identical). **v9 (`419c57ff`) = immediate byte-frozen fallback.** Rationale
  `docs/SUBMISSION_RATIONALE_v10.md`; evidence `runs/finalize/`. Firewall intact (compliance hardening, never agonism).
- **2026-10-23 (b) — organizer Q&A consolidation REOPENED the disulfide route; v10 UNCHANGED.** Owner-pasted consolidated
  Slack Q&A (`docs/ORGANIZER_QA_2026-10-23.md`): §7 — expression **oxidizing**, **paired disulfides ACCEPTABLE**, avoid
  unpaired Cys; "only linear" = no head-to-tail macrocycle (a staple is linear-backbone). Also: ranking = affinity displayed
  for all binders + **agonist special label** (binding is itself a ranked axis); activation assay **SEAP→INDIGO CRE/luciferase**;
  our construct already carries L260. **Re-evaluating the 16 firewall-clean dpbss disulfide-staple designs** on the real
  2-folder construct bar + GLP-1(7-36)/exendin(9-39) controls (`runs/rfd4/dpbss_confirm`) — binding evidence only; the agonism
  edge (pre-organization = the only *demonstrated* de-novo class-B agonist route) is a labeled PRIOR, never a rank. **Any swap
  into the 20 = owner-gated composition change**; owner to confirm the paired-disulfide allowance in Slack (§7 is a synthesis).
  v10 is valid under both readings → no forced change. [[adaptyv-glp1r-production-constraints]]
- Names published verbatim → no PII/prompt-like text. Unique names + sequences. De-novo + zero-shot (hard gate).
- Candidate CSVs live in `runs/` (gitignored). **Upload is USER-GATED** (portal account) — never auto-upload.

## Commits

Stage only source, docs, configs, harness. Never stage `results/ runs/ envs/ third_party/ weights/ data/raw/`.
Repo-local identity **Vijayavallabh** + noreply (id 88388452). Descriptive message, **no AI attribution**; push to `origin`.

## Open questions / must re-verify before upload

- ~~`molecule_class` live value (`protein` vs `single_chain`)~~ — RESOLVED 2026-10-13 (live portal = "Single chain", accepts both; owner chose to emit `single_chain` 2026-10-14).
- ~~Macrocycle / non-canonical policy~~ — RESOLVED 2026-10-23: **linear-backbone + PAIRED disulfides eligible**, 20 standard
  AAs only, 10–250/chain; no head-to-tail macrocycle, no NCAAs, avoid unpaired Cys (`docs/ORGANIZER_QA_2026-10-23.md`; owner to Slack-confirm the disulfide allowance before deploying staples).
- Whether de-novo *motif scaffolding* of a novel (non-GLP-1) message is permitted (a sibling Adaptyv comp forbade motif scaffolding) — prefer fully-generated/blind-search designs.
- Organizer-unspecified: EC50/affinity/agonism thresholds, the reference agonist, the selection-prompt weighting.
