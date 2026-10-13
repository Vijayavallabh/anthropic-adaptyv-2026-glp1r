# De Novo Generation Methods (2024–2026) for a GLP1R Agonist — Capability Evidence

Scope: generators/pipelines for de novo binders/agonists in the Track-3 allowed formats (protein 10–250 aa [micro <40 / mini 40–100 / large >100], nanobody, scFv, Fab), with emphasis on demonstrated **GPCR / membrane-protein / peptide-agonist** capability. Target = human GLP1R (P43220), a **class B1 GPCR**. Cutoff 2026-10-13. Status labels: **[PR]** peer-reviewed, **[pre]** preprint, **[dev]** developer/company claim (no paper or weights).

> **The single most important finding up front.** *Binding ≠ activation, and this gap is maximal for a class B GPCR.* GLP1R activation is a two-domain process: the receptor extracellular domain (ECD) captures the agonist's C-terminal helix (affinity), then the agonist **N-terminus must insert deep into the 7TM bundle** and trigger the TM6-outward / Gs-coupling conformational change (activation). A design that only engages the ECD or an arbitrary extracellular surface is, at best, an **antagonist**. The de novo field in 2024–2026 is overwhelmingly a **soluble-binder** field; agonism of any receptor is rare, and **de novo agonism of a class B GPCR has essentially one claimed precedent (EvoBind cyclic peptides, preprint, n=3).** Treat every "X% success" number below as a *binding/soluble* rate unless the row explicitly says agonism.

---

## EVIDENCE REGISTER

