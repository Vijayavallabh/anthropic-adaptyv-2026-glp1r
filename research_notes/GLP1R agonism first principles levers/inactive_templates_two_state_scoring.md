# Inactive/Apo GLP1R templates and the validity of two-state differential co-folding as an agonism/efficacy signal

Scope: experimental inactive/apo structural templates for human GLP1R (P43220) and class B1 surrogates; whether an ACTIVE-vs-INACTIVE differential of a docking/co-folding/interface score has precedent as an efficacy/agonism proxy; whether "conformational selection" has a computable prospective definition; practical template-biasing of AF3-free co-folders toward a supplied inactive template; and how to build an inactive GLP1R model if needed.

Tiering legend: [PR] peer-reviewed; [pre] preprint; [HYP] hypothesis / no evidence found; [in-silico] tool/documentation capability (not a validated result). All PDB resolutions/ligands are from RCSB/PMC entries cited inline.

**Headline correction to the task's premise:** Experimental *inactive-state* human GLP1R structures DO exist (full-length 6LN2; TMD-only 5VEW/5VEX). The "if no experimental inactive GLP1R exists" branch is therefore not binding — but every inactive GLP1R structure is NAM-bound and heavily thermostabilized, so it is an *engineered* inactive state, not a pristine apo ground state. Details below.

---

## KQ1 — What experimental INACTIVE/APO GLP1R structures exist, and what class B1 homolog inactive structures can serve as surrogate inactive templates?

### Takeaway
Human GLP1R has three experimental inactive-state structures (full-length 6LN2 at 3.2 Å; TMD-only 5VEW and 5VEX at 2.7/3.0 Å), all bound to a negative allosteric modulator (NAM) and all thermostabilized/fusion-engineered — none is a clean apo. Among class B1 homologs, only GCGR (4L6R, 5EE7, 5XEZ, 5XF1) and CRF1R/CRHR1 (4K5Y, 4Z9G) have genuine experimental inactive/antagonist-bound structures; GIPR, GLP2R, secretin receptor (SCTR) and PTH1R have no clean antagonist-bound inactive experimental structure (all deposited structures are active, G-protein-coupled cryo-EM).

