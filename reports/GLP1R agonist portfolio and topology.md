# GLP1R Track-3 — cross-domain extension: portfolio math, topology, assumption re-challenge → v5c

**Date:** 2026-10-15 · **Method:** 3-agent extension analysis (portfolio-probability math + topology/
pre-organization chemistry + reachability-wall re-challenge), each fed the firewall + current roster +
the prior reports, then the one surviving lever was **built and verified** on idle GPUs.

## Decision (BLUF)
A deep cross-domain pass (abstract math / chemistry / physics, per the standing request) over the already
3×-researched problem found **exactly one** firewall-compatible, verified improvement, and it is **marginal
and on rankable priors only** — not an agonism gain (none is possible in-silico; see Firewall). Ship a new
**v5c** (`submissions/glp1r_track3_v5c.csv`, md5 `61c2d9e4d806b799a278efe7efb31063`): v5b with **one swap**
(slot 13 `pglad_053` → `dpbss_010`, a fresh, clean, model-validated disulfide-stapled R299-aimer), raising
the win-path's **constrained-topology count 2 → 3** and trading a no-verified-aim PepGLAD hedge for an
aimed (4.76 Å), disulfide-constrained design. **v5b is retained byte-frozen as the fallback.** Two *larger*
levers were examined and **rejected on evidence**. Upload remains USER-GATED.

## Firewall (unchanged, upheld)
Class-B GLP1R agonism is **unprovable and unrankable in-silico**; the wet-lab cAMP/CRE-SEAP assay is the only
verdict. Nothing here claims or ranks activation. The disulfide constraint and R299 aim are **rankable
priors** (pre-organization, proteolytic robustness, correct-aim, topology mirroring the sole cyclic de-novo
precedent) and a diversity/coverage hedge — not evidence of function.

## What was NOT redone
Three prior deep-research reports (2026-10-13/14) already exhausted the **literature SOTA** (`De novo GPCR
agonist design methods`) and the **physics first-principles levers** (`GLP1R agonism first principles levers`:
two-state ΔΔG, ENM/normal-mode, two-domain, His7, enhanced-sampling MD — all NO-GO/downgraded) and the
**foundational survey** (`GLP1R de novo agonist design`). This round researched only the genuine delta the
request added: abstract-math portfolio optimization, topology/pre-organization chemistry, and a hard
re-challenge of the load-bearing assumptions. Notes: `research_notes/GLP1R agonist portfolio and topology/`.

## The three levers (convergent verdicts)
| Lever (cross-domain root) | Verdict | Basis |
|---|---|---|
| **Portfolio P(≥1 hit) optimization** (probability / Markowitz / submodular / bandit / DPP) | **Don't churn 4/6/7/3; raise lineage/topology-cell count** | Re-splitting the 4 lineages moves P(≥1) <0.03 and flips sign with regime; the only regime-robust lever is **cell count** (a shared-mode/Esary-Proschan association argument: positive intra-lineage correlation only lowers P(≥1); a new cell's first shot ≈8× a 7th cousin's marginal). Fund from lowest-marginal slots (PepGLAD, saturating + no aim). |
| **Topology / pre-organization** (chain-entropy physics, macrocyclization thermodynamics) | **Promote a clean disulfide R299-aimer; generate fresh** | Pre-org buys ≤~1–4 kcal/mol but realized benefit is ≤1 order and often ~0/negative unless the free-state matches bound; prefer a disulfide that pre-organizes the scaffold while **leaving the threading termini free**. EvoBind (the sole precedent) is **head-to-tail backbone cyclic (NOT disulfide, not submittable)** — so a submittable intramolecular disulfide only *partially* mirrors it, but is the closest eligible analog. |
| **Reachability-wall + non-orthosteric re-challenge** (deep-pocket insertion; allostery/ago-PAM/exoframe) | **Wall holds; all non-orthosteric routes CLOSED** | Every named deep-insertion route (penetrating-pentamer ~0.008% class-A yield; pocket-seeded diffusion / RFd3 buried-atom / ODesign — only reshuffle unrankable binders; RFpeptides head-to-tail = ineligible) is infeasible/ineligible in ≤20 slots. Peptide ago-PAM/exoframe sites are intracellular/membrane → unreachable by an extracellular peptide. Nothing new post-2026-10-01 moves the wall. |

All three independently converge on the same action: **add clean constrained-topology / distinct cells, funded from the weakest PepGLAD hedges** — a rankable-prior + coverage move, firewall-safe.

