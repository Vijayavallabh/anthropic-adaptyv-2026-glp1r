# session handoff

## Where things stand (2026-10-14d, brutal stress test done)

**Pipeline F0–F9 COMPLETE + a brutal per-design stress test produced a stronger best-20 (v3). The ONLY remaining
action is the owner's USER-GATED upload — never auto-upload.** Autonomous-to-deadline (deadline 2026-10-25 23:59 AoE).

- **THREE submission candidates staged (all validate PASS, all ≤20, molecule_class=`protein`):**
  - **v1** `submissions/glp1r_track3.csv` — **19 designs**, md5 `be5b7621447eeab3402f409bcec76c9d`.
    **ZERO-RISK FALLBACK** — the only fully portal-novelty-cleared set (12 EvoBind peptides + 7 ECD binders).
  - **v2** `submissions/glp1r_track3_v2.csv` — **20 designs**, md5 `924a30807086c94e993b78392e9766e8`.
    v1 + slot-20 DiffPepBuilder hedge (dpbv2_029). Portal-parsed clean (all 20 "Single chain/Passed").
  - **v3** `submissions/glp1r_track3_v3.csv` — **20 designs**, md5 `1fbbbb23ba8bbec2912aff7bf274d188`.
    **RECOMMENDED "best-20"** from the stress test: 7 developability drops + win-path rebalanced to a diverse
    **7 EvoBind : 9 DiffPepBuilder** (was 12:1 monoculture) + hedge trimmed to the 4 best. 8 clean/10/2 liability
    (vs v2 7/9/3/1); graft-free; lengths 13–76. **All 9 DPB are from the corrected-target (R299) run** (post-review
    fix — the first v3 `3fbdb2b0…` wrongly used 5 mis-centered-target DPB). Report: `reports/GLP1R submission stress test and best-20 rebuild.md`.
- **v3 is a DIVERSITY + developability + eligibility gain, NOT a demonstrated agonism gain** (agonism unrankable
  in-silico; both generators floor at the reachability wall). **COST: the 9 new DiffPepBuilder designs are NOT
  portal-novelty-cleared** — the owner must run portal novelty on them at upload (binary, un-self-verifiable).
  **All 9 DPB are from the corrected-target (R299) run** (post-review fix); fallback pool = remaining vest2
  keepers (`dpbv2_007/017/048`). `eb_accv_l22` (v3 rank 4) = best mechanistic bet but 100% raw id to glucagon
  (cov 0.14; portal-cleared in v1) — re-check first.
- **Agonism is UNPROVABLE in-silico** (confirmed 5×): no activation oracle; folded de-novo proteins can't reach
  the 7TM vestibule; only threading peptides approach it; af2ig is membrane-blind. Win = the wet-lab cAMP/SEAP assay.

## Do next

1. **Owner's call at upload — three options, ranked by the stress test:**
   - **v3 (recommended)** if willing to run portal-novelty on 9 new DPB (strongest developability + method diversity).
   - **v2** if minimizing new portal checks to one (only slot-20 is new).
   - **v1 (zero-risk)** if avoiding any new portal check (all 19 already cleared).
   The upload click is USER-GATED — never auto-upload.
2. **Before uploading v3:** run portal novelty on the 9 DPB (`dpbv2_021/043/013/015/049/034/040/054/024`)
   + re-check `eb_accv_l22`. If any DPB fails, substitute from the fallback pool (`dpbv2_007/017/048`) and re-run
   `scripts/assemble_portfolio.py data/candidates/portfolio_v3_order.txt submissions/` (byte-reproduces `1fbbbb23…`).
3. **No build work pending.** Optional, only if the owner asks: re-MPNN salvage of `ecd_des_8_7`'s novel backbone for
   a 5th hedge binder (GPU); a more-aggressive 5:11 win-path split; or portfolio re-ordering.

## Invariants (full list in AGENTS.md)

- **Agonism ≠ binding.** Score agonism vs **6X18 active state**; binding vs the inactive 24–432 construct; keep
  separate; demerit off-state binders. **No in-silico score proves agonism** — only the cAMP/SEAP assay does.
- De-novo / zero-shot only; no GLP-1/exendin/glucagon/semaglutide/GIP identity; **linear/disulfide, natural AAs**
  (no head-to-tail macrocycle).
- Keep AF3/Protenix-v2/ESM-3/ESMC out of submitted-design provenance (ODC-BY; DiffPepBuilder uses ESM-2 = clean).
  Default 4 GPUs; one process/GPU; never clobber a foreign job.

## Compute (2026-10-14)

No background GPU tasks running; all GPU work released. This session's work was CPU-only (portal byte-check +
evidence-script replay). Concurrent SEPIQ/TNF/AMP sessions may hold GPUs — verify idle with `nvidia-smi` before
launching; GPU 0 has a 4.7 GB orphan from a dead PID (non-blocking, usable).

## Gated (owner OK required)

Portal upload (USER-GATED account); >4 GPUs; env/setup changes beyond the approved init; creating/altering the
GitHub repo or changing its visibility.
