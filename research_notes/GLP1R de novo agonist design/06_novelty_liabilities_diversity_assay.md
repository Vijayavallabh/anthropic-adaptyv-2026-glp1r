# Novelty, Sequence Liabilities, Portfolio Diversity, Functional-Assay Interpretation, and Compliance — GLP1R Challenge-3

Scope: the novelty bar, compliance checklist, liability filters, diversity criteria, and how a functional hit is judged for the Anthropic × Adaptyv 2026 **Challenge 3 / Track 3 (open)** de novo GLP1R agonist submission (ranked CSV `name,sequence,molecule_class`). Research cutoff "today" = 2026-10-13; live pages fetched this session.

## Evidence register (tiers)

- **Tier 1 — authoritative / live organizer pages (fetched 2026-10-13):**
  - GLP1R Challenge-3 page — https://proteinbase.com/competitions/anthropic-adaptyv-2026/challenges/glp1r
  - Competition landing page — https://proteinbase.com/competitions/anthropic-adaptyv-2026
  - Official competition terms — https://proteinbase.com/competitions/anthropic-adaptyv-2026/terms
  - Adaptyv/Proteinbase novelty definition — https://www.adaptyvbio.com/blog/novelty
- **Tier 2 — peer-reviewed / primary method literature:** TAP (PNAS 2019), ANARCI (Bioinformatics 2016), CamSol (JMB 2015), SAP (Chennamsetty PNAS 2009 via secondary), deamidation/isomerization clinical-antibody study (mAbs 2019), GLP1R assay papers.
- **Tier 3 — third-party summaries, preprints, vendor docs, search-synthesis, and my own inference** (labeled inline; treat as weaker).
- Items the organizer has **not** published a number for are stated as **"unspecified"** — never invent a threshold.

---

## Q1. ADAPTYV / PROTEINBASE NOVELTY DEFINITION (and eligibility vs scientific-novelty distinction)

### Takeaway
Proteinbase scores novelty on a **1–4 scale** (not literally "4/4 vs 3/4" — that shorthand means "scores 4 on a 4-point scale"), combining a **sequence** axis (MMseqs2, ~30% identity ≈ same fold, ~70% ≈ same protein) and a **structural** axis (ESMFold2-Fast → domain segmentation → Foldseek → TM-align; TM ≥0.8 over ≥70% coverage = high, TM ≥0.5 = moderate). **Level 4 (de novo) requires sequence ≤30% AND less-than-moderate structural similarity.** This scientific score is used by Proteinbase to annotate/triage and feeds the Claude selection prompt; it is SEPARATE from the hard **eligibility** rule ("de novo, zero-shot, not modified from an existing binder").

