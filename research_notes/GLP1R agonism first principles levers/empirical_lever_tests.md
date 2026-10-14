# Empirical lever tests (coordinator layer, 2026-10-14)

First-principles levers generated for the GLP1R de-novo **agonist** task, then validated/killed against
the four literature notes in this folder + my own cheap experiments. Tiers: [PR] peer-reviewed ·
[pre] preprint · [HYP] hypothesis · [in-silico] prediction. **No in-silico score proves agonism; only
the cAMP/SEAP assay does** (project invariant upheld throughout).

## Lever verdicts (summary)

| Lever | Idea (cross-domain root) | Verdict | Basis |
|---|---|---|---|
| **L1** | Two-state differential: efficacy = ΔΔG(active−inactive) (MWC/ternary-complex thermodynamics) | **TEST (running)** | Strong retrospective precedent; no peptide/class-B precedent → method-qualification first |
| **L2** | Allosteric normal-mode / PRS coupling to the TM6 activation motion (elastic-network allostery) | **NO-GO (empirical)** | GLP1R TM6 activation is not a soft ENM mode (see below) |
| **L3** | De-novo two-domain (address+message) agonist with controlled register | **DOWNGRADE** | Register control for an ECD→TM-spanning single chain is unprecedented/unsolved [agent-3] |
| **L4** | His7-surrogate pharmacophore abstraction | **DROPPED** | Research agent terminated by `[bio]` classifier; also highest eligibility risk (converges on native motif) |

## L2 — NO-GO, established empirically (CPU-only, numpy ANM)

- Built the **active−inactive Cα deformation vector** (active 6X18 chain R vs inactive 6LN2 chain A,
  SVD superposition with iterative core-trim).
- **Finding 1 (failure mode avoided):** the naive whole-receptor vector is dominated by **ECD motion
  (mean 23 Å, max 35 Å)** — the extracellular domain swings between peptide-free inactive and
  peptide-bound active. That is *not* the activation signal. Restricting to the TM bundle (res 136–423)
  and superposing on the stable TM core (core-RMSD 1.26 Å) isolates the true signature:
  **max displacement 18.8 Å at residue 346 (TM6 cytoplasmic tip)** — matches the ~18 Å TM6 swing
  (Zhang 2017, [10.1038/nature22394] [PR]).
- **Finding 2 (the NO-GO):** a Cα-ANM of the active TM domain (Rc=15 Å; 6 rigid-body modes ~1e-15 = correct)
  does **not** encode activation as a soft mode. Best single nontrivial mode overlap with the activation
  vector = **0.26**; cumulative overlap = 0.10 (1 mode), 0.52 (10 modes), 0.69 (50 modes).
- **Mechanistic reason [HYP, grounded]:** class B activation is a *localized TM6 kink at PxxG*, not a
  global breathing mode, so ENM/PRS (which excels at global-soft-mode allostery; agent-2 note) is the
  wrong physics here. Consistent with agent-2's literature finding that *no* ENM activation study exists
  for any class B receptor and "no single soft mode reproduces the full inactive→active path."
- **Decision:** dropped L2 before the (gated) ProDy install. The mandatory sanity check did its job.

## L1 — two-state differential (TEST; method-qualification on controls)

- **Theory [PR]:** intrinsic efficacy = differential stabilization of active (R*) vs inactive (R):
  ΔΔG_eff = G_bind(R*) − G_bind(R) (ternary-complex / MWC / operational model; efficacy_thermodynamics note).
  Agonist ΔΔG_eff ≪ 0; neutral antagonist ≈ 0 (binds both states — the crisp binding≠activation case).
- **Precedent:** active−inactive *docking* differential classifies agonist/blocker on β2AR at AUC 0.98
  (Costanzi & Vilar, PMC3265623 [PR]); A2A FEP ΔΔG(R*−R) matched Δ-efficacy ~70% (Jespers 2021 [PR]);
  two-state FE sims *prospectively* produced novel partial agonists (Panel 2023 [PR]). **No precedent for
  peptides or class B** → first run is **method-qualification**, trusted only if control bands separate.
