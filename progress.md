# progress

**Project:** anthropic-adaptyv-2026-glp1r — de-novo human GLP1R **agonist** (Challenge 3, Track 3)
**Deadline:** 2026-10-25 23:59 AoE · **Updated:** 2026-10-13

## Status

- **F1 Research — DONE.** 8-stream wave + cited synthesis (`reports/`, `research_notes/`); load-bearing claims
  verified first-hand. Strategy (user-approved): **mechanism-hedged portfolio S1–S4**.
- **F0 Harness + env — DONE.** `init.sh` gate PASSES (uv sync + compile + 12 tests + validator). FoldSeek/MMseqs2
  installed. Private repo pushed: `Vijayavallabh/anthropic-adaptyv-2026-glp1r` (commit `91ded84`).
- **F2 Stage 0 target prep — DONE.** 6X18 active-state target (chain R; gaps 130–135 + 339–343 confirmed) + GLP-1(7–36)
  message geometry (chain P) extracted; WT `24–432` construct model (409 aa); hotspots + positive controls + checksummed
  `data/target/manifest.json`. CPU/light; **no GPU used.**

## Feasibility (honest)

**Frontier moonshot.** No standalone designed protein has agonized a class B GPCR; only direct GLP1R-agonist precedent
is EvoBind (preprint, n=3, cyclic). **Win = activation (cAMP/SEAP), not binding.** No in-silico score proves agonism.

## Next step — F3 generation (USER-GATED)

**Owner asked to report before any generation — holding here.** F3 is the first GPU step: generate de-novo, active-state-
conditioned, 7TM-vestibule-targeted designs per S1–S4 (EvoBind-linear / RFdiffusion / RFpeptides / Baker-style mini-protein
+ ProteinMPNN), heavily filtered. Will propose the concrete generation plan (tools, GPU shards, counts, provenance) and
await go-ahead.

## Compute

8× H100 idle, 0 jobs. Default 4 GPUs; burst to 8 only in idle windows. **No GPU design job launched yet.**

## Gated (owner OK required)

Launching generation (F3); using >4 GPUs; portal upload; env/setup changes beyond the approved init.
