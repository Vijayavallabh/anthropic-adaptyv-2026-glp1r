# De novo human GLP-1R agonist candidates — methodology

## Objective and hypothesis
The goal is a de novo, gene-encodable single-chain protein that **agonizes** human GLP-1R
(UniProt P43220), a class B GPCR. Our guiding premise is that **activation is not the same as
binding**: a ligand that only engages the extracellular domain or receptor surface defaults to an
antagonist, whereas agonism requires reaching the **7TM extracellular vestibule** (the orthosteric
peptide-binding site) to stabilize the active-state conformation. No standalone de novo protein has
been reported to agonize a class B GPCR, so we treated this as a frontier objective and built a
**mechanism-hedged portfolio** rather than betting on a single confident agonist.

## Design generation (de novo / zero-shot)
All designs are de novo and were generated without starting from, or grafting, any native incretin.
To decorrelate architectural and sequence biases we used several **orthogonal generators**: a
Boltz-based generative model (BoltzGen), a flow-matching all-atom design method (RFD4-Proteina),
RFdiffusion (including a structure-conditioned motif campaign and extracellular-domain scaffold
miniproteins), a diffusion peptide designer (DiffPepBuilder), a latent-diffusion peptide designer
(PepGLAD), and a masked protein language model (PepMLM). Every candidate was gated for eligibility:
natural amino acids only, single chain, 10–250 residues, and **no significant identity** to GLP-1,
exendin-4, glucagon, or GIP (longest contiguous match ≤ 3 residues).

## In-silico evaluation — what we can and cannot measure
Each **bare** design (expression tags removed) was co-folded against wild-type GLP-1R residues
24–432 with **two independent structure predictors (Boltz-2 and Chai)** to guard against
single-model docking artifacts. We scored interface confidence (ipSAE, ipTM), a monomer
expression/foldability proxy (ESMFold2 pLDDT), hydrophobicity (mean Kyte–Doolittle), and engagement
of the extracellular vestibule / ECL2 (around R299) as a necessary-condition proxy for orthosteric
reach. To pass, a design had to **reproduce vestibule engagement across both predictors over
multiple random seeds** (a two-fold-robust gate), removing designs that only one model confidently
docks. All metrics were calibrated against native controls: GLP-1(7-36) and exendin-4 (agonists),
exendin(9-39) (antagonist), and scrambled-sequence negatives.

## The central limitation, stated plainly
We did **not**, and believe one cannot, rank these designs by predicted agonism. For a class B GPCR
there is no validated in-silico method that separates agonists from antagonists — in our own control
panel, the antagonist exendin(9-39) and scrambled-sequence negatives reach the vestibule and score on
the interface metrics just as the agonists do. We therefore use vestibule engagement and interface
confidence **strictly as binding/expression necessary conditions**, and regard the functional
cell-based reporter assay as the only determinant of agonism. The portfolio is accordingly a
**coverage bet**: a diverse set of independently-generated, high-confidence vestibule binders chosen
to maximize the probability that at least one architecture activates the receptor.

## Portfolio
Twenty single-chain designs span multiple independent generator lineages and are
**lineage-diversity-capped** to avoid redundancy. The large majority reproduce two-fold-robust
vestibule engagement; all are **0-Cys linear** peptides/miniproteins that pass a developability
screen (hydrophobicity, aggregation-prone runs, oxidation risk). Designs are ordered best-first by
measured binding/expression confidence together with lineage diversity, using length-matched
comparison so that interface scores are not inflated by sequence length. The intent is breadth of
credible, independently-generated vestibule binders rather than a single highest-scoring candidate,
because the activation readout — not any computational score — is the true test.
