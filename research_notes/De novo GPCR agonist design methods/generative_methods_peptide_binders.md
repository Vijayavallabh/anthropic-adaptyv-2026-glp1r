# Generative methods for de novo peptide / mini-protein binder design targeting GPCRs (2023–2026)

*Scope note: this report stays strictly at the level of algorithms, software, inputs, benchmarks, reported hit rates, and licensing to inform computational TOOL SELECTION. It does not address receptor-activation mechanism or pharmacophore content. Where a source studies agonists/antagonists, only the binder-design methodology and its measured binding performance are extracted.*

---

## KQ1 — Which generative models are SOTA for de novo peptide / mini-binder design (2024–2026)? Inputs, all-atom target context, licensing, reported success rates.

### Takeaway
The 2024–2026 SOTA for target-conditioned de novo mini-binder design is a small cluster of tools: **RFdiffusion** (and its all-atom successors **RFdiffusionAA** and **RFdiffusion3**), **BindCraft** (AF2-hallucination), and **AlphaProteo** (closed). For *peptide*-specific design the field is **DiffPepBuilder, PepFlow, PepGLAD, PepHAR** (diffusion/flow), **EvoBind/EvoBind2** (AF-guided in-silico evolution), and the new all-atom universal generator **BoltzGen**. Experimental hit rates span ~<1% (early pipelines) to 10–100% (BindCraft, AlphaProteo, BoltzGen on favorable targets), but are strongly target-dependent. Licensing splits cleanly: ProteinMPNN/BindCraft/Boltz are MIT, RFdiffusion is BSD, Genie2 Apache-2.0, Chroma has gated weights, and AlphaProteo is closed (no public weights).

### Cited Findings