### Cited Findings
- **6LN2 — full-length human GLP1R, INACTIVE, 3.2 Å, X-ray.** "Peptide-free crystal structure of the full-length human GLP-1R in an inactive state." Orthosteric peptide site is empty (apo for peptide), but the TMD contains the NAM **PF-06372222**. Stabilized by Fab7F38 (binds ECD non-competitively) plus a rubredoxin fusion in ICL2, C-terminal truncation, and thermostabilizing mutations (no nanobody in the crystal). TMD closely matches the earlier inactive TMD (Cα RMSD 0.6 Å); ECL1/ECL3 ordered, stalk disordered. Wu et al., *Nat Commun* 2020. — [PMC7062719](https://pmc.ncbi.nlm.nih.gov/articles/PMC7062719/)
- **5VEW — human GLP1R TMD only, INACTIVE, 2.70 Å, X-ray**, bound to NAM **PF-06372222** (ligand code 97Y); construct is a GLP1R–T4 endolysin chimera (455 aa), expressed in *S. frugiperda*. RCSB abstract: "The receptor is in an inactive conformation with compounds that restrict movement of the intracellular tip of helix VI." Song et al., *Nature* 546:312–315 (2017), DOI 10.1038/nature22378. — [RCSB 5VEW](https://www.rcsb.org/structure/5VEW)
- **5VEX — human GLP1R TMD only, INACTIVE, 3.00 Å, X-ray**, bound to NAM **NNC0640** (same paper). — [RCSB 5VEX](https://www.rcsb.org/structure/5VEX) (compound-to-ID mapping resolved via the RCSB 5VEW entry, which explicitly names PF-06372222 and states NNC0640 "belongs to the related entry 5VEX"; an earlier search snippet had the mapping reversed, so RCSB is authoritative.)
- **GCGR (closest class B1 homolog) inactive structures:**
  - **5XEZ / 5XF1 — full-length human GCGR, INACTIVE, 3.0 Å / 3.19 Å, X-ray.** Zhang et al., *Nature* 2017; ECD+TMD linked by a 12-residue stalk (β-strand in this inactive form). — [RCSB 5XEZ](https://www.rcsb.org/structure/5XEZ); [RCSB 5XF1](https://www.rcsb.org/structure/5XF1)
  - **4L6R (apo GCGR TMD)** and **5EE7 (GCGR TMD + NNC0640, 2.5 Å)** appear in the June-2022 OUP inventory of class B1 TMD-containing PDB structures. — [OUP class B1 structure table](https://academic.oup.com/view-large/404814143) (verify ligand/resolution at RCSB before use).
- **CRF1R / CRHR1 inactive (antagonist-bound TMD):**
  - **4K5Y — human CRF1R TMD, 2.98 Å, X-ray**, bound to antagonist **CP-376395**; Hollenstein et al., *Nature* 499:438–443 (2013); described as a model for class B GPCRs. — [PDBe 4K5Y](https://www.ebi.ac.uk/pdbe/entry/pdb/4k5y/index)
  - **4Z9G — same complex, 3.18 Å** (hexagonal form), Dore et al. 2017; starting model 4K5Y; simulations address the full inactive multidomain state. — [RCSB 4Z9G](https://www.rcsb.org/structure/4z9g)
- **Activation-state geometry that distinguishes the states (class B1):** inactive/inactive-like class B1 receptors (PTH1R, GCGR, GLP-1R, CRF1R) show a straight or moderate TM6 (≈145° kink), whereas peptide-activated PTH1R shows the sharp ≈90° TM6 kink; comparison drawn in the 2023 PCO371–PTH1R Nature study. — [PMC10307627 (Fig 2/Fig 10)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10307627/figure/Fig2)

### Inferences
- The right structural *discriminator* between the active and inactive templates for GLP1R is the **TM6 intracellular kink** (sharp ≈90° active vs straight ≈145° inactive) and the TM6 outward swing that opens the Gαs pocket. The inactive GLP1R crystals are explicitly defined by NAMs that "restrict movement of the intracellular tip of helix VI," i.e., they lock exactly the feature a de novo *agonist* must be able to release. So 6LN2/5VEW are mechanistically appropriate inactive references for an agonism differential, despite the engineering.
- Because 6LN2/5VEW/5VEX are NAM-bound and fusion-stabilized, the *orthosteric/ECD* geometry is not a pristine ground state; for a differential that keys on the ligand-facing pocket you may prefer the TMD coordinates (TM6) over the engineered loops.
- For class B1, you have a clean 2-state experimental pair only for GLP1R itself and for GCGR; CRF1R gives a second antagonist-bound inactive TMD. These three are the only usable experimental inactive class B1 templates.

### Gaps
- No clean *apo* (modulator-free) inactive GLP1R exists; all inactive GLP1R structures carry a NAM and heavy engineering.
- Could not confirm from this search any experimental inactive-state structure for GIPR, GLP2R, SCTR, or PTH1R; the literature treats PTH1R's inactive reference as "inactive-like"/computational. A full RCSB/GPCRdb enumeration filtered by state is recommended to confirm these absences and to re-verify 4L6R/5EE7 ligand+resolution.

---

## KQ2 — Does any published method rank ligand EFFICACY (agonist vs antagonist, partial vs full) by a DIFFERENTIAL of a docking/co-folding/interface score between an active-state and an inactive-state template?

### Takeaway
Yes, but only for **small-molecule docking against class A GPCRs with high-resolution crystal structures in both states** — most directly Costanzi & Vilar (β2-adrenergic receptor), where the active-minus-inactive docking-score difference (ΔScore) separated agonists from blockers with ROC AUC 0.98 / ~95% accuracy retrospectively. There is NO published method that applies an active-vs-inactive *co-folding/interface-confidence* differential (ΔipTM, ΔPAE, Δ ipSAE, Δ interface-pLDDT) to rank **de novo** or **peptide** agonist efficacy for any GPCR, including class B1.

### Cited Findings
- **Two-state docking ΔScore as an efficacy classifier (the strongest precedent).** Costanzi & Vilar, "In silico screening for agonists and blockers of the β2 adrenergic receptor: implications of inactive and activated state structures," *J Comput Chem* 33(5):561–572 (2011/2012). Docked 60 ligands (30 agonists, 30 blockers) + ~55,800 ZINC decoys to four β2AR crystal structures — 2RH1 (inactive, carazolol), 3NYA (neutral antagonist), 3PDS, and 3P0G (activated, nanobody-stabilized, full agonist BI-167107). **The difference between the 3P0G (active) and 2RH1 (inactive) docking scores classified ligands into agonists vs blockers: ROC AUC = 0.98; 97% of agonists (29/30) scored better at the active structure; 93% of blockers (28/30) scored better at the inactive structure; overall ≈95% classification; LDA watershed 0.03 kcal/mol.** — [PMC3265623](https://pmc.ncbi.nlm.nih.gov/articles/PMC3265623/)
- **Prospective conformation-selective docking yields agonists.** Scharf et al., "Comparative docking to distinct G protein-coupled receptor conformations exclusively yields ligands with agonist efficacy," *Mol Pharmacol* (2019): docking to several active-state β2AR conformations gave a 37% experimentally-confirmed hit rate, and aggregating ranks across multiple active-state structures "exclusively yields agonists." — [Nottingham Repository record](https://nottingham-repository.worktribe.com/output/3331208/comparative-docking-to-distinct-g-proteincoupled-receptor-conformations-exclusively-yields-ligands-with-agonist-efficacy)
- **General corroboration (review-level).** Docking against active-state structures enriches agonists and inactive-state structures enrich blockers; receptor-ensemble docking and induced-fit docking can bias an inactive crystal toward recognizing agonists. Caveat repeated in the field: a docking score "can be interpreted in terms of ligand binding, but not ligand function," and the two-state pockets are often very similar, limiting discrimination. — [Frontiers Mol Biosci 2022 review](https://www.frontiersin.org/journals/molecular-biosciences/articles/10.3389/fmolb.2022.879212/full)
- **Closest thing in the co-folding/AI world (single-state, not a differential).** DeorphaNN (bioRxiv 2025): a graph neural network that predicts GPCR agonist identity from **active-state** AlphaFold GPCR–peptide complexes + interatomic interactions + AlphaFold-Multimer pair representations. It reports that AF-Multimer confidence scores *alone* give only "partial discrimination" between agonist and non-agonist complexes, and that adding active-state structure + pair-representation embeddings improves discriminatory power; developed on *C. elegans*, generalizes to human. It does **not** compute an explicit active-minus-inactive differential, and the abstract reports no AUROC/accuracy number. — [bioRxiv 2025.03.19.644234](https://www.biorxiv.org/content/10.1101/2025.03.19.644234v1)

### Inferences
- The *concept* the project wants (within-candidate active-minus-inactive differential as an efficacy proxy) is validated in principle — Costanzi/Vilar is a direct, high-performing instance — but every validated instance is: (i) **docking** of small molecules, not **co-folding** of a binder; (ii) **class A** (β2AR) with pristine active+inactive crystals; (iii) **retrospective** classification of known agonists/blockers, not prospective de novo ranking. Transfer to de-novo **peptide/mini-binder agonist** co-folding on **class B1 GLP1R** is an untested extrapolation, i.e. [HYP], not established method.
- DeorphaNN is the most relevant existence proof that AlphaFold *active-state* co-folding confidence carries *some* agonism signal, but it explicitly needed a learned model on top because raw confidence only "partially" discriminates — a caution that a bare ΔipTM/Δipae threshold may be weak on its own.

### Gaps
- Found no paper computing ΔipTM / ΔPAE / Δ ipSAE / Δ interface-pLDDT between an active and an inactive co-folded complex to rank efficacy, for any GPCR or allosteric system. This specific metric appears to be novel/unpublished.
- No quantitative DeorphaNN performance numbers retrievable from the abstract (full-text behind preprint PDF; binary-only on fetch).

---

## KQ3 — Does "conformational selection" / "active-state-selective binding" have a quantitative, computable, prospectively-used definition (ΔΔG, ΔPAE, Δ ipSAE, Δ interface-pLDDT)?

### Takeaway
The *thermodynamic* definition is standard and computable as a two-state ΔΔG (ligand stabilizes the active vs inactive ensemble), and it has been operationalized as a docking-score difference (Costanzi/Vilar ΔScore). But a co-folding-confidence version (ΔPAE/ΔipTM/Δ ipSAE/Δ interface-pLDDT between an active and inactive co-fold) has **no published prospective use** — it would be a new metric.

### Cited Findings
- **Thermodynamic/conceptual definition.** Agonists and antagonists stabilize GPCR conformations of the active and inactive ensembles respectively (conformational selection), attributed to Boehr et al. 2009 and Abrol et al. 2013. — [Frontiers Mol Biosci 2022 review](https://www.frontiersin.org/journals/molecular-biosciences/articles/10.3389/fmolb.2022.879212/full)
- **Operationalized as a docking ΔScore (computable, validated retrospectively).** ΔScore = (active-state docking score) − (inactive-state docking score); AUC 0.98 for β2AR agonist/blocker classification (see KQ2). — [PMC3265623](https://pmc.ncbi.nlm.nih.gov/articles/PMC3265623/)
- **AF2 MSA-subsampling as a proxy for the conformational landscape (computable, used prospectively for population shifts).** Subsampled/shallow MSAs let AlphaFold2 sample both active and inactive GPCR/transporter conformations (del Alamo et al., *eLife* 2022); related work predicts how mutations shift active-state *populations* in kinases with reported accuracy up to ~80% (PMC10973385), i.e. a population metric rather than a per-ligand efficacy score. — [eLife 75751](https://elifesciences.org/articles/75751); [PMC10973385](https://pmc.ncbi.nlm.nih.gov/articles/PMC10973385)
- **State-biasing toolkit (computable knobs).** SPEACH_AF (MSA masking to favor under-represented states), Stein & Mchaourab in-silico MSA editing, Kern-group sequence clustering (noted to mispredict some structures), Heo & Feig template-only no-MSA modeling. — [Frontiers Mol Biosci 2023 "Biasing AlphaFold2"](https://www.frontiersin.org/journals/molecular-biosciences/articles/10.3389/fmolb.2023.1121962/full); [PMC11621821](https://pmc.ncbi.nlm.nih.gov/articles/PMC11621821/)

### Inferences
- A defensible, computable "conformational-selection score" for a de novo GLP1R binder is implementable today as a per-candidate differential across two forced co-folds: Δ = (interface confidence on the **active** 6X18 template) − (interface confidence on the **inactive** 6LN2/5VEW template), using any of ipTM, ipae/PAE_interface, ipSAE, or interface-pLDDT. This is the direct co-folding analogue of Costanzi/Vilar's ΔScore. Its *construction* is sound; its *predictive validity for efficacy* is unproven [HYP].
- Because co-folders can be pushed to either state via templates/MSA, the differential is well-posed only if both states are *forced* (otherwise the model's default-state bias dominates and the difference is an artifact of which state it preferred).

### Gaps
- No prospective validation of a co-folding differential (ΔPAE/ΔipTM/Δ ipSAE/Δ interface-pLDDT) against measured efficacy for any system — the metric would need an internal calibration set (e.g., known GLP1R agonists vs antagonists/NAMs) before being trusted as a ranking axis.

---

## KQ4 — Can AF3-free co-folders (Boltz-2, Chai-1, OpenFold3, Protenix) be template-biased/seeded toward a supplied inactive template? How?

### Takeaway
All four accept user-supplied structural templates and can be pushed toward them; **Boltz-2 is the only one with an explicit, documented "force the template" potential** (`force: true` + `threshold`). Chai-1 and Protenix support custom templates but expose no documented hard-enforcement flag; OpenFold3 supports user templates with an effect ranging from weak prior to near-fixed scaffold. All also support MSA subsampling / single-sequence mode as an orthogonal state-biasing lever.

### Cited Findings
- **Boltz-2 / Boltz (strongest control).** YAML top-level `templates:` list, per entry: `cif:` (or `pdb:`) path; optional `chain_id` (query chain(s) to template) and `template_id` (template chain(s), to set the mapping yourself); **`force:` (default `false`) — when `true` a potential enforces the template**, and `threshold:` sets the allowed Cα deviation in Å (required when using `force`). Without `force`, the template is input information only (soft). MSA: `msa: empty` = single-sequence mode (supported, "not recommended"); `--use_msa_server` for auto MSA; subsampling via `--subsample_msa`, `--num_subsampled_msa`, `--max_msa_seqs`. — [Boltz prediction docs](https://github.com/jwohlwend/boltz/blob/main/docs/prediction.md)
- **Chai-1 / chai-lab.** `--use-templates-server` (alongside `--use-msa-server`). Custom templates in two steps: supply your own `m8` hit file, and place structure files at `$CHAI_TEMPLATE_CIF_FOLDER/identifier.cif.gz` (identifier must match the m8). Advanced API `chai_lab.chai1.run_folding_on_context` with a hand-built `AllAtomFeatureContext` lets you inject templates programmatically. MSAs via `aligned.pqt` (a3m-convertible) or `--use-msa-server` (ColabFold MMseqs2); default runs single-sequence (embeddings "without MSAs or templates"). **No documented hard template-enforcement flag** (no `force`/`threshold` equivalent found). — [chai-lab README](https://github.com/chaidiscovery/chai-lab/blob/main/README.md)
- **OpenFold3.** Supports user-specified templates for co-folding, provided by uploading a structure file or entering a PDB ID; reported effect ranges "from a weak prior to a nearly fixed scaffold." Precomputed-alignment workflow uses a per-chain `template_alignment_file_path`. A template-module inter-chain masking bug was identified and corrected. — [OpenFold3 input-format docs](https://openfold-3.readthedocs.io/en/stable/input_format_reference.html); [Rowan write-up](https://rowansci.substack.com/p/openfold3-and-co-folding-with-templates)
- **Protenix (ByteDance, AF3 reproduction).** Template support present for `protenix-v2`, `protenix_base_default_v1.0.0`, and `protenix_base_20250630_v1.0.0` (Template column ✅); **absent for `protenix_base_default_v0.5.0` (❌)**; v1 release note: "Supported Template/RNA MSA features." Input schema/fields documented in `docs/msa_template_pipeline.md` and `docs/infer_json_format.md` (exact JSON key not shown on the README). — [Protenix README](https://github.com/bytedance/Protenix/blob/main/README.md)
- **AF3 family template format (for reference; AF3 itself is not "AF3-free").** Templates specified per protein chain in JSON with structure file + query/template index mappings; empty list = template-free. — [AlphaFold3 custom-templates docs (mirror)](https://www.mintlify.com/google-deepmind/alphafold3/advanced/custom-templates)

### Inferences
- Practical recipe for a forced two-state GLP1R co-fold: run each candidate twice — once templated to the **active** 6X18 (GLP1R chain) and once to the **inactive** 6LN2 (or 5VEW TMD) — then take the interface-confidence differential. **Use Boltz-2 for the hard-enforced inactive fold** (`force: true`, small `threshold`, `template_id` mapped to the GLP1R chain) because it is the only tool with documented template enforcement; Chai-1/Protenix/OpenFold3 can replicate the *soft* version. Pin only the GLP1R receptor chain to the template and leave the de novo binder free.
- MSA subsampling is a second, template-free way to force the inactive state (shallow/subsampled MSA tends to surface alternative/inactive conformations), usable as a cross-check that the template is driving the state rather than the MSA.

### Gaps
- Exact Protenix template JSON key/syntax and whether it supports hard enforcement were not confirmed (need `docs/infer_json_format.md`).
- Chai-1/OpenFold3/Protenix lack a documented equivalent of Boltz's `force`+`threshold`; strength of their template bias is qualitative.
- Known issue (possibly stale): Boltz templates combined with affinity prediction were reported to error (2025 ChimeraX ticket) — verify before combining template + affinity in one run.

---

## KQ5 — If no experimental inactive GLP1R exists, how best to BUILD one (GCGR-inactive homology, GPCRdb refined model, AF2 inactive-biased prediction)?

### Takeaway
Building is largely unnecessary because experimental inactive GLP1R exists (6LN2 full-length; 5VEW/5VEX TMD). If a modulator-free / de-engineered inactive model is wanted, the best options in rough priority are: (1) use/repair the experimental 6LN2 TMD; (2) download the GPCRdb AlphaFold2-MultiState **inactive** GLP1R model; (3) AF2 MSA-subsampling / SPEACH_AF inactive-biased prediction; (4) homology from GCGR inactive (5XEZ/5XF1) or CRF1R (4K5Y) as class B1 surrogates.

### Cited Findings
- **Experimental inactive GLP1R already available** — 6LN2 (full-length), 5VEW/5VEX (TMD) (see KQ1). — [PMC7062719](https://pmc.ncbi.nlm.nih.gov/articles/PMC7062719/); [RCSB 5VEW](https://www.rcsb.org/structure/5VEW)
- **GPCRdb AlphaFold2-MultiState models.** GPCRdb (2023) provides state-specific models of **all human non-olfactory GPCRs in inactive, intermediate, and active states** built with AlphaFold2-MultiState (so a GLP1R inactive model is included), plus "refined" structures with re-modeled missing/distorted regions and reverted mutations; refined/model pages at gpcrdb.org/structure/homology_models. (Note: a direct download for the *inactive* GLP1R model was not individually confirmed in this search; only an active refined GLP1R entry, 7LCJ, was seen directly.) — [GPCRdb 2023, PMC9825476](https://pmc.ncbi.nlm.nih.gov/articles/PMC9825476/); [GPCRdb refined 7LCJ (active)](https://gpcrdb.org/structure/refined/7LCJ)
- **AF2 inactive-biased prediction (de-novo state sampling).** Shallow/subsampled MSAs sample inactive GPCR states (del Alamo et al., *eLife* 2022); SPEACH_AF MSA-masking biases toward under-represented states. — [eLife 75751](https://elifesciences.org/articles/75751); [Frontiers "Biasing AlphaFold2" 2023](https://www.frontiersin.org/journals/molecular-biosciences/articles/10.3389/fmolb.2023.1121962/full)
- **Class B1 surrogate inactive templates for homology** — GCGR 5XEZ/5XF1 (full-length inactive) and CRF1R 4K5Y/4Z9G (antagonist-bound inactive TMD) (see KQ1). — [RCSB 5XEZ](https://www.rcsb.org/structure/5XEZ); [PDBe 4K5Y](https://www.ebi.ac.uk/pdbe/entry/pdb/4k5y/index)

### Inferences
- The cleanest inactive GLP1R template for the two-state differential is the **6LN2 TMD** (experimental, human, correct TM6-restricted geometry) after stripping the Fab/rubredoxin fusion and optionally the NAM; the GPCRdb AF2-MultiState inactive model is the best fully-computational alternative if you want no engineering artifacts. GCGR/CRF1R homology is a third-line surrogate only if a GLP1R-specific inactive template proves inadequate — but since GLP1R's own inactive structure exists, homology from a paralog adds error with no benefit.
- Whichever inactive template is chosen, it should carry the diagnostic inactive TM6 (straight, ≈145°) so the active-minus-inactive differential actually probes the activation switch.

### Gaps
- Direct retrieval/confirmation of a downloadable GPCRdb AF2-MultiState *inactive* GLP1R coordinate file was not completed (only the active refined 7LCJ entry was seen); confirm on the GLP1R structure-models page before relying on it.
- No benchmark found comparing accuracy of a GCGR-homology inactive GLP1R vs the AF2-MultiState inactive model vs experimental 6LN2.

---

## Cross-cutting bottom line (binding vs activation; for the report-writer)
- BINDING signal (does the de novo binder dock/co-fold onto GLP1R) is well-supported by standard co-folding confidence. ACTIVATION/efficacy is the hard part: the only *validated* structure-based efficacy proxy is the two-state **docking** ΔScore (Costanzi/Vilar, β2AR, AUC 0.98, retrospective, class A, small molecules) [PR], plus conformation-selective docking enriching agonists (Scharf 2019) [PR].
- A two-state **co-folding** differential (ΔipTM/ΔPAE/Δ ipSAE/Δ interface-pLDDT between a forced-active and forced-inactive co-fold) is **computable today** (Boltz-2 `force`+`threshold` on the inactive 6LN2/5VEW template vs active 6X18) but has **no published efficacy validation** for any GPCR — it is [HYP] and must be locally calibrated against known GLP1R agonists vs antagonists/NAMs before being used as a ranking axis. DeorphaNN [pre] is the nearest evidence that active-state co-folding confidence carries agonism signal, but it needed a learned GNN on top because raw confidence only "partially" discriminates.
- The correct inactive-state discriminator for GLP1R is the TM6 intracellular kink (sharp ≈90° active vs straight ≈145° inactive); the NAM-bound inactive GLP1R crystals (6LN2/5VEW) are mechanistically ideal for this because the NAMs lock exactly that TM6 tip.
