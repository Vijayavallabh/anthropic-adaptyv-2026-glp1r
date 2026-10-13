# GLP1R Structure, Ligand Recognition & Activation Mechanism — Target Geometry for a De Novo AGONIST

**Scope:** Human GLP1R (UniProt **P43220**, 463 aa, class B1 GPCR). Written for the Anthropic × Adaptyv 2026 Challenge 3 / Track 3 de novo **agonist** task. The win condition is **ACTIVATION** (cell-surface GLP1R → Gαs → cAMP → CRE-SEAP), not merely binding. All residue numbers are **UniProt P43220** numbering unless a Wootten class-B index (superscript `b`, e.g. R2.60b) is given. Researched 2026-10-13; author training cutoff Jan 2026, so all facts below were re-verified with live tools (RCSB REST/GraphQL, PDBe SIFTS, PubMed, web).

> **CRITICAL framing for the team:** Binding ≠ activation. The GLP-1 system works by a **two-domain ("two-step") model**: the receptor **ECD (24–139)** captures the **C-terminal helix** of the peptide (affinity / "address"), and the peptide's **N-terminus (His7…Phe12)** then inserts into the **deep 7TM orthosteric pocket** (the "message"), triggering a TM6 kink + outward swing that opens the intracellular face for Gαs. An ECD-only binder, or an antibody/nanobody that merely occludes the peptide site, is an **antagonist**. To agonize you must deliver an N-terminal "message" element into the 7TM core.

---

## EVIDENCE REGISTER (load-bearing sources)

