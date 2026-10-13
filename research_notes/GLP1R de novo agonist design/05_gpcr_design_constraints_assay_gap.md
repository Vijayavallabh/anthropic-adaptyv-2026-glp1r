# GPCR Design Constraints and the Binding-vs-Functional Assay Gap (GLP1R de novo agonist)

**Scope:** Why a de novo GLP1R binder can pass the detergent (DDM/CHS) binding assay yet fail the cell-surface cAMP/CRE-SEAP agonism assay, and how design should account for membrane/detergent, thermostabilizing mutations, N-glycans (N63/N82/N115), and tags (N-FLAG, C-His).
**Context:** Anthropic × Adaptyv 2026, Challenge 3, Track 3. Target = human GLP1R (UniProt P43220). Binding construct = Sino Biological 13944-H18H-DD (residues 24–432, detergent-solubilized, N-FLAG + C-polyHis, undisclosed thermostabilizing mutations). Functional = full-length cell-surface GLP1R → Gαs → cAMP → CRE-SEAP. Research cutoff 2026-10-13.

---

## EVIDENCE REGISTER

Tiers: **T1** = direct human GLP1R experimental/structural; **T2** = other class B1 GPCR / GLP1R-adjacent; **T3** = other-GPCR extrapolation (A2AR, β1AR, NTSR1); **T4** = vendor/patent/practical guidance (not peer-reviewed).

