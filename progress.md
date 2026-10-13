# progress

**Project:** anthropic-adaptyv-2026-glp1r — de-novo human GLP1R **agonist** (Challenge 3, Track 3)
**Deadline:** 2026-10-25 23:59 AoE · **Updated:** 2026-10-13

## Status

- **F1 Research — DONE.** 8-stream research wave + cited synthesis (`reports/GLP1R de novo agonist design.md`;
  `research_notes/.../01-08`). Load-bearing claims verified first-hand (Baker class-B→antagonists-only;
  EvoBind cyclic-peptide GLP1R agonist). **Strategy chosen (user-approved): mechanism-hedged portfolio S1–S4.**
- **F0 Harness + env — ACTIVE.** Scaffold written (AGENTS/CLAUDE/feature_list/configs/src/tests/init.sh).
  Remaining: run the `init.sh` gate, install the FoldSeek/MMseqs2 novelty gate, create + push the private GitHub repo.

## Feasibility (honest)

**Frontier moonshot.** No standalone designed protein/antibody has ever agonized a class B GPCR; the only direct
GLP1R-agonist precedent is EvoBind (preprint, n=3, cyclic). **Win = activation (cAMP/SEAP), not binding.**
No in-silico score proves agonism. Value rests on Track-3 novelty + a mechanism-hedged 20-design bet.

## Next step

1. Finish **F0**: `./init.sh` gate PASS → install novelty gate → create private repo `anthropic-adaptyv-2026-glp1r` + first commit.
2. **F2 (Stage 0 target prep):** build the 6X18 active-state design target + WT/apo 24-432 construct model + hotspot
   selections + positive/negative control complexes (CPU/light; no generation GPU yet). **Report before any generation.**

## Compute

8× H100 idle, 0 jobs. Default 4 GPUs; burst to 8 only in idle windows. **No GPU design job launched yet.**

## Gated (owner OK required)

Portal upload; using >4 GPUs; any further environment/setup change beyond the approved init.

## Key facts (see configs/target.yaml)

- Target P43220; active-state ref **6X18** (clean, no thermostab mutations) — design/validate agonism here, NOT the construct.
- Construct Sino 13944-H18H-DD = 24–432, DDM/CHS, **proprietary (likely inactive-biasing) mutations** → score binding here, agonism against 6X18.
- Agonism needs a **7TM-vestibule "message"** (His7-charge logic) → TM6 kink. ECD-only binder = antagonist.
- `molecule_class` conflict (`protein` vs `single_chain`) — validator accepts both, emits `protein`, **verify at upload**.
