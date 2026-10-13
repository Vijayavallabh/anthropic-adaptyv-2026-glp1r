# session handoff

## Where things stand (2026-10-13)

- **F0 harness + repo — DONE.** `init.sh` gate passes; private repo `Vijayavallabh/anthropic-adaptyv-2026-glp1r`
  pushed (commit `91ded84`); FoldSeek/MMseqs2 installed in `tools/`.
- **F1 research — DONE.** Strategy = **mechanism-hedged portfolio** (S1 message micro/mini-protein [primary],
  S2 two-domain, S3 exoframe ago-PAM, S4 ECD-clamp control). Evidence: `reports/` + `research_notes/`.
- **F2 Stage 0 target prep — DONE.** `data/target/manifest.json` (checksums); 6X18 active-state target + GLP-1(7–36)
  geometry; WT 24-432 construct model; hotspots; positive controls. CPU/light.

## Do next

1. **F3 generation is USER-GATED** — the owner asked to report before any generation. Propose the generation plan
   (per-strategy tools/counts, GPU shards on ≤4, provenance, eligibility pre-screen) and await go-ahead; then launch.
2. On go-ahead: S1 (EvoBind-linear + RFdiffusion/RFpeptides active-state message designs, vestibule-hotspot-targeted) +
   S2 (two-domain) + S3 (exoframe) + S4 (≤1–2 clamp controls) → ProteinMPNN/LigandMPNN (F4) → binding fold/score (F5)
   → agonism-hypothesis gate (F6) → novelty+liabilities (F7) → rank & pick ≤20 (F8) → submission package (F9, user-gated).

## Invariants (full list in AGENTS.md)

- **Agonism ≠ binding.** Score agonism vs **6X18 active state**; binding vs the inactive 24-432 construct; keep separate;
  demerit off-state binders. **No in-silico score proves agonism.**
- De-novo only; no GLP-1/exendin/glucagon/semaglutide identity; **linear/disulfide, natural AAs** (no macrocycle).
- Keep AF3/Protenix-v2/ESM-3 out of submitted-design provenance (ODC-BY). Default 4 GPUs; one process/GPU.
- Confirm EvoBind install + a linear mode before relying on it (flagged in `configs/tools.yaml`).

## Gated (owner OK)

Generation launch (F3); >4 GPUs; portal upload (USER-GATED account); env/setup beyond the approved init.