| # | Topic | Citation / date | System | Finding | Tier / Limitation |
|---|-------|-----------------|--------|---------|-------------------|
| 1 | Two-domain binding/activation | de Graaf 2016, Pharmacol Rev, DOI 10.1124/pr.115.011395 | Human GLP1R review | ECD binds C-terminal half of peptide; peptide N-terminus inserts into 7TM to induce activation | T1 / review |
| 2 | ECD autoinhibition / intrinsic agonist | Yin 2016, Cell Discov, DOI 10.1038/celldisc.2016.42 | Human GLP1R, cell | Apo-receptor auto-inhibited by ECD–TMD contact; peptide binding switches ECD to "auto-activated"; ECD can trans-activate | T1 / mutant-based model |
| 3 | ECD peptide-binding groove architecture | Runge 2008, JBC, DOI 10.1074/jbc.M708740200 | Human GLP1R ECD + exendin-4(9-39), 2.2 Å | Groove = N-terminal α-helix of ECD + loop between two antiparallel β-strands; peptide is amphipathic α-helix | T1 |
| 4 | ECD binds peptide as helix 13–33 | Underwood 2009, JBC, DOI 10.1074/jbc.M109.033829 | Human GLP1R ECD + GLP-1, 2.1 Å | GLP-1 is kinked continuous α-helix Thr13–Val33 on ECD; isolated ECD binds exendin-4 ≫ GLP-1 | T1 |
| 5 | Active-state 7TM hallmark | Zhang 2017, PMID 28538729 (GLP-1R–Gs cryo-EM) | Human GLP1R–Gs | Peptide N-terminus inserts deep into TM core; TM6 bends sharply, intracellular half swings out ~18 Å (Cα Lys346), TM5 ~7 Å | T1 |
| 6 | Gs can drive TM6 opening without ligand | Zhao 2024, Cell Discov, nature.com/articles/s41421-024-00649-0 | GLP1R/GCGR/GIPR–Gs | Ligand-free receptors still promote large outward TM6 movement when coupled to Gs | T1 |
| 7 | Small-molecule agonist pocket | Kawai 2020 (LY3502970/orforglipron), PNAS, DOI 10.1073/pnas.2014879117; PDB 6X1A/6XOX | Human GLP1R | Nonpeptide agonist binds an upper pocket formed by ECD + ECL2 + TM1/2/3/7; contacts BOTH ECD and 7TM; activates | T1 |
| 8 | Small-molecule, species-specific | Danuglipron/PF-06882961, J Med Chem DOI 10.1021/acs.jmedchem.1c01856 + cryo-EM | Human GLP1R | Binding pocket depends on primate-specific Trp33; closed TM7/ECL3 = non-biased agonist | T1 / species caveat |
| 9 | Thermostabilized active-state StaR | RCSB 5NX2 (full-length GLP1R + truncated peptide agonist) | Human GLP1R StaR | 11 thermostabilizing mutations; trapped in ACTIVE conformation | T1 |
| 10 | Thermostabilized inactive full-length | Wu/Song 2020, Nat Commun, nature.com/articles/s41467-020-14934-5 | Human GLP1R | Peptide-free inactive-state 3.2 Å; carries thermostabilizing mutations from prior inactive TMD constructs | T1 |
| 11 | Thermostabilization biases a state | Serrano-Vega 2008 PNAS DOI 10.1073/pnas.0711253105; Frontiers Pharmacol 2015 (fphar.2015.00082) | β1AR, A2AR, NTSR1 | Inactive-state lock lowers agonist affinity (~10×, more for efficacious agonists), antagonist unaffected; thermostab partly works by *preventing the agonist conformation* | T3 |
| 12 | Detergent vs nanodisc conformation | Ye/Prosser 2024 JACS DOI 10.1021/jacs.4c15106 (A2AR ¹⁹F-NMR); Springer 2023 10.1007/s10858-023-00430-7 | A2AR | Antagonist-state equilibria similar across micelle/nanodisc/vesicle; agonist-state differs; DDM/CHS ≠ bilayer, LMNG/CHS ≈ bilayer | T3 |
| 13 | Detergent rigidifies, under-represents flexible states | Bower 2026 Protein Sci DOI 10.1002/pro.70475 | NTSR1 | Detergent micelles favor one state; LMNG structures emphasize rigidified states, under-represent flexible ligand-responsive conformations | T3 |
| 14 | GLP1R N-glyc sites + function | "Role of N-linked glycosylation…GLP-1R," J Physiol Endocrinol Metab, 10.1152/ajpendo.00067.2010 | Human GLP1R, COS-1 | N-glyc at N63/N82/N115; tunicamycin abolished agonist binding; triple Asn→Gln raised EC50 (lower potency); N63,82Q ≈ WT | T1 |
| 15 | N-glyc controls surface expression | Whitaker 2012, PLoS One, DOI 10.1371/journal.pone.0032675 | GIPR/GLP1R, CHO | All Asn glycosylated; N-glyc enhances surface expression + function (weaker effect on GLP1R than GIPR); extends half-life via less ER degradation | T1 |
| 16 | N-glyc matters for class B1 drug design | Lee 2025, Carbohydr Res review, DOI 10.1016/j.carres.2025.109641 | Class B1 GPCRs | N-glyc enhances ligand-binding affinity + activation potency; GLP1R sites contribute collectively; "drug development…should consider N-glycosylation effects" | T2 / review |
| 17 | Sino construct identity | Sino 13944-H18H-DD page + datasheet | Human GLP1R | Arg24–Ser432; N-FLAG + C-polyHis; **HEK293-expressed**; proprietary thermostabilizing mutations; detergent platform; endotoxin <1 EU/µg | T4 / vendor |
| 18 | Sino QC binding | Sino 13944-H18H-DD page | Human GLP1R | Binds anti-GLP1R Ab (glutazumab-derived) EC50 2–6 ng/mL; binds dulaglutide-hIgG4 EC50 10–30 ng/mL (Ni-plate ELISA) | T4 / vendor — but confirms ECD groove is natively presented |
| 19 | His-capture SPR artifacts | Cytiva "Approaches for capture of His-tagged proteins in Biacore" (digi-16083) | SPR | Ni²⁺ surface gives nonspecific binding; native His-rich proteins respond even without tag; use matched reference (anti-His or non-activated NTA) | T4 |
| 20 | BLI nonspecific-binding blocker | ACS Omega 2022, DOI 10.1021/acsomega.1c05659 | BLI | 1% BSA + 20 mM imidazole + 0.6 M sucrose blocker; 20 mM imidazole does not weaken His-tag/Ni-NTA binding | T4 |
| 21 | Reporter amplification masks partial agonism | Willard/Novikoff 2021 ScienceDirect S2212877821000211 | GLP1R, cell | Tirzepatide 31% / MAR709 59% max Gαs recruitment (Emax) vs GLP-1(7-36), **but cAMP Emax equal to full agonist** (downstream amplification) | T1 |
| 22 | CRE-reporter reference potency | Patent methods (CRE-luc HEK293) | GLP1R reporter | Exendin-4 used as 100% reference; exendin-4 EC50 ~1.93 nM in CRE-luciferase | T4 / patent methods |

---

