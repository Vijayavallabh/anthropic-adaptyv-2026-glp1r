# GLP1R submission — brutal stress test + best-20 rebuild (v3)

**Date:** 2026-10-14 · **Scope:** adversarially stress-test every design in the submission and
produce the strongest possible 20, willing to reject any/all. **Outcome:** a materially improved
**v3** (`submissions/glp1r_track3_v3.csv`, md5 `3fbdb2b0d148f1012ef0e40a5aead191`, validator
rows=20 errors=0 warnings=0 PASS). **Upload remains USER-GATED; nothing uploaded.** v1 (19,
portal-cleared, md5 `be5b762…`) is preserved as the zero-risk fallback; v2 (20, `924a3080…`) also intact.

## Tiering (project invariant)
[measured] = computed this session on the same pipeline · [PR]/[pre] = literature · [HYP] = hypothesis.
**No in-silico score proves agonism** — upheld throughout. Agonism is unrankable in-silico for a class-B
GPCR (confirmed 3× prior: two-state co-fold + ENM both NO-GO), so the win-path arm is judged ONLY on
developability + eligibility + diversity + mechanistic-plausibility-as-hypothesis, never on binding.

## Method
1. **Hard quantitative layer** [measured] — `scripts/stress_liab.py` re-derived a uniform liability panel
   for all 20 designs + both replacement pools: length, Cys count/parity (free-thiol), **longest CONTIGUOUS
   single-residue run** (catches poly-Ala that max-fraction dilutes), Shannon entropy, GRAVY, aromatic %,
   net charge, pI, ProtParam instability (proline-FP aware), Met+Trp oxidation load, deamidation/isomerization
   motifs, and **longest common substring vs each incretin** (graft detector).
2. **Adversarial multi-agent prosecution** — a dynamic workflow (6 agents): 4 independent skeptics argued the
   calibrated case AGAINST every design → KEEP/WEAK/DROP; a defender steelmanned every flag (overturning several);
   a portfolio architect synthesized the best-20. Agents were given the hard evidence + the scientific invariants
   so skepticism was calibrated (not naive), and were barred from GPU/file mutation.
3. **Verification before implementing** — every architect pick was independently re-audited on the hard pipeline
   (the DPB "clean" flag was shown to under-count Met/Trp); DPB backfills were re-selected by a coverage-gated
   cousin filter + lowest-eligibility-first; the final CSV was re-validated, graft-checked, and byte-reproduced.

## What the stress test found
**Strengths confirmed** [measured]: (a) de-novo claim holds — longest common substring to ANY incretin is ≤3
for ALL 20 designs incl. the 9 new ones (no grafts; elevated local %id is dispersed, not a graft); (b) the 7
ECD binders that pass the af2ig gate were exactly the 7 submitted (no better unused binder exists).

