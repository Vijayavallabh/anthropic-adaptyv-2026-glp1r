# Submission dossier — de-novo GLP1R agonist (Anthropic × Adaptyv 2026, Challenge 3 / Track 3)

**Target:** human GLP1R (UniProt P43220), class B GPCR. **Win condition:** *activation* (cell-surface
GLP1R → Gαs → cAMP → CRE-SEAP), **not** binding. **Deadline:** 2026-10-25 23:59 AoE.
**Package:** `submissions/glp1r_track3.csv` — 19 designs, `name,sequence,molecule_class`, rows in our
best-first ranking. Validator: `rows=19 errors=0 warnings=0`, exit 0 (Track 3). **md5 `be5b7621447eeab3402f409bcec76c9d`** is the
submission's byte identity (stable across the packaging commit `c69dc93` and this dossier's later commit; verify by
bytes, not by commit). Private repo. **Upload is USER-GATED — not uploaded.**

## 1. Result in one line (honest)

This is a **frontier moonshot**: no standalone designed protein has ever agonized a class B GPCR, and the only
direct de-novo GLP1R-agonist precedent is a preprint cyclic peptide (Li/Bryant 2025, EvoBind, EC50 31.9 nM).
We submit a **mechanism-hedged portfolio**: 12 de-novo threading peptides (the agonism bet, LOW confidence) +
7 de-novo ECD miniprotein binders (the binding hedge, antagonist-leaning). **No in-silico score proves agonism**
— only the functional assay does; every agonism claim here is an explicitly-labeled hypothesis.

## 2. Objective priority & strategy

1. **Agonism** — plausibly drives the active state / TM6 opening (the prize).
2. **Binding** to the detergent 24–432 construct — the gate before the functional assay.
3. **Design + method novelty** — Track-3 reward and an eligibility gate.

