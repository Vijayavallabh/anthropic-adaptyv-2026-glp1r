# session handoff

## Where things stand (2026-10-14e — moonshots re-examined + orthogonal 2-folder validation; v3 unchanged)

**Pipeline F0–F9 COMPLETE. A full moonshot re-examination + an orthogonal 2-folder engagement validation this
session did NOT change the submission — v3 stands, now better-validated. The ONLY remaining action is the owner's
USER-GATED upload — never auto-upload.** Autonomous-to-deadline (deadline 2026-10-25 23:59 AoE). Owner lifted the
compute ceiling to **8 H100s + 500 GB** (2026-10-14).

- **FOUR submission candidates staged (all validate PASS, all ≤20, molecule_class=`single_chain`):**
  - **md5s (2026-10-14e, after the owner's `molecule_class` = `single_chain` correction; portal-accepted via v4):**
    v1 `1ce4e943d897832965a66b5f3bef9123`, v2 `66cefdcf92e0d2aef2322a2a1442f1ed`,
    v3 `6b846b831f58c081f55ce0f8f66aad8c`, v4 `945b30b3b7b577084d9de22e83652ce0` (v4 = the portal-checked file).
    All byte-reproducible via the updated assembler. Any `protein`-era hashes elsewhere in this file predate this change.
  - **v1** `submissions/glp1r_track3.csv` — **19 designs**, md5 `be5b7621447eeab3402f409bcec76c9d`.
    **ZERO-RISK FALLBACK** — the only fully portal-novelty-cleared set (12 EvoBind peptides + 7 ECD binders).
  - **v2** `submissions/glp1r_track3_v2.csv` — **20 designs**, md5 `924a30807086c94e993b78392e9766e8`.
    v1 + slot-20 DiffPepBuilder hedge (dpbv2_029). Portal-parsed clean (all 20 "Single chain/Passed").
  - **v3** `submissions/glp1r_track3_v3.csv` — **20 designs**, md5 `1fbbbb23ba8bbec2912aff7bf274d188`.
    **RECOMMENDED "best-20"**: 7 developability drops + win-path rebalanced to **7 EvoBind : 9 DiffPepBuilder**
    (from 12:1) + hedge trimmed to 4. Graft-free; lengths 13–76. All 9 DPB from the corrected-target (R299) run.
    Report: `reports/GLP1R submission stress test and best-20 rebuild.md`.
  - **v4** `submissions/glp1r_track3_v4.csv` — **20 designs**, md5 `25b9d439a93e5478934a5b8f8b1c0e26`.
    v3 with the weakest-Boltz-support EvoBind (`eb_accv_l18`, slot 6) swapped for **`pglad_029`** (the only de-novo
    design to pass the 2-folder Boltz+Chai engagement consensus; necessary-condition only, confounded). Diff vs v3 =
    exactly that one row; v3 still byte-reproduces. **CONTINGENT on portal novelty** (`pglad_029` = 57.1% local id to
    oxyntomodulin). Build: `scripts/assemble_portfolio.py data/candidates/portfolio_v4_order.txt submissions/ v4`.
- **Orthogonal 2-folder engagement validation (this session, M4) — DONE; v3 UNCHANGED.** Boltz-2 + Chai co-fold of
  every win-path peptide (first scoring beyond EvoBind's own AF2). **2-folder consensus: NO de novo design shows
  confirmed agonist-like engagement** — the one Boltz "agonist-like" hit (`dpbv2_030`, unselected) is scramble-like
  in Chai (a single-folder artifact, like the `scr_s3` decoy). So no better-engaging design was left out → the v3
  selection is validated, not re-cut. Evidence: `data/candidates/boltz_winpath_calibration.csv`,
  `data/candidates/chai_consensus.csv`; tools `scripts/chai_fold_adapt.py`, `scripts/chai_consensus.py`.
  Caveat: necessary-condition only; both folders memorize natural complexes → Chai is a scramble-breaking negative
  control, not a positive de-novo oracle. No agonism proof.
- **v3 cost unchanged:** the 9 new DPB are NOT portal-novelty-cleared — owner runs portal novelty at upload (binary).
  Fallback pool = `dpbv2_007/017/048` (048 has an instability flag).
- **Agonism is UNPROVABLE in-silico** — confirmed now from **4 independent directions**: literature (no de novo
  class-B agonist exists; Baker did GLP1R as antagonist), our own exhausted pocket attempts (RFd3 vestdeep lipid-wrap
  + S2 two-domain bridge 0/24 + buried hotspots), and the Boltz+Chai 2-folder engagement consensus. Win = the
  wet-lab cAMP/SEAP assay.

## Do next

1. **Owner's call at upload — four options:** **v4** (v3 + `pglad_029`, the engagement-validated shot — pick if it
   clears portal novelty) / **v3** (cleanest best-20, recommended default) / **v2** (one new design) / **v1**
   (zero-risk, fully portal-cleared). The upload click is USER-GATED — never auto-upload.
2. **Before uploading v3:** run portal novelty on the 9 DPB (`dpbv2_021/043/013/015/049/034/040/054/024`) + re-check
   the identity-margin designs **`eb_accv_l22`** (glucagon raw id) and **`dpbv2_040` = `glp1r_14`** (eligibility
   45.5% id / 0.50 cov). If any fails, substitute from `dpbv2_007/017/048` and re-run
   `scripts/assemble_portfolio.py data/candidates/portfolio_v3_order.txt submissions/` (byte-reproduces `1fbbbb23…`).
3. **New-generator long-shot RAN (owner-requested) — one live candidate: `pglad_029`.** PepFlow found nothing (0/8).
   PepGLAD surfaced **`pglad_029` (MALTSTQQLTNAKYQ, 15 aa, linear, 0 Cys, CLEAN, provenance-clean)** — the only de-novo
   design to clear the 2-folder Boltz+Chai engagement-consensus bar (Chai iptm 0.71 ≈ GLP-1's 0.69). CAVEAT:
   necessary-condition only (not agonism); most incretin-similar survivor (57.1% local id to oxyntomodulin, graft-free)
   → portal-novelty RISK + signal confound. **OWNER CALL:** optionally swap `pglad_029` into v3 for the weakest-
   orthogonal-support win-path pick (a Boltz-scramble-like EvoBind, e.g. `eb_accv_l18`), contingent on portal novelty;
   **v4 is now STAGED** (`submissions/glp1r_track3_v4.csv`, md5 `25b9d439…`, validator PASS) with that swap — upload still owner-gated + contingent on `pglad_029` portal novelty. Evidence: data/candidates/pepglad_longshot{,_consensus}.csv.

## Invariants (full list in AGENTS.md)

- **Agonism ≠ binding.** Score agonism vs **6X18 active state**; binding vs the inactive 24–432 construct; keep
  separate; demerit off-state binders. **No in-silico score proves agonism** — only the cAMP/SEAP assay does.
- De-novo / zero-shot only; no GLP-1/exendin/glucagon/semaglutide/GIP identity; **linear/disulfide, natural AAs**
  (no head-to-tail macrocycle).
- Keep AF3/Protenix-v2/ESM-3/ESMC out of submitted-design provenance (ODC-BY; DiffPepBuilder uses ESM-2 = clean;
  RFd3/RFdAA = BSD-3 clean; Chai-1 Apache-2.0). Up to 8 GPUs (owner-authorized 2026-10-14); one process/GPU; never
  clobber a foreign job.

## Compute (2026-10-14e)

Owner lifted the ceiling to **8 H100s + 500 GB**. This session only GPU **0** was free (4.7 GB dead-PID orphan,
0 % util, usable); GPUs **1–7** held foreign jobs at 93–95 % — never touched. M4 Boltz-2 (114 folds) + Chai Stage-2
(30 folds) ran on GPU 0 and released. Verify idle with `nvidia-smi` before launching; concurrent SEPIQ/TNF/AMP
sessions often hold several GPUs.

## Gated (owner OK required)

Portal upload (USER-GATED account); creating/altering the GitHub repo or changing its visibility; env/setup changes
beyond the approved init. (GPU ceiling raised to 8 on 2026-10-14 — >4 GPUs no longer gated, but still use only free ones.)
