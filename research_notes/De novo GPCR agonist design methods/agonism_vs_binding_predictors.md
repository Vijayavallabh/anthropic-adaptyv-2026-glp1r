# Computational methods distinguishing functional modulation from binding for GPCRs: reliability and failure modes (2022–2026)

> Scope note: methods/benchmark level only. Facts drawn from PubMed are attributed per PubMed's terms with DOI links; preprints and vendor/news items are flagged as such. "BAcc" = balanced accuracy; "agonism prediction" here means ranking/classifying a ligand's functional effect (agonist vs antagonist/inactive, or efficacy) as distinct from binding affinity.

## Key Question 1: What structure-/simulation-based approaches claim to predict or rank GPCR functional response, and what are their validation sets and reported accuracy?

### Takeaway
Four families exist: (a) multi-state structural templates (active vs inactive), (b) conformational-selection / ensemble-docking scoring, (c) MD-derived interface/contact metrics tied to the active state, and (d) ML classifiers trained on functional (EC50/IC50) data. The best-validated functional classifier (GPCRact, 2026) reaches ~0.82 three-class balanced accuracy in-distribution but is 93% class-A data and degrades out-of-family; dedicated efficacy ML methods (Dynamic-GLEP, Provasi–Filizola) restrict themselves to class A and report only modest AUCs (0.71–0.85). Elastic-network/normal-mode analyses describe the activation transition but have no across-ligand efficacy benchmark.

### Cited Findings

