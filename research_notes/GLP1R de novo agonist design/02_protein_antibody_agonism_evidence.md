# 02 — Can a protein / nanobody / scFv / Fab / mini-protein AGONIZE GLP1R (or any GPCR), and by what mechanism?

Scope: the core feasibility question for the **activation** hypothesis of Anthropic × Adaptyv 2026, Challenge 3, Track 3 (de novo agonist of human GLP1R, UniProt P43220, a **class B1 secretin-family GPCR**). Win condition = **activation** (cell-surface Gαs/cAMP, CRE-SEAP), not binding. **Binding ≠ activation is flagged throughout** — it is the dominant risk here.

Research date 2026-10-13. Training cutoff Jan 2026; 2025–2026 items verified with live tools (PubMed/ChEMBL MCP + web). Peer-reviewed vs preprint vs patent/trade is labeled on every item.

---

## EVIDENCE REGISTER

| # | Citation (type) | Date | System (class, species) | Finding | Limitation / gap to GLP1R |
|---|---|---|---|---|---|
| 1 | Faust et al., *Nature* [10.1038/s41586-022-05173-3](https://doi.org/10.1038/s41586-022-05173-3) (PMID 35940204) — **peer-reviewed** | 2022 | TSHR, **class A** glycoprotein-hormone R, human | Activating human autoantibody **M22** (a Fab/mAb) and TSH both push the leucine-rich ECD into an **upright active conformation**; M22 heavy/light chains mimic TSH α/β subunits. Active cryo-EM with M22 + allosteric agonist ML-109 | ECD-reorientation activation is **specific to glycoprotein-hormone receptors** with a large LRR ECD; GLP1R ECD is small and does not work this way. M22 is a natural autoantibody, not engineered de novo |
| 2 | Ma et al., *Sci Adv* [10.1126/sciadv.aax7379](https://doi.org/10.1126/sciadv.aax7379); PDB 6KNM — **peer-reviewed** | 2020 | Apelin R (APJ/APLNR), **class A** peptide R, human | Single-domain antibody **JN241** binds the extracellular side (ECL2) and pushes its **CDR3 loop into the orthosteric pocket** (antagonist); **inserting one Tyr into CDR3 → full agonist JN241-9**. "First cocrystal of a class A GPCR with a functional antibody" | Immunization yielded **only antagonists**; agonism needed rational CDR3 engineering. Class A, shallow peptide pocket; class-B extrapolation unproven |
| 3 | Nat Commun [10.1038/s41467-024-50827-7](https://doi.org/10.1038/s41467-024-50827-7); PDB 8QJ2 — **peer-reviewed** | 2024 | MC4R, **class A** melanocortin peptide R, human | Panel of MC4R-specific **full-agonist nanobodies**; lead **pN162 binds deep in the orthosteric pocket, CDR3 occupies the α-MSH site** (active-state, 3.4 Å) | Discovery used an engineered ConfoBody + an active-state-stabilized MC4R–β2AR hybrid as bait. Class A; not class B |
| 4 | Cheloha et al., *Nat Commun* [10.1038/s41467-020-15884-8](https://doi.org/10.1038/s41467-020-15884-8) (PMC7190724) — **peer-reviewed** | 2020 | **PTHR1 (class B1)**, cells + mouse | Nanobody tethered to a weak PTH N-terminal fragment = potent agonist. **"No VHHs that directly activate GPCRs have been identified"; VHH alone did NOT activate**, the conjugate did. VHH-PTH(1-14) EC50 **0.075 nM vs 4.3 nM** free peptide (57×); >4500× PTHR1-vs-PTHR2 selectivity | Agonism comes from the **tethered PEPTIDE pharmacophore**, not the nanobody; VHH binds ECD and raises the peptide's effective concentration (avidity/tethering). Mechanism, not a standalone protein agonist |
| 5 | PTHR1 biased / "activation in trans", *Nat Commun* [10.1038/s41467-024-49068-5](https://doi.org/10.1038/s41467-024-49068-5) — **peer-reviewed** | 2024 | **PTHR1 (class B1)** | Nanobody–peptide conjugate = **most biased PTHR1 agonist reported**; signals via "activation **in trans**" across two receptor protomers | Still a conjugate (peptide provides agonism); PTHR1 ≠ GLP1R |
| 6 | ADGRG2 nanobody, *Nat Chem Biol* [10.1038/s41589-025-01896-2](https://doi.org/10.1038/s41589-025-01896-2) (PMID 40374856) — **peer-reviewed** | 2025 | ADGRG2, **adhesion GPCR (class B2)**, cells + animal | Engineered biparatopic nanobody **Nb23-bi** targets the N-terminal fragment and acts as a **positive allosteric modulator**, enhancing DHEA-induced activation; therapeutic in animal models | A **PAM that enhances an existing agonist**, not a standalone agonist. Adhesion-GPCR tethered-agonist biology differs from secretin-class GLP1R |
| 7 | Baker/IPD, bioRxiv [2025.03.23.644666](https://www.biorxiv.org/content/10.1101/2025.03.23.644666) → *Nature* 2026 [10.1038/s41586-026-10656-8](https://doi.org/10.1038/s41586-026-10656-8); PDB 9MNI — **preprint + peer-reviewed** | 2025–2026 | Multiple GPCRs; **de novo miniproteins** | **De novo miniprotein agonists only for class A MRGPRX1** (2 full EC50 **390 nM & 1 µM**, 1 partial 1.4 µM; ~7/50 designs active at 10 µM). Agonists **occlude the orthosteric site (TM2–TM7)** to stabilize the active state. **GLP1R, GIPR, GCGR, CGRPR were made only as ANTAGONISTS** binding the ECD; **GLP1R binders 27 nM and 5.3 nM** | **No class B agonist achieved.** "It has been particularly difficult to generate GPCR agonists… need for conformational selectivity." The GLP1R designs were **binders/antagonists, not agonists** — a direct negative result for this challenge |
| 8 | EvoBind, bioRxiv [2025.06.06.658268](https://www.biorxiv.org/content/10.1101/2025.06.06.658268) — **preprint** | 2025 | **GLP1R + GCGR**, cells | **Blind (sequence-only, no structure) de novo CYCLIC PEPTIDE dual agonists**; 18-mer EC50 **32 nM (GLP1R)** / 542 nM (GCGR); "no similarity to known agonists" | Not peer-reviewed; a **peptide**, not an antibody/scaffold; presumed orthosteric peptide mimicry; cell cAMP only |
| 9 | Wei et al., ProteinMPNN GLP-1RA, bioRxiv [2025.03.26.645438](https://www.biorxiv.org/content/10.1101/2025.03.26.645438) / *Adv Sci* 2025 (PMC12561408) — **preprint + peer-reviewed** | 2025 | **GLP1R**, cells + mouse | Template-based design (from semaglutide–GLP1R, PDB 7KI0) of **GLP-1 analogue peptides**; 52% in-vitro success; long-acting leads | **GLP-1 analogue peptides** (native mechanism), not novel scaffolds/antibodies |
| 10 | Orforglipron/LY3502970, PDB 6XOX; *Sci Transl Med* [10.1126/scitranslmed.adp5765](https://doi.org/10.1126/scitranslmed.adp5765) — **peer-reviewed** | 2020/2025 | **GLP1R (class B1)**, cryo-EM | Non-peptide agonist binds the **upper-bundle orthosteric pocket**; contacts ECD, ECL2, **TM1/2/3/7**; oxadiazolone H-bonds **Lys197 (TM2)** | Small molecule reaching **into the 7TM**; shows activation from the upper bundle but still requires pocket penetration |
| 11 | Danuglipron/PF-06882961, PDB 6X1A; PF-06883365 PDB 7S15 — **peer-reviewed** | 2021 | **GLP1R**, cryo-EM | Occupies the **receptor core, overlapping the GLP-1 N-terminal end**; **Trp33 (ECD) caps** the top of the pocket; drives a distinct active conformation | Small molecule in the **deep/core 7TM pocket**; a protein would need a loop/helix to reach there |
| 12 | TT-OAD2 (chemotype comparison; ResearchGate 396495949 and *Nature* 2020 Zhang et al.) — **peer-reviewed** | 2020–2025 | **GLP1R**, cryo-EM | Binds TM3/ECL2; a dichlorobenzyl group **protrudes beyond the orthosteric pocket into the extrahelical region between TM2/TM3**; biased agonist | Unusual, partly extrahelical pocket — still within the TM region, not purely extracellular |
| 13 | BETP, *Nat Chem Biol* 2016 (PMC4865917) — **peer-reviewed** | 2016 | **GLP1R**, cells | Covalent **ago-PAM** modifies **Cys347 (intracellular loop 3)** + Cys438; C347 essential | **Intracellular/covalent site — NOT reachable by an extracellular biologic** |
| 14 | Compound 2 ago-allosteric, PMC8213797 / bioRxiv 2021.05.29.446269 — **peer-reviewed** | 2021 | **GLP1R**, cryo-EM | Covalently bonds **C347 at the cytoplasmic end of TM6 and triggers TM6 outward movement**; C347A abolishes PAM effect but not peptide signaling | Cytoplasmic covalent PAM — proof an allosteric site can drive TM6, but **not extracellularly accessible** |
| 15 | Steyaert/Manglik review, *Annu Rev Pharmacol Toxicol* [10.1146/annurev-pharmtox-010716-104710](https://doi.org/10.1146/annurev-pharmtox-010716-104710) (PMID 27959623) — **peer-reviewed review** | 2017 | GPCRs broadly | **Active-state-stabilizing nanobodies (e.g., Nb80, Nb39) bind the INTRACELLULAR G-protein pocket as G-protein mimetics**; also used as conformational biosensors | These are **intracellular tools**, not extracellular agonists. **Nb35 likewise stabilizes the Gs heterotrimer** (Gαs–Gβ) in GLP1R/class-B cryo-EM (6B3J, 7KI0, 6X1A, 6XOX) — a crystallization/cryo-EM chaperone, not an agonist |
| 16 | GAlbudAb, *Cardiovasc Diabetol* 2013 (PMID 24125539); exendin-4–nanobody–HSA (PMID 37730142) — **peer-reviewed** | 2013/2023 | **GLP1R**, rodent | GLP-1 / exendin-4 **peptide fused to an anti-albumin domain antibody / nanobody** for half-life extension | The antibody/nanobody is **only a half-life module**; the **peptide is the agonist**. Do NOT mistake "antibody–GLP1 fusions" for antibody agonists |
| 17 | Patents US20160297883; US9863959 — **patent disclosures (not peer-reviewed)** | — | class B GPCRs / GPCRs | Claim **peptide-grafted antibodies** with agonist activity at class B GPCRs (lists secretin receptors); and intracellular active-state-stabilizing nanobodies | Patent claims, no public validation data; "peptide-grafted" again implies a **peptide pharmacophore** carried by an antibody |

---

## Key Question 1 — Agonist antibodies/nanobodies at GPCRs (any class): documented examples and mechanisms; any class B agonist antibody/nanobody at all?

### Takeaway
Agonist antibodies/nanobodies at GPCRs **exist and are well documented, but almost exclusively at class A** and by one of three mechanisms: (a) **ECD-mimicry/reorientation** (glycoprotein-hormone receptors only), (b) **a long CDR3 loop inserted into the orthosteric 7TM pocket** to stabilize the active state, or (c) **tethering a weak peptide agonist** (conjugate). **No standalone antibody/nanobody is a confirmed agonist of a peptide-hormone class B GPCR**; the only class B "agonists" in antibody format are **nanobody–peptide conjugates** where the peptide supplies the agonist pharmacophore.

### Cited Findings
- **TSHR (class A) — activating autoantibody M22**: TSH and the activating autoantibody M22 both push the TSHR ECD into an **upright active conformation**; M22 heavy/light chains mimic the TSH α/β subunits — [Nature 2022, PMID 35940204](https://doi.org/10.1038/s41586-022-05173-3). The web summary of the 2022 cryo-EM (PDB 7XW6) adds that M22 does **not** engage the hinge, i.e., antibody activation uses a different (non-"pull") route than TSH. This is the clearest **antibody-as-GPCR-agonist** precedent, but the ECD-reorientation switch is unique to glycoprotein-hormone receptors.
- **Apelin receptor (class A) — engineered agonist single-domain antibody JN241-9**: antagonist JN241 binds the extracellular face/ECL2 and pushes **CDR3 into the orthosteric pocket**; **adding one Tyr to CDR3 converts it to a full agonist (JN241-9)** — [Ma et al., Sci Adv 2020, 10.1126/sciadv.aax7379; PDB 6KNM](https://doi.org/10.1126/sciadv.aax7379). Immunization produced only antagonists.
- **MC4R (class A) — full-agonist nanobodies**: a panel of MC4R full-agonist nanobodies; **pN162 binds deep in the orthosteric pocket, its CDR3 occupying the α-MSH site** (active-state 3.4 Å, PDB 8QJ2) — [Nat Commun 2024, 10.1038/s41467-024-50827-7](https://doi.org/10.1038/s41467-024-50827-7).
- **β2AR / kappa-opioid / muscarinic — active-state nanobodies are INTRACELLULAR**: active-state-stabilizing nanobodies (Nb80; KOR Nb39) are **G-protein mimetics that bind the cytoplasmic pocket**, used to capture agonist-bound structures and as biosensors — [Annu Rev Pharmacol Toxicol 2017, PMID 27959623](https://doi.org/10.1146/annurev-pharmtox-010716-104710); [KOR Cell 2018, PMID 29307491](https://doi.org/10.1016/j.cell.2017.12.011). **These are not extracellular agonists** and would be inaccessible to a secreted binder in a cell assay.
- **Class B (PTHR1) — nanobody–peptide conjugate agonists**: a receptor-binding VHH tethered to a weak PTH fragment is a potent, highly selective agonist, but **"no VHHs that directly activate GPCRs have been identified"** and **the VHH alone did not activate** — [Cheloha et al., Nat Commun 2020, 10.1038/s41467-020-15884-8](https://doi.org/10.1038/s41467-020-15884-8). A 2024 follow-up makes the most biased PTHR1 agonist via "activation **in trans**" — [Nat Commun 2024, 10.1038/s41467-024-49068-5](https://doi.org/10.1038/s41467-024-49068-5).
- **Adhesion GPCR (class B2, ADGRG2) — PAM nanobody**: engineered biparatopic **Nb23-bi positively modulates** DHEA-induced ADGRG2 activation (a PAM, not a standalone agonist) — [Nat Chem Biol 2025, PMID 40374856](https://doi.org/10.1038/s41589-025-01896-2).
- **Patent** (not peer-reviewed): "peptide-grafted antibodies having agonist activity against a class B GPCR," listing secretin receptors — [US20160297883](https://patents.justia.com/patent/20160297883).

### Inferences
- The **mechanistic menu for an antibody-format agonist is narrow**: ECD reorientation (GLP1R lacks the right ECD for this), CDR3 insertion into the 7TM orthosteric pocket (demonstrated only at class A peptide receptors with accessible pockets), or peptide tethering (the peptide, not the protein, agonizes).
- **The only route proven at class B is the conjugate** — strategically this argues a GLP1R design should either (a) present a GLP-1-like N-terminal segment that can insert into the 7TM, or (b) be a tethered/CLAMP-style construct, rather than a "blind" binder.

### Gaps
- No standalone (non-conjugate) antibody/nanobody agonist of any **peptide-hormone class B** receptor was found in the literature. Whether CDR3-insertion agonism (apelin/MC4R style) can be transplanted to a class B deep, ECD-gated pocket is untested.

---

## Key Question 2 — GLP1R specifically: any antibody/nanobody/DARPin/affibody/monobody/scaffold AGONIST or PAM (vs antagonists)? Bispecific/biparatopic agonist concepts?

### Takeaway
**No standalone protein-scaffold agonist (or extracellular PAM) of GLP1R is reported.** The GLP1R "biologic agonists" in the literature are all one of: (i) **GLP-1/exendin peptides fused to antibody fragments purely for half-life** (the peptide agonizes), (ii) **nanobody-tethered GLP-1 conjugates** (peptide agonizes), or (iii) **de novo designed peptides** (EvoBind, ProteinMPNN) that mimic GLP-1. When the leading de novo design lab targeted GLP1R with protein scaffolds, they produced **binders/antagonists, not agonists**.

### Cited Findings
- **Baker/IPD de novo miniproteins**: **GLP1R (and GIPR, GCGR, CGRPR) were designed only as ANTAGONISTS** that bind the ECD to sterically block peptide binding; **GLP1R binders reached 27 nM and 5.3 nM** but **no GLP1R agonist** — [bioRxiv 2025.03.23.644666 / Nature 2026, 10.1038/s41586-026-10656-8](https://doi.org/10.1038/s41586-026-10656-8). De novo **agonists were obtained only for class A MRGPRX1**.
- **GLP1R de novo PEPTIDE agonists do exist**: EvoBind's blind sequence-only 18-mer cyclic peptide gave **EC50 32 nM at GLP1R** (dual GCGR/GLP1R) — [bioRxiv 2025.06.06.658268](https://www.biorxiv.org/content/10.1101/2025.06.06.658268); ProteinMPNN GLP-1 analogues, 52% in-vitro hit rate — [bioRxiv 2025.03.26.645438 / Adv Sci 2025](https://www.biorxiv.org/content/10.1101/2025.03.26.645438). Both operate by **GLP-1 peptide mimicry** (natural two-domain mechanism), not a novel scaffold.
- **Antibody–GLP1 fusions = half-life modules, not antibody agonists**: GLP-1 fused to an anti-albumin domain antibody (GAlbudAb) — [Cardiovasc Diabetol 2013, PMID 24125539](https://doi.org/10.1186/1475-2840-12-148); exendin-4–anti-HSA-nanobody fusion — [Protein Expr Purif 2023, PMID 37730142](https://doi.org/10.1016/j.pep.2023.106373). Agonism is entirely from the peptide.
- **Nanobody-tethered GLP-1 conjugate**: the Cheloha/CLAMP approach has been extended beyond PTHR1 to a GLP1R-specific nanobody tethered to a GLP-1 variant (per the class B review context around [Nat Commun 2020, 10.1038/s41467-020-15884-8](https://doi.org/10.1038/s41467-020-15884-8)); again the peptide carries the agonism.
- **GLP1R antagonist/blocker landscape is well populated** (ECD-binding antibodies and small-molecule/peptide antagonists), consistent with ECD binding being easy and typically non-activating. (ChEMBL target CHEMBL1784 mechanism table = 16 AGONIST entries, all peptides/small molecules, 1 ANTAGONIST.)

### Inferences
- **The binding→activation gap is the whole game for GLP1R.** A sub-nM GLP1R binder (readily achievable, per Baker's 5.3 nM) is, by default, most likely an **antagonist or silent binder**. Activation demands a specific active-state-driving interaction.
- A **biparatopic/bispecific or CLAMP-style** construct (nanobody for affinity/anchoring + a GLP-1-derived segment that inserts into the 7TM) is the **most evidence-grounded "biologic agonist" concept** for GLP1R — but it leans on a peptide pharmacophore and would need to respect the challenge's format/novelty rules.

### Gaps
- I could not locate a primary paper (vs review mention) with Gs/cAMP numbers for the specific **GLP1R nanobody–GLP-1 conjugate**; its potency/bias are a gap.
- No DARPin/affibody/monobody GLP1R agonist found at all (absence, not disproof).

---

## Key Question 3 — Nanobodies in GLP1R/class-B structures: G-protein-side vs extracellular agonists

### Takeaway
The famous class-B structural nanobody **Nb35 is intracellular** — it staples the Gαs–Gβ interface to stabilize the receptor–Gs complex for cryo-EM; it is **not an agonist and never contacts the extracellular/orthosteric surface**. The same is true of active-state nanobodies like Nb80/Nb39 (G-protein-pocket mimetics). **Extracellular active-state-stabilizing agonist nanobodies exist only for class A** (apelin JN241-9; MC4R pN162), via CDR3 insertion into the orthosteric pocket.

### Cited Findings
- **Active-state nanobodies bind the cytoplasmic G-protein pocket** as G-protein mimetics (Nb80 etc.); used to trap agonist-bound states and as biosensors — [Annu Rev Pharmacol Toxicol 2017, PMID 27959623](https://doi.org/10.1146/annurev-pharmtox-010716-104710). KOR active state stabilized by intracellular Nb39 — [Cell 2018, PMID 29307491](https://doi.org/10.1016/j.cell.2017.12.011); Nb6/Nb39 as state biosensors — [Nat Commun 2020, PMID 32123179](https://doi.org/10.1038/s41467-020-14889-7).
- **Nb35** is the standard Gs-complex-stabilizing nanobody used across GLP1R/class-B cryo-EM (ChEMBL lists GLP1R–Gs structures 6B3J, 7KI0, 6X1A, 6XOX that rely on it); it binds the **G-protein heterotrimer on the intracellular side**, so it cannot be an extracellular design target or an agonist.
- **Extracellular agonist nanobodies (class A only)**: apelin JN241-9 CDR3 into the orthosteric pocket — [Sci Adv 2020](https://doi.org/10.1126/sciadv.aax7379); MC4R pN162 CDR3 into the α-MSH site — [Nat Commun 2024](https://doi.org/10.1038/s41467-024-50827-7).

### Inferences
- A cell-surface Gαs/cAMP assay (the challenge readout) **only sees extracellular binders**. Any intuition imported from Nb35/Nb80 "active-state nanobodies" is **misleading** — those work from the cytoplasm and are irrelevant to a secreted de novo design.
- The transplantable precedent is the **class A CDR3-insertion agonist nanobody**; the open question is whether a loop/helix can reach GLP1R's deeper, ECD-capped 7TM pocket from outside.

### Gaps
- No extracellular active-state-stabilizing agonist nanobody for **any class B peptide-hormone receptor** exists to copy.

---

## Key Question 4 — Small-molecule/peptidomimetic agonist & ago-PAM binding SITES → where could a PROTEIN agonist bind and still drive TM6?

### Takeaway
Non-peptide GLP1R agonists prove the receptor can be switched on from **within the upper/core 7TM bundle** (not from the ECD alone), and ago-PAMs prove an **intracellular TM6-cytoplasmic site** can drive TM6 outward — but **both productive agonist sites are inside the helical bundle**, which an extracellular protein can reach only with a thin inserted loop/helix. GLP1R activation hinges on the **sharp TM6 kink/outward swing** triggered by engagement deep in the bundle (classic GLP-1 N-terminus insertion).

### Cited Findings
- **Orforglipron (LY3502970, PDB 6XOX)**: binds the **upper-bundle orthosteric pocket**, contacting **ECD, ECL2, TM1/2/3/7**, anchored by oxadiazolone H-bonds to **Lys197 (TM2)** — [web summary + Sci Transl Med 2025, 10.1126/scitranslmed.adp5765](https://doi.org/10.1126/scitranslmed.adp5765).
- **Danuglipron (PF-06882961, PDB 6X1A)**: occupies the **receptor core, overlapping the GLP-1 N-terminal end**; **Trp33 of the ECD caps the pocket**; analogue PF-06883365 (PDB 7S15) confirms the W33 "lid."
- **TT-OAD2**: TM3/ECL2 contacts with a group **protruding into the extrahelical region between TM2/TM3**; biased agonist (web chemotype comparison).
- **ago-PAMs BETP and compound 2 are intracellular/covalent**: both act via **Cys347** — BETP on ICL3 — [Nat Chem Biol 2016, PMC4865917](https://pmc.ncbi.nlm.nih.gov/articles/PMC4865917/); **compound 2 bonds C347 at the cytoplasmic end of TM6 and triggers TM6 outward movement** — [PMC8213797](https://pmc.ncbi.nlm.nih.gov/articles/PMC8213797/). C347A abolishes PAM potentiation but not peptide signaling.
- **Native mechanism (background)**: class B1 activation is **two-domain** — the peptide C-terminus binds the ECD for affinity, then the **peptide N-terminus inserts into the 7TM core and drives the TM6 kink** that opens the Gs-coupling cavity (GLP1R ECD = small α/β-fold, not a glycoprotein-hormone LRR).

### Inferences
- **Productive agonism requires reaching into the bundle.** An extracellular protein that merely coats the ECD or ECL surface (as Baker's GLP1R binders do) will most likely **block** rather than activate — matching the observed GLP1R antagonist outcomes.
- The small-molecule data define the **target sub-pocket**: a de novo protein agonist most plausibly needs a **peptide-like N-terminal segment or an extended loop** that occupies the danuglipron/GLP-1-N-terminus region (core, under the Trp33 cap) to trip TM6. The orforglipron "upper-bundle" site is shallower and might be a more reachable foothold for a protein, but activation from there still engages TM1/2/3/7.
- The **intracellular ago-PAM site (C347/TM6) is off-limits** to a secreted biologic — do not design toward it.

### Gaps
- No structure or model exists of a **protein-sized** ligand occupying the GLP1R small-molecule pocket; whether an antibody loop/miniprotein helix can physically reach the core past the Trp33 cap is unquantified.

---

## Key Question 5 — VERDICT: any precedent for a de novo/engineered protein or antibody that AGONIZES a CLASS B GPCR?

### Takeaway
**No** — there is **no precedent for a standalone de novo or engineered protein/antibody/nanobody that directly agonizes a class B (secretin-family) GPCR, including GLP1R.** This is a **first-order risk** for the activation hypothesis and should be stated plainly. The nearest precedents are: **(a) class A agonist antibodies/nanobodies** (TSHR M22; apelin JN241-9; MC4R pN162), **(b) de novo class A miniprotein agonists** (Baker MRGPRX1), and **(c) class B tethered-peptide nanobody conjugates** (PTHR1 CLAMP; GLP1R GLP-1–nanobody fusion) where the **peptide**, not the protein scaffold, is the agonist.

### Cited Findings
- **Direct negative result at GLP1R**: the state-of-the-art de novo design campaign made **GLP1R binders/antagonists (5.3–27 nM), no agonist**; de novo **agonism succeeded only for class A MRGPRX1** — [Nature 2026, 10.1038/s41586-026-10656-8](https://doi.org/10.1038/s41586-026-10656-8). The authors note agonists are "**particularly difficult**… need for conformational selectivity."
- **Class B agonism only via conjugate**: "**no VHHs that directly activate GPCRs have been identified**"; PTHR1 agonism needed a tethered peptide — [Nat Commun 2020](https://doi.org/10.1038/s41467-020-15884-8).
- **Closest standalone antibody agonists are class A**: TSHR M22 — [Nature 2022](https://doi.org/10.1038/s41586-022-05173-3); apelin JN241-9 — [Sci Adv 2020](https://doi.org/10.1126/sciadv.aax7379); MC4R pN162 — [Nat Commun 2024](https://doi.org/10.1038/s41467-024-50827-7).
- **Agonist "biologics" beyond GPCRs exist** (context for feasibility of antibody-driven activation generally): agonist antibodies that **cluster/dimerize** single-pass receptors (RTKs, cytokine receptors, Frizzled/class-F surrogate Wnt agonists) are routine — but GPCR activation is a **conformational switch, not a dimerization event**, so cross-linking logic does not transfer cleanly to GLP1R.

### Inferences
- The challenge is attempting something **without direct precedent**. The evidence favors a design that **builds in a known activation mechanism** rather than hoping a binder activates: (1) a **GLP-1-mimetic N-terminal segment** presented on a stable scaffold/miniprotein (closest to EvoBind/ProteinMPNN and to the native switch), or (2) a **CLAMP/biparatopic** construct (nanobody affinity + inserted peptide pharmacophore). A "blind" de novo binder to the ECD/ECL is the **lowest-probability** path to activation.
- **For any candidate, a binder is not an agonist until a functional cAMP/CRE-SEAP readout proves it.** Expect most high-affinity GLP1R binders to be antagonists.

### Gaps
- Unknown whether class A CDR3-insertion agonism can be engineered into a class B deep pocket; no one has published trying.
- The precise Gs/cAMP potency and format of the GLP1R GLP-1–nanobody conjugate remain a documentation gap.

---

## (A) Strategic takeaways
1. **No standalone protein/antibody agonist of any class B GPCR (incl. GLP1R) is on record — treat this as the #1 risk.** The only class B "biologic agonists" are **conjugates whose tethered peptide supplies the agonism** (PTHR1 CLAMP; GLP1R GLP-1–nanobody). State this plainly to the team.
2. **Binding ≠ activation is maximal here.** The best de novo lab made **GLP1R binders down to 5.3 nM that are antagonists** ([Nature 2026](https://doi.org/10.1038/s41586-026-10656-8)); de novo **agonism worked only at a class A receptor (MRGPRX1)** with an accessible pocket. Plan assays so every candidate is functionally screened, not ranked by affinity.
3. **Activation requires reaching into the 7TM bundle to drive TM6.** Small-molecule agonists bind the upper/core pocket (orforglipron: ECD+ECL2+TM1/2/3/7, Lys197; danuglipron: core, under the Trp33 cap); the ago-PAM TM6/C347 site is **intracellular and unusable**. An extracellular protein must insert a loop/helix into the bundle or mimic the GLP-1 N-terminus — a flat ECD/ECL binder will most likely **block**.
4. **The two evidence-grounded agonist mechanisms to pursue** are: (i) **orthosteric-pocket CDR3/loop or helix insertion that stabilizes the active state** — proven at class A (apelin JN241-9, MC4R pN162, Baker MRGPRX1), unproven at class B; and (ii) **present a GLP-1-derived N-terminal pharmacophore on a scaffold** (CLAMP/biparatopic or a miniprotein carrying a GLP-1-like helix), the highest-probability route but peptide-dependent (watch novelty rules).
5. **Ignore intracellular "active-state" nanobodies (Nb35, Nb80, Nb39).** They are G-protein-side cryo-EM/biosensor tools, invisible to a cell-surface cAMP assay and irrelevant as a design template.
6. **De novo GLP1R agonism is achievable in PEPTIDE format** (EvoBind 32 nM, ProteinMPNN analogues) — if the challenge's 10–250 aa "protein" format permits a GLP-1-mimetic peptide/mini-protein, that is the de-risked backbone; pure antibody/nanobody/Fab formats carry the unprecedented-mechanism risk.

## (B) Gaps
- No primary Gs/cAMP data located for the **GLP1R GLP-1–nanobody conjugate** (only review-level mention).
- Whether **class A CDR3-insertion agonism transfers to class B's deep, ECD-gated pocket** is untested anywhere.
- No structural/model evidence that a **protein-sized** ligand can physically occupy the GLP1R core pocket past the **Trp33 cap**.
- EvoBind and the ProteinMPNN/HelixDiff GLP1R results are **preprints** (ProteinMPNN also has a peer-reviewed Adv Sci version); independent replication of potencies not verified.
- No DARPin/affibody/monobody GLP1R agonist found (absence of evidence).

## (C) Confidence
- **High** that **no standalone protein/antibody/nanobody agonist of a class B GPCR (incl. GLP1R) is published** (consistent across the SOTA de novo paper, the CLAMP papers' explicit statement, and the GLP1R antibody landscape being antagonist-dominated).
- **High** on GLP1R small-molecule/ago-PAM binding sites and the TM6 activation requirement (multiple peer-reviewed cryo-EM structures).
- **High** on the class A agonist-antibody precedents (TSHR, apelin, MC4R) and their mechanisms (peer-reviewed, with PDBs).
- **Medium** on the exact transferability conclusions (mechanistic inference, not a tested result) and on the GLP1R conjugate/EvoBind specifics (review- and preprint-level).