| # | Citation (authors / short title / venue / year) | ID | Date | Experimental system | Core finding used | Limitation |
|---|---|---|---|---|---|---|
| E1 | Zhang X et al. "Differential GLP-1R Binding and Activation by Peptide and Non-peptide Agonists." *Mol Cell* 80:485. 2020 | DOI 10.1016/j.molcel.2020.09.020 | 2020 | cryo-EM 2.1 Å, **human** GLP-1R–Gs | 6X18 (GLP-1), 6X19 (CHU-128/OWL833), 6X1A (PF-06882961); construct & numbering | Peer-reviewed. Active complex only |
| E2 | Zhang Y et al. "Cryo-EM structure of the activated GLP-1 receptor in complex with a G protein." *Nature* 546:248. 2017 | DOI 10.1038/nature22394 | 2017 | cryo-EM 4.1 Å, **rabbit** GLP-1R–Gs + **human** GLP-1 | Pocket residues; TM6 ~18 Å swing; PxxG kink; polar networks | **Receptor is rabbit (O. cuniculus)**; 4.1 Å (modest); numbering conserved vs human |
| E3 | Liang Y-L et al. "Phase-plate cryo-EM structure of a biased agonist-bound human GLP-1R-Gs complex." *Nature* 555:121. 2018 | DOI 10.1038/nature25773 | 2018 | cryo-EM 3.3 Å, **human** GLP-1R–Gs + exendin-P5 | 6B3J; human-direct active state; biased-agonist geometry | Peer-reviewed |
| E4 | Underwood CR et al. "Crystal structure of GLP-1 in complex with the ECD of GLP-1R." *J Biol Chem* 285:723. 2010 | DOI 10.1074/jbc.M109.033829 (PMC2804221) | 2009/2010 | X-ray 2.1 Å, **human** ECD + GLP-1 + mutagenesis | ECD groove residues; Phe28 anchor; Y69/Y88/L89/P90/R121/E127/E128 | ECD only (no 7TM); isolated domain |
| E5 | Runge S et al. "Crystal structure of the ligand-bound GLP-1R ECD." *J Biol Chem* 283:11340. 2008 | DOI 10.1074/jbc.M708740200 | 2008 | X-ray 2.2 Å, **human** ECD + exendin-4(9-39) (antagonist) | ECD hydrophobic groove = N-term α-helix + β-hairpin loop | Antagonist fragment; ECD only |
| E6 | Wootten D et al. "A Hydrogen-Bonded Polar Network in the Core of GLP-1R Is a Fulcrum for Biased Agonism." *Mol Pharmacol* 89:335. 2016 | DOI 10.1124/mol.115.101246 (PMC4767408) | 2015/2016 | Mutagenesis + modeling, **human** GLP-1R (cAMP/Ca/ERK) | Central polar network R190/N240/Q394/H363/E364 drives bias | Model-guided; pre-cryo-EM models |
| E7 | Adelhorst K et al. "Structure-activity studies of glucagon-like peptide-1." *J Biol Chem* 269(9):6275. 1994 | PMID 8119974 (no DOI; PII S0021-9258(17)37366-0) | 1994 | Ala-scan, **rat** GLP-1R binding + RIN-2A membrane cAMP | Pharmacophore: positions 7,10,12,13,15 direct; 28,29 conformational | **Rodent receptor**; older assay |
| E8 | Song G et al. "Human GLP-1R transmembrane domain structure in complex with allosteric modulators." *Nature* 546:312. 2017 | DOI 10.1038/nature22378 | 2017 | X-ray 2.7 Å, **human** 7TM domain + PF-06372222 (NAM); companion 5VEX = NNC0640 | Inactive-state / NAM reference (5VEW/5VEX) | 7TM only (no ECD); thermostabilized construct |
| E9 | Kawai T et al. "Structural basis for GLP-1R activation by LY3502970, an orally active nonpeptide agonist." *PNAS* 117:29959. 2020 | DOI 10.1073/pnas.2014879117 (PMID 33177239) | 2020 | cryo-EM 3.1 Å, **human** GLP-1R–Gs + LY3502970 | 6XOX = orforglipron; partial, G-protein-biased; upper-bundle site | Peer-reviewed |
| E10 | Zhao P et al. "Activation of the GLP-1 receptor by a non-peptidic agonist." *Nature* 577:432. 2020 | DOI 10.1038/s41586-019-1902-z | 2020 | cryo-EM 3.0 Å, **human** GLP-1R–Gs + TT-OAD2 | 6ORV; non-peptide activation geometry | Peer-reviewed |
| E11 | Zhang X et al. "Structure and dynamics of semaglutide- and taspoglutide-bound GLP-1R-Gs." *Cell Rep* 36:109374. 2021 | DOI 10.1016/j.celrep.2021.109374 | 2021 | cryo-EM 2.5 Å, **human** GLP-1R–Gs + semaglutide | 7KI0 = **semaglutide (peptide)** | Peer-reviewed |
| E12 | Zhang X et al. "Evolving cryo-EM structural approaches for GPCR drug discovery." *Structure* 29:963. 2021 | DOI 10.1016/j.str.2021.04.008 | 2021 | cryo-EM 2.9 Å, **human** GLP-1R–Gs + PF-06882961 | 7LCI = danuglipron | Peer-reviewed |
| E13 | Ma H et al. "Structural insights into the activation of GLP-1R by a small molecule agonist." *Cell Res* 30:1140. 2020 | DOI 10.1038/s41422-020-0384-8 | 2020 | cryo-EM 4.2 Å, GLP-1R–Gs + small-molecule full agonist | 7C2E | Low resolution (4.2 Å); ligand unnamed in PDB record |
| E14 | Wu F et al. "Full-length human GLP-1R structure without orthosteric ligands." *Nat Commun* 11:1272. 2020 | DOI 10.1038/s41467-020-14934-5 (PMC7062719) | 2020 | X-ray 3.2 Å, **human** full-length inactive (peptide-free) | Inactive full-length; closed ECD conformation | PDB ID not re-verified here |
| E15 | Hennen S et al. "Structural insight into antibody-mediated antagonism of GLP-1R." *Sci Rep* 6:26236. 2016 | DOI 10.1038/srep26236 (PMC4872540) | 2016 | X-ray + pharmacology, **human** ECD + Fab 3F52 | Anti-ECD Fab = **competitive antagonist**; small-molecule agonist NOT blocked | Confirms ECD-block ≠ agonism |
| E16 | Aksu H et al. "Insights into the structure and activation mechanism of class B1 GPCRs." *Mol Biol Rep* 51:966. 2024 | DOI 10.1007/s11033-024-09876-w | 2024 | **Review** | Two-step binding/activation model summary | Review (secondary) |
| E17 | (2024/25) "Structural basis for chemotype diversity in small molecule GLP-1R agonist drug discovery" | ResearchGate pub 396495949 | ~2024/25 | cryo-EM, 5 new small-molecule GLP-1R–Gs structures (aleniglipron, lotiglipron, cpds 73/3b/355) | Recent chemotype expansion; GLP-1R druggable by diverse small molecules | **Could not fully verify venue/peer-review status** |
| E18 | RCSB REST/GraphQL + PDBe SIFTS (6X18, 5VAI, 5VEW, 7KI0, 7LCI, 6XOX, 7C2E) | data.rcsb.org; ebi.ac.uk/pdbe | 2026-10-13 | Database records | Construct ranges, chains, organisms, numbering offset | DB metadata; author-numbering field was null in SIFTS excerpt (see Q1) |

---

## Q1 — KEY HUMAN GLP1R STRUCTURES + 6X18 chain R verification

### Takeaway
There is a deep, mostly **peer-reviewed, human-direct** structural set for the **active (agonist-bound, Gs-coupled)** state (6X18, 6B3J, and the small-molecule complexes), one human **inactive/NAM** reference (5VEW/5VEX + full-length apo 6-series), and ECD-only crystal structures. **Two IDs in the brief are mis-grouped:** **6X1A = PF-06882961/danuglipron (small molecule)**, and **7KI0 = semaglutide (peptide)** — corrections below. The classic "first active class B" structure **5VAI uses a RABBIT receptor**, so human-direct active-state evidence rests on **6X18 and 6B3J**.