## KEY QUESTION 1 — Does a detergent-solubilized (DDM/CHS) 24–432 construct present a native, agonist-competent 7TM pocket?

### Takeaway
The detergent 24–432 construct contains **both** the ECD groove and the full 7TM, and its ECD groove is demonstrably natively folded (it captures dulaglutide and an anti-GLP1R antibody). However, antagonist/inactive conformations of GPCRs are robust across membrane mimetics while the **agonist/active 7TM conformation is the one most perturbed by detergent** — so the detergent construct is a reliable readout of *binding/capture* but an unreliable readout of whether the 7TM is in an *activatable* state.

### Cited Findings
- The Sino 13944-H18H-DD construct spans Arg24–Ser432, i.e. ECD (≈24–139) + the complete 7TM bundle; it is detergent-solubilized and HEK293-expressed — [Sino product page](https://www.sinobiological.com/recombinant-proteins/human-glp1r-13944-h18h-dd).
- The construct's ECD groove is natively presented: it binds dulaglutide-hIgG4 (a GLP-1/Fc agonist) with EC50 10–30 ng/mL and an anti-GLP1R antibody with EC50 2–6 ng/mL in a Ni-plate ELISA — [Sino product page](https://www.sinobiological.com/recombinant-proteins/human-glp1r-13944-h18h-dd). This confirms the orthosteric peptide-capture surface survives detergent solubilization.
- Across GPCRs, **antagonist-bound conformational equilibria are similar in detergent micelles, nanodiscs, and vesicles, whereas agonist-bound equilibria differ between environments** — [Ye/Prosser A2AR ¹⁹F-NMR, JACS 2024](https://pubs.acs.org/doi/10.1021/jacs.4c15106).
- Conformational populations differ strongly between **DDM/CHS and LMNG/CHS** micelles; LMNG/CHS resembles the lipid-bilayer nanodisc, implying **DDM/CHS is further from the native bilayer state** — [A2AR ¹⁹F-NMR, J Biomol NMR 2023](https://link.springer.com/article/10.1007/s10858-023-00430-7).
- Detergent/LMNG-stabilized structures "emphasize…rigidified states and under-represent flexible, ligand-responsive conformations" — [Bower, Protein Science 2026 (NTSR1)](https://onlinelibrary.wiley.com/doi/full/10.1002/pro.70475).
- Sino also sells a **nanodisc** GLP1R (13944-H98H-NA-B) and a biotinylated AVI version (13944-H49H-B) — [Sino 13944-H49H-B](https://www.sinobiological.com/recombinant-proteins/human-glp1r-13944-h49h-b), useful as orthogonal membrane-mimetic checks.

### Inferences
- In a micelle the detergent belt wraps the TM hydrophobic surface, leaving the **extracellular ECD and the 7TM extracellular vestibule solvent-exposed** — so a mini-protein/peptide binder can physically reach both in the binding assay (the construct is not the limiting factor for *access*).
- Because DDM/CHS biases away from the native agonist/active state, a design can register strong *binding* to the detergent construct without that binding corresponding to an activatable receptor — the binding assay is **necessary but not sufficient** for agonism.
- The nanodisc sibling product is a cheap orthogonal filter: a true agonist-relevant binder should bind the nanodisc construct at least as well as the detergent construct; a detergent-only binder is a red flag.

### Gaps
- No GLP1R-specific NMR/HDX comparison of DDM/CHS vs nanodisc conformational populations was found; the detergent-vs-nanodisc evidence is A2AR/NTSR1 (class A) extrapolation.
- The datasheet PDF (cdn1.sinobiological.com/reagent/13944-H18H-DD.pdf) returns HTTP 403; exact detergent identity (DDM/CHS vs LMNG), purity %, and buffer were not directly confirmed beyond "detergent platform" and the assignment-stated DDM/CHS.

---

## KEY QUESTION 2 — Do the thermostabilizing mutations lock the inactive state / reduce agonist-induced conformational change? How big is this risk and can it be mitigated?

### Takeaway
This is the single largest translation risk. Conformational thermostabilization frequently works *by preventing the agonist (active) conformation*, which lowers agonist affinity ~10× and biases the receptor to the inactive state. A binder selected purely for affinity to the undisclosed-StaR detergent construct may be stabilizing an inactive/non-native 7TM vestibule and could behave as an antagonist/inverse agonist (or simply a non-agonist) on the WT cell-surface receptor. The ECD groove is the conformation-independent, construct-vs-WT-shared surface — but ECD-only binding does not activate (see Q5), so it is a mitigation for *binding transfer*, not for *agonism*.

### Cited Findings
- StaR/conformational thermostabilization = a small number of point mutations away from the ligand site that **bias the receptor to one physiologically relevant conformational state** — [StaR review, Drug Discov Today Technol 2016](https://www.sciencedirect.com/science/article/abs/pii/S1471489216300595).
- For β1AR, inserting thermostabilizing mutations **reduced the affinity of all ligands ~10-fold, with the most efficacious agonists reduced even more**; decreased agonist affinity with unaffected antagonist affinity is the signature of **inactive-state stabilization** — [Frontiers Pharmacol review 2015](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2015.00082/full).
- Mechanistically, "a proportion of the thermostabilization is due to mutations that **prevent the formation of the agonist conformation**," because agonist-state conformations are intrinsically less stable — [Serrano-Vega PNAS 2008](https://www.pnas.org/doi/10.1073/pnas.0711253105); [Frontiers Pharmacol 2015](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2015.00082/full).
- The opposite bias is also possible: agonist-state-locked A2AR-GL26 shows antagonists binding with up to **320-fold decreased affinity**; some constructs (NTSR1, A2AR active-intermediate) retain near-WT agonist affinity — [Frontiers Pharmacol 2015](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2015.00082/full). So the direction of bias is construct-specific, not universally "inactive."
- GLP1R can be thermostabilized in EITHER state: an **active-state** full-length StaR with 11 mutations exists ([RCSB 5NX2](https://www.rcsb.org/structure/5NX2)); **inactive-state** thermostabilized full-length constructs also exist ([Nat Commun 2020](https://www.nature.com/articles/s41467-020-14934-5)). The commercial 13944-H18H-DD mutations are undisclosed, so its state bias is unknown.
- The active state requires a large TM6 outward swing (~18 Å at Cα Lys346) driven by deep insertion of the peptide N-terminus — [Zhang 2017 GLP-1R–Gs cryo-EM, PMID 28538729](https://pubmed.ncbi.nlm.nih.gov/28538729/). Mutations that damp TM6 mobility would blunt exactly this.

### Inferences
- **Risk magnitude: HIGH but bounded.** If the undisclosed mutations are inactive-biased (common for binding-reagent/antibody-antigen StaRs), a 7TM-vestibule binder optimized against the construct is at material risk of being a non-agonist/antagonist on WT. If they are mild/active-compatible (like 5NX2), the risk is lower. Because the vendor markets it as an antibody-screening/binding antigen, inactive or at least rigidified bias is the prudent default assumption.
- **Mitigation hierarchy:**
  1. Anchor affinity on the **ECD groove**, which is conformation-independent and identical between construct and WT (the ECD carries no 7TM thermostabilizing mutations). This guarantees binding *transfers* from construct to WT — but does not by itself give agonism.
  2. For agonism, design the 7TM-engaging element against the **WT active-state** structure (e.g., the GLP-1R–Gs cryo-EM active state, PMID 28538729; or 5NX2 active StaR), NOT against an inactive model, and **do not over-fit the 7TM contacts to the detergent construct's pocket**, which may be non-native.
  3. Require an **active-state co-fold** check: the design + WT GLP1R (+ optionally Gs) should predict/accommodate the open-TM6 active conformation and reproduce peptide-N-terminus-like contacts to TM1/2/3/5/6 and ECL2/ECL3. A design that only co-folds well against the inactive/thermostabilized 7TM is suspect.
  4. Where feasible, counter-screen on the **nanodisc** construct and on WT cell-surface receptor to catch conformation-selection artifacts.

### Gaps
- The identity, number, and positions of the 13944-H18H-DD thermostabilizing mutations are undisclosed; whether they bias inactive, active, or are state-neutral is unknown and could not be resolved from public sources.
- No direct measurement found of how the specific commercial construct's agonist vs antagonist affinities compare to WT.

---

## KEY QUESTION 3 — N-glycosylation (N63/N82/N115): which surfaces are shielded, does the Sino construct carry glycans, and how should design avoid clashes?

### Takeaway
The Sino construct is HEK293-expressed, so N63/N82/N115 carry human-type complex N-glycans — and so does the cell-surface functional receptor; glycosylation is therefore present and broadly consistent across **both** assays. The practical design risk is not an assay mismatch but **modeling against a glycan-free structure**: all three sites are on the ECD, and designing an epitope that overlaps a glycan will clash in reality in both assays.

### Cited Findings
- GLP1R is N-glycosylated at **Asn63, Asn82, Asn115**; blocking N-glyc (tunicamycin) interfered with biosynthesis/trafficking and **abolished agonist binding**; triple Asn→Gln (N63,82,115Q) significantly **raised EC50** (reduced potency) while N63,82Q matched WT — [Role of N-linked glycosylation in GLP-1R, Am J Physiol Endocrinol Metab 2010](https://journals.physiology.org/doi/full/10.1152/ajpendo.00067.2010).
- When human GLP1R is expressed in CHO cells, **each Asn is glycosylated**; N-glyc enhances cell-surface expression and function in parallel (effect weaker on GLP1R than GIPR) and extends receptor half-life by reducing ER degradation — [Whitaker 2012, PLoS One, DOI 10.1371/journal.pone.0032675](https://doi.org/10.1371/journal.pone.0032675).
- Across class B1 GPCRs, N-glycans "enhance pharmacodynamic properties such as receptor–ligand binding and receptor activation potency," and for GLP1R the sites **contribute collectively**; the review explicitly states drug development "should consider the N-glycosylation effects on peptide ligand affinity and receptor activation potency" — [Lee 2025, Carbohydr Res, DOI 10.1016/j.carres.2025.109641](https://doi.org/10.1016/j.carres.2025.109641).
- The Sino binding construct is expressed in **HEK293** cells — [Sino product page](https://www.sinobiological.com/recombinant-proteins/human-glp1r-13944-h18h-dd) — i.e. it carries mammalian complex-type glycans, not high-mannose/aglycosyl.

### Inferences
- All three sequons (N63, N82, N115) lie inside the ECD (24–139), i.e. on the same domain as the peptide-capture groove. The **safest design choice is to target the ECD groove face and the 7TM extracellular vestibule and avoid placing the binder epitope on top of any of the three glycan sites**; glycans can be modeled (e.g., add representative complex N-glycans at N63/N82/N115) and used as an exclusion zone (~15–20 Å) during design/scoring.
- Because glycans are present in BOTH the HEK293 binding construct and the cell-surface functional receptor, glycan shielding is a **consistent constraint, not a source of binding→function divergence** — a design that binds around the glycans in the detergent assay should see the same glycans in the functional assay. (Minor residual risk: HEK293 vs the functional cell line may process glycans slightly differently, but both are mammalian complex-type.)
- A design validated only against a deglycosylated cryo-EM model or a glycan-free AlphaFold model risks an epitope that is sterically occluded by glycan in the real receptor — this would fail BOTH assays, not just one.

### Gaps
- No residue-level map found of which ECD surface each glycan (N63 vs N82 vs N115) occludes, nor how close each is to the peptide-binding groove; this should be checked directly on a glycosylated GLP1R model/structure.
- The specific glycoform/heterogeneity of the Sino HEK293 preparation is not disclosed.

---

## KEY QUESTION 4 — Tags (N-FLAG, C-His): risk of binding the tag/linker, and is the FLAG near the ECD groove?

### Takeaway
There are two distinct tag risks: (a) a **binding false-positive** where the design engages the C-terminal poly-His / capture chemistry or the N-terminal FLAG rather than the receptor; and (b) the FLAG sits at the mature N-terminus, which is **contiguous with the ECD N-terminal α-helix that forms part of the peptide-binding groove** — so a groove-targeting design could pick up (or be perturbed by) the non-native FLAG. Both are manageable with standard controls and by designing epitopes away from the termini.

### Cited Findings
- Construct tags: **N-terminal FLAG** (DYKDDDDK) + **C-terminal polyHis**, on the Arg24–Ser432 chain — [Sino product page](https://www.sinobiological.com/recombinant-proteins/human-glp1r-13944-h18h-dd).
- The ECD peptide-binding groove is built from "a well defined **α-helix in the N terminus** of nGLP-1R and a loop between two antiparallel β-strands" — [Runge 2008, JBC, DOI 10.1074/jbc.M708740200](https://doi.org/10.1074/jbc.M708740200). The bound peptide is an amphipathic α-helix (GLP-1 as a kinked helix Thr13–Val33 — [Underwood 2009, JBC, DOI 10.1074/jbc.M109.033829](https://doi.org/10.1074/jbc.M109.033829)).
- His-capture SPR artifacts: a Ni²⁺ surface without ligand can give nonspecific binding, and **native histidine-rich proteins can respond even without a His-tag**; Cytiva recommends a matched reference (anti-His-immobilized or non-activated NTA) — [Cytiva, Approaches for capture of His-tagged proteins](https://cdn.cytivalifesciences.com/api/public/content/digi-16083-pdf).
- BLI blocker to suppress nonspecific binding: 1% BSA + **20 mM imidazole** + 0.6 M sucrose; 20 mM imidazole does not weaken His-tag/Ni-NTA binding — [ACS Omega 2022, DOI 10.1021/acsomega.1c05659](https://doi.org/10.1021/acsomega.1c05659).

### Inferences
- **Immobilization geometry is favorable:** C-terminal His-capture tethers the receptor by the (truncated) intracellular C-terminus, orienting the **extracellular ECD + 7TM vestibule toward solution** — i.e. the agonist-relevant surface is the one presented to the analyte. Good for presenting the right face; neutral-to-helpful for the gap.
- **FLAG proximity risk:** the mature N-terminus (res ~24) leads directly into the ECD α1 helix that forms one wall of the peptide groove. An N-terminal FLAG is therefore spatially adjacent to the groove, and its acidic DYKDDDDK motif is a plausible off-target electrostatic hotspot. A groove-targeting design could gain affinity from FLAG contacts that do not exist on the native (non-tagged) WT receptor, inflating apparent binding. (Inference from Runge 2008 architecture + construct design; not directly measured.)
- **Controls to require:** (i) an irrelevant His-tagged protein of similar size on the same capture chemistry; (ii) a reference/unloaded sensor; (iii) soluble His (imidazole) and/or soluble FLAG peptide competition; (iv) ideally orthogonal confirmation on the AVI-biotin construct (13944-H49H-B) which uses a different immobilization. Epitope should be mapped to the receptor body, not the termini.

### Gaps
- No structure of the tagged construct was found, so FLAG-to-groove distance is inferred from ECD architecture, not measured.
- Whether the design pipeline will even see the tags (many groups model the untagged receptor) is a workflow choice; if the untagged receptor is used for design, FLAG off-target binding is only an assay-interpretation risk, not a design driver.

---

## KEY QUESTION 5 — Binding modality (His-capture SPR/BLI) vs functional readout: what must a design satisfy to pass BOTH?

### Takeaway
To pass the binding assay a design needs measurable affinity to the construct (His-captured SPR/BLI); to pass the functional assay it must be an **agonist** — i.e. it must engage the **7TM extracellular vestibule and drive the active-state transition (TM6 opening)**, not merely dock on the ECD. The central binding→function gap is precisely this: the ECD groove is a high-affinity *capture* site whose occupancy alone does **not** trigger Gαs/cAMP. Reassuringly, the CRE-SEAP reporter is strongly amplified, so even a partial agonist can read as functionally positive — but it still must be an agonist, not just a binder.

### Cited Findings
- **Two-domain mechanism:** the ECD binds the C-terminal half of the peptide; the **peptide N-terminus inserts into the 7TM to induce activation** — [de Graaf 2016, Pharmacol Rev, DOI 10.1124/pr.115.011395](https://doi.org/10.1124/pr.115.011395). The apo-receptor is auto-inhibited by the ECD; peptide binding switches it to an "auto-activated" state — [Yin 2016, Cell Discov, DOI 10.1038/celldisc.2016.42](https://doi.org/10.1038/celldisc.2016.42).
- **Activation structural hallmark:** peptide N-terminus inserts deep into the TM core; TM6 bends and its intracellular end swings out ~18 Å, opening the Gαs site — [Zhang 2017, PMID 28538729](https://pubmed.ncbi.nlm.nih.gov/28538729/). Gs coupling alone can also drive TM6 opening in ligand-free complexes — [Zhao 2024, Cell Discov](https://www.nature.com/articles/s41421-024-00649-0).
- **A small molecule in the upper 7TM/ECD vestibule can activate:** orforglipron/LY3502970 binds a pocket formed by the ECD + ECL2 + TM1/2/3/7 — contacting **both** ECD and 7TM — and is a full oral agonist — [Kawai 2020, PNAS, DOI 10.1073/pnas.2014879117](https://doi.org/10.1073/pnas.2014879117). This shows agonism does not require reaching the deepest peptide pocket, but **does** require 7TM engagement that perturbs the activation machinery. Danuglipron's pocket depends on primate-specific Trp33 and adopts a closed TM7/ECL3 (non-biased) conformation — [J Med Chem 2022, DOI 10.1021/acs.jmedchem.1c01856](https://doi.org/10.1021/acs.jmedchem.1c01856).
- **Reporter amplification masks partial agonism:** tirzepatide and MAR709 are partial agonists for proximal Gαs recruitment (Emax 31% and 59% of GLP-1(7-36)) yet give **cAMP Emax indistinguishable from the full agonist** because of downstream amplification — [Novikoff/Müller 2021, Mol Metab, ScienceDirect S2212877821000211](https://www.sciencedirect.com/science/article/pii/S2212877821000211). CRE-SEAP (transcriptional reporter) adds a further amplification/integration step beyond cAMP.
- **Reference agonist / potency scale:** exendin-4 (or GLP-1(7-36)NH2) is the standard 100% reference; in a CRE-luciferase HEK293 reporter exendin-4 EC50 ≈ **1.93 nM** — [patent methods](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11932618) (T4). GLP1R has appreciable constitutive/basal activity (class B1), so inverse agonism/antagonism is detectable as a drop below basal.

### Inferences
- **Pass-both profile:** a design should (1) dock on the ECD groove and/or upper vestibule for affinity (binding assay), AND (2) place a chemical "trigger" into the 7TM extracellular vestibule that reproduces agonist-like contacts (TM1/2/3/6/7, ECL2/ECL3) and is compatible with TM6 opening (functional assay). An ECD-only binder is the canonical false positive: strong SPR/BLI signal, zero cAMP (or even antagonism if it locks the auto-inhibited ECD–TMD arrangement).
- The reporter's amplification **lowers the efficacy bar**: a weak/partial de novo agonist may still cross the CRE-SEAP threshold. This is favorable, but the readout is slow (hours) and integrates signal, so it will not rescue a pure binder with no intrinsic efficacy.
- Because the thermostabilized detergent construct may not report efficacy at all (Q2), **binding rank order on the construct is a poor predictor of functional rank order**; functional potency should be predicted independently (active-state co-fold / induced TM6 opening), not read off binding affinity.
- Practically, a design most likely to pass both is a **peptide/mini-protein that mimics GLP-1's bipartite engagement** (ECD-binding helix + a 7TM-inserting N-terminal segment), validated against the WT active-state structure, rather than a flat ECD-surface binder.

### Gaps
- The exact CRE-SEAP protocol parameters for this challenge (cell line, reference agonist, fold-over-basal threshold, incubation time, whether a minimum % of exendin-4/GLP-1 Emax is required to "pass") are not public; patent/vendor methods are only indicative.
- No public dataset found on de novo (non-natural) GLP1R agonists passing a reporter assay, so the empirical hit rate for binder→agonist conversion at GLP1R is unknown.

---

## (A) RANKED TAKEAWAYS — risks + mitigations

1. **[HIGHEST] ECD-only "capture" binders are the dominant false-positive.** The ECD groove is a high-affinity site whose occupancy does not activate; a flat ECD binder passes detergent binding and fails cAMP (possibly even antagonizes). *Mitigation:* require a 7TM-vestibule-engaging element (mimic the GLP-1 N-terminus or the orforglipron ECD+TM1/2/3/7 pocket) and validate by active-state co-fold showing compatibility with TM6 opening — do not treat binding affinity as an agonism proxy. [de Graaf 2016; Yin 2016; Zhang 2017 PMID 28538729; Kawai 2020 PNAS]

2. **[HIGH] Undisclosed thermostabilizing mutations likely bias the construct's 7TM toward a non-native/inactive conformation.** Thermostabilization often works by *preventing the agonist conformation* (β1AR: ~10× agonist-affinity loss), so a binder optimized to the construct's 7TM pocket may stabilize an inactive state and fail on WT. *Mitigation:* anchor affinity on the conformation-independent ECD groove (identical in construct and WT), design 7TM contacts against the WT **active-state** structure (not the construct/inactive model), avoid over-fitting to the detergent pocket, and counter-screen on the nanodisc construct (13944-H98H-NA-B) and WT cells. [Serrano-Vega 2008; Frontiers Pharmacol 2015; RCSB 5NX2; Nat Commun 2020]

3. **[MEDIUM] DDM/CHS detergent under-represents the active/agonist conformation.** Antagonist states are robust across mimetics but agonist states are detergent-sensitive, and DDM/CHS is further from the bilayer than LMNG/CHS or nanodiscs. *Mitigation:* use the nanodisc sibling product as an orthogonal binding check; weight functional prediction over construct binding affinity. [JACS 2024 A2AR; Protein Sci 2026 NTSR1]

4. **[MEDIUM] Glycan clash from designing against a glycan-free model.** N63/N82/N115 carry complex glycans in both the HEK293 construct and the cell-surface receptor; an epitope overlapping a glycan fails in reality. *Mitigation:* model complex N-glycans at N63/N82/N115 and treat them as a ~15–20 Å exclusion zone; prefer the groove/vestibule faces. Note this is a *consistent* constraint across both assays, not a source of divergence. [AJP-Endo 2010; Whitaker 2012; Lee 2025]

5. **[MEDIUM→LOW] Tag false positives and FLAG-near-groove perturbation.** The design could bind the C-His/capture chemistry or the acidic N-FLAG, and the FLAG sits adjacent to the ECD groove-forming α1 helix. *Mitigation:* standard SPR/BLI controls (irrelevant His-tagged protein, matched reference surface, imidazole/FLAG competition), orthogonal immobilization (AVI-biotin construct), and epitope mapping to the receptor body; design the binder epitope away from both termini. [Cytiva His-capture; ACS Omega 2022; Runge 2008]

6. **[LOW / net-favorable] The CRE-SEAP reporter is strongly amplified, lowering the efficacy bar.** Even partial agonists can read as functionally positive (tirzepatide = 31% Gαs Emax but full cAMP Emax). *Implication:* intrinsic efficacy, however modest, is rewarded — but a zero-efficacy binder is not rescued. Benchmark against exendin-4/GLP-1(7-36) (EC50 ~1–2 nM). [Novikoff 2021; patent CRE-luc methods]

## (B) GAPS
- Identity/positions/state-bias of the 13944-H18H-DD thermostabilizing mutations are undisclosed; cannot confirm whether the construct's 7TM is inactive-, active-, or neutral-biased.
- Sino datasheet PDF is 403-blocked; exact detergent (DDM/CHS vs LMNG), purity, buffer, and glycoform not directly confirmed (DDM/CHS taken from the assignment brief).
- No residue-level map of which ECD surface each of N63/N82/N115 shields relative to the peptide groove.
- Exact challenge functional-assay parameters (cell line, reference agonist, pass threshold / minimum %Emax, incubation) not public.
- No GLP1R-specific detergent-vs-nanodisc conformational dataset; that evidence is class A (A2AR/NTSR1) extrapolation.
- No public precedent for a de novo (non-natural) GLP1R agonist converting from binder to functional agonist — empirical binder→agonist hit rate unknown.

## (C) CONFIDENCE
- **High confidence:** (i) ECD-only binding is non-activating and the two-domain/7TM-insertion requirement is the core gap (multiple T1 human-GLP1R structural + pharmacological sources); (ii) the construct is HEK293/glycosylated at N63/N82/N115 and the ECD groove is natively presented (vendor QC + T1 glyco papers); (iii) thermostabilization can bias conformational state and reduce agonist affinity (well-established principle, T3 but mechanistically general); (iv) reporter amplification can mask partial agonism (T1 GLP1R).
- **Medium confidence:** the *direction and magnitude* of the specific commercial construct's state bias (undisclosed mutations → inferred, not measured); the detergent-under-represents-active-state claim as applied to GLP1R (class A extrapolation); FLAG-to-groove proximity (architectural inference, not a tagged-construct structure).
- **Low confidence / unknown:** quantitative binder→agonist conversion probability for this specific assay pair; exact functional pass criteria.
- **Overall:** The qualitative risk model (bind ECD + must engage/activate 7TM; beware thermostabilized/detergent conformation; account for glycans and tags) is well supported. The largest residual uncertainty is the undisclosed thermostabilizing mutations, which makes the WT active-state structure — not the commercial construct — the correct design/validation reference for agonism.
