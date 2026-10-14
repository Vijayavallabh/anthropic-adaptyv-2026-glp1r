# session handoff

## Where things stand (2026-10-14, latest commit `b633b4d`)

**Pipeline F0–F9 COMPLETE. Submission staged + validated + portal-parsed. The ONLY remaining action is the
owner's USER-GATED upload — never auto-upload.** Autonomous-to-deadline otherwise (deadline 2026-10-25 23:59 AoE).

- **F0–F9 — DONE** (see `feature_list.json` for per-feature evidence). Mechanism-hedged portfolio built, ranked,
  packaged, dossier written (`docs/SUBMISSION_DOSSIER.md`).
- **Two submission candidates staged (both validate PASS, both ≤20, molecule_class=`protein`):**
  - **v1** `submissions/glp1r_track3.csv` — **19 designs**, md5 `be5b7621447eeab3402f409bcec76c9d`. The
    portal-confirmed, zero-new-risk set (12 EvoBind agonism peptides ranks 1–12 + 7 ECD binders ranks 13–19).
  - **v2** `submissions/glp1r_track3_v2.csv` — **20 designs**, md5 `924a30807086c94e993b78392e9766e8`. v1 UNCHANGED
    + slot-20 `glp1r_20_ago` (DiffPepBuilder orthogonal agonism hedge, dpbv2_029; honest LOW confidence).
  - **Owner loaded v2 into the live portal (2026-10-14):** all 20 parsed "Single chain / Passed", "0 needing fixes";
    byte-cross-checked every row against the committed v2. **Portal novelty = BINARY pass/fail only (no score).**
    Slot-20 is the only new variable vs the earlier-cleared 19 → a clean go/no-go. Swap `LEQIIDYLLDALYR`
    (dpbv2_043, cleaner novelty) staged if its gate ever returns fail.
- **Agonism is UNPROVABLE in-silico** (the honest ceiling, not a skipped step): no activation oracle; folded de-novo
  proteins can't reach the 7TM vestibule (confirmed 5×); only flexible threading peptides approach it; af2ig is
  membrane-blind. Win = the wet-lab cAMP/SEAP assay. Every agonism claim is labeled LOW-confidence.
- **Evidence scripts hardened (2nd /code-review, commit `b633b4d`):** `harvest_diffpep.py`,
  `diffpep_vest2_eval.py`, `diffpep_vest2_fullfold_engage.py` made fail-loud + idempotent; every evidence CSV
  reproduces byte-for-byte; submission bytes untouched.

## Do next

1. **Owner's call at upload: v1 (conservative 19) or v2 (+orthogonal hedge 20).** v2 is parsed-clean and recommended
   (a free 20th slot spent on a decorrelated agonism bet). The upload click is USER-GATED — never auto-upload.
2. If the portal's novelty gate ever fails slot-20 → regenerate v2 with the swap `LEQIIDYLLDALYR` (dpbv2_043) and
   re-validate (≈1 min), then re-parse.
3. **No build work is pending.** Optional, only if the owner asks: the ECD-arm af2ig hedge (valid for soluble ECD
   binders, not the vestibule agonism arm); a slot-20 swap; or portfolio re-ordering.

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
