# Prior Art & Precedent: Engineered/De Novo Agonists, the Minimal GLP1R Agonist Pharmacophore, and Competition Precedent

> Scope: prior art and precedent for de novo / engineered receptor **agonists** (not binders), the minimal GLP1R **activation** pharmacophore ("message/address"), transferability of engineered-agonist mechanisms to a monomeric class B GPCR, and the Anthropic×Adaptyv competition precedent. Research cutoff 2026-10-13. **Binding ≠ activation is treated as a hard distinction throughout.**
> PubMed-derived facts are attributed to PubMed with DOI links per that tool's terms.

---

## EVIDENCE REGISTER (tiers + direct-human-GLP1R vs extrapolation)

| # | Finding (short) | Tier | Direct GLP1R? | Source |
|---|---|---|---|---|
| E1 | GLP1R activation = 2-domain: peptide **C-term "address"→ECD**, **N-term "message"→7TM core**, driving a **sharp kink in TM6** that pivots its intracellular half out to admit Gs α5 | **T1** (peer-rev, cryo-EM, human GLP1R) | YES | Zhang 2017 Nature, [10.1038/nature22394](https://doi.org/10.1038/nature22394) |
| E2 | His7 is indispensable for activation: deleting N-terminal His (or the His7 α-amino) drops affinity+potency; the **imidazole positive charge** (ring + basic function + positioning) is crucial for GLP-1 action | **T1** | YES | Adelhorst et al. 1994 J Biol Chem (SAR); Endocrine J 1997 [10.1507/endocrj.44.701](https://doi.org/10.1507/endocrj.44.701) |
| E3 | **11-mer agonist** = optimized 9-mer (N-terminal 9 aa of GLP-1, incl. His7) + C-terminal biphenylalanine (BIP) dipeptide "cap"; **potency ≈ native 30-mer** in vitro | **T1** | YES | Mapelli 2009 J Med Chem, [10.1021/jm900752a](https://doi.org/10.1021/jm900752a) |
| E4 | **Boc5** (substituted cyclobutane) = first **orthosteric non-peptide full agonist**; cryo-EM: one arm inserts **deep into the orthosteric pocket overlapping GLP-1 A8–D15**, other arms fill TM1–7/TM1–2/TM2–3 clefts | **T1** | YES | PNAS 2022, [PMC9171782](https://pmc.ncbi.nlm.nih.gov/articles/PMC9171782); PDB 7X8S/7X8R |
| E5 | **Cyclic 11-mer N-terminal GLP-1** (side-chain link 2–5 or 5–9) = nM agonist; **stapling/helix-constraint** boosts cAMP & protease resistance, can bias away from β-arrestin | **T1** | YES | Hoang 2015 J Med Chem (PMID 25839426); i,i+7 staple scan [PMC7366314](https://pmc.ncbi.nlm.nih.gov/articles/PMC7366314); Plisson 2017 Eur J Med Chem |
| E6 | **De novo dual cyclic-peptide agonist of GLP1R/GCGR**: 18-mer cyclic, **EC50 32 nM (GLP1R)**, 542 nM (GCGR), cAMP; sequence-only EvoBind2/AF2 design; "almost no consecutive similarity" to the 8JIQ GLP-1 analogue; weak β-arrestin (possible Gs bias) | **T3** (preprint) + experimental cAMP; **structural = AF2 only (T4)** | YES (functional) | bioRxiv 2025.06.06.658268, [full](https://www.biorxiv.org/content/10.1101/2025.06.06.658268v1.full) |
| E7 | **Baker de novo GPCR miniproteins**: **agonists only for class A (MRGPRX1)** via active-state stabilization in the orthosteric pocket (TM2–7), cryo-EM 0.7 Å; full+partial agonists EC50 390 nM/1 µM/1.4 µM; 7/50 expressed designs active | **T1** | NO (class A) | Nature 2026, [10.1038/s41586-026-10656-8](https://doi.org/10.1038/s41586-026-10656-8); [PMC12157396](https://pmc.ncbi.nlm.nih.gov/articles/PMC12157396/) |
| E8 | Same Baker work on **class B (GLP1R/GIPR/GCGR/CGRPR): produced ANTAGONISTS only**, by targeting the **ECD**; GLP1R antagonist dGI1_024 IC50 **61 nM**, mGI1_008 **39 nM**. Discussion: **agonists are especially hard** (must discriminate subtle active-vs-inactive orthosteric differences) | **T1** | YES (but antagonist) | same as E7 |
| E9 | **De novo "GPCR exoframe modulators" (GEMs)**: de novo proteins binding the **TM-domain outer (lipid-facing) surface**; functional range incl. **ago-PAM**; a GEM **restored activity of D1 loss-of-function mutants**. Prototype = dopamine D1 (class A) | **T1** | NO (class A D1) | Nature 2026, [10.1038/s41586-025-09957-1](https://doi.org/10.1038/s41586-025-09957-1) (PMID 41699180) |
| E10 | De novo **IL-2/IL-15 mimic Neo-2/15**: recapitulates the cytokine binding site, binds **IL-2Rβγ heterodimer**, signals by bringing receptor subunits together; no topology/sequence relation to IL-2 | **T1** | NO (cytokine) | Silva 2019 Nature, [10.1038/s41586-018-0830-7](https://doi.org/10.1038/s41586-018-0830-7) |
| E11 | De novo agonists by **valency/geometry (clustering)**: FGFR cyclic oligomers (Cell 2024, [10.1016/j.cell.2024.05.025](https://doi.org/10.1016/j.cell.2024.05.025)); soluble **Notch** agonists by cell-cell bridging/clustering (Cell 2025, [10.1016/j.cell.2025.07.009](https://doi.org/10.1016/j.cell.2025.07.009)); **TLR3** minibinder agonists (Nat Commun 2025, [10.1038/s41467-025-56369-w](https://doi.org/10.1038/s41467-025-56369-w)); **Novokines** fusing binder pairs → pSTAT (bioRxiv 2025, [10.1101/2025.10.12.681920](https://doi.org/10.1101/2025.10.12.681920)) | **T1–T3** | NO | as cited |
| E12 | De novo **insulin-receptor agonists**: de novo binders to individual IR ECDs **fused in different orientations/flexibility** induce distinct IR conformational changes → tunable agonism | **T1** | NO (RTK) | Mol Cell 2025, [10.1016/j.molcel.2025.09.020](https://doi.org/10.1016/j.molcel.2025.09.020) |
| E13 | **Known GLP1R PAMs (BETP, "compound 2" quinoxaline)** are **covalent, act at intracellular Cys347 (ICL3)**; potentiate cAMP, partial-agonist activity | **T1** | YES | Nat Chem Biol [10.1038/nchembio.1581](https://doi.org/10.1038/nchembio.1581); [PMC4865917](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4865917/) |
| E14 | Adaptyv EGFR competition success: R1 **2.5%** binders (5/201); R2 **95% expression** (378/400), **~13.25% binders** (53/400); 30/130 participants made ≥1 binder | **T2/T3** (preprint + blog) | N/A | bioRxiv 2025.04.17.648362 [full](https://www.biorxiv.org/content/10.1101/2025.04.17.648362v2.full.pdf); [Adaptyv blog po104](https://www.adaptyvbio.com/blog/po104) |
| E15 | Challenge 3 = **"Design a GLP1R agonist"** (Oct 12–25); public page does **not** disclose the wet-lab assay (binding vs functional cAMP) nor novelty rule; "Selection will not rely on a single in-silico metric" | **T2** (primary org page) | YES | [Proteinbase competition page](https://proteinbase.com/competitions/anthropic-adaptyv-2026) |

Tier key: **T1** peer-reviewed + experimental; **T2** peer-reviewed/primary-org but extrapolation or incomplete; **T3** preprint/not peer-reviewed; **T4** in-silico-only / vendor / patent.

---

## Q1. Minimal GLP1R agonist pharmacophore (what still ACTIVATES)

### Takeaway
GLP1R is a **monomeric class B GPCR** activated by a **two-domain "address→message"** mechanism: the peptide C-terminal helix docks the extracellular domain (ECD, the "address," for affinity) and the **N-terminal ~8 residues (the "message") insert into the 7TM orthosteric pocket**, where **His7's cationic imidazole** and neighboring residues trigger a **TM6 kink/outward swing** that opens the intracellular Gs pocket. The smallest entities that still give full Gs/cAMP activation are an **~11-mer peptide** (optimized N-terminal 9-mer + a lipophilic cap) and **non-peptide small molecules** (Boc5) that occupy the same deep pocket — i.e., **activation lives in the N-terminal message + pocket contacts, not in the bulk of the address.**

### Cited Findings
- **Two-domain mechanism / TM6 kink (the activation switch).** Cryo-EM of peptide-activated GLP1R–Gs: the peptide is "clasped between the N-terminal domain and the transmembrane core"; activation produces a **sharp kink in the middle of TM6**, pivoting its intracellular half outward to accommodate the Gs Ras-like α5-helix — According to PubMed, Zhang 2017 Nature, [DOI 10.1038/nature22394](https://doi.org/10.1038/nature22394).
- **Two-step model generalized across class B1.** Regions near the hormone **C-terminus bind the ECD**; regions near the peptide **N-terminus interact with the TM domain and transmit the activation signal** — According to PubMed, Aksu 2024 Mol Biol Rep review, [DOI 10.1007/s11033-024-09876-w](https://doi.org/10.1007/s11033-024-09876-w).
- **His7 indispensability.** Deletion of the N-terminal histidine (or of the His7 α-amino group) **decreased receptor affinity and potency**; a 1997 study found the **positive charge of the His imidazole side chain** (ring + basic function + correct positioning), not the free α-amino charge, is decisive for GLP-1 action — Adelhorst et al. 1994 J Biol Chem SAR (surfaced via [IPR exhibit](https://www.docketalarm.com/cases/PTAB/IPR2023-00722/Mylan_Pharmaceuticals_Inc/03-16-2023-Petitioner/Exhibit-1005-Adelhorst_1994)); Endocrine Journal 1997, [DOI 10.1507/endocrj.44.701](https://doi.org/10.1507/endocrj.44.701).
- **DPP-IV inactivation.** Native GLP-1 is cleaved to **GLP-1(9–36)amide** (loss of His7-Ala8), the physiological inactivation step — multiple sources in the His7 search set (e.g., [Bioscience Reports 2016](https://port.silverchair.com/bioscirep/article-pdf/36/1/e00285/477464/bsr036e285.pdf)).
- **Residues for activation vs binding.** A structural analysis flags **His7, Gly10, Asp15, Phe28 as important for receptor activation**, with His7 also important for binding (GLP-1 search set, e.g., [ResearchSquare rs-1721735](https://www.researchsquare.com/article/rs-1721735/v1) — lower-tier/secondary).
- **11-mer agonists (the "message + minimal cap").** An 11-residue class: a structurally optimized **9-mer (closely related to the N-terminal 9 aa of GLP-1)** linked to a **C-terminal biphenylalanine (BIP) dipeptide**; SAR produced **11-mers with in-vitro potency similar to the native 30-mer**, active in vivo — According to PubMed, Mapelli 2009 J Med Chem, [DOI 10.1021/jm900752a](https://doi.org/10.1021/jm900752a). Interpretation: the ~30-residue "address" helix can be collapsed to a small lipophilic cap as long as the N-terminal message is intact.
- **Cyclic/stapled N-terminal agonists.** An 11-residue N-terminal GLP-1 analogue **cyclized (side-chains 2–5 or 5–9)** remained a **nanomolar cAMP agonist** (N-terminal β-turn + C-terminal helix) — Hoang 2015 J Med Chem (PMID 25839426). Systematic **i,i+7 staple scanning** across GLP-1 and **double-stapled exendin-4** improved helicity/protease resistance ([PMC7366314](https://pmc.ncbi.nlm.nih.gov/articles/PMC7366314)); **helix constraints increased cAMP/insulin secretion but not β-arrestin-2** (Gs bias) — Plisson 2017 Eur J Med Chem.
- **Boc5 — the smallest/most-reduced full agonist motif.** The non-peptide **Boc5** (and WB4-24) give **cAMP to GLP-1 levels**; cryo-EM shows **one arm inserted deeply into the orthosteric pocket normally used by the peptide N-terminus, overlapping GLP-1 residues A8–D15**, with additional arms filling TM clefts — PNAS 2022, [PMC9171782](https://pmc.ncbi.nlm.nih.gov/articles/PMC9171782), PDB 7X8S/7X8R. Oral GLP1R small-molecule agonists (danuglipron, orforglipron, LY3502970/CHU-128 class) make the analogous deep-pocket contacts.

### Inferences
- The **activation pharmacophore reduces to: (i) deliver a cationic/aromatic "message" moiety (His7-equivalent) into the deep 7TM pocket to make the conserved polar contacts, (ii) occupy enough of the pocket/TM clefts to stabilize the TM6-kinked active state.** Affinity ("address") and activation ("message") are separable — you can shrink or replace the address, but you cannot remove the message.
- Because a **small molecule (Boc5) achieves full agonism purely by occupying the pocket**, the minimal activating element is a **compact pocket-filling moiety**, not a large interface — favorable for a small designed peptide/macrocycle that threads a "message" into the pocket, and unfavorable for bulky antibody scaffolds whose loops cannot reach the deep pocket.
- The competition rule (no modifying GLP-1/exendin/semaglutide) means a design **must satisfy this pharmacophore with a de novo sequence** — i.e., recreate His7-like contacts without copying the HAEGTFTSD… sequence. That is the hard, novel core.

### Gaps
- The **exact GLP1R orthosteric residues** the message contacts (the central polar network / TM6 trigger residues) were not pulled here (adjacent structural-researcher scope); only the mechanism (TM6 kink) and the A8–D15 overlap footprint are documented.
- No source here quantifies the **shortest possible** activating peptide below 11 residues; 11-mer is the documented floor for near-native potency (small molecules aside).

---

## Q2. Engineered-agonist scaffolds for ANY receptor — mechanism templates & transferability to GLP1R

### Takeaway
Nearly all **de novo / engineered protein agonist** successes work by **dimerizing or clustering receptors with defined valency/geometry** (cytokine, growth-factor, death, Notch, TLR, Toll receptors). **That mechanism does NOT transfer to GLP1R**, a monomeric class B GPCR whose activation is an **intramolecular conformational change** (N-terminal message → TM6 swing), not receptor oligomerization. The **only transferable precedents** are the two that act by **conformational/active-state stabilization**: (a) Baker's class A **MRGPRX1 orthosteric-pocket agonists**, and (b) the **exoframe ago-PAM** (TM-surface allosteric activation). Critically, **when the same Baker pipeline faced class B receptors incl. GLP1R, it produced antagonists, not agonists** — the strongest available signal that GLP1R de novo agonism is unsolved and hard.

### Cited Findings — clustering/valency class (does NOT transfer)
- **IL-2/IL-15 mimic (Neo-2/15).** De novo protein recapitulating the cytokine binding site; binds **IL-2Rβγ** and signals **independently of IL-2Rα** — mechanism = engaging/apposing receptor subunits — According to PubMed, Silva 2019 Nature, [DOI 10.1038/s41586-018-0830-7](https://doi.org/10.1038/s41586-018-0830-7).
- **FGFR.** Designed **cyclic homo-oligomers (up to 8 subunits)** with a de novo FGFR-binding module tune signaling by **receptor valency and geometry** (association + transphosphorylation) — Cell 2024, [DOI 10.1016/j.cell.2024.05.025](https://doi.org/10.1016/j.cell.2024.05.025).
- **Notch.** Soluble cytokine-like Notch agonists = **designed complexes with precise valency/geometry that cluster Notch / bridge cells** to supply the mechanical pull — Cell 2025, [DOI 10.1016/j.cell.2025.07.009](https://doi.org/10.1016/j.cell.2025.07.009).
- **TLR3.** De novo minibinders that **bind/cluster TLR3** to initiate signaling (nanomolar) — Nat Commun 2025, [DOI 10.1038/s41467-025-56369-w](https://doi.org/10.1038/s41467-025-56369-w).
- **Novokines.** **Fuse pairs of de novo binders** to force **non-natural receptor heterodimers** → 75/1000+ activated pSTAT — bioRxiv 2025, [DOI 10.1101/2025.10.12.681920](https://doi.org/10.1101/2025.10.12.681920).
- **Death receptors (DR5/Fas).** Agonism scales with **valency/clustering**: trivalent DR5 nanobodies mimic ligand, pentamers most potent via faster DISC/caspase assembly (PMID 25484045); DNA-origami nanopatterning tunes DR5 supercluster valency/spacing; **designed protein nanocages that array antibodies enhance receptor signaling** (Divine et al. 2021 Science, [science.abd9994](https://www.ipd.uw.edu/publication-pdfs/223/fa1115642f8d245bd2af776521143c7b/science.abd9994.pdf)).

### Cited Findings — conformational class (CONCEPTUALLY transfers to GPCR)
- **Insulin receptor (RTK, conformational).** De novo binders to **individual IR ECDs fused in different orientations/with different flexibility** induced **different IR conformational changes → tunable agonism** — the closest "geometry-induced conformational agonism" analogue, but IR is a pre-dimerized RTK — Mol Cell 2025, [DOI 10.1016/j.molcel.2025.09.020](https://doi.org/10.1016/j.molcel.2025.09.020).
- **Class A GPCR orthosteric agonism (direct method template).** Baker MRGPRX1 agonists: "**active-state stabilization alone would be sufficient to generate agonists**"; from MetaGen/RifDock scaffolds docked into a **large orthosteric epitope spanning TM2–7**; cryo-EM showed a design **stabilizing the active-state conformation (0.7 Å Cα-RMSD to model)**; full + partial agonists (EC50 390 nM, 1 µM, 1.4 µM); **7/50 expressed designs active at 10 µM** — Nature 2026, [DOI 10.1038/s41586-026-10656-8](https://doi.org/10.1038/s41586-026-10656-8), [PMC12157396](https://pmc.ncbi.nlm.nih.gov/articles/PMC12157396/). A companion workflow is **motif-directed RFdiffusion starting from a 5-residue peptide placed on hotspot residues in the recessed pocket**.
- **TM-exoframe allosteric agonism (novel mechanism).** **GEMs** are de novo proteins binding the **outer TM-domain surface** (modeled on natural TM regulators), spanning **ago-PAM / NAM / biased** function; an **ago-PAM GEM restored activity of dopamine D1 loss-of-function mutants** — Nature 2026, [DOI 10.1038/s41586-025-09957-1](https://doi.org/10.1038/s41586-025-09957-1).

### Cited Findings — the direct GLP1R negative/positive signal
- **Baker class B outcome: antagonists, not agonists.** For **GLP1R/GIPR/GCGR/CGRPR the pipeline targeted the ECD and produced antagonists** (GLP1R dGI1_024 IC50 **61 nM**, mGI1_008 **39 nM**); the Discussion states **agonists are especially hard** because they require discriminating subtle active-vs-inactive orthosteric differences — [PMC12157396](https://pmc.ncbi.nlm.nih.gov/articles/PMC12157396/). No de novo **class B agonist** is reported there.
- **GLP1R PAM sites are intracellular.** The validated GLP1R PAMs (BETP, "compound 2") are **covalent at Cys347 in ICL3** — i.e., an **intracellular** modulator site, **not reachable by an extracellularly applied protein** — Nat Chem Biol [DOI 10.1038/nchembio.1581](https://doi.org/10.1038/nchembio.1581), [PMC4865917](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4865917/).

### Inferences
- **Explicit transfer verdict:** clustering/valency precedents (Neo-2/15, FGFR, Notch, TLR3, Novokines, DR5/Fas) are **mechanistically irrelevant** to GLP1R — apposing/clustering GLP1R copies will not create the TM6 kink. Do **not** import "design a multivalent/oligomeric agonist" from the cytokine playbook.
- **What transfers:** only **active-state conformational stabilization** — either (a) **orthosteric pocket occupancy delivering a de novo message** (MRGPRX1 template + Boc5 + the EvoBind GLP1R peptide) or (b) **TM-surface exoframe allostery** (GEM template). Both are **class A-proven, class B-unproven**.
- **Format ⇒ mechanism mapping (decisive for the competition's allowed formats):** an **antibody/nanobody/scFv/Fab** CDR loop can reach the **ECD/vestibule** but almost certainly **cannot thread into the deep 7TM pocket** → in that format you are steered toward **ECD/ECL binding**, which Baker's data shows yields **antagonists**, not agonists. A **small designed peptide/miniprotein/macrocycle (≈10–40 aa)** is the format that can physically present a pocket-inserting message. This is the single most important architecture constraint.

### Gaps
- No peer-reviewed de novo **class B GPCR agonist** exists (only the preprint E6 and the class A templates). Transferability of the MRGPRX1 and GEM methods to GLP1R is an **inference**, not demonstrated.
- The exoframe/GEM paper did not test any secretin-family/class B receptor; whether a GLP1R exoframe binder can be an **ago**-PAM (intrinsic efficacy, not just potentiation requiring endogenous GLP-1) is unknown.

---

## Q3. Stapled/bicyclic peptide & affibody/DARPin/monobody agonists; "molecular glue"/clamp agonism

### Takeaway
For GLP1R, the constrained-peptide route is **well precedented and points back to the orthosteric-message strategy**: cyclized/stapled N-terminal peptides retain nM agonism and can be Gs-biased. Scaffold agonists (affibody/DARPin/monobody) have **no GLP1R agonist precedent**; as rigid surface binders they behave like the clustering or ECD-binding classes and are **antagonist-prone** for a monomeric GPCR unless engineered as a conformational clamp/exoframe. "Molecular glue/clamp" agonism maps onto **active-state conformational selection**.

### Cited Findings
- **Stapled/cyclic GLP-1 agonists retain activation** (E5): cyclic 11-mer N-terminal analogue = nM cAMP agonist (Hoang 2015, PMID 25839426); i,i+7 staple scan + double-stapled exendin-4 improve helicity/stability ([PMC7366314](https://pmc.ncbi.nlm.nih.gov/articles/PMC7366314)); helix constraint raises cAMP without β-arrestin (bias) (Plisson 2017 Eur J Med Chem).
- **De novo macrocyclic GLP1R agonist exists (E6):** 18-mer cyclic, EC50 32 nM, sequence-only AF2/EvoBind — bioRxiv [2025.06.06.658268](https://www.biorxiv.org/content/10.1101/2025.06.06.658268v1.full).
- **Clamp/conformational-selection agonism precedent (non-GPCR):** IR agonists built by **fusing de novo binders into geometries that select an active conformation** (E12, Mol Cell 2025).
- **"Diversion"/biased-agonism by de novo binders:** de novo binders to the chemokine **CCL25 convert it into a biased agonist** differentially tuning CCR9 vs ACKR4 — a "ligand-reshaping" concept (bioRxiv 2026.01.23.701245, [pdf](https://www.biorxiv.org/content/10.64898/2026.01.23.701245.full.pdf)).

### Inferences
- A **conformationally constrained de novo macrocycle/mini-helix** that presents a de novo message into the pocket is the **highest-precedent constrained-peptide route**; stapling is a maturation tool (helicity, protease/DPP-IV resistance, Gs bias), not the activation mechanism itself.
- Affibody/DARPin/monobody formats inherit the **ECD-binding → antagonist** risk (Q2); use them only for an **exoframe/clamp** design, not a naive surface binder.

### Gaps
- No affibody/DARPin/monobody **GLP1R agonist** in the literature found; transfer is inferential.

---

## Q4. Competition precedent (Challenges 1 & 2) and Adaptyv de novo success rates

### Takeaway
Challenges 1 (EGFR) and 2 (TNF-α) were **binder** problems (EGFR plain/conditional binder; TNF-α pH-switch conditional binder with mouse cross-reactivity) — both solved with the local **conditional-binder playbook** (RFdiffusion/partial-diffusion → ProteinMPNN → AF2-initial-guess binding gate → orthogonal co-fold → two-state physics for the switch → structural novelty gate). **Challenge 3 (GLP1R) is categorically different: "Design a GLP1R agonist" demands ACTIVATION, which that binder playbook does not address.** Adaptyv's published de novo **binder** hit rates are modest (EGFR R2 ~13% binders, 95% expression); there is **no published de novo agonist success rate** for their pipeline.

### Cited Findings
- **Local repo precedent.** EGFR (Challenge 1) and TNF-α (Challenge 2) used the identical challenge-agnostic conditional-binder pipeline and objective ordering (selectivity > cross-reactivity > affinity; novelty as a gate) — `/home/prachh/v/anthropic-adaptyv-2026-egfr/{README.md,docs/METHODS.md}`, `/home/prachh/v/anthropic-adaptyv-2026-tnf/{README.md,docs/PLAN_TNF.md,docs/METHODS.md}`. Load-bearing binding gate = **AF2 initial-guess pae_interaction < 10 on a full-atom target**; novelty = **structural (ESMFold single-seq max TM vs PDB+AFDB, <0.5→4/4, 0.5–0.8→3/4, ≥0.8 DQ), Proteinbase portal authoritative**; the portal also runs an internal **cousin-dedup**.
- **EGFR competition outcomes (E14).** R1 de novo binder hit rate **2.5% (5/201)**; R2 **95% expression (378/400)** and **~13.25% binders (53/400)** (Adaptyv blog states "14%"); **30/130 participants** produced ≥1 binder — bioRxiv [2025.04.17.648362](https://www.biorxiv.org/content/10.1101/2025.04.17.648362v2.full.pdf); [Adaptyv blog po104](https://www.adaptyvbio.com/blog/po104).
- **Competition structure (E15).** Proteinbase lists: C1 EGFR "conditional binder" (Sep28–Oct7, closed), C2 TNF-α "conditional binder" (Oct5–18), **C3 GLP1R "Design a GLP1R agonist" (Oct12–25)**, C4/C5 TBA. "**Selection will not rely on a single in-silico metric**"; per-challenge requirements "published when each problem opens." Design caps cited elsewhere: **≤20 for Tracks 2/3**, de novo/zero-shot, not modifications of existing binders — [Proteinbase page](https://proteinbase.com/competitions/anthropic-adaptyv-2026).

### Inferences
- The **binder-centric pipeline must be extended with an activation/agonism gate**. A high AF2/Boltz ipTM or low pae_interaction proves **binding, not activation** — exactly the pitfall the task warns about; it is the agonist analogue of "a positive static score proves direction not selectivity" from the TNF switch playbook.
- Because **selection is multi-metric and method-novelty is explicitly rewarded**, an agonist design with a **credible, mechanism-grounded activation rationale** (pocket-message or exoframe) and a **novel method** should score well even at a low wet-lab hit rate — consistent with the diverse-portfolio lesson.

### Gaps
- **The GLP1R challenge's wet-lab readout is not public.** It is unknown whether Adaptyv measures **functional activation (cAMP/GloSensor/Gs/β-arrestin)** or only **binding** — this directly determines whether "agonist rationale" must be designed-in or merely claimed. The challenge's wording ("agonist," vs "binder" for C1/C2) **implies a functional readout**, but this is unconfirmed.
- No published **Adaptyv de novo agonist** hit rate (their public data are binders only).

---

## Q5. SYNTHESIS — ranked candidate strategies, gaps, confidence

### Core design logic (the one thing to get right)
GLP1R activation is **intramolecular conformational change** (N-terminal message → TM6 kink → Gs pocket), **not** receptor clustering. Therefore reject the entire cytokine/death-receptor **valency/clustering** playbook. A de novo agonist must either **(a) place a de novo "message" into the 7TM orthosteric pocket** to make His7-equivalent contacts, or **(b) stabilize the active TM conformation allosterically from the TM exoframe.** Format matters: only small peptides/miniproteins can reach the deep pocket; antibody/nanobody formats steer toward ECD binding → antagonism.

### (A) Ranked strategies

**1. De novo orthosteric "message-macrocycle"/miniprotein (active-state stabilizing).** — *Highest viability; strong direct precedent.*
Design a compact (~12–40 aa) de novo peptide/miniprotein (optionally cyclic/stapled) whose exposed N-terminal/loop segment inserts into the orthosteric pocket and reproduces the activation pharmacophore (a cationic/aromatic His7-surrogate + A8–D15-footprint contacts), stabilizing the TM6-kinked active state.
- *Activation rationale:* mimics the native message (E1–E3), the Boc5 pocket-occupancy mode (E4), and the MRGPRX1 "active-state stabilization" method (E7); a de novo 18-mer already hit **EC50 32 nM** on GLP1R (E6).
- *Why selected / novelty:* use **structure-aware active-state design (motif-directed RFdiffusion from a small message motif + validation on the agonist-state GLP1R–Gs structure)** rather than EvoBind's AF2-only route — a methodologically stronger, novel improvement over the one existing (weakly validated) precedent. De novo sequence satisfies the no-GLP-1-modification rule.
- *Main risk:* threading a de novo segment deep enough to trigger TM6; avoiding a bind-but-not-activate outcome.

**2. De novo two-domain (address+message) mini-agonist.** — *Best novelty×mechanism fit.*
Reconstruct the natural mechanism with **both parts de novo**: a de novo "address" subdomain binding the ECD/ECL (affinity + selectivity) covalently presenting a constrained de novo "message" element positioned to insert into the 7TM.
- *Activation rationale:* directly instantiates the validated 2-domain/2-step activation model (E1, E2); the 11-mer shows the address can be minimal as long as the message inserts (E3); IR precedent shows geometry/orientation of fused de novo modules can *induce* an active conformation (E12).
- *Why selected / novelty:* a **fully de novo two-domain class B agonist is essentially unprecedented** → high design-novelty with the strongest mechanistic rationale; the address domain buys the affinity/selectivity that a bare message peptide lacks.
- *Main risk:* geometric coupling (address pose must present the message with correct register/depth); more moving parts than Strategy 1.

**3. TM-exoframe ago-PAM miniprotein (GEM-style).** — *Highest method-novelty moonshot; hedge.*
Design a de novo protein binding the **lipid/extracellular-facing outer TM surface** of GLP1R to allosterically bias the active state (ago-PAM), analogous to GEMs on D1 (E9).
- *Activation rationale:* exoframe allostery activated/ rescued a class A GPCR (E9); GLP1R is known to be allosterically activatable (E13) — though the validated chemical PAM site (Cys347) is intracellular and thus a *different* site than an exoframe binder would use.
- *Why selected / novelty:* **no class B exoframe agonist exists** → maximal method novelty; orthogonal to everyone else's orthosteric attempts.
- *Main risk:* must bind a **membrane-embedded hydrophobic surface** (hard to design, express, and validate); a PAM may need endogenous GLP-1 to show agonism unless it carries intrinsic efficacy; class-B-unproven.

**4. Active-state ECD/ECL conformational clamp (nanobody/miniprotein).** — *Lower priority; antagonist-risk caution.*
A binder that clamps the agonist-bound ECD/ECL conformation to shift equilibrium toward active.
- *Activation rationale:* conformational selection; plausible given the ECD reorientation in activation.
- *Why caution:* **Baker's class B data show ECD-targeting de novo binders become antagonists, not agonists (E8).** Include only if designed explicitly against the active-state ECD pose with a functional gate; otherwise expect an antagonist. Best suited to antibody formats that cannot reach the pocket — but precisely those are the ones that tend to antagonize.

*Ranking rationale:* 1 > 2 for near-term viability (1 has the most direct precedent and simplest geometry); 2 edges 1 on novelty and affinity/selectivity; 3 is the high-novelty hedge; 4 is the fallback but carries the clearest documented failure mode (antagonism).

### (B) Gaps (what the report writer should flag)
1. **Assay unknown (most consequential):** whether Adaptyv scores GLP1R **function (cAMP/Gs/β-arrestin)** or only **binding** is not public (E15). If binding-only, a mere ECD binder could "win" despite being an antagonist; if functional, activation must be engineered-in and in-silico-validated.
2. **No peer-reviewed de novo class B GPCR agonist** exists — the only direct GLP1R precedent (E6) is a preprint with **AF2-only structural validation, n=3 peptides, GLP1R activity serendipitous** (designed for GCGR), and commercial-conflict disclosure. Treat as proof-of-feasibility, not a validated recipe.
3. **In-silico activation oracle is unestablished.** Structure predictors (AF2/Boltz) model the complex but not the Gs-activation step; there is no validated cheap predictor that a design will *activate* (vs bind). An activation-specific gate (e.g., does it recapitulate the active-state pocket/TM6 geometry; does it displace into the active-state structure; MD of the active vs inactive complex) must be built and positive-controlled (GLP-1, exendin, Boc5 as knowns).
4. **Exact orthosteric trigger residues** for GLP1R (central polar network / TM6 PxxG kink residues the message must contact) not compiled here (adjacent structural scope).
5. **Format eligibility of macrocycles:** rules allow "protein (10–250 aa)"; whether a cyclized peptide counts as a "protein" vs requiring a linear expressible chain should be confirmed against the official C3 terms when published.

### (C) Confidence
- **High:** the activation mechanism (2-domain, His7, TM6 kink) and the minimal pharmacophore (11-mer; Boc5 pocket occupancy) — multiple T1 human-GLP1R sources.
- **High:** clustering/valency de novo agonists do **not** transfer to GLP1R; conformational/orthosteric stabilization is the only viable class — T1 mechanism + T1 Baker class B antagonist-only result.
- **Medium:** that a de novo orthosteric message-peptide/miniprotein can be designed to *activate* GLP1R — one preprint (E6, EC50 32 nM) + strong class A method precedent (E7), but class-B agonism peer-reviewed-unproven.
- **Medium-low:** exoframe ago-PAM transfer to class B GLP1R (class A D1 only).
- **Low/unknown:** the competition's functional assay and in-silico-activation scorability (Gaps 1, 3).

### Key source links (primary)
GLP1R mechanism [Zhang 2017](https://doi.org/10.1038/nature22394) · class B1 review [Aksu 2024](https://doi.org/10.1007/s11033-024-09876-w) · 11-mer [Mapelli 2009](https://doi.org/10.1021/jm900752a) · Boc5 [PMC9171782](https://pmc.ncbi.nlm.nih.gov/articles/PMC9171782) · His7 [Endocrine J 1997](https://doi.org/10.1507/endocrj.44.701) · stapled/cyclic [PMC7366314](https://pmc.ncbi.nlm.nih.gov/articles/PMC7366314) · **de novo GLP1R/GCGR cyclic agonist** [bioRxiv 658268](https://www.biorxiv.org/content/10.1101/2025.06.06.658268v1.full) · **Baker GPCR miniproteins** [Nature 2026](https://doi.org/10.1038/s41586-026-10656-8) / [PMC12157396](https://pmc.ncbi.nlm.nih.gov/articles/PMC12157396/) · **GEM exoframe** [Nature 2026](https://doi.org/10.1038/s41586-025-09957-1) · Neo-2/15 [Silva 2019](https://doi.org/10.1038/s41586-018-0830-7) · FGFR [Cell 2024](https://doi.org/10.1016/j.cell.2024.05.025) · Notch [Cell 2025](https://doi.org/10.1016/j.cell.2025.07.009) · TLR3 [Nat Commun 2025](https://doi.org/10.1038/s41467-025-56369-w) · Novokines [bioRxiv 2025](https://doi.org/10.1101/2025.10.12.681920) · IR agonists [Mol Cell 2025](https://doi.org/10.1016/j.molcel.2025.09.020) · GLP1R PAM [Nat Chem Biol](https://doi.org/10.1038/nchembio.1581) · Adaptyv EGFR lessons [bioRxiv 648362](https://www.biorxiv.org/content/10.1101/2025.04.17.648362v2.full.pdf) / [blog](https://www.adaptyvbio.com/blog/po104) · [Proteinbase competition](https://proteinbase.com/competitions/anthropic-adaptyv-2026)
