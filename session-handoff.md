# session handoff

## Where things stand (2026-10-26, DEADLINE DAY — FINAL = `submissions/glp1r_track3_v16.csv`, md5 `ca321795`, PASS 20/0/0 = v12 + 2 reserve upgrades)

**FINAL = v16 (a strict surgical upgrade of v12). Fallback = v12 (`ae879c97`, portal-confirmed, byte-identical tested-10 → near-equivalent).** On "improve v12 at all costs," I ran a **mining pass**: Chai-confirmed 38 Boltz-strong, R299-reaching designs that had never gotten the 2-folder gate (6 Boltz + 4 Chai seeds, all 8 GPUs; `runs/picker/mine_*`). **30/38 confirmed 2f-robust.** Two findings drove v16: (1) the mining winners are predominantly **the same dominant BoltzGen architecture v12 already caps at 4** — so a full re-allocation over them (saved as context, allocator output) **over-concentrates** (6 BoltzGen + 5 RFd4, 6 families, length-confounded minis promoted, rank-1 pLDDT dropped to 67) = the cousin-pile trap, NOT an improvement; (2) two v12 **reserve** members are **confirmed-dead** at 6 seeds — `glp1r_08` (DiffPep, Boltz R299 0/6) and `glp1r_37` (EvoBind, 1/6) don't robustly reach the vestibule. **v16 = v12 with ONLY those 2 reserve slots (rows 14, 16) replaced** by the best length-honest, high-pLDDT, 2f-robust, non-cousin mining winners: `glp1r_50_ago` (v4_reader_101_0, 21aa, R299 6/3, pLDDT 87) and `glp1r_51_ago` (v4_reader_069_0, 22aa, R299 6/2, pLDDT 90), both de-novo (graft 3/2) + 0-Cys. **The proven, diverse tested top-10 is byte-identical to v12** (strong length-honest rank-1 `glp1r_25`, pLDDT 92). So v16 is a small but strict upgrade: +2 robust binders in the 20, zero change to the tested set. Honest scope: a marginal reserve-only gain — v12 and v16 are near-equivalent bets (same tested-10); the mining's main result is that **v12 was already near the firewall-imposed ceiling** (the frontier is a single dominant BoltzGen architecture + length-confounded minis; no large improvement exists). Rationale `docs/SUBMISSION_RATIONALE_v16.md` (+ the v14→v12 reversal in `_v12.md`). **FIREWALL INTACT:** binding/expression + diversity, never agonism (the in-silico agonism-pose signal was tested + found non-discriminating this session). **Upload USER-GATED** — upload `v16` (2 new sequences → fresh portal parse; both clean single_chain so low risk), OR `v12` if you prefer zero re-parse (near-equivalent). Only the owner's final submit click remains; deadline 2026-10-26 11:59 UTC.

## Where things stand (2026-10-26, earlier — superseded by v16 above — FINAL = `submissions/glp1r_track3_v12.csv`, md5 `ae879c97`, PASS 20/0/0, portal-confirmed; supersedes v14)

**FINAL = v12 (gate-max + 8-lineage diversity best-20). v14's agonism arm was RETRACTED after the user's own devil's-advocate refuted it, and a final-day 8-GPU confirmation fold validated v12.** Sequence of events today: (1) The user invoked a cold **devil's-advocate** on v14; I **conceded the kill shot** — v14's R190 "deep-switch" agonism arm is a **null signal**: the project's own control panel (`runs/rfd4/ctrlpanel/scorecard_2folder.csv`) shows **scrambled-GLP-1 negatives engage the same central-polar residues (190|363|364, 190|364) as the agonists AND the antagonist** exendin(9-39); the deep-core generation spec was simply the vestibule spec **minus the R299 hotspot**, so the celebrated "3%→24% switch engagement" is an R299-deletion artifact (total central-polar engagement flat 61.5% vs 60.0%); and the flagship/arm touch R190 *alone*, fewer switch residues than a scramble. Also conceded (ORGANIZER_QA §1): **binding is a displayed, ranked axis**, so v14's net binding downgrade hurt the axis that scores. (2) The user said **"whatever it takes to win in the next 4h, all GPUs."** All 8 GPUs were free, so I ran a **multi-seed confirmation fold** of the 36 top binding contenders (bare+WT 24-432, **6 Boltz + 4 Chai seeds**; pipeline `scripts/picker/`, scores `runs/picker/confirm15_scores_{boltz,chai}.csv`). **Result: v12's strongest members are robust at the higher seed count** (`glp1r_32`/vest_76 ipSAE 0.61/0.79, R299 5/4; `glp1r_34`/v2_deep_060_1 6/4; `glp1r_35`/vest_91 5/2; `glp1r_30/31` 2f-robust) **and the v14 flagship never makes the 2f-robust cut** (reaches R299 in only 1 Chai seed even at 6/4 seeds) — independently confirming it was not special. (3) Re-allocating over the complete pool (deep-core designs merged on-axis) **over-concentrates length-favored cousins** (6 BoltzGen incl. near-twins `v2_deep_060_0/1` + 5 RFd4; only 6 families) — a length-confounded ipSAE bump at the cost of diversity. That set is saved as **v15** (`submissions/glp1r_track3_v15.csv`, md5 `39f3cf00`, validated PASS) for reference but is **NOT preferred**. **DECISION: ship v12** — 8 families (BoltzGen 4 / RFd4 4 / PepGLAD 3 / DiffPep 4 / ECD 2 / EvoBind 1 / RFd3 1 / PepMLM 1), ≤4/lineage, 17/20 2f-robust, **length-honest rank-1** `glp1r_25` (30aa, pLDDT 92), already validated + portal-parse-confirmed (zero re-upload risk). Rationale `docs/SUBMISSION_RATIONALE_v12.md`; cross-metric checks `data/candidates/v14_cross_metric_scorecard.md`. **Fallbacks:** v15 (`39f3cf00`, higher-ipSAE cousin-heavier), v14 (`1f25ed31`, retracted), v11 (`fc3653c4`), v10 (`6769ef67`), v9 (`419c57ff`). **FIREWALL INTACT:** v12 is ranked on measurable binding/expression + lineage diversity, NEVER agonism; the in-silico agonism-pose signal was explicitly tested this session and found non-discriminating; the wet **INDIGO CRE/luciferase** assay is the only verdict. **Upload USER-GATED — v12 is the artifact to upload (replacing v14 on the portal); only the owner's final submit click remains; deadline 2026-10-25 23:59 AoE = 2026-10-26 11:59 UTC.**

## Where things stand (2026-10-25 — superseded by v12 above — FINAL = `submissions/glp1r_track3_v14.csv`, md5 `1f25ed31`, PASS 20/0/0, PORTAL-CONFIRMED + byte-verified; owner-adopted)