### Cited findings — structure catalogue (all verified via RCSB REST/GraphQL, E18)

**Active-state, PEPTIDE agonist + Gs (agonist references):**
- **6X18** — human GLP-1R + **GLP-1(7-36)NH2** + Gs, cryo-EM **2.1 Å** (E1). The cleanest high-res human active reference.
- **6B3J** — **human** GLP-1R + **exendin-P5 (ExP5)** + Gs, cryo-EM 3.3 Å (E3). Biased agonist.
- **5VAI** — **rabbit (O. cuniculus)** GLP-1R + human GLP-1 + Gs (Gαs human, Gβ1 rat, Gγ2 bovine, Nb35 llama), cryo-EM 4.1 Å (E2). First activated class-B structure; **receptor is rabbit** — use for mechanism, not for exact human side-chain states.
- **7KI0** — human GLP-1R + **semaglutide (PEPTIDE)** + Gs, 2.5 Å (E11). *Correction: the brief listed 7KI0 under small molecules — it is a peptide complex.* Companion: taspoglutide.

**Active-state, SMALL-MOLECULE / oral agonist + Gs (how non-peptides activate):**
- **6ORV** — **TT-OAD2** (non-peptide), 3.0 Å (E10).
- **6X19** — **CHU-128 / OWL833** (non-peptide; note EMDB names OWL833), 2.1 Å (E1).
- **6X1A** — **PF-06882961 (danuglipron, Pfizer; small molecule)**, 2.5 Å (E1). *Correction: the brief listed 6X1A as a peptide complex — it is a danuglipron small-molecule complex.*
- **6XOX** — **LY3502970 = orforglipron (Chugai/Lilly oral)**, 3.1 Å (E9). OWL833/LY3502970/orforglipron are the same/closely related Chugai-origin series.
- **7LCI / 7LCJ** — **PF-06882961 (danuglipron)** –GLP-1R–Gs, 2.9 Å (E12).
- **7C2E** — small-molecule full agonist –GLP-1R–Gs, 4.2 Å (E13; ligand not named in PDB record).
- **7S15** — PF-06883365: a carboxylic-acid small molecule that **ion-pairs R380** in the pocket (later chemotypes CHU-128/LY3502970/TT-OAD2 bind without engaging R380) — from web/E17 context; verify ID directly.
- **2024/25 chemotype-diversity set** — 5 new structures incl. **aleniglipron, lotiglipron** (E17; venue not fully verified).

**Inactive / antagonist / NAM references (what "off" looks like):**
- **5VEW** — human **7TM domain** + NAM **PF-06372222**, X-ray 2.7 Å; **5VEX** = + NAM **NNC0640** (E8). Thermostabilized 7TM-only construct; NAMs bind an extrahelical/lipid-facing site at the cytoplasmic TM6 region, locking the inactive conformation.
- **Full-length peptide-free inactive** GLP-1R, X-ray 3.2 Å, with a **closed ECD** (E14).
- **Anti-ECD Fab 3F52** = competitive **antagonist** that blocks the ECD GLP-1 site; it also blocked a short peptide agonist but **not** an allosteric small-molecule agonist (E15) — direct proof that ECD occlusion ≠ agonism.

**ECD-only crystal structures (the "capture" half):**
- **3IOL** (E4, human ECD+GLP-1); **3C59/3C5T** (E5, human ECD + exendin-4(9-39)).