- **Templates (fetched to data/raw/):** active = **6X18** (chain R, WT-like); inactive = **6LN2** (chain A,
  full-length, NAM-bound) + 5VEW (TMD) as backup. Note: both inactive structures carry **A346** where
  active 6X18 has **K346** — a thermostabilizing mutation at the TM6 hinge (now disclosed via structure).
- **Method:** Boltz-2 (2.2.1) template-FORCED co-fold of each ligand against active (6X18, template_id F)
  and inactive (6LN2, template_id A) — `force: true, threshold: 5.0`, receptor query = construct_24_432 (409 aa),
  msa empty. Differential of interface confidence (cheap first pass; MM/GBSA ΔΔG is the principled escalation
  per efficacy note). **Controls:** GLP-1(7-36)/exendin-4 (agonist, expect ΔΔ≪0), exendin(9-39) (antagonist,
  expect ≈0), scramble (expect ≈0). A rim-binding ECD antagonist from the portfolio is the critical 5th
  control to add (binds both states, ΔΔ≈0 — separates binder from agonist).
- **RESULT (2026-10-14): NO-GO on method-qualification.** 8 forced co-folds (4 controls × 2 states, GPU 0).
  Interface-iptm differential (act−ina): GLP1_7_36 **+0.648**, exendin_4 **+0.621**, **exendin_9_39 (antagonist) +0.735**,
  scr_s0 (scramble) **+0.417**. Agonist mean +0.634 vs non-agonist +0.576 → gap +0.058 (noise at n=1). The metric
  ranks by **binding strength, not agonism**: the orthosteric **antagonist scored HIGHEST**, the weak-binding
  scramble lowest — the exact binding≠activation confound. Forcing *did* produce distinct states (act-vs-ina
  receptor fold RMSD 23–28 Å), so this is a genuine method failure, not a setup artifact. Structural reason:
  the only available inactive templates are NAM-occluded (6LN2/5VEW), so every orthosteric peptide fits the
  better-formed active pocket; and a global interface-confidence differential cannot read the TM6-drive that
  defines agonism. **Not escalating to MM/GBSA** — same occluded-pocket + no-activation-readout cause would
  recur; cost unjustified; result confirms (does not contradict) the agonism-unprovable-in-silico prior.
- **Net:** both two-state scoring (L1) and normal-mode allostery (L2) fail to rank class-B agonism in-silico.
  The firewall holds. See [[lesson-glp1r-agonism-insilico-rankers-fail]].

## Tool-provenance finding (affects the staged, user-gated submission)

- **EvoBind** (generator of the top-12 agonism arm in v1/v2): **no LICENSE file in third_party/EvoBind**
  (first-hand); agent-3 reports the published protocol is **CC-BY-NC**. Conflicts with the AGENTS.md
  invariant to keep submitted-design provenance permissive (ODC-BY release). Legal gray area
  (sequences-as-data vs code license), not a certainty — flagged for the owner's gated-submission decision.
- **Clean alternatives installed:** DiffPepBuilder (**MIT**, confirmed first-hand; the v2 slot-20 generator)
  and RFdiffusion (BSD). A license-clean agonism arm ranked by L1 is a available de-risking hedge.

## Cited literature notes in this folder
- `inactive_templates_two_state_scoring.md` — inactive templates + two-state scoring precedent
- `allosteric_normal_mode_ranking.md` — ENM/PRS methods (L2)
- `conformational_selective_two_domain_sota.md` — state-selective/two-domain SOTA + EvoBind/license (L3)
- `efficacy_thermodynamics_mwc.md` — MWC/ternary-complex → ΔΔG_eff estimator (L1)
- (pharmacophore note intentionally absent — L4 dropped on `[bio]` classifier)