### Cited Findings
- **Sequence-novelty tool/DBs:** MMseqs2 searches **SwissProt, PDB, patent sequences, the therapeutic-antibody database, and PLAbDab**; the best identity hit is used. ~30% identity is the rule of thumb for "roughly the same fold"; ~70% suggests "same protein from a different organism." Viral proteins can share active-site residues at very low overall identity. — [Adaptyv novelty blog](https://www.adaptyvbio.com/blog/novelty)
- **Structural-novelty pipeline:** structure predicted with **ESMFold2-Fast** (ESMFold was the old default); domains segmented by a **consensus of 3 domain predictors** (drawing on The Encyclopedia of Domains / TED); structure search by **Foldseek then TM-align**. — [Adaptyv novelty blog](https://www.adaptyvbio.com/blog/novelty)
- **Structural thresholds (TM weighted by coverage):** **High** = ≥70% of sequence covered by domains matching a known structure at **TM ≥0.8**; **Moderate** = >70% covered at **TM ≥0.5**. — [Adaptyv novelty blog](https://www.adaptyvbio.com/blog/novelty)
- **General 1–4 novelty scale:** 1 Essentially known (seq >0.70 AND ≥moderate structural); 2 Familiar (seq >70% alone, OR high structural, OR seq >30% + moderate structural); 3 Partly novel (seq >30% OR moderate structural, but only one); **4 De novo (seq ≤30% AND less-than-moderate structural — "measurably doesn't resemble anything we can find").** — [Adaptyv novelty blog](https://www.adaptyvbio.com/blog/novelty)
- **Separate antibody novelty scale** (applies to nanobody/VHH/VNAR/scFv/Fab): variable domains IMGT-numbered; **CDRH3 compared against PLAbDab by edit-distance identity**. CDRH3 <70% = de novo; ≥95% = essentially unchanged. Levels: 1 Known (CDRH3 ≥95%, or CDRH3 ≥70% + global ≥95%); 2 Known CDRs/engineered (CDRH3 70–95%, global <95%); 3 Novel CDRs/familiar framework (CDRH3 <70%, global ≥70%); **4 Fully de novo (CDRH3 <70% AND global <70%)**. — [Adaptyv novelty blog](https://www.adaptyvbio.com/blog/novelty)
- **Eligibility rule (hard filter, distinct from the score):** all designs must be **de novo, zero-shot**, and **may not be modified from an existing binder**; this is a pass/fail filter applied before selection. — [GLP1R Challenge-3 page](https://proteinbase.com/competitions/anthropic-adaptyv-2026/challenges/glp1r)
- **How the scientific score is used:** the novelty blog says Proteinbase uses these scores to **annotate and triage** proteins; it does NOT state a minimum level for eligibility. For Tracks 2/3 the pooled **Claude-based selection prompt "considers predicted quality, novelty, and method novelty"** and "will not rely on a single in silico metric." — [Adaptyv novelty blog](https://www.adaptyvbio.com/blog/novelty); [GLP1R Challenge-3 page](https://proteinbase.com/competitions/anthropic-adaptyv-2026/challenges/glp1r); [competition page](https://proteinbase.com/competitions/anthropic-adaptyv-2026)

### Inferences
- **"4/4 vs 3/4" = scoring 4 vs 3 on this 1–4 scale.** Maximum novelty credit requires hitting de novo on BOTH axes (level 4). A design with a novel sequence but a fold that Foldseek/TM-align matches to a known structure at TM ≥0.5 is capped at **level 3** — this is why de novo helical bundles (which structurally resemble natural helical bundles) typically cap at 3 even with ≤30% sequence identity (consistent with project memory `reference-adaptyv-novelty-metric.md`: "helical bundles cap at 3/4 (structural)").
- **Two distinct "novelty" concepts must not be conflated:** (a) the eligibility filter (de novo/zero-shot/not-a-modified-binder) is binary and mandatory; (b) the 1–4 scientific score is a ranking/triage signal that rewards reaching level 4. A design can be fully eligible (de novo) yet score only 3 (structural resemblance).
- For a **de novo single-chain GLP1R agonist** (molecule_class `protein`), the novelty axis that bites is **structural**: to reach level 4 you need a fold whose domains do NOT hit a known PDB/AFDB structure at TM ≥0.5 over ≥70% coverage. Method novelty (the generative pipeline) is scored separately by the Claude prompt and is worth cultivating independently.

### Gaps
- The blog does **not** state DB **versions/snapshot dates** (SwissProt/PDB/PLAbDab release, Foldseek/TM-align/ESMFold2-Fast versions) — unspecified. AFDB and UniProt (beyond SwissProt) are **not** named as sources; cannot confirm AFDB is searched (contradicts the looser project-memory note that assumed AFDB; the live page names SwissProt+PDB+patents+therapeutic-antibody DB+PLAbDab only).
- The blog does not give the exact MMseqs2 parameters (coverage/e-value) or how "less-than-moderate" structural is computed when no domain matches at all.
- No published mapping from novelty level → selection probability or score weight (the weighting is inside the unpublished Claude prompt).

---

## Q2. COMPLIANCE — Challenge-3 submission rules (verified against the live page + terms)

### Takeaway
Confirmed against the live GLP1R page: **CSV `name,sequence,molecule_class`, ranked; up to 20 designs (Track 3); single-chain 10–250 aa; molecule_class ∈ {protein, nanobody, scfv, fab_kappa, fab_lambda}** (the Challenge-3 brief vocabulary is AUTHORITATIVE — the old `single_chain` vocabulary is superseded); **Fab = `{VH}:{VL}` colon-separated; names unique; designs unique**; hard filter = de novo/zero-shot. All submissions and **design names are published as submitted** under **ODC-BY**, and every synthesized design is **biosecurity-screened**.

### Cited Findings
- **Target:** human GLP1R, **UniProt P43220-1, residues 24–432 (409 aa)**, supplied in DDM/CHS detergent; recommended epitope = **peptide-binding groove of the extracellular domain**. Goal: a binder that **also activates** — "A design must be an agonist, confirmed in a functional assay, to count." — [GLP1R Challenge-3 page](https://proteinbase.com/competitions/anthropic-adaptyv-2026/challenges/glp1r)
- **Submission format:** CSV ordered by your ranking preference, with at minimum `name`, `sequence`, `molecule_class`. — [GLP1R Challenge-3 page](https://proteinbase.com/competitions/anthropic-adaptyv-2026/challenges/glp1r)
- **molecule_class vocabulary (AUTHORITATIVE, current):** `protein`, `nanobody`, `scfv`, `fab_kappa`, `fab_lambda`. Accepted design types = "Single chain protein, nanobody, scFv, or Fab." — [GLP1R Challenge-3 page](https://proteinbase.com/competitions/anthropic-adaptyv-2026/challenges/glp1r)
- **Maximum designs:** up to **40 for Track 1**, up to **20 for Tracks 2 and 3** (FAQ: Track 1 "at least 20 and at most 40"). The brief's "20" is confirmed for Track 3. — [GLP1R Challenge-3 page](https://proteinbase.com/competitions/anthropic-adaptyv-2026/challenges/glp1r)
- **Single-chain length:** **10–250 amino acids.** Categorization bands (not limits): microbinder <40, **minibinder 40–100 inclusive**, large binder >100. — [GLP1R Challenge-3 page](https://proteinbase.com/competitions/anthropic-adaptyv-2026/challenges/glp1r)
- **Antibody rules:** a design counts as nanobody/antibody if annotated as such **by a tool like ANARCI**; **no antibody length limits are stated**; common framework regions recommended as a starting point; scFvs may be reformatted to a preferred linker. — [GLP1R Challenge-3 page](https://proteinbase.com/competitions/anthropic-adaptyv-2026/challenges/glp1r)
- **Fab encoding:** a single sequence with VH and VL **separated by a colon (`{VH}:{VL}`)**, molecule_class `fab_kappa` or `fab_lambda` (heavy first). — [GLP1R Challenge-3 page](https://proteinbase.com/competitions/anthropic-adaptyv-2026/challenges/glp1r)
- **Names / uniqueness:** `name` must be a **unique identifier**; each **design must be unique** (same design not submitted twice). **"Design names are published as submitted"** → avoid identifying/personal information in names (Terms §8.3). — [GLP1R Challenge-3 page](https://proteinbase.com/competitions/anthropic-adaptyv-2026/challenges/glp1r); [Terms](https://proteinbase.com/competitions/anthropic-adaptyv-2026/terms)
- **Hard filters (all designs):** length band, nanobody/antibody annotation criteria, uniqueness, and **de novo + zero-shot** (not modified from an existing binder). — [GLP1R Challenge-3 page](https://proteinbase.com/competitions/anthropic-adaptyv-2026/challenges/glp1r)
- **Selection (Tracks 2/3):** all designs pooled and assessed by a **Claude-based selection prompt** (predicted quality + novelty + method novelty); **~375 designs/problem per track**; ~1,500 designs screened per problem (50% T1, 25% T2, 25% T3). Track 2/3 testing is at Sponsors' discretion, no guaranteed allocation, up to one **384-well plate (incl. controls)** per problem. — [GLP1R Challenge-3 page](https://proteinbase.com/competitions/anthropic-adaptyv-2026/challenges/glp1r); [Terms §5.4](https://proteinbase.com/competitions/anthropic-adaptyv-2026/terms)
- **Ranking objectives:** (1) affinity vs human GLP1R; (2) confirmed activation in the functional assay — **binders that do not activate the receptor do not count**. **No numeric affinity threshold is published.** — [GLP1R Challenge-3 page](https://proteinbase.com/competitions/anthropic-adaptyv-2026/challenges/glp1r)
- **Deadline:** **Sunday 2026-10-25, 23:59 AoE (UTC−12)**; window Oct 12–25 (challenge is "Open"). — [GLP1R Challenge-3 page](https://proteinbase.com/competitions/anthropic-adaptyv-2026/challenges/glp1r); [competition page](https://proteinbase.com/competitions/anthropic-adaptyv-2026)
- **Licensing/publication:** Proteinbase data under **Open Data Commons Attribution License (ODC-BY)** (Terms §6). Submitting consents to publishing the design, data, and results as "Published Materials" under ODC-BY; **negative results are published too**; sequences, predicted structures, design methods, and measurements for tested designs are published openly. Participants **retain ownership**; grant a non-exclusive, worldwide, royalty-free, perpetual license; publication may affect patentability (file before submitting). — [Terms §6](https://proteinbase.com/competitions/anthropic-adaptyv-2026/terms)
- **Biosecurity / compliance:** every design submitted for wet-lab synthesis is **screened for biosecurity risk**; Sponsors may reject any concerning submission (Terms §5.5). Participants must hold rights/consents and comply with applicable law and Anthropic's Usage Policy. — [Terms §5.5, §3.3](https://proteinbase.com/competitions/anthropic-adaptyv-2026/terms)
- **Eligibility:** 18+ (or local majority age); **excluded**: residents/entities of Belarus, China, Cuba, Iran, Myanmar, North Korea, Russia, Sudan, Syria, Crimea, DNR/LNR, and sanctioned persons (Terms §3.1). Track 3 (open) needs no affiliation; Claude use optional, no credits. — [Terms §3.1](https://proteinbase.com/competitions/anthropic-adaptyv-2026/terms); [competition page](https://proteinbase.com/competitions/anthropic-adaptyv-2026)

### Inferences
- **The `molecule_class` ambiguity is resolved:** the live Challenge-3 page explicitly lists `{protein, nanobody, scfv, fab_kappa, fab_lambda}`. The older `{single_chain, ...}` vocabulary from a prior example CSV is **superseded** — do not use `single_chain`. A de novo single-chain binder is `protein`.
- **A de novo single-chain `protein` agonist should sit in the minibinder band (40–100 aa)** to be a conventional design, but anything 10–250 aa is legal. The agonist mechanism (must occupy/activate the peptide-binding groove of the ECD + 7TM) argues for a peptide-mimetic or small scaffold rather than a large domain.
- **Name hygiene matters** because names are published verbatim: use neutral codenames (no email, real name, institution, or anything identifying). My caller's email (vallabh2006@...) and personal identity must NOT appear in any `name`.
- With ~375 Track-3 designs selected per problem and a shared 384-well plate, **the 20 slots are a ranking exercise**: put the strongest-quality + most-novel (design and method) designs at the top of the CSV.

### Gaps
- **No numeric affinity threshold** and **no numeric agonism threshold** are published ("unspecified") — organizer judges functionally (see Q5).
- Whether **unselected** submissions (not wet-lab tested) are published is not stated in the terms (only tested designs are explicitly described as published).
- CSV encoding details beyond the three columns (header exactness, allowed extra columns, delimiter/quoting, whether ranking is row-order only) are not fully specified; row-order = ranking is stated.
- No explicit max length for antibody chains or Fab combined length; "no antibody length limits stated."

---

## Q3. ANARCI — antibody/nanobody/scFv/Fab recognition, numbering, CDRs, diversity

### Takeaway
ANARCI aligns a query to **HMMER3 HMMs of germline V-domains** (VH, Vκ, Vλ, TCR) across species; a sequence is "recognized as" an antibody/nanobody/scFv/Fab when a V-domain aligns above threshold. It supports **Kabat, Chothia, Enhanced Chothia, IMGT, and AHo** numbering (Proteinbase/novelty uses **IMGT**; CDRH3 is the novelty discriminator). A nanobody = single VHH domain; scFv/Fab = VH+VL pair. CDR diversity (esp. CDR-H3) is the main lever for antibody novelty and specificity.

### Cited Findings
- **Mechanism / recognition:** ANARCI aligns each input to **HMMs built with HMMER3**, one per germline domain type (VH, Vλ/Vκ, Vα/Vβ) and species (human, mouse, rat, rabbit, pig, rhesus); the best alignment sets the numbering and classifies the domain. — [ANARCI, Bioinformatics 2016](https://academic.oup.com/bioinformatics/article/32/2/298/1743894)
- **Numbering schemes:** supports **Kabat, Chothia, Enhanced Chothia, IMGT, and AHo**; IMGT uses 128 positions, AHo 149; Chothia follows Kabat but shifts a VH-CDR1 insertion to the structural loop. — [ANARCI, Bioinformatics 2016](https://academic.oup.com/bioinformatics/article/32/2/298/1743894)
- **Scheme-dependent CDR boundaries:** CDR definitions differ by scheme (Kabat = sequence-variability; Chothia = structural loops; **AbM = compromise between Kabat and Chothia**; IMGT = its own numbering). E.g., Kabat places insertions at H35A/H35B; Chothia CDR-H1 loop ends H32–H34 by length. — [ANARCI, Bioinformatics 2016](https://academic.oup.com/bioinformatics/article/32/2/298/1743894)
- **Newer successor:** **ANARCII** (2025 preprint) is a generalized language model for antigen-receptor numbering; can convert IMGT output to Kabat/Martin/Chothia/AHo without renumbering. — [ANARCII, bioRxiv 2025](https://www.biorxiv.org/content/10.1101/2025.04.16.648720v1.full)
- **Challenge use:** Proteinbase says a design "counts as a nanobody or antibody if annotated as such **by a tool like ANARCI**," and the novelty antibody scale numbers variable domains by **IMGT** and compares **CDRH3 vs PLAbDab by edit-distance**. — [GLP1R Challenge-3 page](https://proteinbase.com/competitions/anthropic-adaptyv-2026/challenges/glp1r); [Adaptyv novelty blog](https://www.adaptyvbio.com/blog/novelty)
- **CDR-H3 is the specificity/novelty driver (transfer fact):** below ~70% CDR-H3 identity, epitope transfer is unreliable (a threshold, not a gradient); >80% identity at equal length ≈ clonotype; H3 is necessary-but-not-sufficient for a given specificity; same-epitope antibodies can have divergent H3 when germline-paired. — [project SEPIQ notes `nanobody_epitope_databases_methods.md`, synthesizing mAbs 2020 / PMC7039645 / PMC5852061](https://pmc.ncbi.nlm.nih.gov/articles/PMC7039645)

### Inferences
- To have a design **classified** as `nanobody`/`scfv`/`fab_kappa`/`fab_lambda` (rather than silently falling back to `protein`), it must present a **recognizable germline-like V-domain framework** — a de novo "antibody-shaped" sequence with non-germline framework may fail ANARCI annotation and be rejected or reclassified. Using **common framework regions** (as the page recommends) de-risks ANARCI recognition.
- For a de novo **single-chain `protein`** agonist, ANARCI is irrelevant to classification, but note: a protein that happens to be Ig-fold-like could be auto-flagged — keep the `protein` class honest.
- **Antibody-route novelty** to reach level 4 needs **CDRH3 <70% edit-distance identity to PLAbDab AND global <70%** — i.e., a genuinely novel CDR-H3 on a (recognizable) framework. High CDR diversity (esp. H3 length/composition away from public repertoires) is the explicit lever.

### Gaps
- The 2016 paper's search results did not surface **explicit VHH (nanobody) / scFv-specific handling** in ANARCI; VHH is numbered as a VH domain, and scFv/Fab are numbered per-chain — confirm in current ANARCI docs/source if exact VHH behavior matters.
- Proteinbase does not state **which ANARCI scheme/version/species set** gates the antibody classification filter (novelty scoring uses IMGT; the eligibility annotation tool/threshold is "a tool like ANARCI," unspecified).

---

## Q4. SEQUENCE LIABILITIES — de novo proteins and antibodies (tools/metrics)

### Takeaway
For de novo single-chain proteins the dominant liabilities are **unpaired/free cysteines, surface hydrophobic patches (aggregation), and poor predicted solubility/expression**; standard metrics are **SAP (spatial aggregation propensity), hydrophobic-patch scores, and CamSol**. For antibodies/nanobodies add **sequence-motif liabilities** (N-glyc sequon N-X-[S/T], X≠Pro; Asn deamidation NG/NS/NN/NT/NH; Asp isomerization DG/DS/DD/DT/DH; Met/Trp oxidation; unpaired Cys), **poly-specificity**, and **humanness/germline** distance, with **TAP (Therapeutic Antibody Profiler)** the standard developability panel. Motif presence is a **flag, not a verdict** (high false-positive rate).

### Cited Findings — antibody/nanobody liabilities
- **N-glycosylation sequon:** **N-X-S/T where X is any residue except proline** is the canonical N-glyc motif; affects stability, solubility, half-life, heterogeneity, effector function. — [Geneious Biologics liabilities](https://help.geneiousbiologics.com/hc/en-us/articles/5324606679060-Antibody-Sequence-Liabilities)
- **Deamidation (Asn):** canonical motifs **NG, NS, NN, NT, NH**; lability roughly **NG > NS > NT**; the n+1 residue is the key determinant. — [deamidation/isomerization study, mAbs 2019 (RG 329563487)](https://www.researchgate.net/publication/329563487); [Geneious](https://help.geneiousbiologics.com/hc/en-us/articles/5324606679060-Antibody-Sequence-Liabilities)
- **Isomerization (Asp):** canonical motifs **DG, DS, DD, DT, DH**; **DG and DS most liable**; rate depends on n+1 residue size/flexibility, pH, temperature. — [mAbs 2019 (RG 329563487)](https://www.researchgate.net/publication/329563487)
- **Motifs over-predict (false positives):** in 131 clinical-stage antibodies, only **67% (NG) / 21% (NS)** of expected-labile deamidation motifs showed detectable deamidation; **36% (DG) / 13% (DS)** for isomerization. A liability motif "does not necessarily mean the antibody will be poorly developable." — [mAbs 2019 (RG 329563487)](https://www.researchgate.net/publication/329563487)
- **Remediation:** mutate the motif in the CDR without losing binding (e.g., NG→SG or QG to block deamidation; D52E removed an isomerization site while keeping binding). — [mAbs 2019 (RG 329563487)](https://www.researchgate.net/publication/329563487); [ABT developability review](https://academic.oup.com/abt/article/6/1/13/6823522)
- **TAP (Therapeutic Antibody Profiler) — five developability guidelines:** (1) total **CDR length**; (2) **PSH** (patches of surface hydrophobicity); (3) **PPC** (patches of positive charge in CDRs); (4) **PNC** (patches of negative charge in CDRs); (5) **SFvCSP** (structural Fv charge symmetry parameter). Cut-offs derived from the distribution of **clinical-stage therapeutics (CSTs)**; **amber flag** = within the extreme (5%) tails ("be aware"), **red flag** = value never seen in CSTs ("cause for concern"). Thresholds are guidelines, not strict rules, now set by ~400 Phase-II+ CSTs. — [TAP, PNAS 2019](https://www.pnas.org/doi/10.1073/pnas.1810576116); [PMC6410772](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6410772/)
- **Lambda caveat:** λ-light-chain antibodies have a distinct developability risk profile; enhanced TAP contextualizes this. — [Nature Commun Biol 2023](https://www.nature.com/articles/s42003-023-05744-8)
- **Other antibody liabilities (standard panel):** unpaired/free Cys, Met/Trp oxidation, N-terminal pyroglutamate, fragmentation, and **poly-specificity/non-specific binding** (BVP/PSR/CSI-BLI assays) plus **humanness/germline distance** (e.g., OASis/Sapiens, T20, germline % identity). — [ABT developability review](https://academic.oup.com/abt/article/6/1/13/6823522); [Tamarind developability overview](https://www.tamarind.bio/blog/predicting-antibody-properties-developability)

### Cited Findings — de novo / single-chain protein liabilities
- **SAP (spatial aggregation propensity):** scores exposed hydrophobic patches as aggregation hot-spots from a structural model; reducing high-SAP patches by single mutations increases stability. — [Nature Sci Rep 2018 developability tool](https://www.nature.com/articles/s41598-018-36950-8); SAP method (Chennamsetty 2009).
- **Hydrophobic-patch scoring (hpatch):** a non-pairwise Rosetta term penalizing surface hydrophobic patches; patch descriptors from MD correlate with SEC-measured aggregation (BM hydrophobicity scale best). — [mAbs 2024 surface descriptors](https://www.tandfonline.com/doi/full/10.1080/19420862.2024.2362788)
- **CamSol:** **CamSol Intrinsic** = sequence-only solubility profile + overall score flagging aggregation-prone regions; **CamSol Structural** adds 3D proximity/exposure from a model; **sequence-based DeepSP** predicts SAP/SCM descriptors directly from sequence. — [CamSol, JMB 2015](https://www-vendruscolo.ch.cam.ac.uk/sormanni2015jmb-camsol.pdf); [CamSol pH-dependent, bioRxiv 2022](https://www.biorxiv.org/content/10.1101/2022.05.09.491135v1.full.pdf)
- **Free/unpaired cysteine (transfer/general fact):** odd or unpaired Cys drive disulfide scrambling, covalent aggregation/dimerization, and expression/refolding problems — standard practice is to avoid unpaired Cys in de novo designs unless a specific disulfide is intended (general biochemistry; no single clean URL captured — see Gaps).

### Inferences
- **Minimal liability filter for a de novo `protein` GLP1R agonist:** (1) **no unpaired Cys** (even Cys count, or Cys-free); (2) **no exposed hydrophobic patch** above the design-tool's SAP/hpatch flag; (3) acceptable **CamSol** intrinsic score (>~1 is generally "soluble" on CamSol's scale — verify against tool output); (4) expression/solubility sanity (e.g., SolubleMPNN-style sequence design, or a sequence-solubility predictor). These are the levers most likely to decide whether a de novo binder even expresses and folds in the Adaptyv pipeline.
- **If submitting a nanobody/scFv/Fab:** run **TAP** (flag PSH/PPC/PNC/SFvCSP/CDR-length), scan CDRs for **N-X-[S/T], NG/NS, DG/DS, free Cys, surface Met/Trp**, and check **humanness/germline**. Treat motifs as flags to evaluate in 3D/context, not automatic removals — and never remove a structurally required residue just to clear a flag (cf. project lesson on structural-proline false positives).
- Adaptyv's own pipeline likely applies some of these implicitly (expression is a practical gate), so pre-filtering on solubility/aggregation improves the odds a design reaches a functional readout.

### Gaps
- **No clean primary URL captured for free/unpaired-Cys liability** specifically (well-established biochemistry; flag as Tier-3 general knowledge for the writer to cite a review if needed).
- **Exact current TAP numeric cut-offs** were not retrieved (they live in the TAP web app / PNAS Table 1; a CASS slide listed approximate values e.g. PSH upper ~168–174, PPC ~1.5–3.2, but the amber-vs-red column labels were ambiguous — do not quote as exact).
- No GLP1R-/de-novo-specific liability threshold is published by the organizer; the above are general best-practice, not challenge rules.

---

## Q5. FUNCTIONAL-ASSAY INTERPRETATION — cAMP CRE-SEAP reporter, agonism, full vs partial

### Takeaway
The challenge uses a **cell-based CRE-driven SEAP reporter** in human cells expressing GLP1R: agonist → Gαs → ↑cAMP → CRE activates SEAP → luminescence; each design is compared to **untreated cells (basal)** and a **reference agonist**. Agonism is judged as a **concentration-dependent signal above basal** with a fitted **EC50** (potency) and **Emax** (efficacy); a **full agonist** reaches the reference's Emax, a **partial agonist** plateaus below it. The organizer publishes **no numeric EC50/fold-over-basal threshold** and does **not name the reference agonist** — both unspecified.

### Cited Findings
- **Assay (from the challenge page):** cell-based reporter in human cells expressing GLP1R; **SEAP reporter under a cAMP response element (CRE)**; **Gαs signalling raises cAMP and switches on the reporter**; secreted enzyme read as **luminescence**; each design compared with **untreated cells** and with a **reference agonist**. **EC50 not mentioned** on the page. — [GLP1R Challenge-3 page](https://proteinbase.com/competitions/anthropic-adaptyv-2026/challenges/glp1r)
- **Must activate to count:** "A design must be an agonist, confirmed in a functional assay, to count"; binders that do not activate the receptor do not count. — [GLP1R Challenge-3 page](https://proteinbase.com/competitions/anthropic-adaptyv-2026/challenges/glp1r)
- **CRE-reporter format (literature):** HEK293 engineered to express human GLP1R with a **CRE-driven luciferase** reporter (SEAP is the secreted-enzyme analog); EC50 from **4-parameter logistic (non-linear) fit**. — [AJP-Endo 2013 GLP1R cAMP study](https://journals.physiology.org/doi/full/10.1152/ajpendo.00551.2012)
- **Reference-agonist normalization (literature):** data commonly expressed as **% of a saturating dose of full agonist GLP-1(7-37)** (e.g., 10 nM = 100%) run on each plate, or as **fold-activation over basal** in untreated cells. — [GLP-1R patent normalization example, US (via search synthesis)](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10844049)
- **Potency benchmark (literature):** exendin-4 reported at **EC50 ≈ 1.93 nM** in a HEK293 CRE reporter — an order-of-magnitude benchmark for a strong full agonist (NB: exact primary URL not cleanly captured — Tier 3). — [via search synthesis of GLP1R CRE reporter studies]
- **GLP1R can be intrinsically activated via its ECD:** the extracellular domain has an intrinsic agonist mechanism — relevant since the recommended epitope is the ECD peptide-binding groove. — [Nature Cell Discovery 2016](https://www.nature.com/articles/celldisc201642)

### Inferences
- **How Adaptyv likely reports it:** a dose–response per design giving **EC50 (potency)** and **Emax / % of reference full agonist (efficacy)**, plus **fold-over-basal** at top dose; a hit = statistically significant, dose-dependent signal above untreated basal, ideally approaching the reference agonist's maximum. Because GLP1R is a Gαs GPCR with measurable constitutive/basal activity, the **fold-over-basal** framing (vs untreated cells, explicitly mentioned) is the cleanest agonism call.
- **Full vs partial:** a **full agonist** = Emax ≈ reference (GLP-1/exendin-4, ~100%); a **partial agonist** = reproducible dose-dependent activation plateauing **below** reference Emax even at saturating concentration (still "counts" as an agonist per the page, which only requires confirmed activation). For a de novo design, **any confirmed partial agonism likely counts** — the page sets no Emax floor.
- **Reference agonist (unnamed):** standard GLP1R full-agonist references are endogenous **GLP-1(7-37)/GLP-1(7-36)NH2**, **exendin-4/exenatide**, or **semaglutide/liraglutide**; Adaptyv most plausibly uses GLP-1 or exendin-4 as the 100% anchor (inference, not stated).
- **Design implication:** to score as an agonist (not just a binder), the design must engage the **orthosteric peptide-binding groove of the ECD + 7TM** so as to induce the Gαs-coupling conformation — occupying the groove like the native peptide N-terminus, not merely docking on the ECD surface.

### Gaps
- **No published numeric threshold** for EC50 or fold-over-basal that defines a "hit" — unspecified by organizer.
- **Reference agonist not named** on the page (GLP-1 vs exendin-4 vs semaglutide) — unspecified.
- Whether the readout is reported as EC50+Emax, single-dose fold-over-basal, or both, and at what concentration designs are screened, is not published.
- The exendin-4 ~1.93 nM figure lacks a cleanly captured primary citation; treat as an order-of-magnitude benchmark, not a challenge threshold.

---

## (A) Takeaways + draft compliance checklist

1. **Novelty bar:** Proteinbase scores a **1–4 scale**; "4/4" = reach **level 4 (de novo)** = **sequence ≤30% identity (MMseqs2 vs SwissProt/PDB/patents/therapeutic-Ab/PLAbDab) AND less-than-moderate structural similarity (Foldseek→TM-align, i.e., no domain match at TM ≥0.5 over ≥70% coverage)**. This scientific score is SEPARATE from the binary **eligibility** rule (de novo/zero-shot/not-a-modified-binder). De novo helical bundles typically cap at level 3 on the structural axis — pursue an unusual fold + novel method for full credit. [[novelty blog]]
2. **Draft compliance checklist (Track 3, verified against live page + terms):**
   - [ ] CSV with columns **`name,sequence,molecule_class`**, rows ordered best→worst (row order = ranking).
   - [ ] **≤ 20 designs** (Track 3 cap).
   - [ ] `molecule_class` ∈ **{protein, nanobody, scfv, fab_kappa, fab_lambda}** (NOT `single_chain`).
   - [ ] Single-chain `protein`/`nanobody`/`scfv` sequence **10–250 aa**; minibinder band 40–100.
   - [ ] **Fab** encoded as **`{VH}:{VL}`** (heavy first, colon separator), class `fab_kappa`/`fab_lambda`.
   - [ ] Nanobody/scFv/Fab must be **ANARCI-recognizable** (use common framework regions).
   - [ ] Every `name` **unique** and **non-identifying** (names published verbatim — no personal/institution info; not vallabh2006@... / real name).
   - [ ] Every design **unique** (no duplicates), **de novo + zero-shot**, not modified from an existing binder.
   - [ ] Each design must plausibly **agonize** (occupy the ECD peptide-binding groove), not just bind — non-activating binders do not count.
   - [ ] Eligibility: 18+, not in an excluded country/sanctioned list; biosecurity screening will run on synthesized designs.
   - [ ] Accept that all submitted material + results publish openly under **ODC-BY** (incl. negative results); file any patent **before** submitting.
   - [ ] Deadline **2026-10-25 23:59 AoE**.
3. **Liability filters:** de novo `protein` → **no unpaired Cys**, **low SAP/hpatch surface hydrophobicity**, acceptable **CamSol** solubility, expression sanity. Antibody classes → add **TAP** (PSH/PPC/PNC/SFvCSP/CDR-length), CDR motif scan (**N-X-[S/T], NG/NS, DG/DS**, Met/Trp oxidation, free Cys), poly-specificity, humanness/germline. Motifs are **flags, not verdicts** (high false-positive rate); never strip a structurally required residue to game a flag.
4. **Portfolio diversity (inference from selection design):** selection rewards **quality + design-novelty + method-novelty** and "will not rely on a single in silico metric." With 20 slots, spread across **distinct folds/scaffolds and distinct generative methods** (cap cousins), rather than 20 variants of one lineage — this hedges wet-lab risk and maximizes the novelty/method-novelty axes (consistent with project lesson "pick a portfolio for diversity, not cousins").
5. **Functional hit judged** as dose-dependent **cAMP CRE-SEAP signal above untreated basal**, with **EC50** (potency) + **Emax/% of reference full agonist** (efficacy); **partial agonists likely still count** (no Emax floor published). Reference agonist unnamed (likely GLP-1 or exendin-4).
6. **Authoritative-vocabulary resolution:** the live Challenge-3 page settles the `molecule_class` question — use the Challenge-3 brief vocabulary `{protein, nanobody, scfv, fab_kappa, fab_lambda}`; the prior-challenge `single_chain` example is obsolete.

## (B) Gaps / unverified rules
- **No numeric thresholds** published for affinity, EC50, fold-over-basal, or a minimum novelty level — all "unspecified."
- **Reference agonist not named**; **assay readout format** (EC50+Emax vs single-dose) and screening concentration not published.
- **Novelty DB versions/snapshots and MMseqs2/Foldseek/TM-align/ESMFold2-Fast parameters** unspecified; AFDB/UniProt (beyond SwissProt) not confirmed as novelty DBs (live page names SwissProt+PDB+patents+therapeutic-Ab+PLAbDab).
- **Which ANARCI scheme/version/species** gates the antibody classification filter unspecified (novelty scoring uses IMGT).
- **Exact TAP cut-offs** not retrieved (in TAP web app / PNAS Table 1); free-Cys liability lacks a cleanly captured primary URL.
- Whether **unselected** (untested) submissions are published; exact CSV header/delimiter strictness.
- The **Claude selection prompt** weighting of quality vs novelty vs method-novelty is unpublished (to be released post-competition).

## (C) Confidence
- **High:** Challenge-3 compliance facts (molecule_class vocabulary, 20-design cap, 10–250 aa, Fab `{VH}:{VL}`, uniqueness, deadline, ODC-BY, names-published, biosecurity screening, de novo/zero-shot filter) and the Adaptyv novelty definition (1–4 scale, 30%/70% sequence, TM 0.8/0.5 structural, antibody CDRH3 <70%) — all read directly off live Tier-1 organizer pages on 2026-10-13.
- **High:** standard liability tools/motifs and ANARCI mechanics — consistent across Tier-2 primary literature.
- **Medium:** functional-assay interpretation mechanics (CRE-SEAP, full/partial, fold-over-basal) — assay confirmed Tier-1, but numeric EC50/Emax thresholds and reference agonist are organizer-unspecified; interpretation is standard GPCR pharmacology (inference).
- **Lower:** exact TAP numeric cut-offs, the exendin-4 ~1.93 nM benchmark (Tier-3 search-synthesis), and the inference that AFDB is NOT searched (absence-of-evidence on the blog, not explicit denial).
- **Caution:** Tier-1 pages may be lightly cached; the window/status should be re-checked near the deadline. No numeric thresholds were invented — all unspecified items are flagged.
