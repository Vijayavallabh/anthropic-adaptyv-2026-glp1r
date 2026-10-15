# GLP1R Track-3 — brutal stress test → best-20 rebuild (v5)

**Date:** 2026-10-15 · **Method:** 13-agent adversarial gauntlet (Workflow `wf_3f071638-e29`):
6 prosecutors (compliance/de-novo, portal-novelty, developability, engagement-confound, redundancy-diversity,
portfolio-logic) → 3 defenders → 3 architects (best-20 rebuilds) → 1 judge. Mandate: *stress-test every
design and produce the best-defensible 20 even if it means rejecting all current picks.*

**Result:** ship a **new v5** (`submissions/glp1r_track3_v5.csv`, md5 `4c87e1bd973c11b68a4a2b2fdb41114e`,
20 designs). Drops 11 of v4's designs; keeps 9; adds 11. **Do NOT ship v4 or v3.**

## Firewall (unchanged, upheld)
Agonism is **unprovable and unrankable in-silico** for class-B GLP1R; the wet-lab cAMP/SEAP assay is the
only verdict. No co-fold / iPAE / ipTM / engagement label proves or ranks activation. The win-path is
therefore judged only on the **rankable** axes — compliance, portal-novelty, developability, de-novo/graft
cleanliness, generative-prior quality (correct-aim + method), portfolio diversity — plus the wet-lab lottery
of **independent, clean, diverse shots**. v5 is built to never lose on a rankable axis and to buy the most
diverse clean tickets; it does **not** and **cannot** claim an agonist.

## What the gauntlet found in v4 (the own-goals cut in v5)
1. **Hard developability own-goal** — `eb_prod_l20` (v4 slot 08) carries a lone free thiol (odd Cys) →
   air-oxidized dimers/mixed adducts that convolve a dose-response readout. A clean 0-Cys EvoBind
   replacement (`eb_accv_l18`) sits unused in the same lineage.
2. **Three portal-novelty own-goals** — `dpbv2_015` / `dpbv2_034` / `dpbv2_040` are the **only 3** designs
   in v4 that trip the repo's own `elig_flag` (coverage 0.59/0.54/0.50 → liraglutide/glucagon/GLP1_7_37),
   all **pool `keep==FALSE`**, all with clean sub-0.5 `keep==True` replacements unused.
3. **Heavy-dev picks** — `eb_accv_l22` (instab56 + N-term-Gln pyroGlu + raw-100%-id-glucagon optics),
   `eb_prod_l24` (GRAVY 0.69 + 2M1W oxidation), `dpbv2_054` (instab75 + strained i,i+4 disulfide),
   `dpbv2_024` (most generic DPB mode + instab).
4. **Method monoculture** — v4 win-path was 9/16 (56%) DiffPepBuilder (correlated-failure risk).
5. **Homogeneous over-allocated hedge** — v4 kept the worst ECD binder (`ecd_des_18_5`, af2ig pae 9.55 +
   instab) and a structural monoculture (TM 0.873–0.910).
6. **`pglad_029`'s "2-folder AGREE" is a probable confound, not evidence** — the engagement gate is
   demonstrably miscalibrated (a real agonist, exendin_4, is a false-negative SPLIT; a composition-exact
   GLP-1 scramble scores "agonist-like"). `pglad_029` is kept (sole 2-folder pass, cleanest dev, cov0.47
   sub-threshold) but its AGREE is demoted to a **documented hypothesis, never a ranker**.
7. **`ranked.csv` is a loaded gun** — it orders the agonism arm by `binding_norm`, which would resurrect the
   free-thiol and vicinal-CC landmines; the win-path must never be ordered by a binding number.