**v14 = the agonist-mechanism MOONSHOT portfolio — owner-adopted FINAL (owner directive: "update all the harness files … [v14 submission] … commit and push").** After the "push even further moonshots" campaign, I reframed the moonshot from *binding* to *agonist mechanism*: only ~3% of the base pool engaged the deep activation switch (`central_polar` = R190 central hub / TM6 H363,E364 / TM7 Q394) in Boltz. A **deep-core generation** lever — RFd4-Proteina with the R299 ECL2 **rim** hotspot dropped and the binder forced onto the deep switch only (specs `runs/rfd4/specs/deepcore_{pep,mini}.yaml`) — lifted Boltz switch-engagement to **~24% (217/912)**; after the independent **Chai** fold, **16/80 were two-folder switch-engagers and 7 reached R190 in both folders** — the first firewall-legal enrichment for the *activator pose* this project has produced. **v14 = 3 agonist-arm designs** (rows 1-3: `glp1r_42_mini` RFd4 deep-core mini 49aa, ipSAE_min 0.55, pLDDT 87, N-term-in-7TM 4/3 — flagship at **screen-protected rank-1**; `glp1r_43_ago` RFd4 deep-core peptide 25aa, R190-both, 2f-robust; `glp1r_44_ago` BoltzGen deep 25aa, R190/E364) **+ 13 gate-core binders** (rows 4-16, the v12 gate-max set: `glp1r_28,30,25,29,23,10,33,27,36,08,26,38,31`) **+ 4 tail hedge** (rows 17-20: `glp1r_19,37,21,39`); **8 generator families, 0-Cys**. The agonist bets occupy exactly the picker's **screen-protected rank-1 + reserved long-shot** slots while the 13 binders hold the binder/expresser gate. **Honest trade (recorded, not hidden):** v12 (`ae879c97`) and v11 (`fc3653c4`) score higher on the pure binding-gate ranking; v14 gives up a little of that to seat activator-pose bets where they are most likely to be tested. A relayed side-agent note ("agonist moonshots bind weaker → the binding-ranked contest may test them less") was **affirmed**, which is *why* the moonshots are mixed in (rank-1 + long-shots + 13 gate binders) rather than crowding out the tested slots; **v12 is the drop-in gate-max alternative** if the owner later prefers to optimize the gate. **Re-verified fresh at lock (2026-10-25):** validator rows=20 errors=0 warnings=0 PASS; md5 `1f25ed31bbab4181d3a606cd1e2625fc`; **0-Cys all 20**; **longest contiguous incretin overlap ≤3 all 20** (the 3 new designs 3/2/2 = de-novo, no graft). **PORTAL-CONFIRMED + byte-verified 20/20** (owner pasted the v14 parse: 20 included / 0 needing fixes / all "Single chain · Passed"; portal==disk, evidence `data/candidates/portal_parse_v14_2026-10-25.txt`). Rationale `docs/SUBMISSION_RATIONALE_v14.md`; provenance `data/candidates/v14_provenance.csv`. **FIREWALL INTACT:** R190/deep-core engagement in both folders is a **necessary-condition pose enrichment** (membrane-blind co-fold biased toward the activator pose), **never a proof or a rank of agonism**; the agonist arm is seated as diverse independent shots (coverage / P(≥1 activates)); the **wet INDIGO CRE/luciferase assay is the only verdict**. **Fallbacks (all validator-/portal-clean):** v12 gate-max (`ae879c97`), v11b balanced (`3f4b5bf0`), v11 portal-confirmed reorder (`fc3653c4`), v10 (`6769ef67`), v9 (`419c57ff`). **Upload USER-GATED** — v14 is the artifact to upload (replacing the portal-confirmed v11); only the owner's final submit click remains; deadline **Sun 2026-10-25 23:59 AoE (tonight)**.

## Where things stand (2026-10-25 — superseded by v14 above — FINAL = `submissions/glp1r_track3_v11.csv`, md5 `fc3653c4`, PASS 20/0/0, PORTAL-CONFIRMED)

