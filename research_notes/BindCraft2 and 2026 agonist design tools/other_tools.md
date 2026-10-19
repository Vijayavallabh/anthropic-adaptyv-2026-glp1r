# Newest (2025–2026) de novo protein/peptide DESIGN tools beyond BindCraft2 — for de novo GLP1R (class B GPCR) agonist design

Scope: tools released or materially updated in 2025–2026 that go beyond an Oct-2024 methods survey. Context = de novo GLP1R AGONIST (active-state, vestibule-engaging peptide/mini-protein). **FIREWALL respected: class-B agonism is UNPROVABLE in-silico; no agonism-scoring method is proposed below.** Every tool is flagged GO / NO-GO / CAUTION for ODC-BY submission eligibility, where the governing question is: *does the generator's weights/code license allow releasing the designed sequence openly (permissive / CC-BY-compatible), or does it impose non-commercial / no-derivatives / "outputs owned by vendor" restrictions?*

---

## Key Question 1: What new generators/updates appeared in 2025–2026, and what can they do?

### Takeaway
The 2025–2026 wave is dominated by **all-atom "structure-prediction-inversion" binder designers** (BoltzGen, BoltzDesign1, PXDesign/Protenix, RFdiffusion3) that can take an arbitrary target structure — including a supplied active-state receptor — as design context, plus target-aware peptide diffusion/flow models (PepGLAD, PPFlow) and antibody-specialized tools (Chai-2, Germinal, RFantibody). Three of the strongest general binder designers (BoltzGen, BoltzDesign1, RFdiffusion3) are permissively licensed down to the weights.

### Cited Findings