**7 hard developability drops** (genuine defects that would compromise the wet-lab cAMP/SEAP readout):
| dropped | arm | reason [measured] |
|---|---|---|
| `eb_accv_l36` (old glp1r_03) | agonism | 4 Cys as two **vicinal** pairs (C25-C26, C32-C33) → cannot close intra-pair rings → disulfide scrambling / heterogeneous product; longest (36-mer) |
| `eb_prod_l40` (old 08) | agonism | 3 Cys incl. vicinal C6-C7 on the hardest 40-mer SPPS; pLDDT-50 fold too uncertain to trust SS |
| `eb_accv_l14` (old 09) | agonism | free thiol (odd C8) + C-terminal Met-Met + Trp (ox load cohort-worst) on the **highest eligibility surface** (80% exendin) |
| `eb_prod_l14` (old 12) | agonism | GRAVY 0.56 + contiguous W-L-W double-Trp aggregation/oxidation hotspot; weakest mechanistic proxy |
| `eb_accv_l20` (old 11) | agonism | QSIQSIS low-complexity near-tandem repeat + panel-lowest self-pLDDT 38 = degeneracy/non-specificity risk |
| `ecd_des_8_7` (old 16) | hedge | degenerate C-terminal **poly-Ala run of 7**; its "most-novel" TM 0.705 is a confound (poly-Ala folds non-globular → Foldseek can't match) |
| `ecd_des_10_6` (old 18) | hedge | literal **14-residue contiguous poly-Ala** (N-term) + target_aligned_rmsd **14.49 Å** (non-reproducible pose) + least-novel (TM 0.924) + highest ECD eligibility; worst on 4 axes simultaneously |
| `ecd_des_2_6` (old 14) | hedge | near-duplicate cousin of `ecd_des_2_4` (same des_2 backbone, Arg→Lys surface), strictly dominated → collapse the pair |

**#1 structural fix — the method monoculture:** the win-path was **12:1 EvoBind : DiffPepBuilder**. For an
unrankable win-path, method-correlated failure is the single biggest fixable risk. v3 rebalances to **7 EvoBind
: 9 DiffPepBuilder** across two orthogonal generators (EvoBind = AF2-gradient threading; DiffPepBuilder = SE(3)
diffusion + ESM-2, MIT-licensed). The 9 DPB were chosen clean + low-eligibility + cousin-free (coverage-gated),
length-diverse (12–23 aa).

## v3 composition (20)
- **16 agonism (win-path):** 7 EvoBind (portal-cleared: eb_prod_l32/l26/l20/l24, eb_accv_l22/l18/l26) +
  9 DiffPepBuilder (NEW: dpbv2_021/043/013/049, dpb_vest_020/051/036/002/032).
- **4 binding hedge:** ecd_des_20_7 (best binder pae 6.22), ecd_des_18_5 (cleanest comp, stable pose),
  ecd_des_4_3 (dispersed-Ala, unique des_4 lineage, stable pose), ecd_des_2_4 (single des_2 representative).
- **Liability profile [measured]: 13 fully clean / 5 one-flag / 2 two-flag** — vs v2's 7 / 9 / 3 / 1.
  Graft-free (lcs ≤3 all 20). 20 unique sequences + names.

## Honest risk accounting (what this is and is NOT)
- This is a **method-DIVERSITY + developability + eligibility improvement, NOT a demonstrated agonism gain.**
  Both generators floor at the same ~5 Å reachability wall; agonism remains unprovable in-silico and rests on
  mechanism plausibility + the wet-lab assay. [measured/invariant]
- **The 9 new DPB designs are NOT portal-novelty-cleared.** Portal novelty is a binary pass/fail the owner must
  run at upload (it cannot be self-verified here). v1's original designs were portal-cleared; v3 trades some of
  that cleared status for diversity. 5 of the 9 DPB come from an earlier, geometrically mis-centered target run
  — still valid de-novo peptides (target-centering is irrelevant to an unrankable win-path) but with no reader
  proxy. A fallback DPB pool (`dpb_vest_006`, `dpbv2_030`, etc.) is staged if any pick fails the portal.
- `eb_accv_l22` (rank 4) is the best mechanistic bet (robust reader-reacher, disulfide-stapled) but carries the
  arm's **highest eligibility surface (100% raw id to glucagon, cov 0.14)**; portal-cleared in v1 — re-check first.

## Decision & alternatives
- **v3 (7:9, this file)** = the recommended "strongest defensible" rebuild: does all 7 solid drops, fully breaks
  the monoculture, keeps the maximum portal-cleared EvoBind, and does not over-exhaust the shallow clean-DPB pool.
- **More aggressive (5:11)** was considered (swap EvoBind l32-kept→... + l26/l22 extra DPB): marginally more
  diversity, but 11 novelty gambles + near-exhausts the pool + leans harder on the mis-centered run. Not adopted.
- **v1 (19, portal-cleared)** = zero-risk fallback if the owner prefers to avoid any new portal checks.

## Not done (and why)
- No GPU re-folding of the win-path peptides: re-folding adds no signal (reachability floor confirmed repeatedly;
  agonism unrankable). GPU 0 was the only free GPU; the foreign jobs on 1–7 were never touched.
- Optional, not run: salvage `ecd_des_8_7`'s backbone via anti-low-complexity re-MPNN → af2ig for a 5th hedge
  binder (hedge is lower priority than the win-path; available if the owner wants it).

## Reproducibility
`scripts/stress_liab.py` (hard liability audit) + `scripts/assemble_portfolio.py` (reproducible builder) +
`data/candidates/portfolio_v3_order.txt` (the ranked roster). Rebuild: `uv run python scripts/assemble_portfolio.py
data/candidates/portfolio_v3_order.txt submissions/` → byte-identical md5 `3fbdb2b0…`. Gate:
`uv run python scripts/validate_submission.py submissions/glp1r_track3_v3.csv --track 3` → PASS.
