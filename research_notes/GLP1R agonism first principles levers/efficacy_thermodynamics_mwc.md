# Statistical-Mechanics / Thermodynamic Formalism of GPCR Agonist Efficacy → a Computable Two-State Design Score

> Scope: the abstract-physics grounding for ranking de novo human GLP1R (P43220, class B1) agonist candidates
> by a physics-grounded, computable quantity. Ground truth per project invariants: **no in-silico score proves
> agonism; only the cAMP/SEAP assay does.** This note supplies theory + a feasible estimator, not a proof.
>
> **Tier tags:** `[PR]` peer-reviewed · `[pre]` preprint (not peer-reviewed) · `[HYP]` hypothesis / aspirational
> proposal · `[in-silico]` computational result. Tags combine (e.g. `[PR, in-silico]`).
>
> **Through-line (enforced):** BINDING ≠ ACTIVATION ≠ OBSERVED RESPONSE. Affinity is ΔG of forming a complex;
> intrinsic efficacy is the *differential* affinity between the active (R*) and inactive (R) receptor states;
> observed Emax additionally depends on receptor density and transducer coupling (system-dependent). Every proxy
> below estimates intrinsic efficacy at best, never the assay readout.
>
> Source attribution: classic pharmacology citations and some method papers were retrieved via PubMed; per
> PubMed terms, DOIs are included as links where PubMed returned them.

---

## Key Question 1 — Formalize efficacy (ternary / extended / cubic ternary + MWC two-state); map intrinsic efficacy to ΔΔG_bind(R*−R); assumptions and where it breaks

### Takeaway
Classical receptor theory converges on one statement: **intrinsic (molecular) efficacy is the ligand's preference
for the active receptor state over the inactive one.** In two-state / extended-ternary terms this is exactly a
differential binding free energy, `ΔΔG_eff ≡ ΔG_bind(R*) − ΔG_bind(R)` (equivalently the affinity ratio
`α = K_d(R)/K_d(R*) = exp(−ΔΔG_eff/RT)`): agonist ⇒ ΔΔG_eff < 0 (α > 1); neutral antagonist ⇒ ΔΔG_eff ≈ 0
(α ≈ 1, binds without shifting the equilibrium); inverse agonist ⇒ ΔΔG_eff > 0. This is rigorous *equilibrium*
theory and breaks for kinetics, receptor reserve/coupling, and biased/multi-state agonism.

### Cited Findings — the primary receptor-theory lineage