**(d) ML classifiers trained on functional data — the only approaches with ligand-scale quantitative validation:**
- **GPCRact (2026)** — hierarchical E(n)-equivariant GNN with cross-/self-attention over a 3D graph of binding- and allosteric-site residues; three-class output (nonbinder / agonist / antagonist), stage 1 = binary binder classifier, stage 2 = agonist-vs-antagonist conditioned only on true binders. Trained on **GPCRactDB: 202,925 ligand–GPCR interactions across 295 human GPCRs mapped to 1,602 experimental structures** (modeling subset 195,989). Scaffold-clustered ~20% test split; no separate external set (uses leave-one-receptor-out / leave-one-family-out as OOD). **Final three-class BAcc = 0.819; binding BAcc = 0.890.** Recovers known activation motifs (DRY, NPxxY) via attention. — [GPCRact, PMC12805254](https://pmc.ncbi.nlm.nih.gov/articles/PMC12805254/)
- **AiGPro (2024)** — multitask deep-learning model (protein sequence + ligand) predicting agonist EC50 and antagonist IC50 across **231 human GPCRs**; reports **Pearson r = 0.91 under stratified ten-fold cross-validation**; web server provided. It is a sequence+ligand bioactivity regressor conditioned on assay mode, not a structure-based mechanism model. — [AiGPro, J Cheminform 2024, DOI 10.1186/s13321-024-00945-7](https://doi.org/10.1186/s13321-024-00945-7)
- **Dynamic-GLEP (2026)** — dynamics-informed deep learning: MD-derived conformational ensembles + transfer learning on an equivariant GNN (EquiScore) to distinguish agonists from non-agonists. **5-HT1A: AUC 0.74 (CV), 0.71 (external FDA-related set); A2A: AUC > 0.85.** Explicitly framed around Class A GPCRs. States "most computational approaches still emphasize affinity prediction, with limited capacity to capture the conformational dynamics driving efficacy." — [Dynamic-GLEP, Brief Bioinform 2026, DOI 10.1093/bib/bbag049](https://doi.org/10.1093/bib/bbag049)
- **Provasi & Filizola (2024, preprint)** — fine-tuned deep transfer-learning models (receptor-sequence NLP + mutation effects) to screen for low-intrinsic-efficacy agonists and biased agonists; models provided per individual **Class A** GPCR. No headline accuracy in the abstract; motivated by "limited availability of high-quality data." — [bioRxiv 2024, DOI 10.1101/2024.12.07.627102](https://doi.org/10.1101/2024.12.07.627102)
- **Physics-informed dual-state query learning (2026, preprint)** — frames prediction around an active/inactive receptor equilibrium, jointly predicting affinity and an agonist/antagonist class; attention for class B1 reportedly points to position 2x50 (HETx motif). Full-text metrics not retrievable from the PDF. — [arXiv 2609.16468](https://arxiv.org/abs/2609.16468)
- Named baselines in the GPCRact comparison: **DeepREAL (2022)**, out-of-distribution agonist-vs-antagonist prediction; **GPCR-Filter** modulator-discovery framework ([arXiv 2601.19149](https://arxiv.org/abs/2601.19149)). — [GPCRact, PMC12805254](https://pmc.ncbi.nlm.nih.gov/articles/PMC12805254/)

**(a) Multi-state active/inactive structural templates:**
- Default AlphaFold2 produces predominantly **one** GPCR state with a **preference for inactive conformations**, attributed to training-set imbalance (**178 inactive vs 60 active** experimental structures). — [Meiler-lab multi-state preprint, biorxiv 2021.11.26.470086](https://www.biorxiv.org/content/10.1101/2021.11.26.470086)
- Reducing MSA depth / stochastic MSA subsampling generates multi-state GPCR and transporter models spanning active↔inactive; breadth of predictions correlates with available experimental structures. — [Del Alamo et al., eLife 2022](https://elifesciences.org/articles/75751)
- Protocols to bias AF2 toward a user-defined functional state (active/inactive) for GPCRs/kinases. — [Sala, Hildebrand & Meiler, Front Mol Biosci 2023, DOI 10.3389/fmolb.2023.1121962](https://doi.org/10.3389/fmolb.2023.1121962)
- **PromptGPCR (2026)** — prompts AlphaFold-Multimer/AF3 with structural-biology-informed sequences to predict active AND inactive states; notes AF2/AF3 "often show reduced accuracy for active-state conformations"; reports higher docking success than baselines. — [PromptGPCR, Comput Struct Biotechnol J 2026, DOI 10.34133/csbj.0179](https://doi.org/10.34133/csbj.0179)

**(b) Conformational-selection / ensemble-docking scoring:**
- **GLOW (GaMD + deep learning, 2023)** — 66 µs across 44 GPCR systems; PAMs/NAMs confine active/inactive agonist-G-protein-bound states respectively; concludes "GPCR allostery exhibits a dynamic conformational-selection mechanism" and recommends ensemble docking to a representative conformational set rather than a single structure. — [Do, Wang & Miao, JACS Au 2023, DOI 10.1021/jacsau.3c00503](https://doi.org/10.1021/jacsau.3c00503)
- Opinion: targeting state-annotated in-silico GPCR conformations for ultra-large library screening, while noting it is "still unclear whether the accuracy of these predicted conformations is sufficient" for pharmacologically meaningful screening. — [Sala, Batebi, Ledwitch, Hildebrand & Meiler, Trends Pharmacol Sci 2023, DOI 10.1016/j.tips.2022.12.006](https://doi.org/10.1016/j.tips.2022.12.006)

**(c) MD-derived interface/contact metrics tied to the active state (mechanistic, single-system):**
- Dopamine D2R, 18 µs/system: the agonist (dopamine) maintains TM3/TM5/TM6 interaction points enabling partial ionic-lock opening and TM6 outward movement, whereas the antagonist (sulpiride) disrupts the toggle switch and globally alters TM dynamics; partial agonist (aripiprazole) perturbs IL2 to a non-arrestin-competent state. — [Mansoor & Morra, J Chem Inf Model 2025, DOI 10.1021/acs.jcim.4c02101](https://doi.org/10.1021/acs.jcim.4c02101)
- Integrative DEER + deep-learning structure prediction + MD to reconstruct biased-agonist (β-arrestin-biased) conformations of AT1R; framed as capturing rare functional/signaling states. — [Belyaeva & Elgeti, Structure 2026, DOI 10.1016/j.str.2026.09.003](https://doi.org/10.1016/j.str.2026.09.003)

**(ENM / normal-mode analyses of the activation transition):**
- ENM normal modes reveal a GPCR vestibule dilation/contraction coupled to intracellular G-protein-pocket formation (M2/M3, A2A, β2, CXCR4); **caveat: rhodopsin modes do not correlate with other GPCR family members.** — [Kolan, Fonar & Samson, Proteins 2014](https://cris.biu.ac.il/en/publications/elastic-network-normal-mode-dynamics-reveal-the-gpcr-activation-m-4/)
- ENM applied to rhodopsin mono/di/tetramer activation rearrangements. — [Niv & Filizola, Proteins 2008](https://pmc.ncbi.nlm.nih.gov/articles/PMC2437915)

**Design-oriented structure+dynamics methods (predict efficacy changes from sequence/structure):**
- Computational design of allosteric pathways: 32 D1/D2 receptor variants with reprogrammed agonist-induced signal transduction; predicted structural/dynamic changes matched measured potency and efficacy. — [Hijazi … Barth, bioRxiv 2025, DOI 10.1101/2025.08.13.670154](https://doi.org/10.1101/2025.08.13.670154)
- Allosteric-signaling causality/energetics framework (AlloMAPS); designs switchable agonist–antagonist effector pairs; **GLP1R and GIPR used as case studies** (class B1). — [Dong, Tee & Berezovsky, J Mol Biol 2025, DOI 10.1016/j.jmb.2025.169293](https://doi.org/10.1016/j.jmb.2025.169293)

### Inferences
- The field's only ligand-scale, quantitatively validated *functional* classifiers are ML models trained on measured EC50/IC50 (GPCRact, AiGPro, Dynamic-GLEP). Structure/MD approaches (b,c,ENM) are largely mechanistic and case-based; none reports a cross-ligand efficacy-ranking benchmark.
- GPCRact's two-stage design (binding first, then agonist/antagonist only on true binders) operationally separates "function" from "binding," making it the most relevant single method to the standing assumption — but its OOD degradation (below) is the key caveat for class B.
- ENM/NMA can reproduce the *direction* of the activation transition but has not been shown to *rank ligands* by efficacy; this null is itself informative.

### Gaps
- Could not retrieve GPCRact's DOI/journal name (only PMC ID) or its per-class-B1 numbers (in Table S7, not main text).
- Dual-state physics-informed preprint (arXiv 2609.16468) full-text metrics not parseable from the PDF.
- No head-to-head independent benchmark comparing these functional predictors on a common external test set was found.

---

## Key Question 2: What is specifically known for CLASS B GPCRs about the difficulty vs class A, and do papers quantify that predictors track binding rather than function?

### Takeaway
Class-B functional prediction is materially harder and under-benchmarked: the two dedicated efficacy ML methods are class-A-only; the best three-class model is ~93% class-A data and loses accuracy on unseen families; AlphaFold3 predicts peptide ligands (the native class-B agonists) poorly; and class-B activation is still described as mechanistically "largely unknown." No paper was found that cleanly quantifies a predictor scoring a class-B *antagonist* above an *agonist*, so direct "tracks-binding-not-function" evidence for class B is thin in the public literature.

### Cited Findings
- **GPCRact is class-A-dominated (≈93% of GPCRactDB).** Out-of-distribution tests: **leave-one-receptor-out BAcc 0.63–0.77** and **leave-one-family-out accuracy lower still**, attributed to latent-space distribution shift; authors flag class-A dominance as a limitation for "rarer motifs in other classes." Stratified analysis (Table S7) is *stated* to be "stable across Classes B1, C and F," but those numbers are not in the main text. — [GPCRact, PMC12805254](https://pmc.ncbi.nlm.nih.gov/articles/PMC12805254/)
- **Dynamic-GLEP is explicitly limited to Class A GPCRs** (validated on 5-HT1A, A2A). — [DOI 10.1093/bib/bbag049](https://doi.org/10.1093/bib/bbag049)
- **Provasi & Filizola transfer-learning models are per-Class-A-receptor.** — [DOI 10.1101/2024.12.07.627102](https://doi.org/10.1101/2024.12.07.627102)
- **AlphaFold3 predicts ligand-binding poses poorly for ions, peptides and proteins** despite improved backbone accuracy — directly relevant because class-B endogenous agonists are peptides; authors say limitations "constrain the utility … in functional studies and structure-based drug design." — [He, Li, Shen & Xu, Acta Pharmacol Sin 2024, DOI 10.1038/s41401-024-01429-y](https://doi.org/10.1038/s41401-024-01429-y)
- Class-B activation mechanism described as **"largely unknown"**; a CRF1R photo-crosslinking + MD study reported agonists and antagonists adopt different folds and stabilize distinct TMD conformations, and that class-A activation models may not transfer (class-B extracellular side more open; inactive bundle not uniformly bent). [Reported via web search; primary citation not pinned.] — [search context](https://pmc.ncbi.nlm.nih.gov/articles/PMC7358596)
- Authoritative review framing: "predicting the pharmacological effects of novel GPCR-targeting drugs remains challenging due to the complex functional dynamics of these receptors," and structure-into-pipeline integration "so far [has] largely been retrospective." — [Conflitti … Limongelli, Nat Rev Drug Discov 2025, DOI 10.1038/s41573-024-01083-3](https://doi.org/10.1038/s41573-024-01083-3)
- Where class-B *is* addressed computationally, it is via mechanistic/allosteric modeling (GLP1R/GIPR in AlloMAPS), not efficacy-ranking benchmarks. — [Dong, Tee & Berezovsky, J Mol Biol 2025, DOI 10.1016/j.jmb.2025.169293](https://doi.org/10.1016/j.jmb.2025.169293)

### Inferences
- The strongest *structural* evidence that function-prediction trails binding-prediction is GPCRact's own hierarchy: it reports binding BAcc 0.890 but three-class (function-inclusive) BAcc only 0.819, and "activity predictions become near-random when binding is misclassified" — i.e., the functional call is strictly downstream of, and gated by, getting binding right.
- That both dedicated efficacy ML methods restrict to class A, and the one broad model is 93% class A with falling out-of-family accuracy, is consistent with the standing project assumption that agonism ranking is unreliable for class-B GPCRs — though this is circumstantial (scarcity/degradation), not a published head-to-head class-B failure benchmark.
- AF3's poor peptide-pose accuracy implies that co-folding a class-B peptide agonist into its receptor is unlikely to yield a reliable functional readout even at the binding-geometry level.

### Gaps
- No public paper was found that quantitatively demonstrates an in-silico efficacy predictor ranking a class-B antagonist above an agonist (the specific "tracks binding not function" demonstration). This appears to be an internal/empirical finding rather than a published benchmark.
- GPCRact's actual class-B1 balanced-accuracy numbers were not obtainable (supplementary only).
- The CRF1R "activation largely unknown / agonists≠antagonists folds" claim came through a web-search summary without a cleanly verified primary DOI.

---

## Key Question 3: Do docking / co-folding scores (AlphaFold/Boltz/Chai confidence, interface PAE) correlate with functional outcome vs binding? Any explicit negative findings?

### Takeaway
The consensus is that confidence/docking scores are, at best, weak-to-moderate *binding/interface* proxies and carry **no validated signal for functional efficacy**. Multiple explicit negative findings exist for GPCRs: docking to AF2 models is no better than to homology models and much worse than to experimental structures; AF3 mispredicts peptide poses; and co-folding confidence degrades on GPCR targets under-represented in training. Because agonists and antagonists share the orthosteric site, a single-conformation score cannot settle efficacy.

### Cited Findings
- **Explicit negative (GPCR docking):** AF2 models capture binding-pocket *structure* better than homology models, **but docking-predicted ligand poses to AF2 models are not significantly more accurate than to homology models, and much less accurate than docking to experimental structures** solved without those ligands. — [Karelina, Noh & Dror, eLife 2023, DOI 10.7554/eLife.89386](https://doi.org/10.7554/eLife.89386)
- **Explicit negative (AF3 vs experiment):** significant discrepancies persist in ligand-binding poses, especially ions/peptides/proteins; limitations "constrain the utility … in functional studies and structure-based drug design." — [He … Xu, Acta Pharmacol Sin 2024, DOI 10.1038/s41401-024-01429-y](https://doi.org/10.1038/s41401-024-01429-y)
- **Review consensus:** AF/RoseTTAFold predict overall structure well but **not binding-pocket side-chain positions with docking-grade accuracy**; docking is "a hypothesis generator rather than a precise predictor," yielding many false positives among few correct hits (GPCR focus). — [Chung … Thomsen, Biomolecules 2025, DOI 10.3390/biom15030423](https://doi.org/10.3390/biom15030423)
- **Co-folding confidence as a ranking metric:** AF3/Protenix/Boltz-2 intrinsic confidence can rank actives vs decoys and often beats conventional docking on standard sets, **but performance declines specifically on a novel GPCR dataset under-represented in training** (and on experimentally verified inactives, and when similar actives are excluded). This is screening/binding enrichment, not functional discrimination. — [Shen … Hou, Chem Sci 2025, DOI 10.1039/d5sc06481c](https://doi.org/10.1039/d5sc06481c)
- **ipTM vs affinity (not GPCR-specific, for calibration):** ipTM is a noisy, threshold-dependent proxy — run-to-run Pearson ~0.64 (AF3)/~0.70 (AF2) between ipTM and interaction scores; AF3 complex ΔΔG-on-mutation Pearson 0.86 on SKEMPI 2.0 but "some … structures have large errors not captured in ipTM." No source tests ipTM against *functional* (efficacy) outcome. — [AF_Cache, arXiv 2606.04566](https://arxiv.org/pdf/2606.04566); [Wee & Wei AF3/SKEMPI, PMC11177964](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11177964/)
- **Why a single score fails for efficacy:** agonists and antagonists occupy the same orthosteric pocket, so scores can be near-tied across states (e.g., an ERα ligand: −10.29 kcal/mol agonist-state vs −10.38 antagonist-state). The reliable-ish workaround is **comparing scores across separate agonist-state and antagonist-state structures** (ER set: 35/47 agonists, 18/19 antagonists correctly classified) — which requires both experimental state structures. — [web-search docking summary](https://pmc.ncbi.nlm.nih.gov/articles/PMC4013293/table/T2)
- **Success case (binding geometry, not efficacy):** a multi-angle AF pipeline predicted the N/OFQ–NOP *active-state* peptide–GPCR complex to full-complex Cα RMSD < 1.0 Å (first peptide–GPCR complex at atomistic accuracy), validated against later cryo-EM — but this validates active-state *structure*, not efficacy ranking across ligands. — [Ciancetta et al., J Chem Inf Model 2024, DOI 10.1021/acs.jcim.4c00499](https://doi.org/10.1021/acs.jcim.4c00499)

### Inferences
- Default co-folders (AF2/3, and by extension Boltz/Chai, which share the training-data regime) are biased toward inactive-leaning GPCR states (Q1), so a de-novo binder co-folded by default is predisposed to the state that does NOT report agonism — the confidence score of such a complex reflects *binding plausibility in a non-signaling geometry*, not agonism.
- No located source claims (or demonstrates) that interface PAE / ipTM / co-fold confidence tracks functional efficacy; the burden of evidence currently falls on the "no functional signal" side.
- The only docking approach with demonstrated (modest) efficacy classification is two-state differential scoring, and it is gated on having both experimental active- and inactive-state structures — a prerequisite rarely met for a novel class-B agonist design.

### Gaps
- No GPCR-specific study was found that directly correlates co-fold confidence (ipTM/PAE) with measured agonist *efficacy* (as opposed to binding or actives/decoys enrichment).
- Boltz-2 / Chai-specific functional-vs-binding analyses were not found; evidence is AF2/AF3-centric and extrapolated.

---

## Key Question 4: Are there validated "necessary-but-not-sufficient" structural filters (required contact / pocket engagement) that are reliable even if full functional prediction is not?

### Takeaway
Yes — several contact/engagement criteria are mechanistically well-supported as *necessary* for agonism, and are more reliable than full efficacy ranking: engagement with activation-critical orthosteric residues at sufficient insertion depth, the conserved class-A microswitch contacts (TM3/5/6, toggle switch, ionic lock → TM6 outward movement), and, for class B / GLP-1R specifically, deep peptide-N-terminus insertion into the TM core, the central polar/H-bond network, and TM6 outward movement with the proline-induced kink. These are filters (a candidate lacking them is almost certainly not an agonist), not sufficient predictors of efficacy magnitude.

### Cited Findings
- **Insertion depth / engagement with activation-critical residues** determines agonist vs antagonist for 5-HT receptor photoswitchable ligands: anchoring too deep (H-bonds to Asp3.32/Thr) prevents engagement with activation-critical residues and stabilizes the inactive state; a shallower agonist-compatible pose engages them. — [Weber … Rossetti, Commun Chem 2026, DOI 10.1038/s42004-026-01936-5](https://doi.org/10.1038/s42004-026-01936-5)
- **Class-A microswitch contacts as the activation gate:** agonist-bound D2R preserves TM3/TM5/TM6 contacts enabling ionic-lock opening and TM6 outward movement; antagonist disrupts the toggle switch — a mechanistic, contact-level discriminator. — [Mansoor & Morra, J Chem Inf Model 2025, DOI 10.1021/acs.jcim.4c02101](https://doi.org/10.1021/acs.jcim.4c02101)
- **Residue-level engagement linked to transducer choice** (M1 mAChR): docking + BRET implicate Y7.43 (Gq bias) vs W6.48/Y6.51 (β-arrestin) contacts. — [Wang et al., Int J Mol Sci 2023, DOI 10.3390/ijms24087356](https://doi.org/10.3390/ijms24087356)
- **GLP-1R (class B1) specific necessary features:**
  - A **hydrogen-bonded central polar network** (implicating R2.60, N3.43, Q7.49, H6.52; a predicted E6.53–R2.60 interaction important for GLP-1/exendin-4- but not oxyntomodulin-mediated cAMP) acts as a switch for peptide-mediated (biased) agonism. — [Wootten et al., Mol Pharmacol 2016](https://molpharm.aspetjournals.org/content/molpharm/early/2015/12/23/mol.115.101246.full.pdf)
  - **TM6 outward movement with a sharp mid-helix kink** upon activation is a hallmark of GLP-1R/class-B activation; the peptide is clasped between the N-terminal domain and the TM core (cryo-EM 5VAI). Calcitonin receptor shows analogous large outward movement of TM6/TM7 extracellular ends. — [GLP-1R–Gs cryo-EM (PDB 5VAI) summary](https://www.rcsb.org/structure/5VAI)
  - MD: positive effectors (GLP-1+Gs, PAM) favor TM3/TM5 or TM6/TM7 signaling pathways while a NAM reinforces the central polar network; transient contacts at the base of the binding cavity correlate with G-protein-activation kinetics; R190(2.60) is a recurrent communication hub. — [GLP-1R effector MD, Research Square rs-10245055](https://www.researchsquare.com/article/rs-10245055)

### Inferences
- A practical, relatively reliable in-silico *filter* for a candidate GLP-1R agonist is therefore structural/geometric: (i) the ligand/peptide N-terminus must reach deep into the TM bundle and contact the central polar-network residues, and (ii) the bound/co-folded model should be compatible with (or stabilize) the active TM6-kinked, outward state — not merely a high-confidence perch at the ECD/pocket rim. A model that engages only peripheral/ECD contacts fails the necessary condition for agonism.
- These filters are consistent with the broader finding that agonism is a conformational-equilibrium property: they test *access to the activation machinery*, which is necessary but not sufficient (they cannot rank Emax among ligands that all satisfy them).

### Gaps
- No study was found that *prospectively validated* such a necessary-contact filter as a screening gate across many de-novo GPCR (especially class-B) binders with measured functional outcomes — the contacts are established retrospectively from solved agonist complexes and MD.
- The specific class-B PxxG / TM6 proline-kink motif as a *predictive* (rather than descriptive) filter was not found quantified in a 2022–2026 computational benchmark.
- Whether these filters survive being applied to *predicted* (AF/Boltz/Chai) rather than experimental structures — given those models' inactive-state bias and poor peptide poses — is untested in the located literature.