**BoltzGen (MIT Jameel Clinic / Stärk et al., Nov 2025) — flagship NEW tool.**
- All-atom generative model that "unifies binder design and structure prediction in one system"; design is steered by a **specification language covering binding sites, covalent bonds, structure groups, secondary structure, and design masks** — [MIT Jclinic](https://jclinic.mit.edu/boltzgen/); [bioRxiv 2025.11.20.689494](https://www.biorxiv.org/content/10.1101/2025.11.20.689494.full.pdf)
- Validated across 8 design campaigns / 26 targets across multiple labs; binder types span nanobodies to disulfide-bonded peptides; targets span disordered proteins to small molecules; reported nanomolar affinities for 9 novel protein targets with little PDB sequence identity — [MIT Jclinic](https://jclinic.mit.edu/boltzgen/)
- Presented as following the Boltz-1 / Boltz-2 lineage (open AF3 reproduction family); GitHub [github.com/HannesStark/boltzgen](https://github.com/HannesStark/boltzgen) — [MIT Jclinic](https://jclinic.mit.edu/boltzgen/)

**BoltzDesign1 (Cho et al., Apr 2025) — NEW.**
- Inverts the **Boltz-1** all-atom structure-prediction model to design biomolecular binders **without model fine-tuning** — [bioRxiv 2025.04.06.647261](https://www.biorxiv.org/content/10.1101/2025.04.06.647261.full.pdf)
- Supports **small-molecule targets** (`--target_type small_molecule --target_mols ...`); interface residues (<4 Å) are fixed during sequence redesign; contact-count knobs (`num_inter_contacts`, `num_intra_contacts`). "Boltz1x integration" is on the roadmap (not yet implemented). AlphaFold3 is an optional separate install (not required for core design) — [GitHub yehlincho/BoltzDesign1](https://github.com/yehlincho/BoltzDesign1)

**PXDesign / Protenix-design (ByteDance Seed, 2025) — NEW.**
- Two generators: **PXDesign-d** (diffusion backbone generator) and **PXDesign-h** (hallucination); reports **nanomolar hit rates of 17–82% across 6 of 7 diverse protein targets** — [ByteDance Seed](https://seed.bytedance.com/en/public_papers/pxdesign-fast-modular-and-accurate-de-novo-design-of-protein-binders)
- Full pipeline = PXDesign diffusion → **ProteinMPNN** sequence design → **AF2-IG** evaluation → **Protenix** evaluation (Protenix = ByteDance's AlphaFold3 reproduction) — [HF OneScience-Group/PXDesign](https://huggingface.co/OneScience-Group/PXDesign)
- Public webserver [protenix-server.com](https://protenix-server.com); benchmark repo [github.com/bytedance/PXDesignBench](https://github.com/bytedance/PXDesignBench); checkpoints on Hugging Face — [ByteDance Seed](https://seed.bytedance.com/en/public_papers/pxdesign-fast-modular-and-accurate-de-novo-design-of-protein-binders); [HF card](https://huggingface.co/OneScience-Group/PXDesign)

**RFdiffusion3 (IPD/UW, Butcher et al.; Sept 2025 preprint, Dec 2025 release) — NEW (explicitly in-scope per assignment).**
- All-atom "atom-level diffusion"; designs proteins that bind "any type of molecule commonly found inside living cells": protein–protein, protein–DNA, protein–small-molecule, enzymes, symmetric/binding/catalytic proteins; **atomic functional-site scaffolding**, motif-based conditioning, and hydrogen-bond conditioning; a small-molecule binder-design example ships — [IPD announcement](https://www.ipd.uw.edu/2025/12/rfdiffusion3-now-available/); [bioRxiv 2025.09.18.676967](https://www.biorxiv.org/content/10.1101/2025.09.18.676967.full.pdf); [PMC12458353](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12458353/)
- Training code AND weights released via the Rosetta Commons Foundry: [github.com/RosettaCommons/foundry](https://github.com/RosettaCommons/foundry) (model dir `models/rfd3`) — [IPD announcement](https://www.ipd.uw.edu/2025/12/rfdiffusion3-now-available/)

**Chai-2 (Chai Discovery, Jul 2025) — NEW but PROPRIETARY.**
- Zero-shot de novo binder design: given only a few epitope residues, generates candidates with no known starting binder; outputs **scFv, VHH/nanobody, or miniprotein** formats; can target multiple antigens for cross-reactivity/selectivity — [bioRxiv 2025.07.05.663018](https://www.biorxiv.org/content/10.1101/2025.07.05.663018.full.pdf)
- Company claims **16% hit rate in fully de novo antibody design** (up to 20 designs/target, 52 targets, wet-lab validation <2 weeks); figures are company-reported, no independent replication found — [Chai technical report](https://www.rivista.ai/wp-content/uploads/2025/07/technical_report.pdf); [BioPharmaTrend](https://www.biopharmatrend.com/news/chai-discovery-releases-foundation-model-for-zero-shot-antibody-design-with-1620-hit-rates-1309/)

**Germinal (Mille-Fragoso et al., Stanford, Sept 2025) — NEW (antibody/nanobody).**
- Pipeline: hallucination with **ColabDesign (AlphaFold-Multimer / AF2 params)** → sequence redesign with **AbMPNN** → cofolding with a structure predictor; designs nanobodies (VHH) and scFvs against chosen epitopes; expressed in mammalian cells — [bioRxiv 2025.09.19.677421](https://www.biorxiv.org/content/10.1101/2025.09.19.677421.full.pdf); [GitHub SantiagoMille/germinal](https://github.com/SantiagoMille/germinal)
- Cofolding backends: **AF3 (recommended, filters calibrated to it), Chai (default for nanobody), or Protenix**; language models AbLang1/AbLang2/IgLM — [GitHub SantiagoMille/germinal](https://github.com/SantiagoMille/germinal)

**RFantibody (IPD/UW; Nature, Nov 2025; preprint 2024) — updated/published.**
- Fine-tuned RFdiffusion to generate full-length VHH/scFv antibody fragments binding user-specified epitopes with atomic precision; validated by cryo-EM. Baker notes designs lack drug-level affinity as-is (proof of concept) — [IPD](https://www.ipd.uw.edu/2025/11/rfantibody-in-nature); [GeekWire](https://www.geekwire.com/2025/nobel-winners-lab-notches-another-breakthrough-ai-designed-antibodies-that-hit-their-targets/)

**La-Proteina + Proteina-Complexa (NVIDIA, Sept 2025) — NEW (all-atom flow).**
- La-Proteina: all-atom latent flow-matching generator; public repo covers **unconditional generation and atomistic motif scaffolding** (not target binder design in the public repo); checkpoints LD1–LD7 / AE1–AE3 on NGC — [GitHub NVIDIA-Digital-Bio/la-proteina](https://github.com/NVIDIA-Digital-Bio/la-proteina)
- **Proteina-Complexa** (built on La-Proteina): "flow-matching generative model for fully atomistic protein binder design," distributed on NGC — [NGC proteina_complexa](https://catalog.ngc.nvidia.com/orgs/nvidia/clara/models/proteina_complexa/-/model-card/explainability)

**Pallatom + Pallatom-Ligand (ICML 2025 / ICLR 2026) — NEW.**
- Pallatom: all-atom generator modeling the joint P(all-atom) distribution of structure+sequence (dual-track residue/atomic tokens, atom14); ICML 2025 spotlight — [PMLR v267 qu25c](https://proceedings.mlr.press/v267/qu25c.html); [bioRxiv 2024.08.16.608235](https://www.biorxiv.org/content/10.1101/2024.08.16.608235.full.pdf)
- **Pallatom-Ligand**: all-atom diffusion model for designing **ligand-binding proteins** end-to-end at atomic resolution; ICLR 2026 — [ICLR 2026 poster](https://iclr.cc/virtual/2026/poster/10006900)

**Peptide-specialized target-aware models (in-scope; mostly 2024, directly relevant to a GLP1R PEPTIDE):**
- **PepGLAD** (NeurIPS 2024): full-atom peptide design **conditioned on a binding site**; VAE maps variable-size full-atom residues to fixed latent vectors, diffusion in latent space; **receptor-specific affine transformation** normalizes binding-site geometry for cross-site generalization; +18% diversity / +8% in-silico success in co-design, +26% recall of reference binding conformation (authors' own metrics) — [arXiv 2402.13555](https://arxiv.org/abs/2402.13555); [NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/88ad9774ffcb7a272457e9396f793a07-Abstract-Conference.html)
- **PPFlow** (ICML 2024): target-aware peptide design via conditional **torsional flow matching** on torus manifolds; ships the PPBench2024 protein–peptide dataset — [arXiv 2405.06642](https://arxiv.org/abs/2405.06642); [PMLR v235 lin24z](https://proceedings.mlr.press/v235/lin24z.html)
- **PLAID** (ICLR 2025): all-atom generation in **ESMFold's** latent space; trainable from sequence-only data — [ICLR 2025](https://iclr.cc/virtual/2025/34700)

**AlphaProteo (Google DeepMind, Sept 2024) — announced, NOT publicly released.**
- Announced Sept 2024 as an AI system for designing high-affinity binders; **no public code or model-weights release was found** in 2025–2026 searches — [search context, see Gaps]; DeepMind's prior pattern (AF3) was code-open-but-weights-academic-only/non-commercial — [GEN on AF3 access](https://genengnews.com/topics/artificial-intelligence/alphafold-3-angst-limited-accessibility-stirs-outcry-from-researchers)

### Inferences
- For a **de novo GLP1R peptide/mini-protein**, the natural fit is the co-folding-inversion binder designers (**BoltzGen, BoltzDesign1, PXDesign, RFdiffusion3**) run against a supplied **active-state** GLP1R structure, plus the target-aware peptide tools (**PepGLAD, PPFlow**) for shorter peptides. Antibody tools (Chai-2 antibody mode, Germinal, RFantibody) are architecturally off-target (they build Ig folds, not linear peptides) — consistent with the project's own ledger note that antibody/nanobody-seeding is "not de novo."
- BoltzGen is the single most capable + most permissively licensed new generator: all-atom, binding-site-conditionable, peptide-and-miniprotein-capable, MIT down to weights.

### Gaps
- AlphaProteo: could not confirm any availability terms from a primary DeepMind source; two targeted searches returned only AlphaFold3 material. Treat as **unavailable** (NO-GO on availability) pending a direct DeepMind page check.
- "PepFlow" as a distinct tool could not be cleanly separated from PepGLAD/PPFlow in results — likely a separate multi-modal peptide generator but unverified.

---

## Key Question 2: Model + WEIGHT provenance and LICENSE (ODC-BY GO/NO-GO) for each

### Takeaway
**GO (permissive, weights included):** BoltzGen (MIT), BoltzDesign1 (MIT), RFdiffusion3 (BSD-3, code+weights), PXDesign (Apache-2.0, commercial-OK), RFantibody (free incl. commercial). **GO-with-conditions:** La-Proteina/Proteina-Complexa (Apache code + NVIDIA Open Model License weights). **NO-GO / CAUTION:** anything requiring **AF3 weights** or **ESM3** (non-commercial/academic-only), **Chai-2** (proprietary, no open weights), **AlphaProteo** (unreleased). The eligibility pivot is almost entirely the *weights* license of the generator and of any model kept *in the generation loop* (eval-only AF3 is avoidable).

### Cited Findings

**Verified first-hand this session (authoritative):**
- **RFdiffusion3** — `LICENSE.md` in the Foundry repo reads verbatim **"BSD 3-Clause License ... This copyright and license covers both the source code and model weights referenced for download in the README file."** (GitHub's auto-classifier shows "NOASSERTION/Other" only because a preamble line precedes the standard BSD text.) → fully permissive, commercial-OK, derivatives OK. **GO.** — [Foundry LICENSE.md](https://github.com/RosettaCommons/foundry/blob/production/LICENSE.md)
- **BoltzGen** — "fully open sourced under an **MIT license** for unrestricted commercial and academic use," explicitly "including **data, model weights**, training, and inference code." **GO.** — [MIT Jclinic](https://jclinic.mit.edu/boltzgen/)
- **BoltzDesign1** — repo states "**MIT License**"; downloads **Boltz** weights (Boltz is MIT); AF3 only as optional separate install. **GO** (run AF3-free). — [GitHub yehlincho/BoltzDesign1](https://github.com/yehlincho/BoltzDesign1)
- **PXDesign** — HF card: official repo is **Apache License 2.0**; license "permits academic research and **commercial use**"; PXDesign + Protenix checkpoints downloadable (`hf download OneScience-Group/PXDesign`). Caveat stated on the card: **AF2-IG weights and ProteinMPNN/Protenix follow their own licenses**. **GO** (AF2 params are CC-BY-4.0, commercial-OK with attribution; Protenix is Apache; no AF3 in loop). — [HF OneScience-Group/PXDesign](https://huggingface.co/OneScience-Group/PXDesign)
- **Germinal** — repo is **Apache License 2.0**; but optional deps carry restrictions: **IgLM** = "non-commercial academic license from Johns Hopkins"; **PyRosetta** = "non-commercial, non-profit license; commercial use requires a separate license." AF-Multimer params required; AF3 optional; Protenix separate. **CAUTION** (antibody-only anyway; avoid IgLM/PyRosetta/AF3 paths for clean eligibility). — [GitHub SantiagoMille/germinal](https://github.com/SantiagoMille/germinal)
- **La-Proteina** — repo: **code = Apache-2.0; model weights = NVIDIA Open Model License; other materials = CC-BY-4.0.** — [GitHub NVIDIA-Digital-Bio/la-proteina](https://github.com/NVIDIA-Digital-Bio/la-proteina)
- **NVIDIA Open Model License** — permits **commercial use**; allows creating/distributing derivative models; **NVIDIA claims no ownership of generated outputs**; conditions = user indemnifies NVIDIA, license terminates on patent/copyright litigation. → outputs (designed sequences) are freely shareable → **GO-with-conditions** for La-Proteina/Proteina-Complexa. — [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license); [ScanCode entry](https://scancode-licensedb.aboutcode.org/nvidia-open-model-2025.json)
- **ESM3 / ESMC (EvolutionaryScale)** — ESM3-open (1.4B) weights are **non-commercial** (Community/Cambrian license: "non-commercial use ... bars use in connection with any commercial activities"); larger ESM3 (7B/98B) are Forge-API-only. ESMC (300M/600M/6B) under the Cambrian Open License with a commercial route via SageMaker limited to a drug-discovery/protein-engineering "Permitted Purpose." → **ESM3 = NO-GO; ESMC = CAUTION.** — [Community License](https://www.evolutionaryscale.ai/policies/community-license-agreement); [Cambrian Open License](https://www.evolutionaryscale.ai/policies/cambrian-open-license-agreement); [PyPI esm 3.0.7](https://pypi.org/project/esm/3.0.7)

**Supporting (secondary sources):**
- **Boltz-1 = MIT License** (open-source AlphaFold3 reproduction) — [Model-Centric DL review, arXiv 2502.19173](https://arxiv.org/pdf/2502.19173); [Azure catalog Boltz-1](https://ai.azure.com/catalog/models/Boltz-1)
- **AlphaFold3**: code downloadable for **non-commercial** use; **training weights academic-affiliation-only, on request** → any tool requiring AF3 weights inherits non-commercial/academic restriction. **NO-GO if AF3 is in the loop.** — [GEN](https://genengnews.com/topics/artificial-intelligence/alphafold-3-angst-limited-accessibility-stirs-outcry-from-researchers); [HumanProgress](https://humanprogress.org/ai-protein-prediction-tool-alphafold3-is-now-more-open/)
- **Chai-2**: delivered via Chai Discovery's platform; company raised $70M to expand the platform; **no open weights found** → **NO-GO** (cannot self-host or verify output license). — [BioPharmaTrend $70M](https://www.biopharmatrend.com/news/chai-discovery-raises-70m-to-expand-zero-shot-biologics-design-ai-platform-1331/); [Chai-2 announcement](https://www.chaidiscovery.com/news/introducing-chai-2)
- **RFantibody**: IPD states the software is "free for academic, personal, and **commercial** use," code on GitHub. **GO** (but antibody-only). — [IPD RFantibody](https://www.ipd.uw.edu/2025/11/rfantibody-in-nature)

### Inferences
- **Weight provenance is the eligibility lever, not the architecture.** All four leading co-folding-inversion designers that matter here avoid the AF3-weights trap: BoltzGen/BoltzDesign1 use Boltz (MIT, trained from scratch), PXDesign uses Protenix (Apache, trained from scratch) + AF2-IG (CC-BY-4.0), RFdiffusion3 ships its own BSD-3 weights. All are **GO** for ODC-BY.
- Keep **AF3 and ESM3 out of the generation loop**. AF3 is avoidable as an eval step (use AF2-IG / Boltz / Protenix instead); ESM3 is non-commercial. Tools that *default* to AF3 (Germinal) are still usable if reconfigured, but that adds eligibility risk.
- NVIDIA Open Model License is commercially usable and disclaims ownership of outputs, so La-Proteina/Proteina-Complexa designs are ODC-BY-shareable — but the indemnification + litigation-termination clauses are heavier than MIT/BSD/Apache.

### Gaps
- PepGLAD, PPFlow, Pallatom/Pallatom-Ligand, PLAID: did not pull their repo LICENSE files first-hand; academic repos are usually MIT but this is **unconfirmed** — the report-writer should treat their eligibility as "check repo LICENSE" before reliance.
- Exact AlphaFold2-parameters license (commonly cited as CC-BY-4.0) was not pulled first-hand this session; verify directly before leaning on PXDesign's AF2-IG step for a commercial/ODC-BY claim.
- NVIDIA Open Model License full current text not read line-by-line; acceptable-use-policy scope not enumerated.

---

## Key Question 3: Which can condition on a target POCKET / active state vs only fixed-backbone surface binding?

### Takeaway
The co-folding-inversion designers (BoltzGen, BoltzDesign1, PXDesign, RFdiffusion3) and the target-aware peptide models (PepGLAD, PPFlow) **can condition on a supplied target structure / binding site** — meaning you obtain active-state engagement by *feeding them the active-state GLP1R conformation as fixed context*. **None performs true induced-fit or conformation-selective design of the receptor itself**; the target is treated as (largely rigid) context, so you must supply the desired state.

### Cited Findings
- **BoltzGen**: specification language explicitly constrains generation over **binding sites** (plus covalent bonds, structure groups, secondary structure, design masks). Does NOT mention active-state conditioning per se — [MIT Jclinic](https://jclinic.mit.edu/boltzgen/)
- **BoltzDesign1**: supports **small-molecule target** conditioning; fixes interface residues (<4 Å) during redesign; tunable inter/intra contact counts — i.e., conditions on the provided target pose — [GitHub yehlincho/BoltzDesign1](https://github.com/yehlincho/BoltzDesign1)
- **RFdiffusion3**: **atomic functional-site scaffolding**, motif conditioning, hydrogen-bond conditioning, and small-molecule binder design; atom-level diffusion lets you specify which chemical interactions matter — condition on an atomistic target context — [IPD](https://www.ipd.uw.edu/2025/12/rfdiffusion3-now-available/); [bioRxiv 2025.09.18.676967](https://www.biorxiv.org/content/10.1101/2025.09.18.676967.full.pdf)
- **PXDesign / Protenix**: diffusion generates binder backbones against a target; Protenix is a full AlphaFold3-style co-folder, so the target structure (incl. a chosen receptor conformation) is the design context — [HF OneScience-Group/PXDesign](https://huggingface.co/OneScience-Group/PXDesign)
- **PepGLAD**: explicitly **binding-site-conditioned** full-atom peptide design, with a receptor-specific affine transform to normalize varied binding-site geometries — directly a "design into this pocket" tool — [arXiv 2402.13555](https://arxiv.org/abs/2402.13555)
- **PPFlow**: **target-aware** peptide design (structure-based, into a receptor pocket) — [arXiv 2405.06642](https://arxiv.org/abs/2405.06642)
- **Pallatom-Ligand**: all-atom design of **ligand-binding proteins** end-to-end — pocket-oriented — [ICLR 2026](https://iclr.cc/virtual/2026/poster/10006900)
- **La-Proteina (public repo)**: only **unconditional generation + atomistic motif scaffolding** — NOT target/pocket binder design in the public code; binder conditioning lives in the separate **Proteina-Complexa** model — [GitHub NVIDIA-Digital-Bio/la-proteina](https://github.com/NVIDIA-Digital-Bio/la-proteina); [NGC proteina_complexa](https://catalog.ngc.nvidia.com/orgs/nvidia/clara/models/proteina_complexa/-/model-card/explainability)
- **Chai-2**: conditions on a few **epitope residues** (surface-/epitope-targeted), antibody/miniprotein output — [bioRxiv 2025.07.05.663018](https://www.biorxiv.org/content/10.1101/2025.07.05.663018.full.pdf)

### Inferences
- The practical route to an "active-state-vestibule-engaging" design is: take an experimental **active-state** GLP1R structure (e.g., an active-state cryo-EM model), hand it to BoltzGen / BoltzDesign1 / PXDesign / RFdiffusion3 as fixed target context, and restrict hotspots/binding-site to the vestibule region. Co-folding models (Boltz/Protenix) give the richest all-atom pocket context; RFd3 gives the most explicit per-atom interaction control.
- Because the receptor is held (near-)rigid, **conformation SELECTION is the designer's job, not the tool's**: supplying the active state biases toward vestibule engagement but does not guarantee the receptor would adopt/hold that state on binding — this is exactly the kind of claim the firewall says is not provable in-silico, so it must not be over-stated.

### Gaps
- No tool surfaced that performs explicit **induced-fit / flexible-receptor** conditioning for GPCRs; all treat the provided target as context. Whether any 2025–2026 tool models receptor flexibility during design was not established.

---

## Key Question 4: Which honor the hard constraints (natural AAs; linear; NO reliable disulfide; short/expressible; tolerate N-term (f)Met + C-term GFP11/Twin-Strep tag)?

### Takeaway
All of the general backbone/peptide generators output **natural-AA, linear chains at user-specified (short) length by construction**, and disulfides are optional (place no cysteines / constrain the MPNN step). The N-term-(f)Met + C-term-tag tolerance is a **design-layout choice** (keep the interface and hotspots away from both termini; append the tag as a non-designed segment), not a model capability — so it is satisfiable with every sequence-design-via-MPNN tool, with antibody tools being the poor fit (Ig folds, framework disulfides).

### Cited Findings
- **Natural AAs / linear / length**: ProteinMPNN-style sequence design (used by PXDesign, Germinal, and the common BoltzDesign1/RFd3 workflows) emits the 20 canonical amino acids; diffusion/flow backbone generators produce single linear chains at a user-specified length. (General property of these pipelines) — [HF OneScience-Group/PXDesign](https://huggingface.co/OneScience-Group/PXDesign) (lists ProteinMPNN in-loop); [IPD RFdiffusion3](https://www.ipd.uw.edu/2025/12/rfdiffusion3-now-available/)
- **Disulfide optionality**: BoltzGen was explicitly demonstrated on **disulfide-bonded peptides** among other binder types — i.e., it *can* use disulfides but does not require them; cysteine content is controllable at the sequence-design stage — [MIT Jclinic](https://jclinic.mit.edu/boltzgen/)
- **Peptide-length tools**: PepGLAD and PPFlow are purpose-built for short peptides bound to a target pocket, i.e., inherently short/expressible lengths — [arXiv 2402.13555](https://arxiv.org/abs/2402.13555); [arXiv 2405.06642](https://arxiv.org/abs/2405.06642)
- **Antibody tools are the misfit**: Germinal/RFantibody/Chai-2 (antibody mode) build immunoglobulin folds (VHH/scFv) that rely on framework disulfides and are not linear peptides — [GitHub SantiagoMille/germinal](https://github.com/SantiagoMille/germinal); [IPD RFantibody](https://www.ipd.uw.edu/2025/11/rfantibody-in-nature)

### Inferences
- **Constraint-compliant set** for a linear, natural-AA, disulfide-free, taggable GLP1R peptide/mini-protein: **BoltzGen, BoltzDesign1, PXDesign, RFdiffusion3, PepGLAD, PPFlow, Pallatom-Ligand** — all produce natural-AA linear chains; set a no-Cys (or ≤0 disulfide) constraint in the MPNN/sequence step and lay out hotspots away from both termini so the (f)Met and the C-terminal GFP11/Twin-Strep tag remain free.
- The N-terminal (f)Met and C-terminal tag are best treated as **non-designed flanking segments**; tools with masking/spec languages (BoltzGen's design masks; BoltzDesign1's fixed-interface logic; RFd3 motif conditioning) make it straightforward to exclude termini from the designed interface.
- Antibody-format tools fail the "linear, no reliable disulfide, short" constraints and should be excluded for this objective regardless of their (permissive) licenses.

### Gaps
- No source explicitly documents each tool's behavior with an N-terminal formyl-Met or a C-terminal GFP11/Twin-Strep fusion; this is inferred from how the generators handle fixed/flanking regions, not stated in the tool docs.
- Minimum reliably-designable length per tool (how short a mini-protein each can make before designability collapses) was not quantified from primary sources.

---

## Summary eligibility table (GO/NO-GO for ODC-BY)

| Tool | Released/updated | Base model + weight provenance | License (code / weights) | Pocket/active-state cond.? | Fit to linear-peptide objective | ODC-BY |
|---|---|---|---|---|---|---|
| **BoltzGen** | Nov 2025 | Boltz-family all-atom (trained from scratch; no AF3 weights) | **MIT** (incl. data+weights) | Yes (binding-site spec) | High (peptide+miniprotein) | **GO** |
| **BoltzDesign1** | Apr 2025 | Inverts Boltz-1 (MIT) | **MIT**; Boltz weights MIT; AF3 optional/separate | Yes (small-mol + fixed interface) | High | **GO** (run AF3-free) |
| **RFdiffusion3** | Sept–Dec 2025 | Own all-atom diffusion; IPD weights | **BSD-3 (code+weights)** | Yes (functional-site/H-bond/small-mol) | High | **GO** |
| **PXDesign (Protenix)** | 2025 | PXDesign-d/-h + Protenix (Apache AF3-repro) + AF2-IG (CC-BY-4.0) + ProteinMPNN (MIT) | **Apache-2.0**, commercial-OK | Yes (co-fold target context) | High | **GO** (no AF3 in loop) |
| **La-Proteina / Proteina-Complexa** | Sept 2025 | NVIDIA all-atom flow | Apache code / **NVIDIA Open Model License** weights / CC-BY-4.0 materials | Public repo = motif only; Complexa = binder | Medium | **GO (conditions)** |
| **Pallatom / Pallatom-Ligand** | ICML'25 / ICLR'26 | Own all-atom joint diffusion | **Gap — verify repo** | Ligand-binding (Pallatom-Ligand) | Medium | Verify |
| **PepGLAD** | NeurIPS 2024 | Own full-atom latent diffusion | **Gap — verify repo** | Yes (binding-site conditioned) | High (short peptides) | Verify |
| **PPFlow** | ICML 2024 | Own torsional flow | **Gap — verify repo** | Yes (target-aware) | High (short peptides) | Verify |
| **Germinal** | Sept 2025 | ColabDesign/AF2-Multimer + AbMPNN + AF3/Chai/Protenix | Apache repo; **IgLM/PyRosetta non-commercial; AF3 optional** | Epitope (antibody) | Low (Ig fold) | CAUTION / off-target |
| **RFantibody** | Nature Nov 2025 | Fine-tuned RFdiffusion | Free incl. **commercial** | Epitope (antibody) | Low (Ig fold) | GO-license / off-target |
| **Chai-2** | Jul 2025 | Proprietary Chai foundation model | **Proprietary / platform-only; no open weights** | Epitope | Low–Med (miniprotein mode) | **NO-GO** |
| **AlphaProteo** | Sept 2024 (announced) | DeepMind (unreleased) | **No public code/weights found** | n/a | n/a | **NO-GO (unavailable)** |
| *(dependency)* **AlphaFold3 weights** | — | DeepMind | **Non-commercial, academic-only** | — | — | **NO-GO if in loop** |
| *(dependency)* **ESM3** | — | EvolutionaryScale | **Non-commercial** (ESM3-open); ESMC = caution | — | — | **NO-GO (ESM3)** |