- **Ternary complex model (TCM), De Lean, Stadel & Lefkowitz 1980** — the empirical seed. Agonist binding to the
  β-adrenergic receptor shows two affinity states; the data are fit by H + R + X ⇌ HRX, where X (the G protein /
  nucleotide site) forms a high-affinity ternary complex. Critically: *"the intrinsic activity of the agonist is
  correlated significantly with the affinity constant L of the component X for the binary complex HR"* — i.e.
  **efficacy already maps to a differential (agonist-promoted) affinity for the transducer-coupled state.**
  J Biol Chem 255:7108–7117 — [PubMed 6248546](https://pubmed.ncbi.nlm.nih.gov/6248546/). `[PR]`
- **MWC two-state allosteric model, Monod, Wyman & Changeux 1965** — the statistical-mechanics parent: a protein
  pre-exists in two conformations (T/R here ≙ R/R*) with an equilibrium constant L; ligand binds both but with
  different affinity, and binding *shifts the population* toward the higher-affinity state. The receptor "two-state"
  model is MWC applied to a single protomer. J Mol Biol 12:88–118 —
  [DOI 10.1016/s0022-2836(65)80285-6](https://doi.org/10.1016/s0022-2836(65)80285-6). `[PR]`
- **Operational model of agonism, Black & Leff 1983** — defines efficacy operationally as the **transducer ratio
  τ = [R₀]/K_E** (receptor density over the coupling constant) and gives *"a chemical definition of intrinsic
  efficacy making this parameter experimentally accessible in principle."* Key point for us: the *observed* agonism
  (Emax, via τ) explicitly mixes a **ligand term (intrinsic efficacy)** with **system terms (receptor density,
  coupling)** — so a molecular score can only target the ligand term. Proc R Soc Lond B 220:141–162 —
  [DOI 10.1098/rspb.1983.0093](https://doi.org/10.1098/rspb.1983.0093). `[PR]`
- **Extended ternary complex model (ETCM), Samama, Cotecchia, Costa & Lefkowitz 1993** — adds an explicit
  **R ⇌ R\*** isomerization (needed to explain constitutively active mutants). Core result: *"agonists stabilize
  R\* while inverse agonists stabilize R"*; the constitutively active β2AR mutant shows higher agonist (not
  antagonist) affinity even without G protein — i.e. agonist affinity tracks the R* population. J Biol Chem
  268:4625–4636, 1993 — [Wikidata Q34726898](https://wikidp.org/wiki/Q34726898) (bibliographic record);
  model summarized in [PharmRev review](https://pharmrev.aspetjournals.org/content/57/2/147). `[PR]`
- **Cubic ternary complex model (CTC), Weiss, Morgan, Lutz & Kenakin 1996 (J Theor Biol, 3 papers)** — the
  thermodynamically complete equilibrium model: G protein may bind *both* R and R*, giving 8 species on the
  vertices of a cube; it is a "saturated three-factor log-linear model." **Paper III explicitly reframes efficacy
  as the distribution of receptor species, distinguishing "potential efficacy (a vector)" from "realized efficacy
  (a scalar)"** — the formal warning that a single scalar ΔΔG cannot capture pathway-selective (biased) efficacy.
  Paper I: J Theor Biol 178:151–167 ([Duke record](https://scholars.duke.edu/publication/1268792)); Paper III:
  181:381–397 [DOI 10.1006/jtbi.1996.0139](https://doi.org/10.1006/jtbi.1996.0139). `[PR]`
- **Two-state model of receptor activation, Leff 1995** — the clean modern statement for both GPCRs and
  ligand-gated channels: activation = a conformational change R⇌R*; **a ligand's efficacy is set by its
  *differential* affinity for the active vs resting state.** Trends Pharmacol Sci 16:89–97 —
  [DOI 10.1016/s0165-6147(00)88989-0](https://doi.org/10.1016/s0165-6147(00)88989-0). `[PR]`

### Inferences — the thermodynamic identity (the quantity to compute)

- **Derivation (standard thermodynamic cycle / Wyman linkage; state-function closure).** For the two-state receptor
  with ligand A, build the square:
  `R —(bind A, ΔG_bind(R))→ AR` ; `R* —(bind A, ΔG_bind(R*))→ AR*` ; `R —(activate, ΔG_act^apo)→ R*` ;
  `AR —(activate, ΔG_act^holo)→ AR*`. Because free energy is a state function the cycle closes:
  **`ΔG_act^holo − ΔG_act^apo = ΔG_bind(R*) − ΔG_bind(R) ≡ ΔΔG_eff`.**
  In words: **the free-energy shift a ligand imposes on the activation equilibrium equals its differential binding
  free energy between the two states.** This is *the* link between a bindable quantity and an activation quantity,
  and it is what makes "differential stabilization of the active state" computable. `[PR]`-grounded (it is the ETCM /
  two-state model expressed as a cycle; the linkage logic is Wyman's — see Q4).
- **Design score:** define `ΔΔG_eff = ΔG_bind(R*) − ΔG_bind(R)`. More negative ⇒ stronger R*-stabilization ⇒ more
  agonist-like. Equivalent ratio form `α = K_d(R)/K_d(R*) = exp(−ΔΔG_eff/RT)`; intrinsic efficacy ∝ `ln α =
  −ΔΔG_eff/RT`. Agonist α>1; neutral antagonist α≈1 (binds both states equally — it *has affinity but no efficacy*,
  the sharpest statement of binding≠activation); inverse agonist α<1.
- **GLP1R-specific reading (class B1).** Activation requires the peptide **N-terminal "message" inserting into the
  reorganized 7TM pocket that exists only in R*** (TM6 sharp kink out, central polar network engaged). A ligand that
  only contacts the ECD / vestibule rim binds R and R* almost identically (ΔΔG_eff ≈ 0) → it is an **antagonist by
  construction** — matching the project's observed "folded de-novo binder perches on the rim = antagonist-leaning"
  and Baker's de-novo GLP1R binders being antagonists. So for peptides, ΔΔG_eff is dominated by whether the N-terminus
  makes the **R\*-only core contacts**. This is why the score must be computed on *two* templates, not one.

### Gaps
- The exact closed-form `ΔG_act^holo − ΔG_act^apo = ΔΔG_eff` identity is textbook thermodynamics; I did not locate a
  single canonical paper that writes it in this notation (it is implicit in ETCM/Leff and in Wyman linkage). I
  present it as a derivation, not a quoted result. The Samama 1993 and CTC 1996 primary PDFs were accessed only via
  secondary bibliographic/review records (not full text), so exact equation numbers are not quoted.

---

## Key Question 2 — Computable proxies for ΔΔG_bind(R*−R): cost, accuracy, GPCR precedent, feasibility (uv/https, 1–4 H100, ~1 week)

### Takeaway
Four proxy tiers exist. **FEP/TI between states is the only one with published prospective GPCR validation**, but for
30–39-residue de novo peptides whole-ligand absolute-FEP is effectively intractable at portfolio scale. **Endpoint
MM/GBSA ΔΔG on two co-folded/relaxed templates is the pragmatic, scalable choice** (differencing cancels much
systematic error), though its two-state *efficacy* precedent is thinner than its affinity precedent. **Co-folder
interface-confidence differentials are the cheapest and already in-pipeline, but have no validated efficacy precedent
— they are a mechanism-consistency heuristic, not a calibrated ΔG.** Docking-score differentials are too crude for
peptides.

### Cited Findings — by proxy

**(A) FEP / TI (absolute or thermodynamic-cycle) between R* and R — most rigorous, most expensive**
- Schrödinger ABFEP study (Vögele, Zhang, Kaindl, Wang 2023, `[pre]`): absolute binding FEP on ligands bound to the
  **active and inactive states of 8 GPCRs + 1 nuclear receptor**; comparing the two binding free energies classifies
  agonist vs antagonist with *"very high"/"unprecedented" accuracy*; **"carefully designed restraints are often
  needed to model the conformational ensembles of each state."* The same group states the routinely calculated
  single-state binding free energy *"is a good affinity predictor but may not always predict efficacy"* — the explicit
  binding≠efficacy caveat. ChemRxiv:
  [article 65136d47…](https://chemrxiv.org/engage/chemrxiv/article-details/65136d470065940912f124c8);
  [Figshare copy](https://figshare.com/articles/journal_contribution/Is_the_Functional_Response_of_a_Receptor_Determined_by_the_Thermodynamics_of_Ligand_Binding_/24534663).
  (Exact accuracy % not disclosed in the public abstract/webinar — see Gaps; and the authors sell the FEP software, a
  conflict to note.)
- A2A adenosine receptor, Jespers et al. 2021 `[PR, in-silico]`: FEP **thermodynamic cycles that compare ligand
  binding free energy in an active-like (R\*) vs inactive (R) structure** (does *not* simulate the transition).
  **Qualitative correlation between calculated ΔΔG and experimental Δ-efficacy achieved in "up to 70% of the pair
  comparisons."** Captured mutations: constitutively-inactive T88A predicted to destabilize R* by **~3.98 kcal/mol**;
  for LUF5834+T88A calc −0.23 vs exp −0.13 kcal/mol on EC50. Explicitly separates affinity from efficacy ("there is
  no experimental data for the conformational affinity," modeled computationally). PLoS Comput Biol 17(11):e1009152 —
  [DOI 10.1371/journal.pcbi.1009152](https://doi.org/10.1371/journal.pcbi.1009152). `[PR, in-silico]`
- Relative-FEP affinity benchmark on 8 GPCRs (context for FEP *affinity* accuracy, not efficacy): avg R²≈0.61,
  RMSE≈0.94 kcal/mol `[pre, in-silico]` —
  [ChemRxiv 6507f6cb…](https://chemrxiv.org/engage/chemrxiv/article-details/6507f6cbb6ab98a41ca60e26).
- **Cost/feasibility:** per-ligand ABFEP with state restraints = tens–hundreds of GPU-hours for a *small molecule*;
  a 30–39-mer peptide decoupling/restraint network is far larger and not standard practice — **at most 1–3 control
  ligands feasible in a week, not a 20–200 portfolio.** Relative FEP needs a congeneric series + atom mapping →
  **not applicable to diverse de novo peptides.** Software (OpenMM/pmx/FEP+) runs under uv; no network needed at run
  time. Verdict: **gold standard for a few controls; not the ranker.**

**(B) Endpoint MM/GBSA (or MM-PBSA) on R* vs R — cheap, scalable, the pragmatic ranker**
- GPCR two-state precedent, dopamine D2, 2018 `[PR, in-silico]`: MM/GBSA on **active (D2HighR) vs inactive (D2LowR)**
  models; binding enthalpies **favored the active state, agreeing with measured D2High selectivity**; state-specific
  key residues identified. (Specific DOI/URL not captured in search — minor citation gap; finding from
  [WebSearch synthesis].)
- GPCR, CB1/CB2 `[PR, in-silico]`: MM-GBSA free energies correlated with experiment **better than docking**
  (R²≈0.60 vs 0.37) — [ACS Figshare SI](https://acs.figshare.com/articles/Prediction_of_the_Binding_Affinities_and_Selectivity_for_CB1_and_CB2_Ligands_Using_Homology_Modeling_Molecular_Docking_Molecular_Dynamics_Simulations_and_MM-PBSA_Binding_Free_Energy_Calculations/12061443).
- Nuclear receptor REV-ERBα/NCoR `[PR, in-silico]`: MD + MM-PBSA ranked 35 agonists by potency retrospectively and
  prospectively (4 prospectively ranked compounds confirmed) — [DOI 10.1007/s10822-017-0040-7](https://doi.org/10.1007/s10822-017-0040-7).
  (Potency ranking, *not* a two-state efficacy test.)
- **Accuracy/caveats:** MM/GBSA ΔG–experiment correlation is *"highly case-specific"* (excellent→poor); it neglects
  configurational entropy; a method review notes **FEP is generally more capable than MM/GBSA** at picking active
  ligands/correct poses ([Frontiers Pharmacol benchmark](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2022.1018351/full)).
  **Mitigation specific to us:** the *same-ligand two-state difference* ΔΔG = GBSA(R*) − GBSA(R) cancels large
  systematic terms (ligand internal energy, many receptor self-terms) — the differential is more trustworthy than
  either endpoint, which is the same logic that makes the FEP cycles in Jespers/Panel work.
- **Cost/feasibility:** short restrained MD relaxation (OpenMM, Amber ff14SB/ff19SB, implicit GB; per project memory
  prefer **OpenCL over CUDA** to dodge nvrtc drift) + endpoint MM/GBSA = minutes–low hours per complex on one H100.
  **20–200 complexes × 2 states × a few poses is comfortably a few GPU-days on 1–4 H100.** Runs offline under uv.
  Verdict: **this is the ranker.**

**(C) Co-folder interface-confidence differentials (Boltz-2 / af2ig / AF3 ipTM, ipSAE, interface-PAE) on R* vs R —
cheapest, in-pipeline, but NOT a calibrated energy**
- AlphaFold2 can be coaxed to sample both GPCR states by **shallow-MSA subsampling** (del Alamo et al. 2022):
  models at the extremes of the conformational distribution were among the most accurate (avg TM-score **0.94**);
  teal/orange = similarity to inactive/active experimental GPCR structures. eLife 11:e75751 —
  [DOI 10.7554/eLife.75751](https://doi.org/10.7554/eLife.75751). `[PR, in-silico]` — this supports *building both
  state models*, **not** that confidence predicts efficacy.
- **No validated precedent** that co-fold interface confidence (ipTM/ipSAE/iPAE) tracks agonist efficacy. Co-folders
  are trained to reproduce deposited complexes (heavily agonist/active-biased), ignore the membrane and explicit
  energetics, and report "does a plausible complex exist," not ΔG. Treat **Δconfidence(R*−R) as a mechanism-consistency
  signal, not an efficacy energy.** `[HYP]`
- **Cost/feasibility:** trivial — already running for binding; hours for 100s of peptides on 1–4 H100.
  Verdict: **orthogonal gate + pose source for (B), not a standalone efficacy score.**

**(D) Docking-score differentials — too crude for 30+mer peptides**
- Docking scores are unreliable absolute energies; peptide docking of 30–39-mers is itself unreliable; only useful as
  a coarse pre-filter. No GPCR efficacy precedent worth citing. Verdict: **skip beyond pre-filtering.**

### Inferences
- The feasible stack for *this week* is **(C) to generate/screen two-state poses → (B) MM/GBSA to score the
  differential → (A) reserved for 1–3 controls as a sanity anchor.** This mirrors the published hierarchy (FEP most
  accurate but costly; MM/GBSA scalable; confidence cheapest/least validated).

### Gaps
- Exact ABFEP agonist/antagonist classification **accuracy %, ligand count, per-receptor breakdown** are not in the
  public preprint abstract or the (image-only) Schrödinger webinar PDF; the peer-reviewed version was not located.
- The D2 two-state MM/GBSA study's precise DOI/URL was not captured (appeared only in search synthesis).
- No peptide-ligand (vs small-molecule) two-state FEP/MM-GBSA GPCR benchmark was found — all precedent is
  small-molecule; peptide performance is unquantified (relevant risk for GLP1R).

---

## Key Question 3 — Precedent for predicting agonist-vs-antagonist / efficacy RANK from a two-state binding-free-energy differential (any receptor)

### Takeaway
**Yes — this is an established, validated idea for GPCRs and nuclear receptors, including one prospective
design-and-synthesis success.** Accuracy is good but imperfect (A2A: ~70% of pairwise efficacy comparisons correct;
β2AR: prospective nM partial agonists delivered), and it is demonstrated almost entirely on small molecules.

### Cited Findings
- **β2-adrenoceptor, prospective (strongest precedent), Panel et al. 2023** `[PR, in-silico+exp]`: MD free-energy
  simulations of β2AR in **active and inactive conformations**; known ligands were grouped by efficacy using the
  **calculated shift in ligand affinity upon activation**, then the method **predicted and synthesized a new series →
  partial agonists with nanomolar potencies and novel scaffolds.** This is a genuine prospective validation that a
  two-state affinity differential designs efficacy. Angew Chem Int Ed 62(22):e202218959 —
  [DOI 10.1002/anie.202218959](https://doi.org/10.1002/anie.202218959).
- **A2A adenosine receptor, Jespers et al. 2021** `[PR, in-silico]`: ΔΔG(R*−R) from FEP cycles correlates with
  Δ-efficacy in **up to 70% of pair comparisons**; ribose agonists (NECA ΔΔG ≈ 2× adenosine, matching efficacy rank);
  constitutively-inactive **T88A destabilizes R* by ~3.98 kcal/mol** — [DOI 10.1371/journal.pcbi.1009152](https://doi.org/10.1371/journal.pcbi.1009152).
- **8 GPCRs + 1 nuclear receptor, Vögele et al. 2023** `[pre, in-silico]`: ABFEP active-vs-inactive differential
  classifies agonist/antagonist with *"very high"* accuracy — [ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/65136d470065940912f124c8)
  (exact numbers undisclosed; commercial authorship).
- **β2AR, population-shift validation, Fleetwood, Carlsson & Delemotte 2021** `[PR, in-silico]`: free-energy landscapes
  for 6 ligands; **microswitch expectation values correlate with experimental cAMP Emax** (TM5-bulge R=−0.95,
  connector R=0.93, Y-Y R=−0.75); partial/full agonists shift toward active-like states vs antagonists/inverse
  agonists; **ΔG between active and inactive basins "gave similar results"** to the microswitch readout. eLife
  10:e60715 — [DOI 10.7554/eLife.60715](https://doi.org/10.7554/eLife.60715). (n≈6 ligands → low statistical power.)
- **Dopamine D2, MM/GBSA two-state** `[PR, in-silico]`: active-vs-inactive MM/GBSA matched D2High selectivity (see Q2;
  DOI not captured).
- **Historical "thermodynamic discrimination"** `[PR]`: radioligand studies (adrenergic/adenosine/nicotinic) proposed
  agonists vs antagonists differ in enthalpy- vs entropy-driven binding — a *binding-thermodynamics* (not structural
  two-state) efficacy signal; older and debated — [Bentham Curr Top Med Chem entry](https://www.benthamscience.com/article/25262).

### Inferences
- The two-state ΔΔG differential is **the most directly validated physics-grounded efficacy predictor available**, and
  Panel 2023 shows it is actionable for *design*, not just classification. Expected realistic performance: a useful
  *rank/sign* signal (agonist-leaning vs antagonist-leaning), **not** a quantitative Emax — consistent with the
  project's "gate a credible active-state binder, don't claim agonism" posture.
- All precedent is small-molecule; **extrapolation to 30–39-mer peptides at a class-B 7TM core is unproven** and is
  the central uncertainty.

### Gaps
- No two-state efficacy prediction precedent specifically for **peptide** agonists or for **class B** GPCRs (GLP1R
  included) was found.
- Prospective accuracy as a clean percentage exists only indirectly (A2A pairwise 70%; β2AR = "delivered nM partial
  agonists" rather than a benchmarked rate).

---

## Key Question 4 — Abstract-physics framings to borrow; tractable vs aspirational

### Takeaway
The **free-energy-landscape / conformational-population-shift** picture is the correct abstraction and its
*two-endpoint* reduction (= the ΔΔG_eff we compute) is tractable this week. **Wyman linkage** supplies the exact
theoretical justification (cheap — it's algebra, not simulation). **Full free-energy landscapes, Markov State Models,
and information-theoretic allosteric-coupling measures are physically ideal but far too expensive** for ranking 20–200
candidates (they are ms-scale, per-ligand, one-receptor efforts).

### Cited Findings
- **Conformational-ensemble / population-shift view** `[PR, in-silico]`: efficacy = ligand-induced shift of the
  receptor population toward R*. Fleetwood 2021 operationalized this with string-method-with-swarms free-energy
  landscapes and showed the shift correlates with cAMP — [DOI 10.7554/eLife.60715](https://doi.org/10.7554/eLife.60715).
  **Tractable reduction:** our ΔΔG_eff is exactly the two-endpoint summary of this landscape.
- **Markov State Models of activation (aspirational)** `[PR, in-silico]`: Kohlhoff et al. 2014 built a β2AR activation
  MSM from **~2 ms aggregate simulation on Google Exacycle** with adaptive sampling; found multiple activation
  pathways through metastable intermediates. Nat Chem 6:15–21 —
  [DOI 10.1038/nchem.1821](https://doi.org/10.1038/nchem.1821);
  [Stanford record](https://purl.stanford.edu/vp873ky1987). **Cost verdict: definitively too expensive** — ms sampling
  per receptor, one system at a time; cannot rank a portfolio.
- **Linkage / allostery thermodynamics (Wyman)** `[PR]`: linked-functions theory (Wyman, 1948/1964; Wyman & Gill,
  *Binding and Linkage*, 1990) states that when two processes (ligand binding and the R⇌R* conformational change) are
  coupled, the effect of one on the other is reciprocal and equal — this *is* the ΔΔG_eff = activation-shift identity
  in Q1. Validated historically by the Bohr effect (quantitatively predicted). Background:
  [NAS biographical memoir, Wyman](https://www.nasonline.org/wp-content/uploads/2024/06/wyman-jeffries-1.pdf);
  [MWC/linkage notes](https://web02.gonzaga.edu/faculty/cronk/CHEM245pub/MWC.html). **Tractable: it's the justification,
  not a computation.**
- **Information-theoretic / population measures** `[PR, in-silico]`: Fleetwood used **KL divergence** between apo and
  holo ensembles (plus random-forest classifiers) to identify the microswitches that discriminate efficacy —
  [DOI 10.7554/eLife.60715](https://doi.org/10.7554/eLife.60715). Mutual-information allosteric-coupling analyses exist
  broadly but **require converged ensembles** → **aspirational** at portfolio scale; usable only as post-hoc analysis
  of the few trajectories we can afford.
- **Multi-state reality (why a scalar landscape is incomplete)** `[PR]`: a β2AR allosteric-nanobody study found that
  **17 ligands of varying efficacy require ≥3 receptor states** to explain — [DOI 10.1038/nature18636](https://doi.org/10.1038/nature18636);
  CTC Paper III calls efficacy a *vector* ([DOI 10.1006/jtbi.1996.0139](https://doi.org/10.1006/jtbi.1996.0139)).

### Inferences
- **Borrow:** the population-shift abstraction (reduced to two-endpoint ΔΔG_eff) + Wyman linkage as justification +
  KL/population framing only as *interpretation* of controls.
- **Don't attempt:** MSMs, full free-energy landscapes, or converged mutual-information coupling for ranking — all are
  ms-scale per system and blow the 1-week / 1–4-H100 budget.
- For GLP1R we only need **Gs-coupled cAMP agonism**, so collapsing to a single "active Gs-competent state" (6X18) is
  acceptable; biased/multi-state efficacy is explicitly **out of scope** (and un-rankable by a single ΔΔG anyway).

### Gaps
- No tractable, validated information-theoretic efficacy *ranking* method exists; all require ensembles we cannot
  afford for 20–200 candidates.

---

## Key Question 5 — Concrete recommended estimator (cheap two-state efficacy proxy for ~20–200 peptide–receptor complexes this week)

### Takeaway
Compute **`ΔΔG_eff = ΔG_bind(R*) − ΔG_bind(R)`** by co-folding each peptide onto an **active (R\*) and an inactive (R)
GLP1R template**, relaxing with short restrained implicit-solvent MD, and taking the **same-ligand MM/GBSA
difference**; report it alongside an orthogonal **co-fold confidence differential** and **R\*-only mechanistic contact
readouts**, all **calibrated against controls** (not absolute cutoffs). Rank by ΔΔG_eff, gate on mechanism, and state
plainly it is an intrinsic-efficacy *proxy*.

### Templates (build once)
- **R\* (active):** GLP1R from **PDB 6X18** — GLP-1(7-36)NH2 · GLP1R · Gs · Nb35, cryo-EM 2.10 Å, the project's active
  template (Zhang, Belousoff, Zhao et al. 2020, Mol Cell 80:485 —
  [DOI 10.1016/j.molcel.2020.09.020](https://doi.org/10.1016/j.molcel.2020.09.020);
  [RCSB 6X18](https://www.rcsb.org/structure/6X18)). Cross-check with 7DUR (Cong et al. 2021, Nat Commun —
  [DOI 10.1038/s41467-021-24058-z](https://doi.org/10.1038/s41467-021-24058-z)) and 5VAI (Zhang et al. 2017, Nature —
  [DOI 10.1038/nature22394](https://doi.org/10.1038/nature22394)).
- **R (inactive):** build from **PDB 5VEW / 5VEX** — GLP1R **7TM domain** bound to negative allosteric modulators
  (inactive conformation; TM6 intracellular tip restrained) (Song et al. 2017, Nature 546:312–315 —
  [DOI 10.1038/nature22378](https://doi.org/10.1038/nature22378); [RCSB 5VEW](https://www.rcsb.org/structure/5VEW)).
  **Caveat (weak link):** 5VEW is TMD-only (no ECD), NAM-bound and thermostabilized → may be an over-stabilized,
  non-physiological "very inactive" state. Mitigate by also using a **shallow-MSA AlphaFold2 inactive model**
  (del Alamo 2022 protocol, [DOI 10.7554/eLife.75751](https://doi.org/10.7554/eLife.75751)) and/or grafting the active
  ECD onto the inactive 7TM; **report ΔΔG_eff sensitivity across ≥2 inactive references.**
- **Separation of scores (project invariant):** ΔΔG_eff is the **agonism/activation** proxy (scored against the WT
  active state, never the thermostabilized construct). Keep the **binding-gate** score (vs the apo/WT `24–432` model)
  entirely separate; **demerit off-state-only binders.**

### Pipeline (per peptide; 20–200 peptides)
1. **Two-state co-fold.** Co-fold the peptide onto R* and onto R with the in-pipeline co-folder(s) (Boltz-2 and/or
   af2ig), biasing the receptor to each state via templating / shallow-MSA. Generate ≥5 seeds/poses per state.
   (`[HYP]` that confidence predicts efficacy — use poses + Δconfidence as signal, not as the energy.)
2. **Relax.** Short restrained MD / minimization in **OpenMM** (ff14SB/ff19SB; implicit GB, ideally an implicit-membrane
   slab; heavy-atom restraints on receptor backbone to preserve the templated state). Per project env memory, **try
   OpenCL before CUDA** (nvrtc drift). Runs offline under uv.
3. **Score each state.** Endpoint **MM/GBSA** ΔG_bind(peptide↔receptor) on R* and on R; average over seeds/poses →
   report **mean ± SEM** per state.
4. **Differential.** `ΔΔG_eff = ΔG_bind(R*) − ΔG_bind(R)` (more negative = more agonist-like). The same-ligand
   difference cancels much systematic MM/GBSA error (the Jespers/Panel cycle logic).

### Quantities to report (per candidate)
- `ΔG_bind(R*)`, `ΔG_bind(R)`, **`ΔΔG_eff` ± SEM** (primary rank key), and `α = exp(−ΔΔG_eff/RT)`.
- **Co-fold confidence differential** `Δconf = metric(R*) − metric(R)` for ipSAE / ipTM / interface-PAE (orthogonal
  mechanism signal; label as heuristic).
- **Mechanistic R\*-only readouts** (the physical cause of a negative ΔΔG_eff): N-terminal **insertion depth** into the
  7TM core; **contact with activation-critical residues** (e.g. GLP1R R299 / the central polar network / the TM6-kink
  region per project note 01); **fraction of R\*-specific contacts formed vs R.** Per project memory, **measure across
  ≥2 folds and re-score saved poses** (don't re-rank on a single fold).
- Control percentiles the candidate falls in (below).

### Controls (calibration only — NEVER design seeds; per AGENTS.md)
- **Positive (agonist):** GLP-1(7-36)NH2 and exendin-4 → expect strongly **negative ΔΔG_eff**, deep N-term insertion,
  high Δconf. These set the "agonist band."
- **Negative (neutral/decoy):** scrambled-sequence peptides, matched length & composition → expect **ΔΔG_eff ≈ 0**, no
  insertion.
- **Antagonist discriminator (the crucial one):** a pure ECD/vestibule-rim binder (e.g. a Baker de-novo GLP1R binder,
  a documented antagonist) → expect **good binding to *both* states but ΔΔG_eff ≈ 0** — proves the score separates
  "binder" from "agonist." If available, a **NAM/inverse-agonist** (5VEW chemotype) → expect **ΔΔG_eff > 0**.
- **Calibration rule:** require a candidate's ΔΔG_eff to beat the scramble/antagonist band by more than the controls'
  spread (per-folder, per-template), not an absolute kcal/mol cutoff.

### Honesty / validity statement (must accompany any ranking)
- ΔΔG_eff is an **intrinsic-efficacy PROXY** under explicit idealizations: equilibrium (no kinetics/residence time);
  a single Gs-active state (no bias/multi-state); implicit (or slab) membrane; endpoint MM/GBSA error ≈ 1–2+ kcal/mol
  and case-specific; co-folders ignore energetics and default to agonist-bound geometry (can "hallucinate" an inserted
  pose for a non-agonist — hence energetics + two templates, not confidence alone). It **gates a credible,
  active-state-selective binder**; **only the cAMP/SEAP assay confirms agonism.**
- Optional **FEP anchor:** run one ABFEP (or a single R*↔R thermodynamic cycle) on 1–3 *controls* (GLP-1 positive,
  antagonist, scramble) to check the MM/GBSA sign/rank against the gold standard, budget permitting — this is the only
  piece drawn from tier-(A) and is feasible only for a handful.

### Inferences
- This recipe is the minimal faithful implementation of the Q1 identity, uses the project's existing co-folding +
  OpenMM stack, and is explicitly bounded by the published accuracy of its components (Panel/Jespers rank-level, not
  Emax-level).

### Gaps
- Whether MM/GBSA ΔΔG on co-folded **peptide**–GLP1R poses retains the sign-accuracy seen for small molecules is
  **unvalidated** — the controls are the only in-house calibration; treat the first run as method-qualification, not
  candidate selection, until the control bands separate cleanly.
- Implicit-membrane GBSA for a 7TM pocket is approximate; an explicit-membrane MM/PBSA would be better but is likely
  too costly for 200 complexes in a week (flag for a later, smaller rescoring of the top candidates).