**v11 = v10's EXACT 20 sequences REORDERED for the organizers' published picker rubric** (SET == v10, byte-verified — nothing added/removed; zero import risk). The owner supplied the picker prompt + "replace a lot at all costs, best 20 per the prompt." I reproduced the picker's exact method (bare submitted design + WT GLP1R 24-432 tags-off; ipSAE/ipTM co-fold + ESMFold2 pLDDT + Kyte-Doolittle; BOTH Boltz+Chai) over the full pool (1,607 eligible → 221 shortlist + 271 expansion; ~160 Chai-confirmed; pipeline `scripts/picker/`). **Finding:** only **6-7/20 v10 designs are 2f-robust reachers**; ipSAE is folder-noisy (Boltz optimistic, Chai pessimistic). A draft **wholesale 13/20 swap** was **REFUTED by a cold devil's-advocate (P≈0.70, verified vs our own files):** the both-folder R299 gate is **agonism-blind** (antagonist exendin passes — the HOLD-v9 lesson), 7/17 "robust" sit at the `chai==2` reseed margin, a 0.75-identity near-dup slipped the k-mer dedup, + unvetted imports. The picker is a binder/expresser GATE and the PRIZE is activation → a binding-composite bump by deleting 13 diverse agonism bets optimizes the wrong objective. **Decision: reorder, not replace** — the re-score's real value is the row-order lever (picker takes top-10 of row order; v10 wasn't picker-sorted — `glp1r_25`, our best bare+WT design, was at row 6). v11 front-loads the 6 2f-robust vestibule reachers (rank-1 `glp1r_25`), then single-folder reachers (7-15), weak message peptides (16-17), ECD antagonist-hedge last (18-20). A side-agent "thin binding edge" note was evaluated + addressed (v11's tiers rest on robust cross-folder reach + pLDDT, not the averaged ipSAE; rank-1 is #1 on every axis). **PORTAL-CONFIRMED 2026-10-25:** v11 loaded → parsed clean (20 included / 0 needing fixes / all "Single chain · Passed") in the exact reordered order; byte-verified portal == committed v11 (`fc3653c4`) on names+order+lengths+molecule_class+prefix/suffix = submit==validated (evidence `data/candidates/portal_parse_v11_2026-10-25.txt`). **v10 (`6769ef67`, same set, original order) + v9 (`419c57ff`) = byte-frozen fallbacks.** Rationale `docs/SUBMISSION_RATIONALE_v11.md`; per-design 3-screen evidence `data/candidates/v11_picker_screens.csv`; commit `0522032`. Firewall intact (ordered by measurable binding/reach/expression on the stated vestibule epitope, never agonism). **Upload USER-GATED — only the owner's final submit click remains; deadline Sun 2026-10-25 23:59 AoE (tonight).**

## Where things stand (2026-10-23 — FINAL = `submissions/glp1r_track3_v10.csv`, md5 `6769ef67`, PASS 20/0/0, molecule_class `single_chain`)

v10 = **v9 with exactly one owner-approved change**: `glp1r_04` → its 0-Cys **C9S/C29S** variant (row order + 19 other sequences byte-identical; diff-verified). Adopted after the organizers **definitively confirmed the design space — linear peptides / 20 standard AAs / 10–250 per chain; NO cyclic, NO load-bearing disulfide staple, NO noncanonical** — and that **`molecule_class=single_chain`** (set = single_chain/nanobody/scfv/fab_kappa/fab_lambda; a WebFetch paraphrase had wrongly read "protein" — corrected). The swap removes v9's lone disulfide-capable design in a linear-only competition at zero behavioural cost (fold-verified: `glp1r_04`'s 2 Cys are not load-bearing; the C→S mutant reaches R299 identically). **v9 (`419c57ff`) = immediate byte-frozen fallback** (fully compliant itself). Rationale `docs/SUBMISSION_RATIONALE_v10.md`; audit+candidate+fold `runs/finalize/`. **Upload USER-GATED** (owner's portal click); deadline **Sun 2026-10-25 23:59 AoE**.

This session (`/ambition-lift` /ultrathink): a 4-angle frontier sweep **re-confirmed the firewall** (no wet-validated class-B agonism ranker; de-novo class-B agonism demonstrated only via cyclic/NCAA/disulfide-constrained peptides — all forbidden here); a deep-reader (Q234/V237 TM3) necessary-condition discriminator was **refuted by its own matched controls** (inactive metabolite GLP-1(9-36) passes it — reach ≠ efficacy, do not use). The dpbss disulfide-staple recovery was **stood down** when the organizers confirmed linear-only. Net: HOLD the v9 portfolio, compliance-hardened to v10. Firewall intact; wet cAMP/SEAP the only verdict. Lesson: [[lesson-unverified-constraint-fenced-design-space]].

## Where things stand (2026-10-20 — FINAL upload artifact = `submissions/glp1r_track3_v9.csv` (md5 `419c57ff`, PASS 20/0/0) + rationale `docs/SUBMISSION_RATIONALE_v9.md` = v6b composition with THREE owner-approved swaps: (v7) weakest glp1r_15 → `glp1r_23_ago`/rm_0079 at rank 4; (v8) weakest-remaining glp1r_22 (ipSAE 0.0, 0/2 docked, geometric-only reacher) → `glp1r_24_ago`/bg_0746 at rank 5; (v9, owner "win at all costs") weakest-remaining glp1r_03 (EvoBind, ipSAE 0.428, non-reacher) → `glp1r_25_ago`/bg_1170 at rank 6. bg_0746 + bg_1170 = TWO independent wave-2 BoltzGen architectures (Jaccard ~0.017: the length-honest 22aa outlier + the 30aa dominant-family archetype), both **robust 2-folder R299 reachers** (4/4 both folders, 4 seeds/folder). Seating both = max diverse robust reachers in the top-10 pick window (6 reachers across 5 generators) — a P(≥1 activates) coverage move, NOT an agonism rank (bg_1170's 2/5 central-polar reach is length-consistent, not a quality signal). v8 `3b7d2581` (single-swap) kept as immediate fallback; v7 `9ee8df5b`; deeper v6b_ranked2 `976e7e8e` / v6b_ranked `1571a3d4` / v6b `32819e6f` / v6 `398bfb30` / v6c `643f3fe6`; upload USER-GATED. **PORTAL 2026-10-20: v9 loaded into the Adaptyv portal → parsed clean (20 included / 0 needing fixes / all "Single chain·Passed"); byte-verified portal==committed v9 (`419c57ff`) = submit==validated; the final submit click is the owner's remaining gated step (format/parse gate only — no novelty/agonism assessment).** Driver = the published selection prompt: ≤10 designs/submission taken from the top of our row order → the order front-loads all 6 robust R299 reachers (glp1r_10/21/04/23/24/25) + all lineages into the top 10. See the 2026-10-20 (v9 wave-2) section at the bottom + [[adaptyv-glp1r-selection-rubric]].)

**2026-10-22 — Wave-3 (BindCraft2 v1.0.4 active-state moonshot; owner "use all the resources to your will") → NEGATIVE; v9 UNCHANGED.**
The first **AF2-based** generator used here (orthogonal to v9's Boltz/RFd3 lineages), run against active-state **6X18**
through the validated **Boltz∧Chai 2-folder construct bar**: 3 waves, ~5,000 trajectories, every config (forced-deep /
ordinary / miniprotein / termini-accessible) → **0 clear the bar** (3a 0/1,988 accepted; 3b 0/11; 3c 0/8). With the
2026-10-19 BoltzGen arm (0/21) that is **two orthogonal generators failing identically** — de-novo designs *reach* R299
but don't *dock* with native-comparable confidence in the independent folder (Chai iPAE 10–18 vs native ≤5.5). **HOLD
v9 (`419c57ff`); no candidate v10.** Funnel + evidence: `scripts/bc2/` + `data/candidates/wave3_bc2_funnel_2026-10-22.md`;
full log in `progress.md`. Firewall intact (no agonism claimed/ranked). The in-silico frontier is exhausted; only the
owner's portal submit of v9 + the wet cAMP/SEAP assay remain.

**2026-10-23 — Wave-4 (RFD4-Proteina moonshot; owner "utilize all GPUs / dominate at all costs" + /ultrathink) → NEGATIVE; v9 UNCHANGED, NO v10.**
Ran the newest SOTA generator **RFD4-Proteina** (RosettaCommons × NVIDIA, **BSD-3 code+weights**, ~2026-10-19;
flow-matching all-atom co-design) — installed clean (`third_party/RFD4-Proteina/.venv`), vestibule-conditioned on 6X18,
→ **2,520 designs** → 8-GPU Boltz R299 screen (1,046 reach, 41% — Boltz permissive) → top 202 → Stage-2 Boltz+Chai
2-folder + anchors. The 9 RFD4 minis that appear to "beat" glp1r_25 are **length-confounded** (iPAE bias −0.93 within RFD4).
A side-agent-prompted **length-matched bake-off** (BoltzGen+BC2+RFD4+anchors through ONE pipeline; `runs/rfd4/bakeoff/`)
was decisive and **refuted the "RFD4 breakthrough"**: (1) BoltzGen SHORT peptides (length-unconfounded) clear the bar too
— 26/41 reach R299-both, 6 beat glp1r_25 (best `bg_v4_reader_33` 25aa 4/4-both @ Chai 7.22); the old "BoltzGen 0/21" was a
**tag-off 5.5-cut artifact**. (2) The bar is **agonism-blind** — the antagonist exendin(9-39) reaches R299-both in all 3
runs and PASSES the gate while the agonist exendin-4 FAILS the same run (gate inverts the pair). A 4-agent adversarial
Workflow (`wf_7d8374c6-29c`) reproduced the scorecard byte-exact (0/770) and reached **unanimous HOLD, high confidence**.
**HOLD v9 (`419c57ff`); de-novo frontier now exhausted across 7 generators** (EvoBind, DiffPepBuilder, PepGLAD, RFd3,
BoltzGen, BindCraft2, RFD4-Proteina). Evidence: `runs/rfd4/` + `progress.md` (2026-10-22/23) + memory
[[lesson-cofold-reach-bar-cheaply-clearable-agonism-blind]]. **`/code-review` 2026-10-23** (committed `693c17d`): 9 findings,
none invalidate HOLD; 6 fixed + 1 defensive (fail-loud screen, zero-survivor guard, GPU idle preflight, OMP cap, construct
chai-cut 99, harvest assert, doc fix), 2 pushed back. **NB when reading scorecards: `PASS_2folder` is run-noisy
(`R299_both AND boltz_ipae≤6.0`) — rank by `R299_both` reach + within-length-bin iPAE, never the raw PASS column.**
Firewall intact; only the owner's USER-GATED v9 submit + the wet cAMP/SEAP assay remain.

**Pipeline F0–F9 COMPLETE; v5c survived a brutal reject-everything audit; a mechanism-coverage moonshot then
produced v6, which the owner ADOPTED as the recommended pick (2026-10-16).** **The remaining action is the
owner's USER-GATED upload of v6 — never auto-upload.** Autonomous-to-deadline (deadline 2026-10-25 23:59 AoE).
Compute ceiling = **8 H100s + 500 GB**. **PICK = v6** `submissions/glp1r_track3_v6.csv` (md5
`398bfb3006464811e8ce9ab57afb4dad`, validator PASS 20/0/0); **v5c** (`61c2d9e4…`) byte-frozen fallback; **v5b**
(`b10571b4…`) + **v1** (`1ce4e943…`) deeper fallbacks. **Track-C (watcher `bem3nan8r`) has RUN and resolved
NEGATIVE — no v7**; all owner-approved moonshot tracks (A/B/C/D) are now resolved and no GPU work is pending.

**2026-10-18/19 — owner "try the fix anyway" + "dominate at all costs" (details in the dated sections below):**
Wave-B RFd3 motif-extension is CLOSED (the documented fix anchors the motif but the diffused extension never bonds
to it; reproducible NEGATIVE). Then a maximal-effort, free-8-GPU uniform **2-folder (Boltz+Chai) reach validation**
of the EXACT v6 twenty + 15 non-v6 reach-candidates + 8 native controls **CONFIRMED v6 and justified no change**:
4 v6 members are robust 2-folder R299 reachers (`glp1r_04` at liraglutide level, `glp1r_10/21/22`); the swap check
is NEGATIVE (no candidate dominates; DiffPepBuilder "reachers" don't reproduce reach under independent folders);
and the controls empirically prove the agonist proxy cannot separate agonists from antagonists → the firewall is
re-confirmed, no in-silico re-ranking is valid. **v6 UNCHANGED.** Evidence:
`reports/GLP1R two-folder reach validation 2026-10-19.md` + `data/candidates/v6_twofolder_reach_2026-10-19.csv`.

- **2026-10-16 MECHANISM-COVERAGE MOONSHOT (owner: "full push A+B+C+D") → candidate v6 built + validated.**
  Report: `reports/GLP1R mechanism-coverage moonshot.md`. D(SOTA)=no-go; B(coverage axis)=built (v5c covers 3/4
  approach bins, reader-proximal <4.5Å bin EMPTY); A(RFd3 message-address)=384 backbones → 31 clean+novel → 20
  folded → **3 reproduce consensus <4.5Å to R299 under independent Boltz+Chai** (lead-verified clean; the RFd3
  placement reach is CIRCULAR and not counted; 17/20 fail the non-circular test = reachability wall, valid
  negative); C(2-SS)=RAN→**NEGATIVE** (watcher caught a GPU-6 window; of 42 built structures only 2 realize two
  real disulfides and both fail the committed gates; the 3 clean+band+eligible ones realize only 1 real SS + 2
  free thiols, duplicating `dpbss_010` — no clean double-staple exists; no v7). **v6** `submissions/glp1r_track3_v6.csv` md5
  `398bfb3006464811e8ce9ab57afb4dad`, validator PASS 20/0/0, 17/20 clean (same forced 3-liability floor) =
  v5c minus slots 11(`pglad_034`)+17(`pglad_001`) (most-redundant outer PepGLAD) plus `glp1r_21_ago`
  (des_0039_m7, DFYFDAAMVYLYTKLANPDPKVLEELKKQIALSLIVD) + `glp1r_22_ago` (des_0047_m6,
  WWLEPSDDPKLQELHAQALADWADVIFEETIDFILSLVVRVLLYL) = 2 distinct-backbone RFd3 reader-proximal fillers.
  v6 raises mechanism-coverage 3/4→4/4 + generative priors 4→5 (PepGLAD 6→4). **It is a coverage/robustness
  TRADE, not a strict Pareto win**; caveats = weak/mixed interface confidence + co-fold memorization confound;
  agonism still unprovable (assay-only). Candidates committed: `data/candidates/msgaddr_waveA_candidates.csv`.
  **OWNER ADOPTED v6 as the recommended pick (2026-10-16 via AskUserQuestion); v5c (`61c2d9e4`) byte-frozen
  fallback.** Firewall held (minD_R299/2-fold consensus = necessary-condition coverage filter only, never an
  agonism rank). **Track-C (watcher `bem3nan8r`) has since RUN and resolved NEGATIVE** — first-hand Sγ–Sγ
  verification shows no clean double-stapled "grenade" exists (2-SS realization ≈ 0; the clean candidates carry
  unpaired free thiols and duplicate the `dpbss_010` topology class); v6 unchanged, no v7. Full write-up in the
  Track-C resolution section of `reports/GLP1R mechanism-coverage moonshot.md`.

- **2026-10-16 BRUTAL STRESS TEST (owner: "reject all 20 if a better set exists") → `v5c_stands`, independently
  verified.** A 48-agent adversarial workflow (`glp1r-brutal-stress-test`) attacked every design + the selection
  logic on 6 fronts (per-design teardown / composition challenge / full-pool re-optimization incl. PepMLM+BoltzGen
  / aggregation-synthesizability / novelty hardening / firewall red-team+SOTA), then refuted + firewall-checked
  every finding. 66 findings, 33 CONFIRMED+firewall-safe, **every per-slot finding = KEEP; 0 designs rejected;
  2 pro-change claims REFUTED**. Coordinator re-ran the committed scorers first-hand (not on the agents' word):
  md5 `61c2d9e4` ✓; validate PASS 20/0/0 ✓; certificate **0 Pareto swaps** ✓; **17/20 dev-clean, 3 forced
  liabilities = slots 3/4 (instab) + 20 (POLYRUN)** ✓; **CLEAN-FLOOR = 17** (max dev-clean 20 assemblable from
  ALL clean pools incl. pilots, under the 35%/generator cap, is only 17: PepGLAD 7 + DiffPepBuilder 7 + EvoBind 2
  + ECD 1 + PepMLM 0 + BoltzGen 0) → **a fully-clean 20 is mathematically impossible; v5c's 3 liabilities are the
  FORCED FLOOR, not a defect** ✓. Report: `reports/GLP1R brutal stress test v5c confirmation.md`. Record-hygiene:
  `data/candidates/v5c_struct_novelty.csv` written (corrected for the ACTUAL v5c slots 11=pglad_034 pLDDT60 /
  13=dpbss_010 pLDDT68, both maxTM 0.000 novel; stale v5_struct_novelty.csv mislabeled those two). **One genuine
  decision point surfaced + DECLINED (F2-07):** iff owner re-opens the submission, trim slots 8/11/17 + add 3
  PepMLM (priors 4→5, min-pair 1.88→2.22) — but it WORSENS developability (liab 3→6; 0/21 PepMLM band-passers
  clean), is not a strict Pareto win, and PepMLM shares ESM-2 with DiffPepBuilder (non-orthogonal). KEEP v5c.
  Firewall held: minD_R299 used only as the not-worse gate (all 6 DiffPep-linear aimers miss the 4.5Å gate → did
  no selection work); no agonism/binding signal touched the verdict.

- **EIGHT submission files staged (all validate PASS, all ≤20, all `molecule_class=single_chain`):**
  - **PICK = v6** `submissions/glp1r_track3_v6.csv` — **20 designs**, md5 `398bfb3006464811e8ce9ab57afb4dad`,
    **OWNER-ADOPTED 2026-10-16**. = v5c − slots 11/17 (most-redundant outer PepGLAD) + 2 distinct-backbone RFd3
    reader-proximal coverage-fillers `glp1r_21_ago` + `glp1r_22_ago`; mechanism coverage 3/4→4/4, generative
    priors 4→5, same forced 3-liability floor (the 2 additions clean/0-Cys/eligible). Validator PASS 20/0/0.
    Report `reports/GLP1R mechanism-coverage moonshot.md`.
  - **v5c** `submissions/glp1r_track3_v5c.csv` — **20 designs**, md5 `61c2d9e4d806b799a278efe7efb31063`.
    **Byte-frozen FALLBACK** (brutal-tested Pareto-optimal, portal-parsed 20/20). = v5b with ONE swap (slot 13
    `pglad_053` → `dpbss_010`, a fresh clean DiffPepBuilder disulfide-stapled
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
- **2026-10-15b moonshot re-attack (8-agent adversarial vetting + 2026 SOTA sweep):** the firewall HELD against the
  whole sweep (no new activation oracle survives as a ranker; no new generator breaches the reachability wall;
  nothing post-2026-10-01 changes the board). M2 (structural-novelty max) + M4 (fly-casting/low-pLDDT rescue) KILLED
  on byte-verified evidence. **M1 (principled diversity selection) EXECUTED** → `scripts/diversity_certificate.py`
  + `reports/GLP1R diversity selection certificate.md`: firewall-guarded (GUARD-A no engagement/aim in the kernel),
  TRIPWIRE confirms the band rejects all PepFlow rows, and **v5c is Pareto-efficient / diversity-consistent** under
  the fixed 4/6/1/6/3 matroid. An initial flag (`dpbv2_005`→slot 6) was REFUTED on build — `dpbv2_005` is a
  2-disulfide design (`has_ss`, 4 Cys), not a clean linear upgrade; the Cys-count-hardened certificate now finds
  **0 valid swaps** → v5c confirmed Pareto-optimal (v5d built on owner request, refuted, removed). Firewall citations added to docs/METHODS.md
  (Muratspahić/Baker Nature 2026; Junker & Schoeder PLoS One 2026; Fonteyne RSC Dig. Disc. 2026 — all verified first-hand).

## Do next

1. **Upload the FINAL package — `submissions/glp1r_track3_v9.csv`** (md5 `419c57ff`, PASS 20/0/0) +
   supporting rationale `docs/SUBMISSION_RATIONALE_v9.md`. This is the v6b composition with THREE owner-approved swaps
   (v7: glp1r_15 → rm_0079 @4; v8: glp1r_22 → bg_0746/`glp1r_24_ago` @5; v9: glp1r_03 → bg_1170/`glp1r_25_ago` @6 —
   two independent wave-2 BoltzGen architectures) in the
   **cap-aware ipSAE-informed order** (all 6 robust R299 reachers glp1r_10/21/04/23/24/25 + all agonism lineages in the
   top 10; rank-1 = glp1r_10; binders 18–20 hedge). Fallback = `glp1r_track3_v8.csv` (md5 `3b7d2581`, single-swap) if
   two BoltzGen slots are judged too concentrated — built because the published selection prompt caps designs/submission at 10, taken from the
   top of our row order. The upload click is **USER-GATED** — never auto-upload. **STATUS 2026-10-20: v9 loaded into the portal and parsed
   clean (20 included / 0 needing fixes / all "Single chain / Passed"); byte-verified portal==committed v9
   (`419c57ff`), submit==validated; only the owner's final submit click remains (format/parse gate only).**
   Fallbacks: `v8` single-swap (`3b7d2581`), `v7` (`9ee8df5b`), `v6b_ranked` prize-tier
   (`1571a3d4`), `v6b` unordered (`32819e6f`), `v6` (`398bfb30`), `v6c` (`643f3fe6`), `v5c`/`v1` deeper.
2. **No submission change is pending.** v5c is fully verified (validator PASS, 17/3/0, byte-regression-safe,
   portal-parsed, 0 PDB hits) and now additionally certified Pareto-efficient/diversity-consistent (M1). The
   in-silico win-path levers are exhausted; remaining *agonism* gains are **wet-lab only**.
   **Owner-approved pilots — BOTH RAN, lead-verified, 0 dominators (COMPLETE 2026-10-15).** PepMLM + BoltzGen were
   provenance-VERIFIED clean (PepMLM HF weights MIT & `gated=False` — a subagent's restrictive-license claim was a FALSE
   ALARM, corrected via HF+GitHub APIs; BoltzGen MIT + base Boltz-2 MIT, no ESM-3/ESMC/Protenix/AF3). GPU-blocked through
   watcher cycle 1 (`baopxnp26`, 4h@180s → `no_window`); cycle 2 (`brc0ev2tb`, 12h@600s) caught a durable idle window
   ~21:05 UTC when the foreign job finished and **ran both pilots to completion** (one process/GPU, nothing clobbered).
   Outcome (COMMITTED to `data/candidates/`: `pepmlm_pilot.csv`+`_report.md`, `boltzgen_pilot.csv`+`_report.md`):
   **PepMLM** 105 raw → 89 eligible → 21 band-passing → **0 strict-Pareto dominators vs v5c**; **BoltzGen** 30 raw →
   29 eligible → 3 band-passing → **0 dominators**. Both gates reuse the committed `diversity_certificate`
   (featurize/passes_band/pareto_dominates/load_v5c/AIM) verbatim; I **independently re-drove** those committed
   functions from the raw sequences in my own loop (`scratchpad/verify_pilots_pareto.py`) → confirmed **0 dominators**
   in both pools (0 even among ALL eligible, incl. non-band — no hidden dominator the band masked), and confirmed
   `load_v5c()` returns the frozen 20-member v5c (dpbss_010 at slot 13). **v5c stands UNCHANGED**, now additionally
   stress-tested against 135 fresh de-novo candidates from two independent SOTA lineages (ESM-2 + Boltz-2). The pilots
   were diversity/clean-ticket hedges, NOT a win-path — and no swap is justified (none dominates). **Watcher mission
   COMPLETE — do not re-arm** (both pilots have now executed). NeoPep/PPI-Diff CLOSED on license. **v5d** (owner-approved)
   refuted on inspection (swap-in `dpbv2_005` is a 2-disulfide design, not a clean upgrade) and removed. In-silico
   win-path levers are now fully exhausted; remaining *agonism* gains are wet-lab only (cAMP/CRE-SEAP).
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

## 2026-10-17 — SUPERSEDES the "do not re-arm / levers exhausted" notes above (Wave-B era)

- **v6 is the owner-adopted pick** (`398bfb30`, 2026-10-16); **v5c** (`61c2d9e4`) is the byte-frozen fallback.
  Upload remains USER-GATED. Deadline 2026-10-25 23:59 AoE.
- **Owner approved two moonshot actions** ("go ahead with both"): (A) **Wave-B** RFd3 motif-extension off the proven
  reacher backbones des_0039/des_0047 for a higher-confidence reader-proximal filler; (B) an **adversarial red-team**
  to break the "frontier exhausted / keep v6" conclusion.
- **(B) red-team: DONE → keep v6.** No win-path lever; the one real finding (unmeasured *structural* novelty of the
  two v6 additions) is now measured and within-gate — `glp1r_22_ago` 4-of-4, `glp1r_21_ago` 3-of-4
  (`data/candidates/v6_filler_struct_novelty.csv`; detail in `reports/GLP1R mechanism-coverage moonshot.md`).
- **(A) Wave-B: EXECUTED 2026-10-17 → NEGATIVE → CLOSED (do not re-arm).** The watcher caught a window (~16:33Z)
  and generated 192 RFd3 motif-extension backbones; all are non-physical — the fixed motif was not anchored
  (chain-A Rg ~82–93 Å vs seed 9.5 Å, ~150 Å intra-chain breaks; receptor fine at 20.5 Å; confirmed in the raw
  cif). Not folded. Even a corrected regen is a cousin of glp1r_21/22 (no diversity gain; co-fold-confidence is
  folder pessimism, not agonism), so Wave-B cannot improve the portfolio → CLOSED. Fix hypothesis if ever
  revisited: rebuild the seed without HETATM in chain R, drop `infer_ori_strategy:hotspots`, verify the dialect-2
  fixed-motif contig, and use standard (not fast) mode. **v6 unchanged; no agonism claim.**

## 2026-10-18/19 — Wave-B "try the fix anyway" (owner-instructed) → still NEGATIVE, now mechanistically characterized → CLOSED

- Owner said **"try the fix anyway"** (overriding the cousin-value objection). Ran the full documented fix + beyond.
- **Barrier 1 motif-anchoring = FIXED (fix's central claim confirmed).** Stripping HETATM/waters from the seed +
  dropping `infer_ori_strategy:hotspots` (the NaN-origin bug) anchors the fixed motif perfectly: last-37 Rg 9.4 Å
  = seed, receptor Rg 20.5 Å, contig verified in-log `L=249` = 13 grown + 37 motif + 199 receptor. `--mode exact`.
- **Barrier 2 extension-closure = NEGATIVE (the real wall).** The grown 13-res extension never forms a connected
  chain or bonds to the motif: junction 12–120 Å (closed ≈3.8 Å), extension internally exploded (CA–CA 30–120 Å),
  reproducibly across the FULL sweep — no-realign (≈frac 0.0), `allow_realignment=true` frac 0.5 & 1.0, both
  aggressive (step_scale=3) and default (1.5) dynamics (step-scale control refuted the confound). Likely cause: a
  37-res fixed motif = 74% of the chain; RFd3 won't coherently diffuse a small extension welded to a large held motif.
- **bf16 sub-barrier = SOLVED.** Enabling realignment crashed on cu130 (no bf16 svd/det kernels; bf16 AMP autocast
  re-demotes the Kabsch matmuls). Local float32 **autocast-disable patch** to the TNF kit env's
  `anthropic-adaptyv-2026-tnf/envs/uplifting-rfd3-kit/.../foundry/utils/alignment.py` (`weighted_rigid_align`).
  **LOCAL-ONLY, gitignored (TNF `envs/`), never staged; strictly a correctness fix (float32 Kabsch).** Kept (not
  reverted) — it only makes `weighted_rigid_align` float32, safe for all callers; revert = restore the stock bf16
  block if pristine vendored code is wanted. Lessons: `[[lesson-rfd3-motif-extension-not-anchored]]`,
  `[[env-bf16-autocast-demotes-linalg]]`. Scripts in `scratchpad/.../waveB/` (`wave_b_realign_*.sh`,
  `ca_gate.py`, `diag_split.py`, `convert_ab.py`, `analyze_realignexact.sh`).
- **Wave-B remains CLOSED; no GPU work pending.** v6 (`398bfb30`) and v5c (`61c2d9e4`) UNCHANGED; upload USER-GATED.
- GPU landscape 2026-10-19: foreign vLLM (2×~75 GB) + `mmbu` training (~64 GB) intermittently hold GPUs; grab
  whichever read 0/0 (idle-guard protects). Later in the day all 8 freed.

## 2026-10-19 — owner "dominate at all costs" (×2, over a conserve recommendation) → uniform 2-folder validation → v6 CONFIRMED, no change

- Interpretation recorded in memory [[feedback-dominate-at-all-costs]]: pull every LEGITIMATE lever with real
  compute, but never override the firewall or burn GPUs on confounded metrics / cousin theater. First verified the
  frontier is genuinely exhausted (the lone `pglad_029` 2-folder AGREE is a KNOWN confound — a GLP-1 scramble also
  passes the N-term-in-7TM gate; portfolio already P(≥1)-optimized; new-SOTA scout negative — only Proteina-Complexa,
  wrong mini-protein/ECD regime).
- **Ran the one clean, firewall-safe campaign:** uniform **2-folder (Boltz-2 + Chai-1, single-seed)** cofold of the
  EXACT v6 twenty + 15 top non-v6 reach-candidates + 8 native controls vs the 409-res 24–432 construct, scored by
  the UNCHANGED `scripts/iface_score.py`. (Pipeline notes for next time: `cofold_boltz_shard.sh` 8-way parallel
  hits a shared-JIT/writer contention → only one shard's folds succeed; **run single-GPU** (folds are ~1.3 s each,
  43×1seed ≈ 1 min). Chai shards fine one-process-per-GPU via `CUDA_VISIBLE_DEVICES`. `iface_score.py` needs the
  `uv` env (biopython). Target MUST be `data/target/construct_24_432.seq` (409 res) for the scorer's numbering.)
- **Result → v6 confirmed, NO change justified.** Controls: only native GLP1_7-36 hits AGREE:agonist; potent
  exendin-4 & liraglutide MISS the 2-folder bar and antagonist exendin(9-39) overlaps → the proxy does NOT separate
  agonists (empirical firewall). v6 carries 4 robust 2-folder R299 reachers (`glp1r_04`=liraglutide-level,
  `glp1r_10/21/22`). Swap check NEGATIVE: no non-v6 candidate dominates; the `dpbss_*`/`dpbv2_*` reach-candidates
  that aimed <5 Å in DiffPepBuilder's own pose collapse under both independent folders (vest 0, iPAE 10–20) — the
  reachability wall holds. Evidence committed: `reports/GLP1R two-folder reach validation 2026-10-19.md`,
  `data/candidates/v6_twofolder_reach_2026-10-19.csv` (+ `_foldset_`). `/code-review` found 0 correctness bugs; its
  2 nits fixed (persist derived tables to tracked path; `.gitignore` the `stress_liab.json`/`data/af2ig_targets/`
  transients). **v6 (`398bfb30`) UNCHANGED; upload USER-GATED; no GPU work pending.**

## 2026-10-19b — BindCraft2/2026-tools deep-research + construct probes + BoltzGen active-state arm → HOLD v6 (2-folder NEGATIVE)

Owner "dominate at all costs" → "utilize all the free GPUs extensively" → (AskUserQuestion) "push further on GPUs
first". The one genuinely-new on-mechanism lever — **active-state *generation*** — was tried at full 8-GPU scale and
**REJECTED on the 2-folder cross-predictor bar**; **v6 (`398bfb30`) UNCHANGED**.

- **Firewall re-confirmed** by a BindCraft2 v1.0.4 + 2026-toolscape deep-research pass (report `reports/BindCraft2
  and 2026 agonist design tools.md`, notes `research_notes/BindCraft2 and 2026 agonist design tools/`): BindCraft2
  induced-fit is binder-side, not activation; no eligible 2026 tool induces/scores class-B agonism; Baker *Nature*
  2026 (PMID 42168559) = de-novo class-B designs are antagonists.
- **Production reality folded into AGENTS.md as an invariant** (organizer-clarified): cell-free expression, retained
  (f)Met, C-term GFP11/Twin-Strep tag ON in the assay, disulfide UNCONFIRMED → the message must be **INTERNAL**, both
  termini disposable, **no design may depend on a disulfide**; fold the REAL construct before trusting reach.
  Construct probes show most of v6's reach is tag-fragile (only `glp1r_06/09` Boltz-robust); reach is a positive
  indicator, never a disqualifier. Evidence: `data/candidates/v6_{met,construct}_probe_2026-10-19.csv`.
- **BoltzGen active-state arm → v7 PROPOSED then REJECTED.** ~700 designs → 41 deep-inserters → 21 cross-fold → 3
  production-robust (glp1r_23/24/25) → proposed v7 (md5 `f38c06df`, `runs/glp1r_track3_v7_PROPOSED.csv`, gitignored).
  **2-folder (Chai) check: 0/21 clear the Boltz∧Chai construct bar that GLP-1(7-36) clears (iPAE 4.63)** → a
  Boltz-family artifact (glp1r_23 bare-only iPAE 4.14 vs in-construct 8.64; 24/25 Chai-unconfirmed 15–19). **HOLD v6.**
  Evidence: `reports/GLP1R active-state generation and construct probes 2026-10-19.md` (§6) +
  `data/candidates/boltzgen_{sweep_depthgate,validated,posestab,2folder_chai}_2026-10-19.csv`. Commits `0cc6ec9`,
  `817c793`. Env-reuse (no rebuild; TNF kit `envs/` wiped by disk cleanup): Boltz = `sepiq/.venv-boltz` (2.2.1) +
  `$HOME/.boltz`; Chai = `sepiq/.venv-chai` + `CHAI_DOWNLOADS_DIR=/home/prachh/v/chai_downloads`; BoltzGen fresh in
  `third_party/boltzgen/.venv`. [[lesson-boltzgen-deep-insertion-fails-2folder]] [[adaptyv-glp1r-production-constraints]]
- **No GPU work pending.** The active-state lever is now tried + closed; further generation would be fishing against
  the standing firewall.
- **2026-10-19c slot-13 staple de-risk → v6b (owner-approved).** A side-agent review (relayed by owner) caught that
  v6 still held a design chosen purely for a disulfide staple (glp1r_13 = dpbss_010, Cys9–Cys13) that the new
  Production-reality invariant says not to depend on — added without re-checking v6. Verified by bytes: only
  glp1r_13 depends on the staple (reach fails 2-folder; cell-free "linear only" likely won't form it → 2 free
  thiols); glp1r_04/15 have **incidental** Cys pairs whose reach/engagement value survives linear (kept). **v6b** =
  v6 with glp1r_13 → clean linear `pglad_053` (`GHGKIAAYPWNYTA`, 0 Cys); `submissions/glp1r_track3_v6b.csv` md5
  `32819e6f`, validator PASS 20/0/0, diff vs v6 = one row. **v6 (`398bfb30`) byte-frozen fallback.** Upload USER-GATED.
- **2026-10-19d production-viability screen → v6b confirmed.** `scripts/prod_viability.py` scored all 20 v6b designs
  as the real construct (M+design+GFP11/TwinStrep tail; necessary-condition solubility/aggregation/protease, NOT
  agonism — GFP11 is a split-GFP expression reporter). Staple-swap doubly justified (pglad_053 ≫ dpbss_010 on every
  axis); win-path flags are expected vestibule-peptide hydrophobicity (not churnable); one watch-item
  `glp1r_20_bind`/ecd_des_8_7 (poly-Ala run 20, the forced-floor POLYRUN) — **recommend KEEP** (only structurally-novel
  binder; novelty↔expression trade low-EV/sign-uncertain; owner can swap → ecd_des_2_4 = v6c on request). Evidence
  `data/candidates/v6b_production_viability_2026-10-19.csv`. **v6b UNCHANGED.**
- **2026-10-19e owner "go ahead" → v6c built + ordering recommendation.** (A) **v6c** = v6b with binder slot
  glp1r_20 `ecd_des_8_7`→`ecd_des_18_5` (`submissions/glp1r_track3_v6c.csv`, md5 `643f3fe6`, PASS 20/0/0, diff vs v6b
  = one row). Fixes poly-Ala (run 20→5) BUT the full trade is net-negative: ecd_des_8_7 is the 2nd-strongest (pae
  7.03) AND only structurally-novel (maxTM 0.705) binder; ecd_des_18_5 is weaker (pae 9.55) + common (0.873).
  → **v6b composition still recommended; v6c ready if owner weights expression.** (B) **Ordering (recommended):**
  prize-tier grouping `01 02 03 04 05 06 07 08 09 10 12 13 14 15 16 21 22 | 18 19 20` (all agonism before the 3
  binders; current order has 21/22 after the binders). Do NOT order within the agonism arm (reach≠agonism = firewall).
  Materialized at the user-gated upload once composition is locked. **PICK = v6b; v6c = expression-weighted alt.**
- **2026-10-19f owner "do whatever is required to win at all costs" → FINAL package LOCKED + upload-ready.**
  Composition DECIDED = v6b. Final artifact `submissions/glp1r_track3_v6b_ranked.csv` (md5 `1571a3d4`, PASS 20/0/0)
  = v6b in prize-tier order (17 agonism, then 3 binders; no within-arm reach ordering = firewall). Selection-workflow
  rationale `docs/SUBMISSION_RATIONALE_v6b.md` (honest per-design necessary-condition evidence, firewall caveat, no
  prompt-injection). "At all costs" = maximal LEGITIMATE effort; the firewall, forbidden techniques, and USER-GATED
  upload are NOT overridden; no GPU fishing launched. **Only remaining action = the owner's USER-GATED upload.**

## 2026-10-20 — selection-prompt read (owner-directed) → cap-aware ipSAE reorder → FINAL = v6b_ranked2

Owner directed a thorough read of the published selection page (`proteinbase.com/competitions/anthropic-adaptyv-2026/selection`)
— the **actual Claude selection prompt** that recommends which Track-2/3 designs reach the wet lab (organizers
approve). Decoded from the page's JS data chunk (only the "Brief" tab renders server-side); facts saved to memory
[[adaptyv-glp1r-selection-rubric]]. Decision-critical rules: **max 10 designs/submission** (relaxable only to fill
totals), taken **from the top of our row order** "without second-guessing"; **only the first 20 designs count, in
order**; three screens = **pLDDT, ipSAE, mean Kyte-Doolittle** (no single metric decides; a failed screen never
removes a top pick); **prompt injection → whole ACCOUNT set aside** (other flags set aside only the designs); GLP1R
site = "ECD groove as a starting point; **activation may need more**" (validates the vestibule/R299 agonism arm). All
20 v6b designs pass the hard rules (10–250 aa, single_chain, no dupes, de-novo).

Three owner-approved moves executed (all firewall-clean; **same 20 sequences**, nothing re-folded for generation):
1. **Cap-aware reorder → `submissions/glp1r_track3_v6b_ranked2.csv`** (md5 `976e7e8e70c8d1cf0627666567b208bf`, PASS
   20/0/0). The old prize-tier order buried 2 of 4 R299 reachers + all RFd3/PepGLAD below the 10-cap; the new order
   front-loads all 4 reachers + all 4 agonism lineages into the top 10. Ordered by MEASURED necessary conditions
   (2-folder R299 reach, then best-pose ipSAE + seed-robustness) + lineage/novelty diversity — **NOT agonism**
   (firewall). Rank-1 = `glp1r_10` (both-fold reacher + top ipSAE 0.893, 4/4 seeds, pLDDT 71; rank-1 is
   screen-protected). `glp1r_22` at rank-10 as the structural-novelty long shot. Binders 18–20 hedge.
2. **ipSAE + pLDDT computed on all 20** (canonical `ipsae.py`, Dunbar 2025, cutoffs 10/15) by re-scoring existing
   Boltz-2 co-folds, **sequence-matched** (NOT via the stale `glp1r_track3_mapping.csv`, which maps an older
   composition). iPAE recomputed on the same best pose for coherence. Evidence
   `data/candidates/v6b_necessary_conditions_2026-10-20.csv`. Strong robust interfaces: glp1r_01/10/09/13/05/21
   (ipSAE 0.82–0.90, most/all seeds docked); binders + glp1r_15/22 weak (undocked in single-receptor co-fold).
3. **Rationale reframed** (`docs/SUBMISSION_RATIONALE_v6b.md`): removed the judge-address + "no prompt-injection"
   meta-line (injection→account-setaside risk); now neutral method+evidence data; **epitope stated explicitly**
   (vestibule/R299 agonism arm; ECD groove hedge) with evidence linked; §5 presents ipSAE (judge's own screen) + the
   2-folder R299 reach calibration; §6 the cap-aware ordering principle + refreshed per-design table.

**FINAL (as of this section) = `glp1r_track3_v6b_ranked2.csv` (md5 `976e7e8e`)** supersedes v6b_ranked (`1571a3d4`,
prize-tier; kept as a fallback). Upload remains **USER-GATED**. No GPU fishing — ipSAE was a re-score of co-folds we
already had. ipsae.py fetched from DunbrackLab/IPSAE, read in full + safety-scanned (no network/shell/exec) before
running with `-I`. *(Superseded 2026-10-20 by the v7 re-mine below.)*

## 2026-10-20 (v9 wave-2) — full BoltzGen re-mine → TWO independent robust reachers → seat both → FINAL = v9

Owner ("Go ahead with optional /ultrathink", then "do whatever's required to win at all costs"): re-mined the
**1,220 un-submitted eligible BoltzGen designs** — the complete remaining de-novo frontier — in-mandate (scoring
existing de-novo seqs; no new generation / no env setup; Chai SEQUENTIAL on gpu0 because gpu1–7 were a FOREIGN TfR1
BoltzGen job never clobbered).

**Funnel:** 1,220 Boltz-2 co-folds → 869 reach R299 on Boltz alone (71% = over-optimistic) → 100 diverse
Chai-escalation → 64 reach R299 in BOTH folders → **43 two-folder survivors**. A 5-agent adversarial-verification
workflow **CONFIRMED** these are length-confounded cousins: survival 6%→71% short→long, localized to the Chai iPAE
gate (r=−0.69; 12/12 pass at length 30 = zero discrimination at native GLP-1 length); the 43 collapse to ONE
dominant BoltzGen motif family (93–95%). Multi-seed confirmation (4 seeds × both folders, gpu0): **bg_0746** (22aa,
distinct outlier) and **bg_1170** (30aa, family archetype) both ROBUST-2F; bg_0877 borderline (2/4 Chai) rejected;
rm_0079 control re-confirmed.

**Two owner-gated decisions → v9 = seat BOTH.** (v8) AskUserQuestion → seat bg_0746 (`glp1r_24_ago` @ rank 5), drop
glp1r_22 (ipSAE 0.0, 0/2 docked). Then a relayed side-agent note flagged bg_1170 robustly reaches both central-polar
{190,364} every seed vs bg_0746's {190}; owner said "win at all costs" (delegated). Firewall-grounded call: central
-polar count is a necessary-condition proxy (NOT agonism) and bg_1170's extra 364 is plausibly length-confounded, so
bg_1170 was not seated *for* its cp count — but since bg_0746 and bg_1170 are **two independent architectures**
(Jaccard ~0.017) and agonism is unrankable, P(≥1 activates) is maximized by seating both as diverse independent
shots. (v9) seat bg_1170 (`glp1r_25_ago` @ rank 6), drop glp1r_03 (EvoBind, ipSAE 0.428, non-reacher). Both
firewall-clean (0 Cys, ≤2aa overlap). v9 top-10 = 6 robust both-fold reachers across 5 generators.

**FINAL = `glp1r_track3_v9.csv` (md5 `419c57ff`, PASS 20/0/0)** + `docs/SUBMISSION_RATIONALE_v9.md`. Evidence:
`data/candidates/v9_necessary_conditions_2026-10-20.csv` + `wave2_confirmation_2026-10-20.csv` +
`wave2_funnel_2026-10-20.csv`. Fallback = v8 (`3b7d2581`, single-swap bg_0746 only) if 2 BoltzGen slots judged too
concentrated. FIREWALL INTACT — both BoltzGen seated as diverse independent shots (coverage/P(≥1)), never agonism
ranks. Upload USER-GATED.

## 2026-10-20 (v7 re-mine) — un-submitted-pool re-mine → ONE robust reacher → owner-approved swap → FINAL = v7

Owner directive ("best 20 even if it replaces nearly all, at all costs" + "re-mine first, then decide"): re-mined the
un-submitted de-novo pool with sharper activation-core filters, fully in-mandate (scoring existing de-novo seqs; no
new generation, no gated env setup; idle-GPU windows only; Chai run SEQUENTIAL on gpu0 — parallel Chai deadlocks on a
shared model-load lock).

- **Wave-1 (366 peptide-pool seqs), Boltz-2 co-fold + score:** 135 reach R299, 99 contact ≥2 central-polar
  (activation microswitch {190,240,363,364,394}); 60 strongest taken to Chai.
- **2-folder consensus (Chai-1 on all 60):** dominant signal was a NEGATIVE that VALIDATES the incumbents — Boltz and
  Chai interface confidence DIVERGE for almost all (Boltz 2.6–4 / Chai 7–16 = the folder-artifact wall, same one
  BoltzGen's deep-inserters died on). Only **rm_0079** showed native-comparable Chai iPAE (4.16; native GLP-1 4.49).
- **Multi-seed confirmation (9 candidates, 4 seeds × both folders — the exact bar incumbents cleared):** EXACTLY ONE
  survivor. **rm_0079** = ROBUST-2F — Chai 4/4 dock R299 (median iPAE 4.17), Boltz 3/4 dock (median 3.77), canonical
  ipSAE 0.799, central-polar {190,364} in EVERY Chai seed, 0 Cys, 15aa, gravy −0.6, de-novo (≤2aa incretin overlap).
  The other 8 reproduced the Boltz-confident/Chai-poor artifact and were rejected.
- **Owner-gated composition decision (AskUserQuestion → "Promote rm_0079 to top tier, drop glp1r_15"):** rm_0079 →
  `glp1r_23_ago` at **rank 4** (with robust reachers glp1r_10/21/04); weakest member glp1r_15 (ipSAE 0.012, Chai
  16.1, 2 Cys, not-robust, SAME PepGLAD lineage) removed → NO lineage/epitope diversity loss, strict
  necessary-condition + developability improvement. All 18 other sequences byte-identical; binders stay 18–20.

**FINAL = `glp1r_track3_v7.csv` (md5 `9ee8df5b`, PASS 20/0/0)** + `docs/SUBMISSION_RATIONALE_v7.md`. Evidence:
`data/candidates/v7_necessary_conditions_2026-10-20.csv` + `data/candidates/remine_confirmation_2026-10-20.csv` (the
9 multi-seed candidates + verdicts). v6b_ranked2 (`976e7e8e`) kept as fallback. FIREWALL INTACT — reach /
central-polar / ipSAE are NECESSARY conditions, never agonism ranks; only the wet cAMP/SEAP assay decides. Upload
USER-GATED; owner's click only.