**RFdiffusion (backbone diffusion; Baker lab, Nature 2023)**
- Generates protein-binder backbones given a target structure plus specified interface **hotspot residues**; sequences recovered with ProteinMPNN; designs filtered with AF2. Success rates ~2 orders of magnitude above prior campaigns on IL-7Rα, InsR, PD-L1, TrkA, with ~1 order attributed to RFdiffusion and ~1 to AF2 filtering — [Nature 2023 via IPD/Science summary & search synthesis](https://www.bakerlab.org/2023/05/08/deep-learning-improves-protein-binder-design-tenfold/)
- A news/lecture synthesis cites ~10–20% of RFdiffusion designs binding usefully (vs <1% pre-AI); a course slide cites 0.1–10% in-vitro success — [search synthesis](https://www.cs.princeton.edu/courses/archive/spr26/cos598L/lectures/2026_02_17_lec4_bindcraft.pdf)
- License: **BSD** (permits non-profit and commercial use), per HuggingFace mirror and RosettaCommons-derived model card (secondary; verify repo LICENSE) — [sourcepulse mirror](https://www.sourcepulse.org/projects/875938); [HF mirror](https://huggingface.co/OneScience-Sugon/RFdiffusion/blob/main/README.md)
- Caution: a bioRxiv preprint "RFdiffusion Exhibits Low Success Rate in De Novo Design of Functional Protein Binders for Biochemical Detection" reports poor performance for a detection use-case — [bioRxiv 2025.02.07.636769](https://www.biorxiv.org/content/10.1101/2025.02.07.636769)

**RFdiffusionAA (all-atom; Krishna et al., Science 2024)**
- All-atom model that **conditions on the ligand / non-protein atoms during denoising**, enabling small-molecule-binder and pocket design (used as the baseline for ligand-pocket design benchmarks) — [ODesign, arXiv 2510.22304](https://arxiv.org/abs/2510.22304)

**RFdiffusion3 (all-atom; Baker lab, bioRxiv Sept 2025)**
- Diffuses **every polymer atom including side chains** (not just backbone), generating structures in the context of ligands, nucleic acids, and other non-protein atoms; enables atom-level constraints — [bioRxiv 2025.09.18.676967](https://www.biorxiv.org/content/10.1101/2025.09.18.676967); [PMC12458353](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12458353/)
- Reports improved in-silico benchmark performance at ~1/10 the compute of priors; ~10× faster than RFdiffusion2; demonstrated on DNA-binding proteins and cysteine hydrolases; **open source**. Limitation: weaker on biomolecules absent from training (e.g., non-canonical amino acids) — [GEN coverage](https://www.genengnews.com/topics/artificial-intelligence/rfdiffusion3-now-open-source-designs-dna-binders-and-advanced-enzymes)

**BindCraft (AF2-hallucination; Pacesa et al., Nature 2025)**
- One-shot pipeline that **backpropagates through AlphaFold2 weights** to hallucinate binder sequence+structure; reported **10–100% experimental hit rate**, nanomolar affinities without high-throughput screening, even when binding site is unknown; tested on cell-surface receptors, allergens, de novo proteins, and Cas9 — [bioRxiv 2024.09.30.615802](https://www.biorxiv.org/content/10.1101/2024.09.30.615802v1); [PMC11642741](https://pmc.ncbi.nlm.nih.gov/articles/PMC11642741)
- License: **MIT** (per third-party academic paper) — [search synthesis](https://www.cs.princeton.edu/courses/archive/spr26/cos598L/lectures/2026_02_17_lec4_bindcraft.pdf)

**AlphaProteo (DeepMind, Sept 2024)**
- Reports **3–300× better binding affinities** and higher success than best prior methods on 7 targets; 88% of designs bound for viral target BHRF1; trained on PDB + >100M AF structure predictions; generates strong binders without iterative optimization — [arXiv 2409.08022](https://www.arxiv.org/pdf/2409.08022); [DeepMind blog](https://deepmind.google/blog/alphaproteo-generates-novel-proteins-for-biology-and-health-research/)
- **Availability: closed.** Weights and inference infrastructure not released publicly; access only via a selective "Trusted Tester Program" (secondary source) — [nextomoro summary](https://nextomoro.com/alphaproteo/)

**DiffPepBuilder (peptide; Wang et al., arXiv 2024)**
- **SE(3)-equivariant diffusion** that co-designs peptide sequence + structure for a target; trained on synthetic interface dataset **PepPC-F**; post-hoc **disulfide stapling** for rigidity; reported to beat AfDesign and RFdiffusion+ProteinMPNN on recall/interface quality/diversity over 30 experimentally-verified peptide binders — [arXiv 2405.00128](https://arxiv.org/abs/2405.00128)
- Used in a 2026 LasR peptide-inhibitor pipeline alongside ProteinMPNN, RFdiffusion2, BindCraft — [search synthesis](https://sfera.unife.it/handle/11392/2622470)

**PepFlow / PepGLAD / PepHAR (peptide benchmark suite)**
- On the PepHAR benchmark (success = AF2 complex **ipTM > 0.6**), no-hotspot peptide design: RFdiffusion+ProteinMPNN **25.38%**, ProteinGenerator **24.43%**, **PepFlow 27.96%** (best), **PepGLAD 14.05%**, PepHAR(K=3) 25.54% — [PepHAR, arXiv 2411.18463](https://arxiv.org/html/2411.18463v1)
- Hotspot-given scaffold generation: RFdiffusion 23.15%, PepFlow 24.54%, PepGLAD 14.85%, PepHAR 20–22% — [PepHAR, arXiv 2411.18463](https://arxiv.org/html/2411.18463v1)
- Inputs: PepFlow = flow-matching over **full-atom** peptides given target structure (hotspots can seed sampling); PepGLAD = geometric latent diffusion, target structure, no hotspot input described; PepHAR = target pocket sequence+structure, autoregressively extends from hotspots — [PepHAR, arXiv 2411.18463](https://arxiv.org/html/2411.18463v1)

**EvoBind / EvoBind2 (AF-guided in-silico evolution; Bryant & Elofsson)**
- Designs peptide binders from **sequence information only** (no bound structure) by iteratively mutating to minimize predicted receptor distance and maximize AF confidence; EvoBind2 extends to **cyclic** peptides via a cyclic-offset trick — [bioRxiv 2022.07.23.501214](https://www.biorxiv.org/content/10.1101/2022.07.23.501214.full.pdf); [PMC12280060](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12280060/)
- Reported **46% success linear, 75% cyclic**, affinities 0.26 nM–7.9 µM (secondary/product page — verify in paper) — [Neurosnap EvoBind2](https://neurosnap.ai/service/EvoBind2)
- EvoBindRare adds non-canonical amino acids via a new predictor "RareFold" — [Linköping project page](https://nim.nsc.liu.se/projects/7466)

**BoltzGen (universal all-atom binder; Nov 2025)**
- All-atom generative framework (Boltz lineage) for **proteins, nanobodies, peptides, and small-molecule-context** targets; validated across 8 wet-lab campaigns / 26 targets — [bioRxiv 2025.11.20.689494](https://www.biorxiv.org/content/10.1101/2025.11.20.689494); [PMC12697729](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12697729/)
- **~66% of 9 novel targets** yielded nM binders with ≤15 designs/target (nanobodies and proteins equal); **80% of 5 benchmark targets**; preprint version reports 60% (nanobody) / 50% (protein) — [bioRxiv 2025.11.20.689494](https://www.biorxiv.org/content/10.1101/2025.11.20.689494)
- Independent check (Adaptyv Nipah competition, third-party skills page): BoltzGen 6 binders / 182 tested = **~3% hit rate**, i.e. strongly target-dependent — [Tamarind blog](https://www.tamarind.bio/blog/boltzgen-validated-de-novo-binder-design-for-diverse-targets)

**Chroma (Generate:Biomedicines; Ingraham et al., Nature 2023)**
- Programmable all-atom generative model; **open-source code** but **weights gated** (API key, granted to academic/non-profit users) — implies restriction for commercial use — [GitHub generatebio/chroma](https://github.com/generatebio/chroma); [BusinessWire](https://www.businesswire.com/news/home/20231115950537/en/GenerateBiomedicines-Announces-Publication-of-its-Chroma-Model-in-Nature-A-Transformative-Generative-AI-for-Protein-Therapeutics)

**Genie2 (aqlaboratory; arXiv 2024)**
- Diffusion model for structure design with a **multi-motif scaffolding** framework (co-occurring motifs, unspecified relative placement); solves more motif-scaffolding problems with more diverse solutions than priors; **Apache-2.0**, code+weights freely available. Note: it is a backbone/scaffold generator, not a target-conditioned binder-design tool per se — [arXiv 2405.15489](https://arxiv.org/abs/2405.15489); [HF paper page](https://huggingface.co/papers/2405.15489)

**PepEDiff (structure-free; arXiv 2026)**
- Generates binder sequences in the latent space of a pretrained protein-embedding model given **target sequence + pocket residues** (no 3D structure of complex needed); showcased on the flat PPI target TIGIT — [arXiv 2601.13327](https://arxiv.org/abs/2601.13327)

**Licensing quick-reference (verify repo LICENSE before relying)**
- MIT: ProteinMPNN, BindCraft, Boltz-1/Boltz-2 (repo jwohlwend/boltz) — [Boltz MIT, secondary](https://www.skills.sh/jimliu/science-skills/boltz)
- BSD: RFdiffusion — [sourcepulse](https://www.sourcepulse.org/projects/875938)
- Apache-2.0: Genie2 — [HF](https://huggingface.co/papers/2405.15489); Chai-1 code+weights (secondary) — [search synthesis](https://skills.cat/skills/adaptyvbio/protein-design-skills/boltzgen)
- Open-source: RFdiffusion3 (per GEN) — [GEN](https://www.genengnews.com/topics/artificial-intelligence/rfdiffusion3-now-open-source-designs-dna-binders-and-advanced-enzymes)
- Gated weights (academic/non-profit): Chroma — [GitHub](https://github.com/generatebio/chroma)
- Non-commercial community license: ESM-3 (EvolutionaryScale Community License) — [search synthesis](https://www.cs.princeton.edu/courses/archive/spr26/cos598L/lectures/2026_02_17_lec4_bindcraft.pdf)
- Closed / not released: AlphaProteo — [nextomoro](https://nextomoro.com/alphaproteo/)

### Inferences
- For a competition requiring a runnable, permissively-licensed tool, the practical set is RFdiffusion(+ProteinMPNN+AF2), BindCraft, RFdiffusion3, Boltz-based design (BoltzGen/BoltzDesign1), Genie2, and the peptide diffusion models — AlphaProteo is excluded by closed access, and Chroma's gated weights complicate commercial use.
- Headline "success rates" are not comparable across tools: BindCraft/AlphaProteo/BoltzGen numbers are experimental wet-lab hit rates on curated favorable targets, while PepHAR's 14–28% are *in-silico* ipTM>0.6 pass rates. The Adaptyv Nipah 3% BoltzGen result shows experimental rates collapse on hard targets.

### Gaps
- RFdiffusionAA and RFdiffusion3 exact license/weight-redistribution terms were not confirmed in-session (search did not surface their LICENSE files; needs direct repo check).
- EvoBind2 and DiffPepBuilder headline success rates come from product pages / author preprints without independent replication.
- No peer-reviewed head-to-head benchmark places all these tools on one peptide-binder dataset; PepHAR (in-silico) and Overath (below) are the closest.

---

## KQ2 — Which methods handle DEEP / buried / occluded pockets vs only solvent-exposed surfaces? All-atom conditioning or partial/motif-scaffolding into a cavity?

### Takeaway
All-atom target conditioning plus motif/partial diffusion is the enabling combination for reaching into cavities. **RFdiffusionAA and RFdiffusion3** explicitly condition on buried ligand atoms (RFdiffusion3 has literal "buried-atom" pocket controls); **ODesign** adds a flexible mode that helps form pockets. The single most directly relevant demonstration is the **Baker-lab GPCR miniprotein paper (Muratspahić et al., 2025/2026)**, which reached deep class-A orthosteric 7TM pockets via "penetrating pentamer" motif-scaffolding and partial diffusion — but notably reached class-B receptors (GLP1R, GIPR, GCGR, CGRPR) only at the solvent-exposed **extracellular domain (ECD) surface**, not their deep 7TM core.

### Cited Findings

**GPCR miniprotein design (Muratspahić et al.) — directly on-point** (bioRxiv 2025.03.23.644666 → Nature 2026, 10.1038/s41586-026-10656-8) — [bioRxiv full text](https://www.biorxiv.org/content/10.1101/2025.03.23.644666v1.full); [Nature](https://www.nature.com/articles/s41586-026-10656-8)
- **Deep orthosteric-pocket strategy (class A, e.g. CXCR4, MRGPRX1):** short "penetrating" pentamer motifs are placed in the pocket first (motif-directed RFdiffusion), then scaffolded. For CXCR4, ~**1,000 pentamers generated and the 50 with the deepest insertion** were scaffolded. Membrane-facing hydrophobic residues were temporarily mutated to Gln during scaffolding to avoid membrane-crossing scaffolds. MetaGen scaffolds with **protruding elements (kinked helices, hairpins)** were used to reach recessed epitopes — [bioRxiv](https://www.biorxiv.org/content/10.1101/2025.03.23.644666v1.full)
- **Partial diffusion** (10/15/20 of 50 noising timesteps) refines a seeded pose toward the pocket — [bioRxiv](https://www.biorxiv.org/content/10.1101/2025.03.23.644666v1.full)
- **Surface strategy (class B, e.g. GLP1R, GIPR, GCGR, CGRPR, PTH1R):** designs bind the **soluble extracellular domain (ECD) surface** (steric hindrance), not the deep 7TM pocket. Targets truncated to the binding epitope from cryo-EM/crystal structures (GLP1R 5VAI, GIPR 7FIN/7FIY, GCGR 5XEZ, CGRPR 6E3Y; CXCR4 4RWS; MRGPRX1 active-state 8DWC/8DWG/8DWH) — [bioRxiv](https://www.biorxiv.org/content/10.1101/2025.03.23.644666v1.full)
- Tools used: RFdiffusion (motif-scaffolded, free, and partial diffusion), MetaGen (scaffolds mined from the AlphaFold metaproteome + Rosetta RIFdock), ProteinMPNN, FastRelax, AF2 initial-guess — [bioRxiv](https://www.biorxiv.org/content/10.1101/2025.03.23.644666v1.full)

**RFdiffusion3 — explicit burial controls**
- RFD3 documentation exposes `select_buried` atom controls: one example **fully buries a ligand in a tight pocket**; a variant leaves part of the ligand exposed for a more open pocket — [search synthesis / RFD3 docs](https://hpc.nih.gov/apps/rfd3.html)

**ODesign — pocket geometry sensitivity** (arXiv 2510.22304) — [arXiv](https://arxiv.org/html/2510.22304v1)
- Full-atom "world model"; supports **rigid mode** (true target coords fixed) and **flexible mode** (only internal target distances used). Flexible mode is argued to help "identification and formation of binding pockets." Atomic-level conditioning supported for atomic motif scaffolding — [ODesign arXiv](https://arxiv.org/html/2510.22304v1)
- States ligand binding is "inherently more geometry-sensitive … depends on shaping precise 3D pockets," contrasted with protein-protein binders that work best on "relatively flat, hydrophobic interfaces" — [ODesign arXiv](https://arxiv.org/html/2510.22304v1)

**RFdiffusion cropping caveat**
- Cropping a target to expose a pocket "might expose hydrophobic core residues that were previously buried," misleading the binder away from the intended site; defining hotspots biases diffusion back — [Neurosnap guide, secondary](https://neurosnap.ai/service/RFdiffusion-v2)

**Flat/polar (non-pocket) hard targets**
- For TNFR1 (a flat, polar surface lacking concave hydrophobic sites), RFdiffusion was adapted to produce backbones with more extended contact surfaces — the inverse problem to a deep pocket — [IPD/Science adp1779](https://www.ipd.uw.edu/publication-pdfs/338/57c2a48df8a45632376609ec32458886/science.adp1779.pdf)

### Inferences
- "Reaching into a cavity" in practice = (a) an all-atom target representation so the generator sees the pocket walls, plus (b) a motif/partial-diffusion scheme that *seeds a fragment inside the pocket* and grows a scaffold outward. The GPCR paper's penetrating-pentamer + scaffold is the clearest working template; RFdiffusionAA/RFdiffusion3's buried-atom conditioning is the general-purpose analogue for small-molecule-like pockets.
- For a **class B GPCR deep 7TM orthosteric pocket (e.g. GLP1R core)**, the published GPCR work did *not* demonstrate de novo insertion — it bound GLP1R at the ECD surface. The only demonstrated deep-7TM insertions were class-A receptors. This is a direct tool-selection signal: reaching the GLP1R peptide-binding core de novo is beyond what any cited method has shown experimentally.

### Gaps
- No method reports a controlled ablation isolating "pocket depth" as the independent variable for binder-design success.
- Whether RFdiffusion3's buried-atom control extends to *peptide-segment* insertion (vs small-molecule ligand burial) is not documented in sources seen.

---

## KQ3 — "Reachability" limits: difficulty of a flexible peptide segment inserting into a cavity vs perching on the rim. Quantitative benchmarks?

### Takeaway
There is **no standardized, named "reachability" benchmark** in the literature. The strongest quantitative evidence is indirect: within one consistent GPCR pipeline, deep class-A orthosteric-pocket campaigns show dramatically lower experimental yield (e.g., CXCR4: ~26,000 screened → 2 hits from a single backbone) than solvent-exposed ECD-surface campaigns, and co-fold confidence metrics systematically degrade for pocket/geometry-sensitive design. Flexible-target modeling (ODesign flexible mode) and partial diffusion are the levers reported to improve cavity reach.

### Cited Findings

**Yield gradient within the GPCR pipeline (same tools, different pocket depth)** — [bioRxiv 2025.03.23.644666](https://www.biorxiv.org/content/10.1101/2025.03.23.644666v1.full)
- **CXCR4 (deep class-A orthosteric pocket):** ~26,000 designs screened (biofloating) → only **2 hits, both from one backbone**; best binder dCX1_001 IC50 ~24 nM — the hardest, lowest-yield campaign.
- **MRGPRX1 (class-A orthosteric):** 13,000 screened → 91 selected → 50 expressed → 7 active at 10 µM; functional potencies reported 390 nM–1.4 µM (performance datapoints).
- **CGRPR (class-B ECD surface) via partial diffusion:** 78 expressed → **36 active in a one-point assay** (high yield); best dC2_049 IC50 4.5 nM.
- **GLP1R / GIPR / GCGR (class-B ECD surface):** ~10,000–18,000-member yeast libraries, 96 expressed each; GLP1R binders at 27 nM and 5.3 nM; GIPR/GCGR down to nanomolar–picomolar.
- Interpretation supported by the text: deep orthosteric insertion required bespoke seeding (deepest-insertion pentamer selection, protruding scaffolds), whereas exposed ECD surfaces behaved like conventional PPI-surface design.

**Design-model fidelity when insertion succeeds (cryo-EM)** — [bioRxiv 2025.03.23.644666](https://www.biorxiv.org/content/10.1101/2025.03.23.644666v1.full)
- MRGPRX1 designs: cryo-EM at 3.13–3.29 Å, ~**0.7 Å Cα RMSD** to design models; CGRPR design dC2_049: ~**1 Å Cα RMSD**. Successful deep-pocket binders match models at atomic accuracy — the difficulty is yield/reachability, not model fidelity once a hit is found.

**Geometry sensitivity quantified in silico (ODesign)** — [arXiv 2510.22304](https://arxiv.org/html/2510.22304v1)
- Ligand/pocket design success criterion (Chai-1 refold): **iPAE < 10 and complex pLDDT > ~0.7**; protein-binder criterion (AF3 refold): **iPAE < 10.85, ipTM/pLDDT above thresholds, complex RMSD < 2.5 Å**.
- ODesign vs RFdiffusionAA on 4 ligand-binding targets: **2.38× improvement**; vs BoltzDesign1: **1,142×**. ODesign-Flex "consistently surpassed" ODesign-Rigid — flexible-target modeling materially helps pocket formation.

**RFpeptides macrocycles into/against protein targets** — [bioRxiv 2024.11.18.622547](https://www.biorxiv.org/content/10.1101/2024.11.18.622547.full.pdf); [PMC12643943](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12643943/)
- Cyclic relative positional encoding added to RoseTTAFold2 + RFdiffusion; designability success = ≥1 of 8 LigandMPNN sequences refolds with **pLDDT > 0.8 and backbone RMSD < 2.0 Å**. Tested ≤20 macrocycles/target against 4 proteins → medium-to-high-affinity binders for all 4; X-ray **Cα RMSD < 1.5 Å** to models. (Rigid macrocycles are a route to cavity binding complementary to flexible linear peptides.)

### Inferences
- The implicit "reachability tax": within one pipeline, moving from an exposed ECD surface to a deep class-A 7TM pocket drops experimental yield by roughly 1–2 orders of magnitude (36/78 active for a surface campaign vs 2 hits/~26,000 screened for CXCR4). This is the best available quantitative proxy for cavity-insertion difficulty.
- A flexible linear peptide "perching on the rim" is the default failure mode; the mitigations that worked were (a) explicitly scoring/selecting for insertion depth before scaffolding, (b) partial diffusion from a pocket-seeded pose, and (c) rigidified scaffolds/macrocycles. These are concrete, transferable TOOL-SELECTION tactics.

### Gaps
- No paper defines a numeric "insertion depth" or "rim-vs-inserted" metric or benchmarks tools against it; the depth-selection step in the GPCR paper is bespoke, not a released benchmark.
- No quantitative study isolates flexible-peptide reach specifically into a *class-B GPCR* orthosteric 7TM pocket de novo.

---

## KQ4 — Which downstream filters / oracles best predict experimentally-confirmed binding for designed peptides/binders?

### Takeaway
The best-powered evidence (Overath meta-analysis, 3,766 experimentally-tested binders) finds **AF3 ipSAE_min is the single best confidence metric** for predicting experimental binding (~1.4× average precision over the AF2-initial-guess interface-PAE that RFdiffusion pipelines commonly filter on), but performance is **strongly target-dependent (AP ~0.1–1 across targets)** and no single metric dominates. In practice the recommended stack is: AF2 initial-guess (Bennett pAE_interaction) during generation, then rank with **ipSAE_min** (AF3/Boltz), optionally combined with Rosetta interface shape-complementarity. Notably that meta-analysis did **not** evaluate Boltz-2 or Chai-1.

### Cited Findings

**Overath et al. 2025 meta-analysis (bioRxiv 2025.08.14.670059)** — [bioRxiv full text](https://www.biorxiv.org/content/10.1101/2025.08.14.670059v1.full)
- Dataset: **3,766 de novo binders, 15 diverse targets, 436 (11.6%) confirmed binders** (imbalanced). Each complex re-predicted with **AF2 initial-guess, ColabFold, AF3, and Boltz-1**. **Boltz-2 and Chai-1 were NOT evaluated.**
- **Best single metric: AF3 ipSAE_min** (max-F1 threshold 0.61). It gave a **1.4× increase in average precision over AF2-initial-guess ipAE** (the metric RFdiffusion pipelines commonly filter on). Raw AP values are in figures only.
- **ipTM**: lower AP than ipSAE_min overall but competitive at low recall (ranked second at recall 0.2). **AF2 ipAE** underperformed AF3 ipSAE_min at all thresholds.
- Per-tool best features: ColabFold & Boltz-1 → ipSAE_min / ipSAE_max / LIS; AF2 initial-guess → ΔSAP.
- Interaction features: AF3 ipSAE_min × interface ΔG/ΔSASA (threshold ~−1.5); AF3 LIS × input interface shape complementarity (threshold 0.42). Greedy logistic regression median AP **0.57** (IQR 0.40–0.66); baseline LIS × shape complementarity **0.58** — **no learned model clearly beat the simple composite**; XGBoost gave no improvement.
- **Target dependence: AF3 ipSAE_min AP ranged ~0.1 to 1** across the 15 targets; top feature varied by target.
- Recommended filtering: (1) a single threshold — AF3 ipSAE_min > 0.61, or ipSAE_min × interface ΔG/ΔSASA < −1.5, or LIS × shape complementarity > 0.42; (2) pre-filter on input shape complementarity > 0.62 and binder RMSD < 3.73, then rank by AF3 ipSAE_min. ipSAE_min alone recovered ≥1 binder for all 15 targets at ~10 candidates/target; an RMSD-only filter missed binders for 2 targets. Minimal pipeline cut runtime 1802→230 s/design (87%).

**ipSAE metric itself (Dunbrack lab, 2025)** — [PMC11844409](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11844409/); [bioRxiv 2025.02.10.637595](https://www.biorxiv.org/content/10.1101/2025.02.10.637595.full.pdf)
- Argues AF ipTM is distorted by disordered/accessory regions (trimming a construct changes ipTM without changing the interface). Fix: use only residue pairs with good PAE, adjust the d0 term to count only well-aligned interchain residues, and use PAE values directly. Runs on AF2/AF3/Boltz outputs; repo **DunbrackLab/IPSAE**. Commonly cited ipSAE_min thresholds ~0.61 (standard) / 0.70 (stringent) (threshold figures from secondary skills pages).

**AF2 initial-guess (Bennett et al., Nat Commun 2023)** — [PMC10163288](https://pmc.ncbi.nlm.nih.gov/articles/PMC10163288); [Baker lab](https://www.bakerlab.org/2023/05/08/deep-learning-improves-protein-binder-design-tenfold/)
- Using AF2/RoseTTAFold to score (a) monomer self-consistency and (b) that the structure binds the target increases design success **~10×**; replaces Rosetta sequence design with ProteinMPNN for efficiency. **pAE_interaction** separates validated binders from non-binders; overall experimental success still <1% for some targets. A separate common threshold set: interface pAE < 10 and binder pLDDT > 85 (or >80) considered a pass.

**Boltz-2 (MIT + Recursion, June 2025)** — [boltz.bio/boltz2](https://boltz.bio/boltz2)
- First co-folding model to combine structure + **binding-affinity** prediction (separate regression head on pIC50/ΔG, MSE + rank loss); claims approach to FEP accuracy ~1000× faster; supports template/contact conditioning; MIT-licensed (repo jwohlwend/boltz). It is an affinity *predictor/oracle*, newer than the Overath evaluation window.

**Chai-1** — Apache-2.0 (secondary); used as the ligand-complex refolding oracle inside ODesign's pocket-design success criterion (iPAE/pLDDT) — [ODesign arXiv](https://arxiv.org/html/2510.22304v1)

**Independent cautions on confidence metrics**
- In the Adaptyv EGFR competition, **ipTM achieved AUROC only 0.64** for binding classification, and ipSAE showed a high false-positive rate on one AlphaSeq VHH dataset — metrics are not reliable in absolute terms — [AalphaBio critique, secondary](https://aalphabio.substack.com/p/overconfident-what-structure-prediction)

### Inferences
- The defensible oracle stack for designed peptides/mini-binders: generate+filter with **AF2 initial-guess pAE_interaction** (fast, proven ~10× enrichment), then **re-rank with AF3 (or Boltz) ipSAE_min**, optionally × Rosetta shape-complementarity/ΔG. Expect to recover ≥1 real binder per ~10 top-ranked designs, but calibrate the threshold per target because AP swings from ~0.1 to ~1.
- No oracle is a substitute for testing multiple designs: even the best metric's target-dependence and the EGFR AUROC 0.64 imply high false-positive risk; depth of sampling and per-target calibration matter more than metric choice.
- Boltz-2's affinity head and Chai-1 are plausible additions but were **not** in the largest head-to-head evaluation, so their predictive value for *designed* binders is not yet independently quantified at scale.

### Gaps
- Overath did not test Boltz-2 or Chai-1; no large meta-analysis yet benchmarks the 2025 affinity-aware co-folders as binder-design filters.
- Raw AP/AUROC numbers per metric in Overath are in figures not reproduced in the fetched text; only relative statements (1.4×, median AP 0.57) and thresholds were extractable.
- No oracle study is peptide- or GPCR-specific; the 15-target set is mostly soluble PPI targets, so transfer to deep-pocket GPCR peptide binders is unvalidated.

---

### Source index (primary identifiers)
- GPCR miniproteins: Muratspahić et al., bioRxiv 2025.03.23.644666 / Nature 2026 10.1038/s41586-026-10656-8
- Oracle meta-analysis: Overath et al., bioRxiv 2025.08.14.670059
- ipSAE: Dunbrack, bioRxiv 2025.02.10.637595 / PMC11844409 / DunbrackLab/IPSAE
- AF2 initial-guess: Bennett et al., Nat Commun 2023 (PMC10163288)
- BindCraft: Pacesa et al., Nature 2025 (bioRxiv 2024.09.30.615802 / PMC11642741)
- RFdiffusion3: bioRxiv 2025.09.18.676967 / PMC12458353
- BoltzGen: bioRxiv 2025.11.20.689494 / PMC12697729
- RFpeptides: bioRxiv 2024.11.18.622547 / PMC12643943 / Nat Chem Biol PMID 40542165
- ODesign: arXiv 2510.22304
- PepHAR (+PepFlow/PepGLAD baselines): arXiv 2411.18463
- DiffPepBuilder: arXiv 2405.00128
- AlphaProteo: arXiv 2409.08022
- EvoBind/EvoBind2: bioRxiv 2022.07.23.501214 / PMC12280060
- Genie2: arXiv 2405.15489
- PepEDiff: arXiv 2601.13327
- Boltz-2: boltz.bio/boltz2 (repo jwohlwend/boltz)
