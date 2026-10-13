# session handoff

## Where things stand (2026-10-13)

- **Research complete** (F1): strategy = **mechanism-hedged portfolio** (S1 message micro/mini-protein [primary],
  S2 two-domain mini-agonist, S3 exoframe ago-PAM moonshot, S4 ECD clamp control). Evidence in `reports/` + `research_notes/`.
- **Harness scaffolded** (F0, active): AGENTS.md / CLAUDE.md / configs / src validator / tests / init.sh written.

## Do next (in order)

1. `./init.sh` — confirm the gate PASSES (uv sync + compile + pytest + validator self-check). Fix any scaffold bug first.
2. `scripts/setup_tools.sh novelty` (to be written) — install **FoldSeek + MMseqs2** (absent; the novelty gate).
3. Create private GitHub repo **`Vijayavallabh/anthropic-adaptyv-2026-glp1r`** (name is free), set repo-local identity
   (Vijayavallabh + noreply 88388452), first commit (**no AI attribution**), push.
4. **F2 Stage 0 target prep** (CPU/light): fetch 6X18 → clean chain R to an active-state design target; WT/apo 24-432
   construct model; dump ECD-groove + 7TM-vestibule hotspot selections; assemble positive (GLP-1(7-36)/exendin-4/
   orforglipron/Boc5) + scramble control complexes; glycan/tag exclusion zones. **Report before launching any generation.**

## Invariants to not forget (full list in AGENTS.md)

- **Agonism ≠ binding.** Score agonism vs **6X18 active state**; binding vs the inactive 24-432 construct; keep separate; demerit off-state binders. No in-silico score proves agonism.
- De-novo only; no GLP-1/exendin/glucagon/semaglutide identity; **linear/disulfide, natural AAs** (no macrocycle).
- Keep AF3/Protenix-v2/ESM-3 out of submitted-design provenance (ODC-BY). Default 4 GPUs. Never claim a tool ran unless it ran.

## Gated (owner OK)

Portal upload (USER-GATED, portal account); >4 GPUs; env/setup changes beyond the approved init.