Mechanism (from research): GLP-1 is **bipartite** — its C-terminus is the "address" (binds the ECD), its
N-terminus is the "message" (inserts into the 7TM vestibule and drives the TM6 kink). An ECD-only binder is an
antagonist by default (confirmed: Baker's de-novo GLP1R binders were antagonists/none agonized). We hedged across
S1 (vestibule-message micro/mini), S2 (two-domain), S3 (exoframe), S4 (ECD clamp control).

## 3. Key findings (the load-bearing science)

- **A folded de-novo protein cannot engage the GLP1R vestibule — confirmed 4 independent ways:** RFdiffusion-1
  binders perch on the accessible rim and floor the af2ig interface gate (pae 23.5); RFdiffusion-3 all-atom makes
  large but **lipid-facing** interfaces (circumferential wrap of the membrane-blind TM bundle); EvoBind peptide
  optimization floors at if_dist ≈ 5 Å (never inserts); and a two-domain S2 pilot made **0/24 two-site** designs
  (binders bind the convex ECD, ignore the concave vestibule). Cause is geometric and config-independent: a convex
  binder face cannot fill a concave pocket. **The deep orthosteric "message" pocket is unreachable by any folded
  de-novo design; only a flexible threading peptide even approaches it.**
- **The threading peptides DO engage the activation-critical message-reader — a signal the mean `if_dist` hides.**
  `if_dist` is a *mean* distance to the whole GLP-1 interface; it does not reveal whether a peptide reaches
  **R299** (the ECL2 arginine that reads GLP-1's His7 — the contact most tied to activation). Measuring the actual
  predicted poses across **two independent folds** (the EvoBind design pose + a fresh fixed-seed `predict_only`
  fold): **7/12 peptides place a residue within 4.5 Å of R299 in ≥1 fold, and 4/12 do so robustly in both**
  (`eb_accv_l22` ≈2.5 Å, `eb_prod_l20`, `eb_prod_l40`, `eb_accv_l14`). Independently, **AF2 spontaneously forms a
  clean intramolecular disulfide in 4/12** (`eb_prod_l24` C9–C21, `eb_accv_l22` C7–C18, `eb_prod_l32` C9–C29,
  `eb_prod_l40`): these are **self-pre-organized** in the bound state — closer to the one de-novo form that actually
  worked (the cyclic EvoBind precedent) than to floppy linear peptides. `eb_accv_l22` is the most precedent-like
  (robust R299 reach **and** clean self-disulfide). This is mechanism *plausibility*, hardened to two folds — still
  **LOW-confidence, single-engine (AF2), inactive-biased receptor; no in-silico score proves agonism** (only the
  cAMP/SEAP assay does). Table: `data/candidates/agonism_reader_engagement.csv` (`scripts/score_reader_engagement.py`).
  **The submitted row order is unchanged** — agonism is in-silico-unrankable and a 2-fold metric is too noisy to
  re-rank a portal-confirmed CSV; this is evidence, not a new ranking.
- **Binding gate = af2ig, not Boltz-2.** Boltz-2 *over-docks* this isolated, membrane-blind receptor (global
  ipTM/pTM do not separate binders from scrambles, AUC≈0.5). af2ig `pae_interaction<10` + `plddt_binder>80` +
  `rmsd<2` is the calibrated binder-vs-junk gate. It is membrane-blind, so it **cannot** gate a vestibule contact
  at all — hence the agonism arm has no valid in-silico binding gate and rests on mechanism + the wet-lab assay.
- **Shorter peptides floor best; longer ones floor worse and drift toward the natural incretins.** 14–26 aa
  peptides reach if_dist ~5.0–6.0 Å; 36–44 aa floored *worse* (6.3–7.9 Å) and converged toward incretins (one
  44-mer hit 30% id over 75% coverage → dropped on eligibility). A few CLEAN longer peptides (`accv_l36` 36-mer,
  `prod_l32`, `prod_l40` 40-mer) are nonetheless KEPT as diversity bets: agonism is in-silico-unrankable, the
  if_dist proxy is weak, and independent longer threading peptides are legitimate additional wet-lab shots. So the
  submitted win-path spans 14–40 aa / if_dist 5.0–7.1 Å, not a narrow band.
- **Structural novelty (FoldSeek vs PDB100):** the 7 ECD binders are sequence-novel but structurally common
  helical bundles (max TM 0.87–0.92; one at 0.70) → expected ~3/4 on the portal novelty axis. Peptides are too
  short for a fold-TM; their novelty is sequence-based.

## 4. The portfolio (19 designs, best-first)

Agonism peptides lead (the only win-path); ECD binders follow (competence/novelty/partial-credit hedge). All are
`molecule_class=protein` (single chain). `if_dist` (lower=better) is EvoBind's weak internal binding proxy; `pae`
is af2ig's interface error. These are **not cross-comparable** across arms.

| rank | name | internal | len | arm | binding proxy | notes |
|---|---|---|---|---|---|---|
| 1 | glp1r_01_ago | eb_prod_l24 | 24 | peptide | if_dist 5.30 | hydrophobic |
| 2 | glp1r_02_ago | eb_prod_l26 | 26 | peptide | if_dist 5.77 | **clean** |
| 3 | glp1r_03_ago | eb_accv_l36 | 36 | peptide | if_dist 6.45 | **clean** (4 Cys = potential staple) |
| 4 | glp1r_04_ago | eb_accv_l22 | 22 | peptide | if_dist 5.72 | ⚠ 100% glucagon id over cov 0.14 (3-aa coincidence) |
| 5 | glp1r_05_ago | eb_accv_l18 | 18 | peptide | if_dist 5.79 | **clean**, 0 Cys |
| 6 | glp1r_06_ago | eb_prod_l32 | 32 | peptide | if_dist 5.93 | instab>40 |
| 7 | glp1r_07_ago | eb_prod_l20 | 20 | peptide | if_dist 5.14 | oddCys(1) |
| 8 | glp1r_08_ago | eb_prod_l40 | 40 | peptide | if_dist 7.07 | ⚠ oddCys(3) liability |
| 9 | glp1r_09_ago | eb_accv_l14 | 14 | peptide | if_dist 5.04 | ⚠ 80% exendin-4 id over cov 0.36 |
| 10 | glp1r_10_ago | eb_accv_l26 | 26 | peptide | if_dist 6.27 | instab>40 |
| 11 | glp1r_11_ago | eb_accv_l20 | 20 | peptide | if_dist 5.35 | instab 123 (ProtParam; crude for peptides) |
| 12 | glp1r_12_ago | eb_prod_l14 | 14 | peptide | if_dist 5.52 | ⚠ 67% GLP-1 id over cov 0.43 |
| 13 | glp1r_13_bind | ecd_des_20_7 | 70 | ECD binder | pae 6.22 | **clean**, strongest binder, TM 0.88 |
| 14 | glp1r_14_bind | ecd_des_2_6 | 74 | ECD binder | pae 8.21 | **clean**, TM 0.91 |
| 15 | glp1r_15_bind | ecd_des_2_4 | 74 | ECD binder | pae 7.82 | **clean**, TM 0.91 |
| 16 | glp1r_16_bind | ecd_des_8_7 | 66 | ECD binder | pae 7.03 | poly-Ala (A39%), most novel TM 0.70 |
| 17 | glp1r_17_bind | ecd_des_4_3 | 64 | ECD binder | pae 8.60 | poly-Ala (A31%), TM 0.90 |
| 18 | glp1r_18_bind | ecd_des_10_6 | 77 | ECD binder | pae 7.68 | poly-Ala (A40%), TM 0.92 |
| 19 | glp1r_19_bind | ecd_des_18_5 | 76 | ECD binder | pae 9.55 | instab>40, TM 0.87 |

Per-peptide mechanism annotations (His7-reader R299 reach, self-disulfide) are in
`data/candidates/agonism_reader_engagement.csv` (see §3): `eb_accv_l22`, `eb_prod_l20`, `eb_prod_l40`,
`eb_accv_l14` robustly reach R299 in both folds; `eb_prod_l24`/`eb_accv_l22`/`eb_prod_l32`/`eb_prod_l40`
self-form a disulfide. **Row order is composite-based and deliberately unchanged** (agonism is in-silico-unrankable).

## 5. Ranking methodology (OUR internal weights — NOT the organizer's)

The organizer's scoring formula is unspecified; we did not invent it. Our disclosed composite
(`scripts/rank_portfolio.py`): `0.40·arm_prize + 0.10·binding_norm(within-arm) + 0.25·dev_score + 0.25·elig_safety`.
`arm_prize` encodes the prize priority (peptides=1, binders=0 — binding-only designs cannot win the functional
assay). `binding_norm` is deliberately low-weighted (the submitted peptides span if_dist 5.0–7.1 Å — a weak, floored proxy).
`dev_score` is graded from numeric developability; `elig_safety` is coverage-gated incretin-resemblance. Rows are
best-first; diversity cap ≤2/lineage (only the `des_2` backbone has 2 members).

## 6. Eligibility / de-novo compliance

Hard rule: no modifying GLP-1/exendin-4/semaglutide/known binders; no significant identity. Our gate
(`scripts/eligibility_check.py`): flag if local identity >30% **AND** alignment covers ≥50% of the design.
**2 designs were dropped** on this gate (a 32-mer and a 44-mer that resembled GIP over ≥50% coverage).
The 19 submitted all pass (re-run on the committed CSV: 0 flags). **Full per-peptide incretin-identity table is
GENERATED at `submissions/glp1r_track3_eligibility.csv`** (never hand-picked). **9 of 12 peptides carry raw local
id ≥50% to an incretin** and are marked `recheck`: glp1r_04 (100%/cov0.14 glucagon), glp1r_09 (80%/0.36 exendin-4),
glp1r_11 (75%/0.20 GIP), glp1r_12 (67%/0.43 GLP-1), glp1r_10 (62.5%/0.31 exendin9-39), glp1r_03 (57%/0.19),
glp1r_05 (57%/0.39), glp1r_01 (50%/0.25), glp1r_02 (50%/0.31). These are **short convergent receptor-binding
motifs, not derivations**: the pre-upload audit's decisive check found the **maximum contiguous identical run to
ANY incretin across ALL 19 designs is just 3 residues** (no 4+ verbatim graft); the elevated raw-ids are either
tiny-window Smith-Waterman artifacts or the universally-conserved incretin aromatic anchor (FIxWL/LFIEW) that any
GLP1R-vestibule peptide must converge on. EvoBind generated each peptide by blind optimization, never seeded from
an incretin. The portal's own eligibility screen uses MMseqs2 (`configs/filters.yaml`), which is insensitive to
such short motifs. **The Proteinbase portal is the authority — re-check ALL 9 `recheck` peptides there before
upload; drop/reorder ONLY what the portal actually flags (never pre-emptively drop a win-path peptide over a
3–6 residue coincidence).**

## 7. Developability

`scripts/developability.py` (unpaired Cys, low-complexity/poly-X, GRAVY, ProtParam instability). ECD binders:
3 clean (des_20_7, des_2_4, des_2_6), 3 poly-Ala (re-MPNN-able), 1 high-instability. Peptides: mostly flagged
(short unoptimized peptides are inherently less stable; ProtParam instability is crude at peptide length — see
caveat). Nothing is a hard gate; flags inform rank, not inclusion.

## 8. Honest uncertainty — what would change the picture

- **Agonism is unprovable in-silico here** and the agonism arm is LOW confidence. The peptides are precedent- and
  mechanism-motivated bets; the ECD binders will likely bind but are expected to be antagonist-leaning.
- The portfolio is a **diversity bet** across the only two viable mechanistic lineages (threading peptides, ECD
  binders); folded-vestibule and two-domain routes are closed. Only the **cAMP/SEAP assay** resolves agonism.
- **Win-path monoculture (the key residual risk, per the pre-upload audit):** the 12 agonism peptides are ALL from
  one generator (EvoBind), one topology (linear), one floored proxy — shared failure modes, so the effective number
  of independent agonism bets is well below 12. The highest-value legitimate move to raise win probability is an
  **orthogonal peptide sub-arm** from a clean-licensed generator. **This was EXECUTED 2026-10-14 (§12):**
  DiffPepBuilder (MIT + ESM-2, SE(3) diffusion — decorrelated from EvoBind/AF2) yielded orthogonal R299-engaging
  peptides at a rate comparable to the EvoBind arm (11/21 vs 7/12), refuting the earlier "monoculture is
  irreducible" claim. One honest-LOW-confidence orthogonal candidate (`glp1r_20_ago`) is staged into the free slot 20
  of an alternative 20-design submission (`glp1r_track3_v2.csv`); the conservative 19-design v1 is unchanged. Owner
  chooses v1/v2 at upload.
- **glp1r_08_ago (prod_l40)** is the weakest kept peptide (worst if_dist 7.07, 40-mer, 3 unpaired Cys); it is kept
  as a diversity bet (a free slot, win-path membership unchanged) but is the first candidate to drop if a slot is
  needed. **glp1r_18_bind** (14-residue poly-Ala run) is an owner judgment call — a harmless hedge in a free slot,
  but a minor aggregation/optics liability on a published design; drop it only if you prefer the cleaner optics.

## 9. Provenance, tools & licenses

- **RFdiffusion-1/-3** (generation), **LigandMPNN/ProteinMPNN** (sequence), **AlphaFold2 initial-guess / af2ig**
  (binder gate, CC-BY params), **EvoBind2** (peptide optimization; **CC-BY-NC** — flag on any final pick),
  **Boltz-2** (calibration only), **FoldSeek/MMseqs2** (novelty), **ProtParam/Biopython** (developability).
- Submitted sequences are published under **ODC-BY**. AF3 / Protenix-v2 / ESM-3 were kept **out** of submitted-
  design provenance. EvoBind's CC-BY-NC license governs the peptide-generation *method*; the designed sequences
  are de-novo outputs — confirm license acceptability for the competition before upload.
- Target: 6X18 chain R (active state) for the agonism reference; WT 24–432 construct model for binding.

## 10. Reproducibility

Single-sourced pipeline, all committed to the private repo (`Vijayavallabh/anthropic-adaptyv-2026-glp1r`):
`build_candidate_register.py` (joins af2ig `.sc` + EvoBind `metrics.csv` + developability + eligibility →
`data/candidates/{candidates.csv,register.md}`), `rank_portfolio.py` → `ranked.csv`, `build_submission.py` →
`submissions/glp1r_track3.csv` + mapping, `validate_submission.py` (the gate). Each stage recorded in
`progress.md`; md5 of the submission is `be5b7621447eeab3402f409bcec76c9d`.

## 11. Pre-upload checklist (USER-GATED)

- [ ] `molecule_class`: CONFIRMED on the live portal (owner's 2026-10-13 paste parsed all 19 as **"Single chain"**,
      accepted `protein`, 0 needing fixes). Low-risk; glance at the /submit dropdown once more at upload.
- [x] **Portal novelty/eligibility: CONFIRMED by owner (2026-10-13)** — all 9 `recheck` peptides in
      `submissions/glp1r_track3_eligibility.csv` (glp1r_04/09/11/12/10/03/05/01/02) are tagged **novel enough** on the
      portal (the authority); the convergent-motif reasoning held, **no drops needed**.
- [x] **EvoBind license (CC-BY-NC): CONFIRMED acceptable by owner (2026-10-13)** — covers all 12 win-path peptides.
- [ ] Confirm row order = intended ranking. **OWNER CHOICE of which file to upload (see §12):**
      **v1** = `submissions/glp1r_track3.csv` (19 designs, md5 `be5b762…`, portal-confirmed) — the conservative option;
      **v2** = `submissions/glp1r_track3_v2.csv` (20 designs, md5 `924a3080…`, +1 orthogonal agonism hedge) — adds a
      NEW design that must be novelty-re-checked on the portal. Submit the chosen file **unchanged** (bytes).
- [x] **Orthogonal-generator sub-arm: DONE (2026-10-14, §12).** DiffPepBuilder (MIT + ESM-2) probe executed; result
      = orthogonal win-path diversity IS achievable (11/21 reach R299 vs EvoBind 7/12); one honest-LOW-confidence
      candidate staged into v2 slot 20 (`glp1r_20_ago`). Not folded into v1.
- [ ] Upload is performed by the owner — never automated.

## 12. Orthogonal-generator probe — DiffPepBuilder (RESULT, 2026-10-14)

Owner-approved probe: can an ORTHOGONAL generator diversify the EvoBind win-path monoculture (§8, the audit's #1
risk)? Tool: **DiffPepBuilder** (MIT; SE(3) diffusion + ESM-2 — generation fully decorrelated from EvoBind's
AF2-gradient loop). **Provenance CLEAN:** DiffPepBuilder MIT + **ESM-2** (`fair-esm`, facebook/esm2_t33_650M_UR50D,
MIT) → ODC-BY-compatible (NOT ESM-3/ESMC). Repro: `scripts/run_diffpep.sh` (with env-fix notes),
`harvest_diffpep.py`, `diffpep_gate.py`, `diffpep_vest2_eval.py`, `diffpep_vest2_fullfold_engage.py`.

**Method:** two targets (vestibule R299 = His7 reader; ECD groove), lengths 12–24, 4 samples/length, disulfide
building on. *Target-spec gotcha:* multi-hotspot specs mis-center the crop on the hotspots' centroid; a SINGLE tight
hotspot (R299) is required (the corrected `vest2` target). 117 unique de-novo peptides → **54 pass the project's
eligibility + developability gates** (vest 36, ecd 18; 19 disulfide-capable).

**Key result** (agonism-relevance on the IDENTICAL metric used for the EvoBind arm = R299 reach on a full-receptor
AF2 fold): corrected-vestibule run → 21 clean keepers; **11/21 reach R299 (<4.5 Å) — comparable to the EvoBind
arm's 7/12.** So orthogonal win-path diversity **is achievable** — this REFINES the prior session's "EvoBind
monoculture is target-physics-irreducible" (which predated running a correct orthogonal generator; that claim was
too strong). Evidence: `data/candidates/diffpep_vest2_fullfold.csv`.

**Honest caveats:** DiffPepBuilder R299-reachers have uniformly LOW AF2 plddt (27–37), and R299-reach is
anti-correlated with plddt — **partly** a cross-method artifact (EvoBind seqs were AF2-optimized, DiffPepBuilder's
were not, so AF2 penalizes them; the geometric R299-reach is the method-fair signal) but it cannot be ruled out that
some are genuinely poorly-folded rim-perchers. **af2ig is membrane-blind** (project calibration) → it CANNOT gate a
vestibule binder, so (as for the whole agonism arm) there is no valid af2ig number for these.

**Decision** (adversarial GO/NO-GO workflow: 3 GO / 1 NO_GO + synthesis): **GO** — add ONE orthogonal agonism bet to
the free slot 20, honestly labeled LOW confidence, staged as an ALTERNATIVE (`submissions/glp1r_track3_v2.csv`, 20
designs, md5 `924a30807086c94e993b78392e9766e8`, validator rows=20 errors=0). The portal-confirmed 19-design
`glp1r_track3.csv` is UNCHANGED. Slot-20 candidate **`glp1r_20_ago = EYGAQAYETARTF`** (dpbv2_029: 13-mer, linear,
0 Cys, dev-clean; **2-fold robust R299 reach 3.86/3.92 Å**; readers 13/24 — the mechanism-complete pick). Ready swap
if the portal flags its exendin-4 short-motif id (50%/cov0.46): **`LEQIIDYLLDALYR`** (dpbv2_043: tighter R299
1.6/1.9 Å, cleaner novelty 40%/cov0.36, but 8 readers + hydrophobic). The lone NO_GO dissent (surface-trained
category-error; low-confidence padding on a moonshot arm) is recorded; it does not block a zero-displacement
free-slot diversity hedge, but its concerns ARE the honest label above. **This is a LOW-confidence diversity bet,
not a confidence bet — no in-silico score proves agonism; only the cAMP/SEAP assay does.**