## Experiments run this round (idle GPUs, zero cost)
1. **PepFlow distinct-5th-method cell (Agent 1's biggest lever) — EXAMINED → REJECTED.** The 8 gated PepFlow
   candidates (`pepx_*`, already eligible/clean/novel) are all **low-complexity outliers** vs v5b's accepted
   win-path band: A+G up to 50–60% (v5b cap 35.7%), max single-AA run 3–4 (v5b cap 2), entropy down to 2.57
   (v5b floor 2.81). The firewall bars crediting their (very low) in-silico minD_R299 as agonism signal, so
   the only benefit is lineage-count — offset by a **measured quality/developability downgrade** on a judged
   axis. Not a strict trade-up; rejected. (`scratchpad` analysis; pool `data/candidates/pepgen_longshot.csv`.)
2. **Fresh disulfide-staple generation (Agent 2 primary + Agent 1 fallback) — RUN → YIELDED a clean pick.**
   DiffPepBuilder v1 (SE3 + SSbuilder disulfide), glp1rvest2 R299 target, lengths 14–26, run
   `15D_10M_2026Y_14h_27m`: **+232 samples, +24 disulfide-stapled (27 total)**. (First attempt crashed on a
   GPU device-mask bug — `GPUtil` physical ordinals vs `CUDA_VISIBLE_DEVICES`; fixed by exposing all idle
   GPUs as an identity map.) Scored by the **same** eligibility+dev pipeline as the existing pool (out-of-band
   to protect the positional `dpbv2_*` names): **16 pass the hard gate** (2 Cys, non-vicinal, eligible, clean,
   aim ≤5.5 Å), **all graft-free (lcs ≤3)**, several reaching R299 at **3.3–4.8 Å** (≤ the linear DiffPep
   arm). New pool: `data/candidates/diffpep_ss_vest2.csv` (`dpbss_000–015`).

### The pick: `dpbss_010` (slot 13 of v5c)
`RNAAYYAYCEIDCIDQLLLAAYF` — L23, intramolecular disulfide **Cys9–Cys13** (internal; both threading termini
free, per the pre-org criterion), minD_R299 **4.76 Å** in DiffPepBuilder's own pose, id **42.9%** / cov 0.30,
**lcs 3 (no graft)**, developability **CLEAN** (instab 39, no oddCys, no vicinal CC). Chosen over 15 siblings
as the only candidate that is simultaneously clean-dev, graft-safe, novelty-in-band, aimed, and
internal-non-vicinal. (i,i+4 loop: specify the C9–C13 pairing at synthesis.)

## v5c specification & verification (by bytes)
- Composition: EvoBind 4 / DiffPepBuilder-linear 6 / **DiffPepBuilder-disulfide 1** / PepGLAD 6 / ECD 3 = 20.
  Max single-generator share **7/20 = 35%** (unchanged). Constrained-topology count **2 → 3**.
- Swap: slot 13 `pglad_053` (`GHGKIAAYPWNYTA`, cov0.21/id67, ~29 Å, no verified aim, weakest-novelty hedge)
  → `dpbss_010`. **All other 19 rows byte-identical to v5b.**
- Validator `--track 3`: **PASS, exit 0**, 0 errors / 0 warnings, anarci yes.
- Liability panel: **17 clean / 3 soft / 0 FATAL** (identical profile to v5b; slot 13 is CLEAN).
- **v5b regression:** rebuilding v5b through the extended assembler is **byte-identical** to the committed
  file (md5 `b10571b4…`) — the assembler edit is safe.
- submit==source bytes verified (dpbss_010 == pool bytes); 20 unique names + sequences; all `single_chain`.
- md5 v5c = `61c2d9e4d806b799a278efe7efb31063`.
- Structural novelty (ESMFold single-seq + FoldSeek vs PDB) on `dpbss_010`: pLDDT 0.68, **0 PDB structural
  hits** — consistent with v5b's 0/17-PDB-match standard; the peptide arm's novelty holds (`runs/v5c_newfold/`).

## Decision tree (what each result taught)
- Portfolio math → *don't* re-tune the mix (churn, <3 pt, sign-uncertain) → **kept 4/6/7/3 structure**, only
  raised cell/topology count. ✓
- PepFlow cell available & eligible? → **yes, but low-complexity outlier** → reject (quality downgrade). ✓
- Clean disulfide R299-aimer fieldable in ≤10 days? → existing pool marginal → **generate fresh** → 16 clean
  gated → **swap 1 in (v5c)**. ✓
- Deep-insertion / non-orthosteric lever? → **NO-GO / CLOSED** → no roster change from that axis; wall holds. ✓

## Honest ceiling
v5c is a **marginally** stronger *defensible* 20 than v5b on rankable priors (one more constrained-topology,
correct-aim design; one fewer no-aim hedge; novelty ≈ lateral), reached by a rigorous cross-domain pass that
**rejected the two bigger levers on evidence**. It does **not** and **cannot** improve the agonism odds — that
remains the wet-lab lottery of independent clean diverse shots, and the cAMP/CRE-SEAP assay is the only
verdict. v5b is retained; both are portal-parse-valid; the user decides which to upload.