### 6X18 chain R — exact verification (RCSB GraphQL + PDBe SIFTS, E18)
- **Chain R = GLP-1R**, entity 6, **Homo sapiens, UniProt P43220**. (Other chains: A=Gαs[P63092], B=Gβ1, G=Gγ2, N=Nb35[llama], P=GLP-1(7-36)NH2[human].)
- **Construct span:** SIFTS maps the receptor to **UniProt residues 24–463** (i.e. the entire mature receptor after the 1–23 signal peptide, including the native C-tail to 463).
- **N-terminal tag / fusion:** the deposited entity sequence begins `MKTIIALSYIFCLVFA` (signal-like) + **FLAG (DYKDDDD…)** + **HRV-3C site (LEVLFQGP)** then the native ECD (`…ARPQGATVSLWETVQKWREYRRQ…`). **No BRIL/T4-lysozyme fusion and no engineered thermostabilizing mutations in the receptor** — the active complex is stabilized by **dominant-negative Gαs + Nb35** (the Sexton/Wootten active-cryo-EM strategy), not by receptor mutations.
- **Numbering offset:** the entity/label sequence index runs **+9 vs UniProt** because of the N-terminal FLAG+3C tag (label 33 = UniProt 24; label 472 = UniProt 463). The **deposited author numbering follows UniProt P43220** (the paper and field quote pocket residues as R299, K197, R190 — i.e. UniProt numbers); so when you open 6X18, chain-R residue N ≈ UniProt N. *(SIFTS author_residue_number fields were null in the excerpt read — this auth=UniProt statement is inference from convention + the paper's own residue usage; confidence medium-high.)*
- **Modeled (observed) residue range:** from unobserved-residue features (label numbering, −9 → UniProt): modeled **≈ UniProt 29–423**, with internal **unmodeled gaps at ~UniProt 130–135** (ECD→TM1 stalk/linker) and **~UniProt 339–343 (ICL3)**. The distal **C-tail ~424–463 is disordered/unmodeled**, as are the signal/tag and ECD residues 24–28. A few side chains (e.g. around 58–60, 74, 76, 79, 97, 103, 113–115, 122, 129) are only partially resolved.

### Inferences
- For geometry work, **use 6X18 as the primary human active-state template** (2.1 Å, GLP-1, no receptor mutations); cross-check the biased state with 6B3J (ExP5) and the small-molecule mode with 6XOX/6X19/6ORV. Treat 5VAI as rabbit.
- The **binding assay construct (residues 24–432)** corresponds to **ECD (24–139) + full 7TM**, truncating only the disordered C-tail (433–463) — i.e. it contains the entire orthosteric apparatus that 6X18 models (29–423). So a binder that engages either the ECD groove or the 7TM vestibule will register in the binding assay.

### Gaps
- Exact UniProt numbers of the TM6 **PxxG** Pro/Gly were not extracted (see Q3); 7S15 and the 2024/25 chemotype PDB IDs/venue not independently verified.

---

## Q2 — The two-domain binding site: ECD groove residues + 7TM pocket/vestibule residues

### Takeaway
**(a) ECD groove** = a hydrophobic cleft (human ECD, E4/E5) that grips GLP-1's C-terminal helix (Ala24, Ala25, **Phe28**, Ile29, Leu32, Val33). **(b) 7TM orthosteric pocket/vestibule** = a deep cavity lined by **TM1/2/3/5/6/7 + ECL1/ECL2** (E2/E3) that receives the peptide N-terminus (His7…Thr13). These two sets of residues are the literal target geometry.

### Cited findings — (a) ECD peptide-binding groove (human, Underwood 2010 = E4; Runge 2008 = E5)
- The ECD hydrophobic groove is built from **an N-terminal α-helix of the ECD plus a loop between two antiparallel β-strands** (E5).
- Groove / contact residues (E4): **Leu32** (border of the hydrophobic cavity), **Trp39**, **Asp67**, **Tyr69** (contacts peptide **Val33**), **Pro119**, **Arg121**, **Leu123**, **Glu127**, **Glu128** (Glu128 contacts a positively charged ligand residue). Conserved aromatic core **Trp72 / Trp110** is structural (fold), not groove-lining.
- **Mutagenesis (E4):** **Y69A, Y88A, L89A → no detectable expression/binding (ND)** → these ECD positions (Y69/Y88/L89) are essential for a folded, peptide-competent ECD. **P90A and R121A** significantly reduce binding for both GLP-1 and exendin-4. **L32A** and **E127A** reduce exendin-4 affinity/potency more than GLP-1 (ligand-specific). **T35A** affects exendin-4.
- **Peptide side (E4):** the hydrophobic face **Ala24/Ala25/Phe28/Ile29/Leu32/Val33** inserts into the groove; **Phe28 is the single dominant anchor — F28A causes ~1300-fold affinity loss**. Trp31 is solvent-exposed and does **not** touch the ECD. When ECD-bound, GLP-1 is a **kinked but continuous α-helix from Thr13 to Val33**; residues 7–12 are left free to reach the 7TM core.

### Cited findings — (b) 7TM orthosteric pocket + extracellular vestibule (human numbering; Zhang 2017 = E2 [rabbit receptor, conserved numbering], Wootten 2016 = E6 [human])
The GLP-1 N-terminus penetrates a pocket formed by **TM1, TM2, TM5, TM7 and ECL1/ECL2**, with ECL2 prominent (E2):
- **TM1:** **Y145** (candidate H-bond to peptide Glu9), **S155** (H-bonds backbone of L396/TM7).
- **TM2:** **R190 (R2.60b)** (candidate H-bond to peptide Glu9), **K197** (H-bonds peptide **Thr13**).
- **TM3:** **N240 (N3.43b)** — central polar network (see Q3).
- **TM6:** **H363 (H6.52b)**, **E364 (E6.53b)** — upper-pocket polar residues; E364–R190 salt-bridge is activation-linked (E6).
- **TM7:** **L388** and **S392** (van der Waals with peptide **Glu9**), **L396**, **Q394 (Q7.49b)**.
- **ECL1:** **Q211, H212** (pack against peptide Trp31), **Q213** (possible H-bond to ECD α1 Arg40).
- **ECL2:** **W297, T298, R299** — **R299 reaches peptide His7 and Thr11**; T298/W297-backbone/R299-backbone make polar contacts to peptide Ser14/Ser17/Ser18.
- **Peptide N-terminus contacts (the "message"):** **His7 ↔ R299 (ECL2)**; **Glu9 ↔ L388/S392 (TM7)** vdW and possible R190/Y145 H-bonds; **Thr13 ↔ K197 (TM2)**.
- Non-peptide agonists bind **higher in the bundle** (upper vestibule), contacting **ECD, ECL2, TM1/TM2/TM3/TM7**; LY3502970/orforglipron's pocket is "near the top of the 7TM bundle" formed by ECD + ECL2 (E9). Boc5/WB4-24 arms overlap GLP-1 residues ~A8–D15 (web, MD-supported).

### Inferences
- **Design target = two anchors:** a C-terminal "affinity" element presenting a **Phe28-like aromatic + the Val33/Ile29/Leu32 hydrophobic face** to the ECD groove (Y69/Y88/L89/P90/L32/E128), **and** an N-terminal "message" element presenting a **His7-like + Glu9-like + Thr13-like** triad to **R299(ECL2) / L388-S392(TM7) / K197(TM2) / R190(TM2)**. Hitting the ECD alone = antagonist.
- The small-molecule structures prove the 7TM **upper vestibule is independently druggable** by a non-peptide and can still trigger Gs — relevant if the single-chain design cannot reach full peptide depth.

### Gaps
- TM5-specific contact residue numbers were not individually extracted (E2 lists TM5 among pocket helices and reports K334 as a movement landmark).

---

## Q3 — Agonist vs antagonist vs NAM; the MINIMAL conformational change for Gs coupling

### Takeaway
**Agonist** = engages the deep pocket so as to drive a **sharp TM6 kink at the conserved PxxG motif** and swing the **cytoplasmic half of TM6 outward ~18 Å**, opening the intracellular cavity for the **Gαs α5 helix**. **Antagonist** = occupies the ECD/orthosteric site without driving that TM6 motion (e.g. exendin-4(9-39), Fab 3F52). **NAM** = binds an **extrahelical/lipid-facing site at the cytoplasmic TM6/TM7 end** and **locks TM6 against moving** (PF-06372222, NNC0640). The minimal requirement for cAMP is therefore **not occupancy but the TM6-opening transition**.

### Cited findings
- **TM6 outward movement ~18 Å** at the cytoplasmic end (Cα of **K346 = 6.35b**); **TM5 moves ~7 Å** (K334), upon activation (E2). This is the hallmark class-B activation motion.
- **TM6 kink** occurs mid-helix at the conserved class-B **PxxG motif — Pro6.47b-x-x-Gly6.50b** (E2); the Gly provides the flexible hinge. *(Exact UniProt numbers of this Pro/Gly not extracted here; anchored near H363=6.52b / E364=6.53b — verify in 6X18.)*
- **Central polar network (ligand-proximal core):** **R190 (2.60b), N240 (3.43b), Q394 (7.49b), H363 (6.52b), E364 (6.53b)** form a H-bonded/charge network that is a **"fulcrum" for activation and biased agonism** (E6, human mutagenesis). The **E364–R190** polar link is important for GLP-1/exendin-4-driven **cAMP and ERK**; **Q394** is critical for **Ca2+** for all peptides; N240/Q394 mutations have **ligand-specific** effects (E6).
- **Intracellular "HETX"/polar network at the G-protein face:** **H2.50b, E3.50b, T6.42b, Y7.57b** — this network is **disrupted/reorganized by TM6 outward movement** to permit Gs coupling (E2). An inactive **H180(2.50b)–E247(3.50b)** contact present in the inactive receptor is broken in the active state (MD/accelerated-MD support; lower confidence).
- **TM2–6–7–H8 network:** **R176 (TM2), N406, E408 (TM7–H8)** rearrange on activation to engage the **Gαs α5 helix** C-terminus (E2).
- **ECL2 is the critical transducer:** W297/T298/R299 both bind the peptide N-terminus and couple that binding to the core (E2); ECL2 integrity is required for efficient signalling.
- **NAM mechanism:** PF-06372222 / NNC0640 bind an extrahelical pocket at the cytoplasmic TM6 region and **stabilize the inactive 7TM**, i.e. they prevent the TM6 swing (E8). The peptide-free full-length receptor shows a **closed ECD** inactive resting state (E14).

### Inferences
- The **single most important design criterion for the activation assay**: the molecule must do work on **TM6/ECL2**, not just fill the pocket. Practically, a design should place a group that (i) contacts **R299/ECL2 and the TM6/TM7 upper pocket (H363/E364/L388/S392)** and (ii) is shaped to permit (not block) the TM6 kink. Any element that reaches the **cytoplasmic TM6 end** risks acting as a NAM-like clamp.
- Because the inactive resting ECD is **closed**, a de novo agonist may also need to **shift the ECD open** (or bypass it via a vestibule-binding mode like the small molecules).

### Gaps
- No single human structure gives a clean side-by-side inactive↔active snapshot of the *same* full-length construct with the PxxG residues numbered; the kink residues' UniProt numbers should be read directly off 6X18/5VEW.

---

## Q4 — Biased agonism (Gαs/cAMP vs β-arrestin) and what favours Gs

### Takeaway
Because the competition reads **cAMP/Gs**, the design should be **Gs/cAMP-biased (or at least Gs-efficacious)**. Structurally, **Gs bias correlates with (i) binding high in the bundle, (ii) NOT engaging ECL3, and (iii) a more open extracellular cavity** — exactly the signature of the oral small molecules. Peptide features in **ECL3/TM6/TM7/TM1** tune the arrestin/Gs balance.

### Cited findings
- The **central polar network (R190/N240/Q394/H363/E364) is a fulcrum for biased agonism** (E6): different peptides (GLP-1 vs exendin-4 vs oxyntomodulin) use these residues differently to bias cAMP vs Ca2+ vs ERK; **E364–R190** is specifically tied to **cAMP/ERK**.
- The **biased agonist exendin-P5 (6B3J)** shows distinct backbone conformations in **ECL3, TM6, TM7, TM1** relative to GLP-1 (E3; web figure legend) — i.e. the extracellular/upper-TM region sets the bias.
- **Small-molecule agonists CHU-128, OWL833/LY3502970, TT-OAD2 are strongly Gs/cAMP-biased** (low β-arrestin recruitment, internalization, pERK, Ca2+). In their Gs complexes they **fail to contact ECL3**, producing a **large outward shift of ECL3 and a more open binding cavity** (web review of E1/E9/E10). **Orforglipron/LY3502970 = partial agonist, G-protein-biased, essentially no β-arrestin recruitment** (E9) — an ideal template for "activate cAMP, don't recruit arrestin."
- MD: exendin-4- and oxyntomodulin-bound receptors (more arrestin-biased) are **more dynamic in the ECL3/TM6/TM7 region** than GLP-1-bound (web/PMC8748714).

### Inferences
- **Favour Gs/cAMP** by targeting the **upper vestibule (ECD/ECL2/TM1-2-3-7)** and **avoiding stable ECL3 engagement** and avoiding deep arrestin-promoting TM6/TM7 contacts. A **partial agonist that still triggers the TM6 kink** (orforglipron-like) is sufficient to win a cAMP readout and tends to be cleaner on bias.
- A molecule that drives strong receptor internalization/arrestin could paradoxically *reduce* steady-state surface cAMP signal — another reason to bias Gs.

### Gaps
- There is **no high-resolution human GLP-1R–β-arrestin complex** resolving the exact arrestin-biasing contacts; the "what drives arrestin" picture is still partly inferential (E3 + MD). Structural basis of the Gs/arrestin switch remains incompletely defined (stated explicitly in the literature).

---

## Q5 — Minimal GLP-1 agonist pharmacophore: which residues are indispensable for ACTIVATION vs affinity

### Takeaway
The **N-terminal octapeptide His7-Ala8-Glu9-Gly10-Thr11-Phe12-Thr13-Ser14…** is the **activation "message"**; **His7, Gly10, Asp15 (and Phe28 via conformation)** are most critical for **cAMP/activation**, while **Phe28/Val33/Ile29** dominate **ECD affinity**. On the receptor side, ECD residues **Y69, Y88, L89, P90, R121, E127/E128** are the groove/affinity determinants (Q2); the activation "message" is read by **R299(ECL2), K197/R190(TM2), L388/S392(TM7)**.

### Cited findings — peptide side
- **Adelhorst 1994 (E7; rat receptor, rodent caveat):** full Ala-scan → side chains at **positions 7 (His7), 10 (Gly10), 12 (Phe12), 13 (Thr13), 15 (Asp15)** are **directly involved in receptor interaction**; **positions 28 (Phe28) and 29 (Ile29)** are important for GLP-1 to **adopt the receptor-recognized conformation** (i.e. conformational/affinity, not direct contact).
- Secondary reviews summarising Adelhorst: **His7, Gly10, Asp15 (and Phe28)** are the residues whose Ala substitution most strongly **reduces cAMP (activation)**; **Phe12, Thr13** contribute more to **binding** than to activation (web; verify against E7 fold-changes).
- **His7 is the lynchpin of activation:** it sits at the very bottom of the inserted N-terminus and H-bonds **R299 (ECL2)** (E2). Removing/extending the N-terminus (e.g. GLP-1(9-36), exendin(9-39)) converts agonist→antagonist — consistent with His7-Ala8 being the activation trigger. **DPP-4 cleaves GLP-1 at His7-Ala8**, abolishing activity, underscoring that the first two residues are the message (well-established; not re-cited here).
- **Glu9** makes the TM7 (L388/S392) and TM2 (R190) contacts that read into the core (E2).

### Cited findings — receptor ECD side (human, E4)
- **Y69** contacts peptide **Val33**; **Y88A/L89A → no detectable binding/expression** (groove/fold-critical); **P90A, R121A** reduce binding for both ligands; **E127/E128** line the groove (E128 contacts a basic ligand residue, E127 is exendin-4-selective). These are exactly the brief's Y69/Y88/L89/P90/R121/E128 — **confirmed as ECD groove/affinity determinants** from the human ECD+GLP-1 crystal structure.

### Inferences
- **Minimal functional pharmacophore to reproduce:** (1) a **His-like group at the "position-7" depth** H-bonding **R299**; (2) an **acidic group at "position-9" depth** toward **R190/TM7**; (3) a **Gly-like flexibility at position-10** (turn); (4) a **Phe/aromatic "address" (Phe28-equivalent)** packing the **ECD groove (Y69/Y88/L89/P90/L32)**; (5) a hydrophobic C-terminal helix face (Ile29/Leu32/Val33). A single-chain protein that presents all five, spaced like GLP-1's two domains, is the most mechanism-faithful agonist design.
- Alternatively, **mimic the oral small molecules** (orforglipron/danuglipron/TT-OAD2): a rigid upper-vestibule binder that triggers partial Gs activation without needing the full peptide N-terminus — a lower-risk path to a cAMP-positive hit if full-depth insertion is hard to design.

### Gaps
- Adelhorst's quantitative fold-changes are rat-receptor; **exact human cAMP EC50 shifts per Ala mutant** were not retrieved (would strengthen the activation-vs-affinity split). Human-specific N-terminal mutagenesis (e.g. His7/Asp9/Gly10 in human GLP1R cAMP assays) exists in later Wootten/Sexton work but was not individually fetched.

---

## (A) HIGHEST-IMPACT STRATEGIC TAKEAWAYS

1. **Design for the transition, not the pocket. Binding ≠ activation.** The win condition (cAMP/Gs) requires driving the **TM6 sharp kink (PxxG hinge) + ~18 Å outward swing of the cytoplasmic TM6 end** (E2). The deliverable must engage the **deep 7TM "message" site (R299/ECL2, R190-K197/TM2, L388-S392-Q394/TM7, H363-E364/TM6)** — a molecule that only grips the **ECD groove (Y69/Y88/L89/P90/R121/E128)** will be an **antagonist** (proven by exendin(9-39) and Fab 3F52, E15).

2. **Copy GLP-1's two-domain architecture in a single chain.** Present a **Phe28-anchored hydrophobic C-terminal helix** to the ECD groove **and** a **His7/Glu9/Gly10/Thr13 N-terminal "message"** to the 7TM core (E2/E4/E7). **His7↔R299 and the Phe28 anchor (F28A = 1300-fold)** are the two non-negotiable contacts. The format options (10–250 aa single chain, nanobody/scFv/Fab) favour a **single-chain mini-protein presenting a GLP-1-like N-terminal warhead on a stable scaffold** over a conventional antibody paratope (which naturally occludes rather than inserts).

3. **Bias Gs/cAMP and avoid β-arrestin traps.** The oral small molecules (**orforglipron/LY3502970 = 6XOX; danuglipron = 6X1A/7LCI; TT-OAD2 = 6ORV; CHU-128/OWL833 = 6X19**) are **partial, G-protein/cAMP-biased** agonists that bind **high in the bundle and do not engage ECL3**, giving an open cavity and low arrestin/internalization (E9, web). **Target the upper vestibule (ECD/ECL2/TM1-2-3-7), avoid stable ECL3 and deep cytoplasmic-TM6 contacts.** A clean **partial agonist that still kinks TM6 is sufficient** to win a cAMP readout.

4. **Use the right templates.** Primary human active-state geometry = **6X18 (2.1 Å, GLP-1)** and **6B3J (ExP5)**; small-molecule activation modes = **6XOX/6X19/6ORV**; inactive/NAM "do-not-do" geometry = **5VEW/5VEX** + apo full-length (E14). **5VAI is rabbit** — mechanism only. In 6X18 the receptor is essentially **wild-type (FLAG+3C tag, no BRIL/T4L, no thermostabilizing mutations)**, modeled **UniProt ~29–423** (gaps at 130–135 and ICL3 339–343), author numbering = UniProt.

5. **The binding assay is permissive; the activation assay is the filter.** The Sino 13944-H18H-DD binder (**24–432 = ECD + full 7TM**, DDM/CHS) will register **any** ECD- or vestibule-binder, including antagonists. Do not over-optimize to the binding assay. The **undisclosed thermostabilizing mutations are in this binding construct, not in 6X18** — avoid designs whose affinity hinges on a single fragile 7TM contact that a stabilizing mutation might perturb.

6. **Exploit the receptor's "message-reader" residues as positive-design constraints and hotspots:** ECL2 **R299** (reads His7/Thr11), TM2 **R190/K197**, TM7 **L388/S392/Q394**, TM6 **H363/E364**, TM1 **Y145**; ECD groove **Y69/Y88/L89/P90/L32/R121/E128**. These are the exact atoms the design pipeline should be scored against.

## (B) OPEN QUESTIONS / EVIDENCE GAPS

- **Exact UniProt numbers of the TM6 PxxG Pro/Gly** (6.47b/6.50b) and of the HETX intracellular network (2.50b/3.50b/6.42b/7.57b) were not extracted — read directly off 6X18/5VEW before using as design constraints.
- **Can a de novo single-chain protein actually reach full peptide-insertion depth,** or is a partial, vestibule-binding (small-molecule-like) mode the only realistic agonist geometry for a designed protein? No precedent structure of a *designed* GLP-1R agonist protein was found.
- **Structural basis of the Gs-vs-arrestin switch is still incompletely defined** (no high-res human GLP-1R–β-arrestin complex); "ECL3-avoidance → Gs bias" is well-supported but partly inferential.
- **Human quantitative N-terminal pharmacophore** (per-residue cAMP EC50 shifts in human GLP1R) not fully retrieved; Adelhorst is rat (E7).
- **2024/25 chemotype-diversity structures (aleniglipron/lotiglipron, E17)** and **7S15/R380** details are from secondary sources — verify PDB IDs/venue directly if used.
- **5VAI pocket residue numbers** are from a rabbit receptor; confirm each side chain against the human 6X18/6B3J maps before treating as exact human geometry (the field treats them as conserved, and Wootten 2016's human mutagenesis corroborates R190/N240/Q394/H363/E364).

## (C) CONFIDENCE ON LOAD-BEARING CLAIMS

- **HIGH — Two-domain mechanism; binding≠activation; ECD-block = antagonist.** Multiple independent human-direct structures + pharmacology (E1–E5, E14, E15, E16).
- **HIGH — TM6 outward swing (~18 Å) + PxxG kink is the activation hallmark; ECL2 critical.** E2 (cross-class-B consensus); magnitude/landmark (K346) from rabbit 5VAI but conserved.
- **HIGH — 6X18 identity, resolution, human receptor, WT-like construct (no BRIL/T4L), and PDB-ID corrections (6X1A=danuglipron; 7KI0=semaglutide; 5VAI=rabbit).** Verified via RCSB GraphQL/REST (E18).
- **HIGH — ECD groove residues Y69/Y88/L89/P90/R121/E127/E128 and Phe28 anchor (F28A 1300-fold).** Human ECD+GLP-1 crystal + mutagenesis (E4).
- **HIGH — Central polar network R190/N240/Q394/H363/E364 as activation/bias fulcrum.** Human mutagenesis (E6).
- **MEDIUM-HIGH — 7TM pocket contact residues (Y145/S155, R190/K197, L388/S392/L396/Q394, Q211-213, W297/T298/R299) and specific peptide contacts (His7↔R299, Glu9↔TM7, Thr13↔K197).** From E2 (rabbit receptor; numbering conserved and human-corroborated by E6) and the human E3.
- **MEDIUM-HIGH — 6X18 modeled range (UniProt ~29–423, gaps 130–135 & 339–343) and auth=UniProt numbering.** Derived from RCSB unobserved-residue features + SIFTS; auth-numbering equality is inference (SIFTS author field null in excerpt).
- **MEDIUM — Gs-bias rules (upper-bundle binding, ECL3 avoidance → low arrestin).** Strong structural trend across small-molecule complexes (E9, E1, web reviews) but no arrestin complex to confirm the converse.
- **MEDIUM — Activation-critical N-terminal residues (His7/Gly10/Asp15) vs affinity (Phe28/Phe12/Thr13).** Core claim solid (E7) but quantitative split is rat-receptor + review-synthesized.
- **LOW-MEDIUM — 2024/25 chemotype structures, 7S15/R380, exact HETX/PxxG UniProt numbers.** Secondary/unverified or not directly extracted.