| Method | Citation / date / status | What it generates | Reported EXPERIMENTAL success rate (binding unless noted) | GPCR / membrane / peptide demonstrated? | Key limitation |
|---|---|---|---|---|---|
| **EvoBind** (cyclic peptide GLP1R/GCGR agonists) | Li/Bryant, bioRxiv 2025.06.06.658268, Jun 2025 **[pre]** | De novo **cyclic peptides** from target *sequence only* (AF2 + cyclic offset, no structure) | **AGONIST**: 3 synthesized → all 3 activate GLP1R; best 18-mer **EC50 32 nM (GLP1R)**, 542 nM GCGR (cAMP) | **YES — GLP1R AGONIST, class B GPCR, peptide.** The only direct precedent | n=3 (not a rate); preprint, one lab; **macrocyclic** (format-eligibility risk); no SPR/affinity, no in vivo |
| **Baker GPCR miniproteins** (RFdiffusion + MetaGen) | Baker lab, bioRxiv 2025.03.23.644666 / PMC12157396, Mar 2025 **[pre]** | Mini-proteins vs GPCRs; motif-scaffolded RFdiffusion + Rosetta RIFdock on metaproteome | MRGPRX1 **AGONIST** (class A): 7 agonists / 50 expressed (~14%); 2 full (EC50 390 nM, 1 µM). **GLP1R = ANTAGONIST only** (ECD): IC50 39–61 nM | **YES for GPCRs** incl. GLP1R/GIPR/GCGR — but **class B = antagonists/ECD binders; agonism only for class A MRGPRX1** | For class B they targeted the ECD → **no activation**; agonism needs the deep 7TM pocket they only reached on an easy class A receptor |
| **RFdiffusion** (1) | Watson et al., Nature 2023 **[PR]** | Protein backbones (binders) from target structure + optional hotspots | Soluble binders ~0.1–10% depending on target; independent audits report low rates on hard/functional targets | Membrane/GPCR: only via the Baker GPCR paper's motif-scaffold variant. Peptides: no (backbone) | Flat/polar & deep-pocket targets fail; "binding ≠ function" (biochemical-detection audit, bioRxiv 2025.02.07.636769) |
| **RFdiffusion2** | Nature Methods 2025 (s41592-025-02975-x); bioRxiv 2025.04.09.648075 **[PR]** | **Atom-level motif / active-site scaffolding** (residue indices unknown) — enzymes | 41/41 active sites scaffolded in silico (vs 16 prior); some in vitro catalysis | No GPCR/membrane/peptide-binder demo — built for enzymes | Not a binder/agonist tool per se; best-in-class **motif-scaffolding engine** |
| **RFdiffusion All-Atom (RFAA)** | Krishna et al., Science 2024 **[PR]** | Backbones conditioned on **small molecules / non-protein** context | Small-molecule-binding proteins (low %); no GPCR/membrane | Peptide: no. Small-molecule: yes | Not demonstrated on membrane receptors |
| **RFpeptides** | Rettie et al., Nat Chem Biol 2025 (s41589-025-01929-w); pre 2024.11.18 **[PR]** | De novo **macrocyclic peptide** binders (RF2 + RFdiffusion) | 4/4 **soluble** targets bound with ≤20 macrocycles/target; GABARAP 6 nM; MCL1 2 µM (21% hit), MDM2 low-µM (38% hit) | Peptide: **YES (macrocycle)**. GPCR/membrane: **NO** — all soluble intracellular targets | Soluble-protein targets only; macrocyclic (format risk); µM on 2/4 |
| **Latent-X** | Latent Labs, arXiv 2507.19375, 2025 **[dev]** | Atom-level binders incl. macrocycles & minibinders | Macrocycles: 91% (MDM2), 100% (MCL1) hit; minibinder hits reported | Peptide/macrocycle: yes (soluble). GPCR: no | Company model; soluble targets; access/weights gated |
| **BindCraft** | Pacesa et al., Nature 2025 (s41586-025-09429-6); pre 2024.09 **[PR]** | One-shot binders by AF2 hallucination/backprop | **10–100%** across targets (developer range); e.g. BBF-14 6/11 (55%) | Soluble only in paper; no GPCR/membrane/agonist | Range is per-target; struggles on polar/featureless & novel folds; binding not function |
| **ProteinMPNN / LigandMPNN** | Dauparas et al., Science 2022 / Nat Methods 2025 **[PR]** | **Sequence** design on a fixed backbone (LigandMPNN adds ligand/NA/metal context) | Not a generator of binding geometry; ubiquitous in every pipeline below | Used in Baker GPCR + Wei semaglutide redesign; peptide seqs yes | Needs a backbone/complex as input; does not create a binding mode |
| **BoltzGen** | Stark et al., bioRxiv 2025.11.20.689494, Nov 2025 **[pre]** | All-atom **universal** binder design (protein **and peptide**) vs protein/NA/small-mol targets | **nanomolar binders for 66% of 26 targets** (8 wet-lab campaigns) | Peptide: **YES**. GPCR/membrane: **not demonstrated** (targets dissimilar from known structures, but soluble) | Very new; no GPCR/agonist; TNFα in-silico success = 0 in SeedProteo benchmark (hard targets still fail) |
| **BoltzDesign1** | Cho et al., bioRxiv 2025 **[pre]**; MIT license | Hallucination by inverting Boltz predictor + MPNN | **Not experimentally validated** | No | Single-chain (multi-chain WIP); unvalidated |
| **PXDesign / Protenix-design** | ByteDance Seed, bioRxiv 2025 **[dev/pre]** | Diffusion (PXDesign-d) + hallucination (PXDesign-h) on Protenix (AF3-repro) + confidence filter | **20–73% nanomolar across 5/6 soluble targets** (claims > AlphaProteo) | No GPCR/membrane; peptide not the focus | Soluble benchmark targets; developer-reported |
| **Chroma** | Ingraham et al., Nature 2023 **[PR]** | Programmable all-atom generation (shape/symmetry/substructure conditioners) | No head-to-head experimental binder hit rate; proof-of-concept expression/folding | No GPCR/membrane/agonist | General generator, not a validated binder pipeline |
| **Genie2 / Genie3** | Genie2 arXiv 2405.15489 (2024) **[pre]**; Genie3 EuroHPC 2025 **[pre]** | SE(3) backbone diffusion; **motif scaffolding** + (Genie3) binder design | In-silico metrics; no published experimental GPCR/binder rate | No | Experimental validation sparse; Genie3 details unverified |
| **Pallatom / Pallatom-Ligand** | Qu et al., ICML 2025 / ICLR 2026 **[pre]** | All-atom joint structure+sequence generation | In-silico designability/novelty; no experimental binder rate found | No | No experimental binder/GPCR data located |
| **Protpardelle** | Chu et al., 2024 **[pre/PR]** (not re-verified this session) | All-atom unconditional co-design | No experimental binder/GPCR validation located | No | Unconditional generator; not a target-conditioned binder tool |
| **Proteina-Complexa** | NVIDIA/ManifoldBio, ICLR 2026 **[pre]**; open weights | Atomistic flow-matching binders + test-time compute | "Markedly higher in-silico success" than RFd/BindCraft on 19 soluble targets | No GPCR/membrane | In-silico only; soluble benchmark |
| **SeedProteo** | ByteDance Seed, arXiv 2512.24192, Dec 2025 **[pre]** | All-atom diffusion binders (target mmCIF + hotspots) | **70–80% wet-lab** on PD-L1 / SARS-CoV-2 RBD (soluble) | No GPCR/membrane; webserver-only | Webserver only; soluble targets |
| **RFantibody** | Bennett et al., Nature 2025 (s41586-025-09721-5); pre 2024 **[PR]** | De novo **VHH / scFv / Fab** to a target structure + **chosen epitope** (RFdiffusion→MPNN→RF2 filter) | **Low single-digit %** experimental (secondary coverage cites ~0–2%); emphasizes cryo-EM validation over hit rate | Epitope-targeting: **YES**. GPCR epitope: **not experimentally demonstrated**; no agonism | Low hit rate; small GPCR extracellular epitopes are hard; binding only |
| **Germinal** | Milla/Ovchinnikov et al., bioRxiv 2025.09.19.677421; PMC12485712 **[pre]** | Epitope-targeted de novo **nanobodies / scFvs** onto user framework | **4–22% across 4 soluble targets** (43–101 designs each), nanomolar | Nanobody/scFv: yes; GPCR: no; no agonism | Soluble targets; antibody format = Cys/disulfides |
| **Chai-2** | Chai Discovery, Jun 2025 **[dev]** (no paper/weights) | Zero-shot de novo CDRs (antibody/VHH) **and miniproteins** from epitope | **16–20% across 52 antigens** at 20/target; 5/5 miniprotein targets | Antibody+miniprotein; GPCR not reported; no agonism | Closed (platform only); binding not function |
| **JAM-2** | Nabla Bio, 2025 **[dev]** | Computational antibody design | **~39% across 16 unseen targets** (developer); notes membrane/multipass targets as a focus | Claims hard targets incl. membrane; **no public GPCR-agonist data** | Developer white paper; no agonism |
| **AlphaProteo** | Google DeepMind, Sep 2024 **[dev]** (no paper/weights) | Mini-binder generator | **9–88% on 7/8 soluble targets**; IL-17A ~700× over prior; pM binders | Soluble only; no GPCR/membrane/agonist | Closed (trusted-tester); binding only |
| **EvoBind2 / AfCycDesign / DiffPepBuilder** | 2024–2025 **[pre]** | Cyclic/linear **peptide** binders (AF2 cyclic-offset / diffusion) | Peptide-scale binders (various) | Peptide: yes; GPCR agonism: only via EvoBind (above) | Mostly binders not agonists |
| **Wei et al. "de novo GLP-1RA"** ⚠️ | Advanced Science 2025 (advs.202507044); pre 2025.03.26 **[PR]** | ProteinMPNN redesign of **semaglutide** (fixed backbone, PDB 7KI0) | **AGONIST**: 52% bound (31/60); leads D13/D41/D44 EC50 0.011–0.036 nM; ~3× half-life vs sema in vivo | GLP1R agonist — **but see limitation** | **NOT DE NOVO / NOT ELIGIBLE**: template = semaglutide, 13 sites fixed, **0.68–0.81 identity to semaglutide** → this is "modify semaglutide into a candidate," the forbidden path |

