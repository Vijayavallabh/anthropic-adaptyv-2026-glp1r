# session handoff

## Where things stand (2026-10-15 — cross-domain extension pass → v5c; PICK = v5c)

**Pipeline F0–F9 COMPLETE. The submission has converged to v5c.** A deep cross-domain extension pass this session
(abstract math / chemistry / physics, per the standing request) rejected the two bigger levers on evidence and
produced exactly one verified, firewall-compatible improvement → **v5c**. **The ONLY remaining action is the owner's
USER-GATED upload — never auto-upload.** Autonomous-to-deadline (deadline 2026-10-25 23:59 AoE). Compute ceiling =
**8 H100s + 500 GB** (owner, 2026-10-14).

- **SEVEN submission files staged (all validate PASS, all ≤20, all `molecule_class=single_chain`):**
  - **PICK = v5c** `submissions/glp1r_track3_v5c.csv` — **20 designs**, md5 `61c2d9e4d806b799a278efe7efb31063`.
    = v5b with ONE swap (slot 13 `pglad_053` → `dpbss_010`, a fresh clean DiffPepBuilder disulfide-stapled
    R299-aimer: `RNAAYYAYCEIDCIDQLLLAAYF`, Cys9-Cys13 internal, minD_R299 4.76 Å, id42.9/cov0.30, lcs3, dev CLEAN).
    Raises win-path constrained-topology count 2→3; max generator share 35% (unchanged). Validator PASS; stress
    17 clean/3 soft/0 FATAL; v5b rebuilds byte-identical (assembler edit backward-safe); diff vs v5b = slot 13 only;
    ESMFold+FoldSeek on dpbss_010 = 0 PDB hits. Build: `scripts/assemble_portfolio.py data/candidates/portfolio_v5c_order.txt submissions/ v5c`.
    **Portal-parsed 20/20 "Single chain / Passed" (byte-verified against the committed file).**
  - **v5b** `glp1r_track3_v5b.csv` — 20, md5 `b10571b4…`. **Byte-frozen FALLBACK.** = v5 with the pglad_029→pglad_034
    novelty swap. Portal-parsed 20/20.
  - **v5** `glp1r_track3_v5.csv` — 20, md5 `4c87e1bd…`. Brutal-gauntlet best-20 (13-agent adversarial rebuild).
    Portal-parsed 20/20. Report: `reports/GLP1R v5 brutal stress test and best20 rebuild.md`.
  - **v4** `…_v4.csv` (945b30b3), **v3** `…_v3.csv` (6b846b83), **v2** `…_v2.csv` (66cefdcf) — superseded.
  - **v1** `glp1r_track3.csv` — 19, md5 `1ce4e943…`. **ZERO-RISK FALLBACK** (12 EvoBind + 7 ECD).
- **This session's extension pass (report `reports/GLP1R agonist portfolio and topology.md`, notes in
  `research_notes/GLP1R agonist portfolio and topology/`):** 3 agents (portfolio-probability math / topology-preorg
  chemistry / reachability re-challenge) converged → the only regime-robust, firewall-compatible lever is raising the
  win-path's constrained-topology / lineage-cell count. REJECTED on evidence: **PepFlow 5th-method cell** (all `pepx_*`
  are low-complexity outliers vs the v5b band), **deep-pocket insertion** (reachability wall holds), and
  **non-orthosteric/ago-PAM/exoframe** peptide mechanisms (sites intracellular/membrane → CLOSED). Portfolio math
  says **do NOT churn the 4/6/7/3 mix** (<0.03, sign-uncertain). Executed: fresh DiffPepBuilder disulfide-staple
  generation (idle GPUs, zero cost) → 16 clean-gated graft-free R299-aimers (pool `data/candidates/diffpep_ss_vest2.csv`,
  `dpbss_*`) → one swapped into v5c.
- **Agonism is UNPROVABLE/UNRANKABLE in-silico** (class-B GLP1R) — v5→v5c improvements are RANKABLE-PRIOR + coverage
  only, NOT agonism gains. Win = the wet-lab cAMP/CRE-SEAP assay, the ONLY verdict.

## Do next

1. **Owner's call at upload — PICK = `v5c` (recommended); `v5b` is the byte-frozen fallback; `v1` the zero-risk set.**
   The upload click is **USER-GATED** — never auto-upload. v5c and v5b both parse 20/20 at the portal.
2. **No further build/verification is pending.** v5c is fully verified (validator PASS, 17/3/0, byte-regression-safe,
   portal-parsed, 0 PDB hits). The in-silico levers are exhausted; remaining gains are **wet-lab only**.
3. If a future reason to change the roster arises: `assemble_portfolio.py` now resolves `dpbss_*` (disulfide pool) +
   `dpbv2_*`/`pglad_*`/`eb_*`/`ecd_*`; rebuild from an order file under `data/candidates/portfolio_*_order.txt`
   (byte-reproducible; v5b/v5c/… all rebuild identically).

## Invariants (full list in AGENTS.md)

- **Agonism ≠ binding.** Score agonism vs **6X18 active state**; binding vs the inactive 24–432 construct; keep
  separate; demerit off-state binders. **No in-silico score proves agonism** — only the cAMP/CRE-SEAP assay does.
- De-novo / zero-shot only; no GLP-1/exendin/glucagon/semaglutide/GIP identity (≤3 aa contiguous overlap);
  **linear/disulfide, natural AAs** (no head-to-tail macrocycle).
- **The Challenge-3 upload portal has NO novelty score** (format/parse "Single chain / Passed" only) — lock novelty
  up-front with the local sequence+structure screens, never a portal recheck.
- Keep AF3/Protenix-v2/ESM-3/ESMC out of submitted-design provenance (ODC-BY; DiffPepBuilder uses ESM-2 = clean;
  RFd3/RFdAA = BSD-3; Chai-1 Apache-2.0). Up to 8 GPUs (owner 2026-10-14); one process/GPU; never clobber a foreign job.

## Compute (2026-10-15)

Ceiling = **8 H100s + 500 GB**. This session: DiffPepBuilder disulfide-staple generation on GPU 0 + an ESMFold fold
on GPU 1, both released; a transient foreign ~1 GB job appeared on GPU 0 mid-pass (avoided). Verify idle with
`nvidia-smi` before launching; concurrent SEPIQ/TNF/AMP sessions often hold several GPUs; one process/GPU; never
clobber a running job. NOTE: `run_diffpep.sh` picks the GPU via `GPUtil` (physical ordinals) — pass the full visible
set (e.g. `"0,1,2,3,4,5,6,7"`) as its GPU arg so the `CUDA_VISIBLE_DEVICES` map is identity (a single masked index
can trigger `CUDA error: invalid device ordinal`).

## Gated (owner OK required)

Portal upload (USER-GATED account); creating/altering the GitHub repo or changing its visibility; env/setup changes
beyond the approved init. (GPU ceiling raised to 8 on 2026-10-14 — >4 GPUs no longer gated, but still use only free ones.)
Regular commits/pushes to the existing private repo are the normal checkpoint workflow (NOT gated).