## v5 roster (17 win : 3 hedge; max generator share 35%)
| # | name | internal | source | len | cov/id | note |
|---|------|----------|--------|-----|--------|------|
| 01 | glp1r_01_ago | eb_prod_l26 | EvoBind | 26 | 0.31/50 | clean, independent anchor |
| 02 | glp1r_02_ago | eb_accv_l18 | EvoBind | 18 | 0.39/57 | cleanest EvoBind (instab9.8, 0Cys); replaces free thiol |
| 03 | glp1r_03_ago | eb_accv_l26 | EvoBind | 26 | 0.31/62 | soluble (GRAVY-0.75); soft instab52 only |
| 04 | glp1r_04_ago | eb_prod_l32 | EvoBind | 32 | 0.34/36 | best-novelty long EvoBind; single non-vicinal SS (C9/C29) |
| 05 | glp1r_05_ago | dpbv2_030 | DiffPepBuilder | 14 | 0.21/67* | best-novelty DiffPep; aims R299 (minD 5.1Å) |
| 06 | glp1r_06_ago | dpbv2_013 | DiffPepBuilder | 15 | 0.33/60 | distinct R299-reaching mode (4.73Å) |
| 07 | glp1r_07_ago | dpbv2_043 | DiffPepBuilder | 14 | 0.36/40 | distinct mode (5.36Å) |
| 08 | glp1r_08_ago | dpbv2_049 | DiffPepBuilder | 15 | 0.40/50 | reaches R299 (5.62Å) |
| 09 | glp1r_09_ago | dpbv2_029 | DiffPepBuilder | 13 | 0.46/50 | clean keep=True family rep (replaces keep=FALSE dpbv2_034) |
| 10 | glp1r_10_ago | dpbv2_021 | DiffPepBuilder | 23 | 0.65/20 | **lowest id (20%) in file**; elig_flag=FALSE |
| 11 | glp1r_11_ago | pglad_029 | PepGLAD | 15 | 0.47/57 | sole 2-folder AGREE (hypothesis only); cleanest dev; **novelty-recheck item** |
| 12 | glp1r_12_ago | pglad_046 | PepGLAD | 23 | 0.17/50 | **best portal-novelty in any pool** |
| 13 | glp1r_13_ago | pglad_053 | PepGLAD | 14 | 0.21/67* | 2nd-best novelty |
| 14 | glp1r_14_ago | pglad_010 | PepGLAD | 21 | 0.24/60* | clean, stable |
| 15 | glp1r_15_ago | pglad_048 | PepGLAD | 25 | 0.28/43 | clean disulfide-macrocycle (C1/C24); longest PepGLAD |
| 16 | glp1r_16_ago | pglad_026 | PepGLAD | 21 | 0.29/50 | distinct mode |
| 17 | glp1r_17_ago | pglad_001 | PepGLAD | 22 | 0.36/38 | lowest-id PepGLAD; most stable (instab-12.7) |
| 18 | glp1r_18_bind | ecd_des_20_7 | ECD (RFdiff+LigandMPNN+af2ig) | 70 | 0.11/62 | best validated binder (pae 6.22); hedge anchor |
| 19 | glp1r_19_bind | ecd_des_2_6 | ECD | 74 | 0.18/38 | clean best-novelty ECD (pae 8.21) |
| 20 | glp1r_20_bind | ecd_des_8_7 | ECD | 66 | 0.24/38 | only structurally-novel ECD (TM 0.705); accepts 1 soft lowcplx(A39%) flag |

\*raw best-local %id at low coverage = short-window display artifact (lcs≤3, no graft), not a graft.