*Non-GPCR de novo agonist precedents (mechanism reference, not GLP1R-applicable): insulin receptor agonists (Mol Cell 2025, PMC12702617) by RTK clustering; "Novokines" cytokine mimetics (bioRxiv 2025.10.12, PMC12632978) 75/>1000 activated pSTAT; G-CSFR agonists (bioRxiv 2023.11.25.568662).*

---

## Q1. SOTA generators — inputs, outputs, experimental validation, peptide / membrane capability

### Takeaway
The de novo generator ecosystem is mature for **soluble** protein-protein binders (BindCraft, PXDesign, BoltzGen, AlphaProteo, Chai-2, Proteina-Complexa all report 10–88% soluble hit rates) and now covers **de novo peptides/macrocycles** (RFpeptides, Latent-X, BoltzGen, EvoBind, DiffPepBuilder). **None has an experimentally demonstrated membrane-protein / GPCR binder except the Baker GPCR miniprotein pipeline (RFdiffusion+MetaGen) and EvoBind (peptides).** Every headline rate is a *binding/soluble* rate, not an agonist rate, and is reported on each group's own (mostly easy, soluble) benchmark.

### Cited Findings
- **RFpeptides** (macrocyclic peptide binders): RF2+RFdiffusion pipeline; ≤20 macrocycles/target gave medium–high affinity binders against **4 diverse soluble proteins** (MCL1, MDM2, GABARAP, RbtA); GABARAP 6 nM, MCL1 2 µM; crystal structures <1.5 Å Cα RMSD to models. Peer-reviewed Nat Chem Biol 2025. — [Nature Chem Biol](https://www.nature.com/articles/s41589-025-01929-w); [bioRxiv PDF](https://www.biorxiv.org/content/10.1101/2024.11.18.622547.full.pdf); hit rates 21% (MCL1)/38% (MDM2) — [Latent-X arXiv](https://arxiv.org/html/2507.19375v1)
- **BindCraft**: one-shot AF2-hallucination binders; developer-reported **10–100%** experimental success (range across targets), nanomolar, published Nature 2025; Rosetta baseline <0.1%. Vendor example BBF-14 = 6/11 (55%). — [Nature](https://www.nature.com/articles/s41586-025-09429-6); [Tamarind docs](https://docs.tamarind.bio/tools/bindcraft)
- **BoltzGen**: all-atom universal binder/peptide designer unifying design+folding; **nanomolar binders for 66% of 26 targets** across 8 wet-lab campaigns; targets chosen dissimilar from known structures; open MIT (weights+code). Preprint Nov 2025. — [bioRxiv](https://www.biorxiv.org/content/10.1101/2025.11.20.689494v1); [MIT Jameel](https://jclinic.mit.edu/boltzgen/)
- **PXDesign** (ByteDance/Protenix): diffusion + hallucination + confidence filter; **20–73% nanomolar across 5/6 soluble targets**, claims to surpass AlphaProteo; open. — [ByteDance Seed](https://seed.bytedance.com/en/public_papers/pxdesign-fast-modular-and-accurate-de-novo-design-of-protein-binders)
- **AlphaProteo** (DeepMind, closed): **9–88% on 7/8 soluble targets**, IL-17A ~700× over prior, picomolar binders on 4 targets. — [coverage](https://gigazine.net/gsc_news/en/20240906-google-deepmind-alphaproteo/)
- **RFdiffusion2**: atom-level **motif/active-site scaffolding** without pre-assigned residue indices; scaffolded **41/41** enzyme active sites in silico (vs 16 prior) with in vitro catalysis; Nature Methods 2025. (Best-in-class scaffolding engine — relevant to Q3.) — [Nature Methods](https://www.nature.com/articles/s41592-025-02975-x); [bioRxiv](https://www.biorxiv.org/content/10.1101/2025.04.09.648075v1.full)
- **RFdiffusionAA**: RoseTTAFold-All-Atom fine-tune; backbones conditioned on **small molecules** — not membrane proteins. — [Science 2024 (Krishna)](https://www.science.org/doi/10.1126/science.adl2528) *(DOI from training knowledge; verify)*
- **Latent-X**: atom-level frontier model; macrocycle hit rates **91% (MDM2), 100% (MCL1)** — soluble. — [arXiv 2507.19375](https://arxiv.org/html/2507.19375v1)
- **Proteina-Complexa** (NVIDIA/ManifoldBio, ICLR 2026, open weights): atomistic flow-matching + test-time compute; "markedly higher in-silico success" than RFdiffusion, test-time search beats BindCraft on a **19-target soluble** benchmark. — [NVIDIA GenAIR](https://research.nvidia.com/labs/genair/proteina-complexa)
- **SeedProteo** (ByteDance, Dec 2025): all-atom diffusion, target mmCIF+hotspots; **70–80% wet-lab on PD-L1 / SARS-CoV-2 RBD** (soluble); webserver only. — [arXiv 2512.24192](https://arxiv.org/html/2512.24192v2)
- **Independent caveat on RFdiffusion**: a 2025 audit found a **low success rate** designing functional binders for biochemical detection, concluding RFdiffusion "may not substitute for conventional" antibody generation. — [bioRxiv 2025.02.07.636769](https://www.biorxiv.org/content/10.1101/2025.02.07.636769.full.pdf)
- **β-pairing targeted RFdiffusion** (Nat Commun 2025): conditions RFdiffusion to form edge-β-strand pairing with polar targets; 137 pM–mid-nM binders; **explicitly notes its targets are NOT lipid-embedded membrane proteins**. — [Nat Commun](https://www.nature.com/articles/s41467-025-67866-3)

### Inferences
- For GLP1R, the generator's *codebase* matters far less than **what it is pointed at and whether the output can reach the 7TM pocket.** Soluble-benchmark hit rates (even 66–88%) do not transfer to a class B GPCR orthosteric pocket.
- **Peptide/micro-protein generators (EvoBind, RFpeptides, BoltzGen-peptide, DiffPepBuilder) are the only family with a plausible path into the 7TM pocket**, because a small peptide N-terminus can physically insert where a 60–120 aa folded mini-protein cannot (the Baker paper's own class B designs could not and became ECD antagonists).

### Gaps
- No generator except EvoBind and the Baker pipeline reports *any* experimental GPCR result; BoltzGen/PXDesign/AlphaProteo/Chai-2/Proteina-Complexa GPCR capability is **unknown, not demonstrated**.
- Protpardelle, Pallatom, Genie3 have no experimental binder validation located this session.
- RFdiffusionAA Science 2024 DOI cited from training knowledge, not re-verified this session.

---

## Q2. RFantibody & de novo antibody / nanobody / scFv / Fab — epitope-targeting and GPCR capability

### Takeaway
RFantibody (and Germinal, Chai-2, JAM-2) **can be pointed at a defined epitope**, which is exactly what a GPCR campaign needs, but (a) experimental hit rates are **low** (RFantibody ~0–2%; Germinal 4–22%; Chai-2 16–20%; JAM-2 ~39% developer), (b) **no de novo antibody has been experimentally validated against a GPCR extracellular epitope**, and (c) **an antibody/nanobody binding a GPCR's small extracellular loops would be an antagonist/modulator, not an agonist** — agonism requires reaching the 7TM core, which a bulky Ig fold cannot do. Antibody formats are a weak fit for *agonism* specifically.

### Cited Findings
- **RFantibody** (Bennett et al., Nature 2025): RFdiffusion(antibody-finetuned)→ProteinMPNN→RF2 filter; designs **VHH/scFv/Fab** from target structure + **desired epitope**; free incl. commercial. Experimental hit rates **low** — secondary coverage cites **0–2% across targets**, and that stronger AF3-ipTM filtering may help; the paper emphasizes **cryo-EM structural validation** over raw hit rate. — [Nature](https://www.nature.com/articles/s41586-025-09721-5); [phys.org](https://phys.org/news/2025-11-ai-antibodies.html); [IPD](https://www.ipd.uw.edu/2025/11/rfantibody-in-nature)
- **Germinal**: epitope-targeted de novo **nanobodies/scFvs** onto a user framework; **4–22% across 4 soluble targets**, nanomolar, good expression; open. — [bioRxiv PDF](https://www.biorxiv.org/content/10.1101/2025.09.19.677421.full.pdf); [PMC12485712](https://pmc.ncbi.nlm.nih.gov/articles/PMC12485712/)
- **Chai-2** (closed): zero-shot de novo CDRs + miniproteins from epitope; **16–20% across 52 antigens** at 20 designs/target; 5/5 miniprotein targets. — [Chai](https://www.chaidiscovery.com/news/introducing-chai-2)
- **JAM-2** (Nabla Bio, developer): **~39% across 16 unseen targets**; markets hard/membrane multipass targets as a focus. — [Nabla white paper](https://nabla-public.s3.us-east-1.amazonaws.com/2025_Nabla_JAM2.pdf)
- **Epitope-specific antibody workflow** (Nat Commun 2025): structure-driven de novo epitope-targeted antibodies — confirms epitope-targeting is an active, publishable capability. — [Nat Commun s41467-025-67361-9](https://www.nature.com/articles/s41467-025-67361-9)
- **In the Baker GPCR paper, the GPCR binders were mini-proteins, not antibodies** — and for the class B receptors (GLP1R/GIPR/GCGR) they bound the **ECD** and acted as **antagonists**, not agonists. — [PMC12157396](https://pmc.ncbi.nlm.nih.gov/articles/PMC12157396/)

### Inferences
- A de novo nanobody/scFv/Fab to a defined GLP1R ECD or ECL epitope is **technically buildable** (RFantibody/Germinal/Chai-2 all support epitope targeting) but should be expected to **block or modulate, not activate** — the Ig fold cannot occupy the 7TM orthosteric pocket that drives class B activation.
- If the challenge is scored purely on *agonism*, antibody formats are the **least promising** of the allowed formats; they are only attractive if a positive allosteric / active-state-stabilizing mechanism from outside the pocket is viable (speculative for GLP1R; see Q4).

### Gaps
- Exact per-target RFantibody experimental numbers are from secondary coverage, not the primary table (verify in Nature paper).
- No evidence any de novo antibody has bound a GPCR experimentally, let alone agonized one.

---

## Q3. Motif scaffolding / partial diffusion of an agonist pharmacophore — and the de-novo / eligibility line

### Takeaway
Scaffolding a short functional motif onto a novel scaffold is a **solved capability** (RFdiffusion2 atom-level, RFdiffusion motif mode, La-Proteina, Genie, SALAD, ProteinGenerator inpainting). The scientific risk is that **the only motif known to *activate* GLP1R is the GLP-1/exendin N-terminal pharmacophore itself** — so scaffolding "a GLP-1-like N-terminal pharmacophore" lands you directly on the forbidden side of the eligibility line. The Wei et al. paper is the cautionary archetype: titled "de novo" but actually a semaglutide redesign with 68–81% identity.

### Cited Findings
- **Motif-scaffolding tools exist and work experimentally**: RFdiffusion2 scaffolded 41/41 enzyme active sites (atom-level, no residue-index pre-assignment) with in vitro catalysis — [Nature Methods](https://www.nature.com/articles/s41592-025-02975-x). La-Proteina does **atomistic motif scaffolding** (build a protein around a predefined functional site) — [NVIDIA Research](https://research.nvidia.com/labs/genair/publication/laproteina2025/). SALAD, Genie2/3 scaffold functional motifs — [SALAD bioRxiv](https://www.biorxiv.org/content/10.1101/2025.01.31.635780.full.pdf); [Genie2 arXiv](https://arxiv.org/html/2405.15489v1).
- **The Baker GPCR paper used motif-scaffolded RFdiffusion with ECD hotspots** (GLP1R hotspot **L95**, GIPR M32, GCGR F33/W36/W87) — i.e., scaffolding onto the *receptor's* hotspots, which produced **antagonists** (ECD binders), not agonists. — [PMC12157396](https://pmc.ncbi.nlm.nih.gov/articles/PMC12157396/)
- **Partial diffusion** (noise-and-redenoise an existing design) is standard across RFdiffusion/ProteinGenerator/ODesign/SALAD for carrying over a pose while regenerating around it. — [ODesign arXiv](https://arxiv.org/abs/2510.22304v2)
- **FORBIDDEN archetype — Wei et al. "AI-Driven De Novo GLP-1RA"**: used the **semaglutide–GLP1R complex PDB 7KI0 as template**, **fixed 13 conserved sites** (incl. semaglutide's 8-Aib, 26K, 34R), ProteinMPNN-redesigned the other 18 of 31 residues; lead **D13 = 0.81 sequence recovery (identity) to semaglutide**, D41 0.74, D44 0.68; retained the semaglutide α-helix backbone and C20 lipidation. — [PMC12561408](https://pmc.ncbi.nlm.nih.gov/articles/PMC12561408/)
- **DEFENSIBLE archetype — EvoBind GLP1R agonists**: designed from **receptor sequence only**, "**designed sequences show no similarity to known agonists**," novel binding mode "compatible with active-state stabilisation." — [bioRxiv abstract](https://www.biorxiv.org/content/10.1101/2025.06.06.658268v1)

### Inferences
- **Where the line falls (my read):** A design is *defensibly de novo* when (i) its sequence has no significant identity to GLP-1/exendin/glucagon/semaglutide (EvoBind: "no similarity"), and (ii) its backbone/scaffold is generated, not grafted from the native hormone. It becomes a *modified known binder* (forbidden) when it (a) fixes native agonist residues as a motif, (b) uses the native agonist–receptor complex as the design template/backbone (Wei: 7KI0), or (c) retains high sequence identity to the native hormone.
- **The genuine dilemma:** The GLP1R *activation* pharmacophore (the agonist N-terminus His7/Ala8/Glu9/Gly10/Thr11… reaching TM6/TM7) is extremely specific. If a de novo design must recreate those exact contacts to activate, it will tend to converge toward the native motif and risk the eligibility line. EvoBind's claim is important precisely because it reports activation **without** reusing the native sequence — if that holds up, *a learned/search-based method that rediscovers an activating surface de novo is the only clean route to an eligible agonist.* Motif-grafting the GLP-1 N-terminus is the opposite: high activation odds, but likely ineligible.
- Scaffolding is therefore better aimed at **affinity/ECD engagement + a de-novo-discovered activating contact**, not at transplanting the GLP-1 pharmacophore verbatim.

### Gaps
- No published, eligibility-clean example of scaffolding a *non-native* activating motif onto a GLP1R binder (EvoBind discovers rather than scaffolds).
- The challenge's exact novelty threshold (sequence % identity, TM cutoff) is not in these sources; the Adaptyv/Proteinbase novelty metric (≤30% seq id AND low TM for 4/4) is the nearest reference from the TNF project's notes.

---

## Q4. Biasing toward the active-state 7TM pocket / extracellular vestibule — functional / active-state-conditioned generation

### Takeaway
There is **no generator with a learned "agonism" or "active-state" objective.** "Active-state conditioning" in practice means **choosing an active-state (agonist-/G-protein-bound) cryo-EM structure as the design target and hoping that stabilizing it yields agonism.** This worked for a class A peptide GPCR with an accessible pocket (MRGPRX1), produced only antagonists for class B GPCRs (the ECD was targeted instead), and EvoBind's peptides reportedly hit "the activation surface" by blind sequence search.

### Cited Findings
- **Baker MRGPRX1 agonists were designed against 3 active-state structures** on the hypothesis that "stabilizing the active state alone would be enough for agonism," targeting the **orthosteric pocket spanning TM2–TM7**; 2 full + 1 partial agonist resulted; cryo-EM confirmed active-state binding (~0.7 Å Cα RMSD). — [PMC12157396](https://pmc.ncbi.nlm.nih.gov/articles/PMC12157396/)
- **For class B (GLP1R/GIPR/GCGR) the same study targeted the ECD** (not the 7TM core) and obtained **antagonists/binders only**; the authors explicitly contrast "deeper orthosteric targeting for class A" vs "ECD-directed design for class B." — [PMC12157396](https://pmc.ncbi.nlm.nih.gov/articles/PMC12157396/)
- **CXCR4 antagonists** were designed to engage ECLs + deeper TM to stabilize the **inactive** state — demonstrating conformational-state biasing is just structure choice. — [PMC12157396](https://pmc.ncbi.nlm.nih.gov/articles/PMC12157396/)
- **EvoBind** "consistently identified the receptor's activation surface" and produced peptides adopting "novel binding modes **compatible with active-state stabilisation**" — but via blind sequence-only search, not an explicit active-state objective. — [bioRxiv abstract](https://www.biorxiv.org/content/10.1101/2025.06.06.658268v1)
- **Review framing**: a recognized direct agonism strategy is "designing a binder that **stabilizes a receptor's active conformation**"; others cluster receptors with de novo oligomeric scaffolds (e.g., CD137). — [de novo review PMC12958671](https://pmc.ncbi.nlm.nih.gov/articles/PMC12958671/)
- **Non-GPCR proof that active-conformation stabilization → agonism**: insulin receptor de novo agonists (rigid linkage = full activation, flexible = partial) — [Mol Cell 2025 / PMC12702617](https://pmc.ncbi.nlm.nih.gov/articles/PMC12702617/); Novokines fused binders → 75/>1000 activated pSTAT — [PMC12632978](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12632978/).

### Inferences
- **Practical recipe to bias toward activation on GLP1R:** use an **agonist-bound active-state GLP1R cryo-EM structure** (there are many; GLP-1– and semaglutide–GLP1R–Gs complexes) as the design target, and **condition/hotspot the design onto 7TM-core residues that the agonist N-terminus contacts** — not the ECD. The Baker result predicts this is *necessary* for agonism but is *much harder* for class B than class A (they did not attempt it for class B).
- **Receptor-clustering agonism (insulin receptor / Novokines) does not transfer to GLP1R**: GLP1R signals as a monomer via an intramolecular conformational switch, so dimerizing/clustering scaffolds are not an agonism route here.
- The cleanest demonstrated route to GLP1R activation remains a **small peptide/micro-protein that inserts into the 7TM pocket** (EvoBind), because folded mini-proteins/antibodies cannot physically reach it.

### Gaps
- No tool exposes a trainable "agonist" reward; active-state biasing is entirely manual (structure + hotspot choice).
- No published de novo **folded-protein** (non-peptide) agonist of a class B GPCR exists — the class B 7TM pocket has only been activated de novo by a cyclic peptide (EvoBind, preprint).

---

## Q5. Experimental reality — hit rates, designs per hit, dominant failure modes

### Takeaway
On GPCRs specifically, expect **large display libraries → few hits → even fewer agonists**: the one GPCR agonist campaign screened **~13,000 designs to get 7 (partial/full) agonists among 50 expressed**. On soluble targets, modern tools need only **~20–100 designs/target** for a binder, but that economy **has not been shown to transfer to GPCRs/agonism.** Dominant failure modes: binding without activation, inability to reach the 7TM pocket, partial (not full) agonism, expression/solubility, and oligomerization.

### Cited Findings
- **GPCR agonist campaign economics** (Baker MRGPRX1, class A): **~13,000 designs screened** (OPS-RD), 91 characterized, 50 expressed → **7 agonists at 10 µM (14% of expressed), 2 full + 1 partial**; class B used ~12,000–18,000-member yeast libraries → only binders/antagonists. — [PMC12157396](https://pmc.ncbi.nlm.nih.gov/articles/PMC12157396/)
- **Soluble-target economics**: Chai-2 **16–20% at 20 designs/target**; Germinal **4–22% at 43–101 designs**; BindCraft **10–100%**; BoltzGen **66% of targets**; RFantibody **~0–2%** (needs high-throughput screening). — [Chai](https://www.chaidiscovery.com/news/introducing-chai-2); [Germinal](https://www.biorxiv.org/content/10.1101/2025.09.19.677421.full.pdf); [BindCraft Nature](https://www.nature.com/articles/s41586-025-09429-6); [BoltzGen](https://jclinic.mit.edu/boltzgen/)
- **EvoBind GLP1R agonist**: only **3 peptides synthesized**, all 3 activated GLP1R, best EC50 32 nM — a proof-of-concept n, not a throughput-characterized rate. — [bioRxiv abstract](https://www.biorxiv.org/content/10.1101/2025.06.06.658268v1)
- **Meta-analysis (3,766 characterized binders)**: success is "very inconsistent," no standard prioritization criteria; interface metric **ipSAE** beats ipTM/ipAE for predicting success (1.4× AP). — [bioRxiv 2025.08.14.670059](https://www.biorxiv.org/content/10.1101/2025.08.14.670059.full.pdf)
- **Failure modes observed**: partial-only agonism with unresolved structural basis; oligomerization of some GPCR binders affecting pharmacology; modest hit rates (7/50 agonists; 4/83 MetaGen antagonists); flat/polar & deep pockets fail for backbone generators. — [PMC12157396](https://pmc.ncbi.nlm.nih.gov/articles/PMC12157396/); [RFdiffusion audit](https://www.biorxiv.org/content/10.1101/2025.02.07.636769.full.pdf)

### Inferences
- **Order-of-magnitude planning for a GLP1R agonist**: if following the peptide route, EvoBind-style generation + heavy in-silico filtering (AF3/Boltz cofold + cAMP-proxy ranking) then **order tens of candidates** and expect agonists to be rare; if following a mini-protein/antibody route, expect binders but **low-to-zero agonists** without explicit 7TM-pocket targeting.
- The field has no reliable **in-silico agonism predictor**; structure predictors are "trigger-blind," so computational ranking will select for *binding*, not *activation* — a specific risk for this challenge.

### Gaps
- No throughput-level agonist hit rate exists for class B GPCRs; the only numbers are class A (MRGPRX1) and the n=3 EvoBind GLP1R result.

---

## (A) Takeaways — ranked generator shortlist per allowed format

1. **Micro-protein (<40 aa) / peptide — STRONGEST path to agonism.** Rank: **(1) EvoBind/EvoBind2** — the *only* method with a reported **de novo, sequence-novel GLP1R agonist** (18-mer, EC50 32 nM; "no similarity to known agonists") — eligibility-clean but **cyclic** (confirm macrocycle is an allowed format; a *linear* ≤40-mer micro-protein is explicitly allowed). **(2) BoltzGen (peptide mode)** and **(3) RFpeptides / DiffPepBuilder** as alternative peptide generators (no GPCR agonism shown; RFpeptides is soluble-only + macrocyclic). *A small peptide is the only format physically able to insert into the class B 7TM pocket.* [EvoBind](https://www.biorxiv.org/content/10.1101/2025.06.06.658268v1)

2. **Mini-protein (40–100 aa).** Rank: **(1) Baker GPCR pipeline = motif-scaffolded RFdiffusion + MetaGen (RIFdock) + ProteinMPNN + AF2-ig**, pointed at an **active-state agonist-bound GLP1R cryo-EM structure with 7TM-core hotspots** (the only pipeline with any GPCR experimental validation; but note it yielded class B **antagonists**, so agonism here is unproven and hard). **(2) BindCraft / PXDesign / BoltzGen** for raw binder generation + confidence filtering (soluble-validated only). Expect these to bind/antagonize, not activate, unless 7TM targeting succeeds. [PMC12157396](https://pmc.ncbi.nlm.nih.gov/articles/PMC12157396/)

3. **Large protein (>100 aa).** Lowest agonism odds — a large fold cannot reach the 7TM pocket and GLP1R has no clustering-based activation route. Use only if pursuing an ECD-binding affinity scaffold fused to a separate activating element; generators = same backbone set (RFdiffusion, Chroma, Proteina-Complexa). Not recommended as the primary agonist bet.

4. **Nanobody / scFv / Fab.** Rank: **(1) RFantibody** (epitope-targeted VHH/scFv/Fab, free incl. commercial), **(2) Germinal** (open, 4–22%), **(3) Chai-2** (closed, 16–20%). All can target a defined GLP1R extracellular epitope, but **none has hit a GPCR experimentally and an Ig fold cannot occupy the 7TM pocket → expect antagonist/modulator, not agonist.** Weakest format for *agonism*.

5. **Cross-cutting: active-state biasing is manual.** Whatever generator is chosen, condition on an **agonist/Gs-bound active-state GLP1R structure** and hotspot the **7TM-core contacts the agonist N-terminus makes**, not the ECD — this is the only demonstrated lever that produced de novo GPCR agonism (class A). [PMC12157396](https://pmc.ncbi.nlm.nih.gov/articles/PMC12157396/)

6. **Eligibility red line.** **Do NOT** use the semaglutide/GLP-1/exendin sequence or the native agonist–receptor complex (e.g., PDB 7KI0) as template/motif/backbone — that is the Wei et al. route (0.68–0.81 identity to semaglutide) and is the forbidden "modify a known agonist" path. *Defensibly de novo* = sequence with no significant identity to native incretins + a generated (not grafted) scaffold, verified by a novelty gate (≤~30% seq id and low TM). [PMC12561408](https://pmc.ncbi.nlm.nih.gov/articles/PMC12561408/)

## (B) Gaps
- **No throughput-characterized de novo agonist rate for any class B GPCR** exists; EvoBind's GLP1R result is n=3, single lab, **preprint**, not peer-reviewed, no SPR affinity or in vivo, and uses a **macrocyclic** format whose challenge-eligibility must be confirmed.
- **No folded-protein (mini/large/antibody) de novo agonist of a class B GPCR has ever been reported** — the Baker class B designs are antagonists.
- GPCR/membrane capability of the strongest soluble tools (BoltzGen, PXDesign, AlphaProteo, Chai-2, Proteina-Complexa, SeedProteo) is **unknown — not demonstrated**, not disproven.
- No in-silico **agonism** (vs binding) predictor exists; computational filters will over-select binders. Need an orthogonal functional proxy (e.g., does the design reproduce the agonist-bound active-state contacts / TM6 position).
- EvoBind's "no similarity to known agonists" claim and active-state-stabilization modeling were not independently verified beyond the abstract this session; the full methods (how cyclization, how agonism was assayed quantitatively) should be read from the PDF.
- Exact RFantibody per-target experimental hit rates are from secondary coverage; RFdiffusionAA Science DOI from training knowledge; Protpardelle/Pallatom/Genie3 experimental binder data not located.

## (C) Confidence
- **High confidence**: (i) de novo GPCR agonism has been experimentally demonstrated only for a **class A** peptide receptor (MRGPRX1) via active-state structural conditioning; (ii) for **class B** GPCRs incl. GLP1R the same Baker pipeline produced **ECD antagonists, not agonists**; (iii) the Wei et al. "de novo GLP-1RA" is a **semaglutide redesign (ineligible)**; (iv) soluble-binder hit rates do not equal agonist capability; (v) antibody formats can target epitopes but are poorly suited to 7TM agonism. These rest on peer-reviewed + primary-abstract sources.
- **Medium confidence**: the EvoBind cyclic-peptide GLP1R agonist (EC50 32 nM, sequence-novel) is real and eligibility-clean on sequence — but it is a **single preprint, n=3**, so weight accordingly; the "peptide/micro-protein is the only format that reaches the 7TM pocket" inference is mechanistically sound but not exhaustively proven.
- **Lower confidence**: quantitative RFantibody GPCR prospects and whether any closed/soluble SOTA tool (Chai-2, AlphaProteo, BoltzGen) could be coaxed to a GLP1R agonist — undemonstrated either way.