**Generators:** EvoBind 4 / DiffPepBuilder 6 / PepGLAD 7 / ECD 3 (max 35%, vs v4's 56% DPB).
**Aim honesty:** DiffPep peptides aim at R299 and reach ~5Å (the de-novo reachability wall;
`reaches_R299=False` at the contact cutoff). PepGLAD peptides sit ~26–33Å from R299 → included on
**novelty + clean dev + lineage diversity only**, not on verified aim.

## v5 verification (by bytes)
- validator `--track 3`: **PASS, exit 0**, 0 errors / 0 warnings, ANARCI yes.
- stress-liability panel: **17 clean / 3 one-flag / 0 two-flag / 0 FATAL** (v4 was 8/10/2). The 3 flags are
  2 soft ProtParam instability over-flags (0-Cys solubles) + 1 accepted ECD poly-A(×7).
- 20 unique names, 20 unique sequences, all `single_chain`, all natural AA, len 13–74.
- **submit==source bytes: ALL MATCH** (every row equals its pool-CSV bytes; zero hand-transcription).
- **max contiguous incretin overlap = 3 aa** across all 20 vs 9 known agonists → no graft.
- 0 designs trip `elig_flag`; mean coverage 0.316; only 1 design ≥0.5 (dpbv2_021 at 0.65/id20).
- Cross-validation: 2 independent architect rebuilds overlapped this roster **18/20 and 19/20**.

## GPU experiment verdict
**AGREE-hunt (more PepGLAD + Boltz/Chai to find 2-folder passes): do NOT run — low value.** The signal is
firewall-barred from ranking any pick; the gate is miscalibrated (real agonist fails it); base rate ~1/57;
all PepGLAD sit ~29Å from R299; and ~24 clean low-cov PepGLAD already sit unused (not pool-limited).

**Better idle-GPU use (DONE, GPU 0):** single-seq folded all 20 (ESMFold monomer) + FoldSeek TM-vs-PDB
against the existing `runs/novelty/pdb_db` (same pipeline that scored the ECDs). Summary:
`data/candidates/v5_struct_novelty.csv`.
- **Pipeline validated** — the 3 ECD positive controls reproduce their known TMs (0.92/0.91/0.70).
- **7 of the 17 peptides fold confidently** (pLDDT 72–88; contrary to the "short de-novo peptides fold to
  garbage" prior) — glp1r_16/07/11/06/09/05/08.
- **All 17 peptides return ZERO PDB structural hits** (no match above FoldSeek's detection floor), confident
  folds included. Combined with verified sequence-novelty (no graft, all eligible) → the peptide arm passes
  structural novelty. (For the 13–20 mers "no hit" is partly the short-query detection floor, but the portal
  weights sequence-id there, which is passed; for the confident 21–22 mers it is a genuine no-match signal.)
- **Conclusion: no roster change.** The one unmeasured rankable sub-axis is now measured and clean.

## Residual pre-upload items (upload is USER-GATED)
0. **The Challenge-3 portal has NO novelty score (owner, 2026-10-15)** — it only runs a format/parse gate
   ("Single chain / Passed"). There is no portal recheck to catch an incretin-similar design at upload, so
   novelty is locked up-front with the local screens, not deferred. v5 parsed 20/20 Passed at the portal.
1. ~~Portal-novelty recheck `pglad_029`~~ → **RESOLVED in v5b.** With no portal backstop and its only rationale
   (the firewall-barred AGREE confound) carrying ~0 evidence, the highest-id design `pglad_029`
   (glp1r_11_ago, cov0.47/id57 oxyntomodulin) was swapped for the len-matched clean `pglad_034` (id33.3/cov0.40
   glucagon, lcs2). **v5b** (`submissions/glp1r_track3_v5b.csv`, md5 `b10571b40613d32ad36cbc9859890df7`,
   validator PASS, 17 clean/3 soft/0 FATAL, no graft) is v5 with that one swap = the recommended pick; v5 stays
   as the portal-parsed file.
2. `dpbv2_021` cov0.65 (highest) but id20 (lowest → passes Adaptyv ≤30% id). Naive-raw-coverage fallback:
   `pglad_034` (cov0.40) or `dpbv2_047` (cov0.33, instab>40).
3. ~~Structural-TM blind spot for the 17 peptides~~ → **CLOSED** (0/17 match any PDB fold; see above).
4. `ecd_des_8_7` carries the one accepted soft lowcplx(A39%) flag; clean fallback `ecd_des_2_4` (pae7.82,
   TM0.910).
5. Disulfide picks `eb_prod_l32` (C9/C29) + `pglad_048` (C1/C24): one formable non-vicinal pairing each —
   specify at synthesis.
6. Clean bench alternates (correct-aim DiffPep, unused): `dpbv2_023`, `dpbv2_025` (both cov0.46, 0-Cys, ~5Å).

## Honest ceiling
v5 is the best **defensible** 20 — zero own-goals, maximal clean diverse shots across 4 generators, a
validated-binding hedge — **not** a portfolio that can claim an agonist. Every mechanism statement here is a
hypothesis; the cAMP/SEAP assay is the only verdict.
