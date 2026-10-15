# Constrained/cyclic topology and the agonism-shot quality of a pocket-threading GLP1R peptide

**Scope & firewall (stated up front, binding on every claim below).** Class-B GLP1R agonism is
**unprovable and unrankable in silico**; the cell-based Gαs→cAMP→CRE-SEAP assay is the only verdict
(project invariant; empirically reconfirmed — two first-principles agonism rankers failed, the orthosteric
*antagonist* scored highest on the two-state differential, `reports/GLP1R agonism first principles levers.md`).
A constrained topology (intramolecular disulfide macrocycle; pre-organization in general) can therefore at
best improve a **rankable prior / shot robustness** — pre-organization free energy, protease resistance,
foldability, and topology-match to the one precedent — and it **NEVER proves or ranks agonism**. Nothing
below claims an agonist. Tags: `[fact]`=sourced, `[physics]`/`[chem]`=derivation, `[HYP]`=hypothesis w/ mechanism.

**Current submission verified by bytes (this session).** `submissions/glp1r_track3_v5b.csv`
(md5 `b10571b40613d32ad36cbc9859890df7`, 20 designs): exactly **2 disulfide-capable** designs
(slot 04 `glp1r_04_ago`, 32-mer, 2 Cys = EvoBind `eb_prod_l32` C9/C29; slot 15 `glp1r_15_ago`, 25-mer,
2 Cys = PepGLAD `pglad_048` C1/C24) and **18 linear 0-Cys**; **zero lone-Cys free thiols, zero vicinal CC**.
So 15 of 17 win-path peptides are linear while the sole GLP1R de-novo agonism precedent (EvoBind) is cyclic.

---

## Key Question 1 — Pre-organization thermodynamics: how much binding free energy does disulfide macrocyclization plausibly buy a 13–25-mer?

### Takeaway
The **theoretical ceiling** for pre-organizing a 13–25-mer by one disulfide is **~1–4 kcal/mol** (≈ 1–3 orders
of magnitude in K_d), set by the conformational-entropy the unbound ensemble must otherwise pay on binding; the
**realistically realized** value is usually smaller (~1 order of magnitude, cf. a stapled-peptide 25-fold ≈
1.9 kcal/mol) and is **frequently ~0 or net-negative** because of enthalpy–entropy compensation and
over-rigidification. The benefit materializes **only if the constrained free-state conformation matches the
bound conformation** (Jencks pre-organization).

### Cited Findings (a) — sourced
- Classical bimolecular-association entropy cost (the ceiling the chelate/pre-organization effect draws down):
  **loss of translational + overall rotational entropy for a 2→1 reaction in solution ≈ 45 e.u.** (cal/mol·K)
  at standard state; Page & Jencks judged internal rotations and orientational terms **secondary** — [Page & Jencks 1971, "Entropic Contributions to Rate Accelerations in Enzymic and Intramolecular Reactions and the Chelate Effect", PNAS](https://wikidp.org/Q24617542). At 298 K, 45 e.u. → TΔS ≈ **13 kcal/mol** is the full rigid-body cost; effective molarities up to ~10^8 M (≈ RT·ln10^8 ≈ 11 kcal/mol) are the empirical upper bound of "connection"/pre-organization payoff.
- Effective molarity factorizes **EM = EM_H × EM_S**, and to good approximation the **entropic component depends mainly on the number of rotatable bonds in the ring product**, not on the linker chemistry — [Sun, Navarro & Hunter 2015, Org. Biomol. Chem.](https://dx.doi.org/10.1039/c5ob00231a). Same paper's counterpoint: in a Zn-porphyrin–pyridine system, amide vs ester linkers differed hugely in pre-organization (H-bonded 90–100% vs 60–70%) yet gave **identical terminal-H-bond EMs** → "linker pre-organization had no effect on chelate cooperativity" in that case (pre-organization↔EM link is not automatic).
- Common per-rotatable-bond binding penalty is a **constant 0.4–1.0 kcal/mol** (acknowledged crude); bound conformations commonly sit **4–5 kcal/mol above the ligand's lowest-energy conformation** (Perola & Charifson strain) — surfaced via [PIGNet, arXiv:2008.12249](https://arxiv.org/pdf/2008.12249). A fitted rotatable-bond entropy coefficient of **~−1.76 cal/K·mol** (≈ 0.52 kcal/mol TΔS at 298 K), "close to the C–C value in long-chain paraffins," appears in the docking/patent literature (same search cluster; weak/secondary source).
- Measured configurational-entropy loss can be large: **~25 kcal/mol** for amprenavir binding HIV protease, but **mostly from narrower energy wells in the bound state, not from a drop in accessible rotamers** — [Chang, Chen & Gilson 2007, PNAS, PMID 17242351](https://pubmed.ncbi.nlm.nih.gov/17242351/). (Implication: a static rotamer-count argument overstates what a staple recovers.)
- **Stapled/constrained peptides — the most on-point system:**
  - A synthetic staple restricts conformation, lowering conformational entropy and (sometimes) raising affinity, cell penetration and protease resistance — [Stapled peptide, Wikipedia](https://en.wikipedia.org/wiki/Stapled_peptide).
  - Hydrocarbon-constrained BID/BIM peptides: higher CD helicity but binding governed by **induced-fit + enthalpy–entropy compensation**, interpretable via the ground-state energies of unbound constrained vs unconstrained peptide — [Miles et al. 2016, Chem. Sci., PMC5618334](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5618334/).
  - PSD-95 GK stapled inhibitors (the cleanest entropy test): **staple 1 raised affinity ~25-fold (to 1.36 µM), the entropy gain coming mainly from the constrained helix in the FREE (unbound) state**; staples 2 & 3 gave **larger** entropy gains but **no** affinity improvement because a loose bound state produced a compensating enthalpic loss → "**stabilizing the stapled peptide in free solution [toward the bound fold] is the effective strategy**" — [Unarta et al. 2021, RSC Chem. Biol.](https://pubs.rsc.org/en/content/articlehtml/2021/cb/d1cb00087j).
- **Macrocycle counter-evidence (benefit is not guaranteed):** ITC studies find pre-organization **does not necessarily** yield a more favorable binding entropy (Grb2-SH2 23-membered macrocycles), and some macrocyclic ligands show an **unfavorable** entropy vs linear references; a lactam-bridged VEGF-peptide study found the conformational-entropy saving can be **counterbalanced by an unfavorable vibrational-entropy change when the constraint is too rigid**, though a configurational-entropy gain can partially escape compensation and improve affinity (all surfaced via search; **primary URLs not captured — see Gaps**).

### Derivations (b)
- `[physics]` **Order-of-magnitude for a 13–25-mer disulfide macrocycle.** A single disulfide in an
  already-single chain does not create a new *intermolecular* connection; it **removes conformational
  entropy from the UNBOUND backbone ensemble** by closing the loop between the two Cys. Treat the pre-paid
  entropy as k effective backbone/side-chain rotors restricted toward the bound geometry, at 0.4–1.0 kcal/mol
  each (upper ~1.5). A disulfide that meaningfully pre-restricts the equivalent of **~2–5 rotors** →
  **TΔS_preorg ≈ 1–4 kcal/mol**. Converting at RT·ln10 = 1.36 kcal/mol per decade (298 K): **1.4 kcal/mol ≈ 10×
  K_d, 2.8 ≈ 100×, 4.1 ≈ ~1000×**. This is a **ceiling**, realizable only if the pre-organized conformation = the
  bound conformation; otherwise the chain pays strain (Perola–Charifson 4–5 kcal/mol penalties live here) and
  the net can be ≤0.
- `[chem]` A disulfide is a **local** constraint (clamps only the inter-Cys loop, leaves both termini free),
  whereas head-to-tail backbone cyclization is a **global** constraint (removes both termini, constrains the
  whole ring). For equal ring size the global constraint pre-organizes more rotors → a larger entropic ceiling,
  at the cost (for GLP1R) of locking the N-terminal "message" terminus (see Q2/Q3).

### Inferences & [HYP] (c)
- `[HYP, grounded]` For a compact pocket-threading GLP1R peptide, **expect the realized pre-organization
  benefit to be ≤1 order of magnitude in affinity and quite possibly ~0**, because (i) the bound conformation
  is unknown and unvalidated (AF2-only), so matching it is a guess, and (ii) induced-fit + enthalpy–entropy
  compensation routinely cancels the entropic saving (Miles; Unarta staples 2/3). The disulfide is a bet on a
  **prior**, not a reliable affinity multiplier — and affinity is not agonism regardless.

### Gaps
- No single canonical kcal/mol "entropy gain from macrocyclization" exists; the literature is case-by-case and
  compensation-dominated. The Grb2-SH2 / lactam-VEGF / "unfavorable macrocycle entropy" ITC specifics were
  surfaced via search **without primary URLs** — treat as directional, not quotable.
- No thermodynamic measurement exists for any GLP1R-pocket-threading peptide (linear or constrained).

---

## Key Question 2 — The central tension: for the GLP1R orthosteric case, does a macrocyclic constraint help or hurt the odds of reaching activation depth?

### Takeaway
The tension is real and **unresolved by any in-silico score**, but it is **not symmetric**: rigidity's upside
(entropy pre-payment, stability) is a modest *prior*, while its downside (blocking the induced-fit threading of
the N-terminal message past the Trp33 cap into a deep, narrow class-B pocket) is a *mechanism-level* risk — yet
the one precedent that activated GLP1R **was itself cyclic**, so a constrained topology is at least **tolerated**
at the activation endpoint. The mechanistically-preferred resolution is a disulfide **positioned to pre-organize
the scaffold/address while leaving the N-terminal message tip free to thread**.

### Cited Findings (a) — sourced
- Activation requires the peptide **N-terminal "message" to insert deep into the 7TM bundle and drive a sharp
  TM6 kink / ~18 Å outward swing**; His7's cationic imidazole is indispensable; the message is read by R299
  (ECL2, contacts His7) — [Zhang 2017, Nature](https://doi.org/10.1038/nature22394); project report `reports/GLP1R de novo agonist design.md`.
- **Reachability tax (steep, demonstrated):** moving from an exposed ECD surface to a deep class-A pocket cost
  **1–2 orders of magnitude** in experimental yield in the one on-point campaign (CXCR4: **2 hits / ~26,000
  designs**, class-A), and the class-B receptors (GLP1R included) were reachable **only at the ECD surface →
  antagonists**; **no de-novo insertion into a class-B deep 7TM pocket has ever been demonstrated** — [Baker, Nature 2026](https://doi.org/10.1038/s41586-026-10656-8); synthesized in `reports/De novo GPCR agonist design methods.md`.
- De-novo GLP1R peptides reach only **~4.7–5.6 Å from R299 and perch on the rim** (project folds; EvoBind 7/12 and
  DiffPepBuilder 11/21 reach <4.5 Å on full-receptor AF2, but AF2 is membrane-blind and reachers have low pLDDT
  27–37) — `progress.md`, `reports/GLP1R v5 brutal stress test...md`.
- Induced-fit is the norm for constrained peptides binding PPIs, and **over-rigid** staples give **no** affinity
  gain (PSD-95 staples 2/3) — [Miles 2016, PMC5618334](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5618334/); [Unarta 2021](https://pubs.rsc.org/en/content/articlehtml/2021/cb/d1cb00087j).
- **The precedent is cyclic and still activated:** EvoBind's 18-mer **cyclic** peptide gave GLP1R EC50 **32 nM**,
  "novel binding modes compatible with active-state stabilisation" — [EvoBind GLP1R, bioRxiv 2025.06.06.658268](https://www.biorxiv.org/content/10.1101/2025.06.06.658268).

### Derivations (b)
- `[chem]` A disulfide does **not** have to clamp the threading tip. If placed between a mid/C-terminal Cys
  pair, it pre-organizes the "address"/scaffold loop while the **free N-terminus (the message) stays flexible**
  for induced-fit threading. This decouples the two effects: capture (some) pre-organization where it is safe,
  avoid taxing the depth-critical, flexibility-dependent step.

### Inferences & [HYP] (c)
- `[HYP, mechanism]` **A whole-molecule rigid macrocycle is a double-edged bet for GLP1R orthosteric agonism.**
  Upside: it pre-pays part of the binding-entropy tax and resists proteolysis (rankable priors). Downside: a deep,
  narrow pocket under the Trp33 cap plausibly needs backbone flexibility for the message to thread (induced-fit);
  a constraint that locks the message out converts a would-be agonist into a rim-perching antagonist — exactly the
  class-B failure mode Baker's data show. **Net direction:** a **locally-placed disulfide that spares the N-terminal
  message** is *expected-neutral-to-helpful* (keeps threading freedom, adds a stability/pre-organization prior),
  whereas a **constraint that rigidifies the message tip itself is expected-harmful** for reaching activation depth.
- `[HYP]` The cyclic precedent (EvoBind, head-to-tail, maximally backbone-constrained) activating at 32 nM is
  **weak positive evidence that constraint is tolerated**, but it is **not** evidence that cyclic *beats* linear:
  EvoBind only makes cyclic peptides, so there is **no linear-vs-cyclic comparison at GLP1R**. The precedent cannot
  establish that linear peptides are worse agonists.

### Gaps
- Whether any designed peptide (linear or constrained) actually threads the class-B pocket vs perches on the rim
  is **structurally undemonstrated**; the EvoBind "compatible with active-state stabilisation" claim is AF2-only,
  n=3, no crystal/cryo-EM, no SPR.

---

## Key Question 3 — Is EvoBind's cyclic peptide disulfide-cyclic or head-to-tail (backbone)? Can a submittable disulfide approximate the benefit?

### Takeaway
**EvoBind's cyclic peptides are HEAD-TO-TAIL (backbone/N-to-C) macrocycles, NOT disulfide** — verified by the
project first-hand and consistent with the external method. The exact precedent topology is therefore **not
submittable** (head-to-tail backbone cyclization is a project red line). A submittable intramolecular disulfide
can **partially** approximate the pre-organization prior, but it is a **different, more local** constraint (and
can be positioned to preserve N-terminal threading). RFpeptides is also head-to-tail; disulfide topology is
modelable (HighFold) but is not the native output of either macrocycle generator.

### Cited Findings (a) — sourced
- **INTERNAL GROUND TRUTH (decisive):** "**EvoBind cyclic = head-to-tail macrocycle** (Rettie cyclic-offset;
  confirmed in `src/mc_design.py` + **the precedent's 1-Cys 18-mer**) → non-submittable" — `progress.md`
  (session 2026-10-13b). The 18-mer EC50-32 nM lead has **only one Cys**, which **cannot form an intramolecular
  disulfide**, so its cyclization must be backbone. This is the strongest available evidence and it is first-hand.
- **External corroboration of the mechanism:** the "cyclic offset" is the AlphaFold **cyclic positional encoding**
  (AfCycDesign / Rettie et al.), which enforces a positional encoding invariant to cyclic permutation of the
  sequence — i.e., **head-to-tail (N-to-C) backbone cyclization by construction** — [Rettie et al. 2023, bioRxiv 2023.02.25.529956](https://www.biorxiv.org/content/10.1101/2023.02.25.529956v1.full.pdf) (published [Nat. Commun. 2025, 10.1038/s41467-025-59940-7](https://www.nature.com/nature-index/article/10.1038/s41467-025-59940-7)).
- EvoBind GLP1R paper confirms "cyclic peptide agonists" from the "EvoBind AI platform," sequence-only — [bioRxiv 2025.06.06.658268](https://www.biorxiv.org/content/10.1101/2025.06.06.658268) (license **cc-by-nc**; conflicts with the project's ODC-BY release invariant — owner previously accepted for the existing EvoBind arm, `progress.md`).
- **HighFold** separately shows the two topologies are distinct inputs: it modifies AlphaFold's positional-encoding
  matrices for **head-to-tail cyclization AND disulfide bonds** (HighFold2 adds unnatural AAs) — [HighFold, Brief. Bioinform. 2025, bbaf488](https://academic.oup.com/bib/article/26/5/bbaf488/8259888). (A predictor, not a generator.)

### Derivations (b)
- `[chem]` Head-to-tail vs disulfide are **not interchangeable**: (i) head-to-tail removes both termini and
  constrains the entire ring (sequence-agnostic, larger entropic ceiling); (ii) a disulfide needs **≥2 Cys at
  ring-closing positions** (sequence/structural constraint + oxidation/mispairing liability), clamps only the
  inter-Cys loop, and **leaves the termini free**. For GLP1R the free N-terminus is the activating message, so the
  disulfide's "weakness" (leaving a terminus free) is actually **mechanistically desirable** here.

### Inferences & [HYP] (c)
- A submittable intramolecular disulfide can **capture a fraction** of the precedent's pre-organization prior
  (both reduce the unbound ensemble) but **cannot reproduce its exact topology**. The honest framing: a disulfide
  design **mirrors the precedent's "constrained/pre-organized" category**, not its specific backbone-cyclic form.
- `[HYP]` Because the EvoBind lead was backbone-cyclic with a *free single Cys* and *free termini folded into the
  ring*, the activation-competent geometry did **not** depend on a disulfide at all — consistent with placing any
  submittable disulfide **away from the message tip**.

### Gaps
- Neither EvoBind/EvoBind2 nor RFpeptides reports a **disulfide-vs-backbone** head-to-head (efficacy or affinity)
  — so "a disulfide ≈ the backbone benefit" is an inference, not a measured equivalence.

---

## Key Question 4 — Tooling feasibility: can DiffPepBuilder / RFpeptides / PepGLAD make ELIGIBLE disulfide-constrained R299-aimed candidates in ≤10 days, and at what yield/liability?

### Takeaway
**Yes for DiffPepBuilder and PepGLAD; no for native RFpeptides.** DiffPepBuilder (MIT, installed, already run on
the R299 target) designs **intramolecular** disulfides and is the right submittable-constraint generator; PepGLAD
already produced one eligible disulfide macrocycle (slot 15). RFpeptides' native output is head-to-tail backbone
(not submittable) absent modification. Realistic **clean** yield is **single-digit percent** (reachability wall +
liability gating), but the pipeline is cheap (hours on 1 idle H100) and well inside 10 days.

### Cited Findings (a) — sourced
- **DiffPepBuilder (MIT):** "introduces **disulfide bonds to stabilize the generated peptide structures**"; MD
  "confirmed that the introduction of disulfide bonds **enhanced the structural rigidity and binding performance**"
  (qualitative; no quantitative stapling success rate given) — [DiffPepBuilder, arXiv:2405.00128](https://arxiv.org/abs/2405.00128). "Stabilize the generated peptide" ⇒ **intramolecular** (submittable topology).
- **DiffPepBuilder already ran on this target (internal):** 117 de-novo peptides → **54 pass eligibility+dev**
  (**19 disulfide-capable**); **11/21 clean keepers reach R299 <4.5 Å** (comparable to EvoBind 7/12); reachers have
  **low AF2 pLDDT 27–37** (membrane-blind; DPB seqs never saw AF2). Compute was gen + ~23 AF2 folds on **GPU 0 in
  ~hours** — `progress.md` (sessions 2026-10-14, 2026-10-14b), `reports/GLP1R v5 brutal stress test...md`.
- **PepGLAD can already do it:** slot 15 `pglad_048` is a **clean disulfide macrocycle (C1/C24), 25-mer** — but
  PepGLAD peptides **sit ~26–33 Å from R299** (included on novelty + dev + diversity, **not verified aim**) —
  `reports/GLP1R v5 brutal stress test...md`.
- **RFpeptides (BSD):** ≤20 designs/target gave medium–high-affinity binders for **all 4 targets**, X-ray Cα RMSD
  **<1.5 Å** — but macrocyclization is **head-to-tail backbone** (cyclic offset), **not submittable** without
  switching to a disulfide constraint — [Rettie et al., Nat. Commun. 2025](https://www.nature.com/nature-index/article/10.1038/s41467-025-59940-7).
- **Liability ledger (internal, concrete):** lone **free thiol** (odd Cys) → air-oxidized dimers/mixed adducts that
  convolve a dose-response readout — this was the `eb_prod_l20` own-goal **cut** in v5; **vicinal CC..CC** Cys →
  scrambling/mispairing (`eb_accv_l36`, `eb_prod_l40` **dropped**). A **clean** disulfide = a **single, non-vicinal,
  self-forming** Cys pair (e.g. `eb_prod_l32` C9/C29; `pglad_048` C1/C24) — `progress.md`, `reports/GLP1R v5...md`.

### Derivations (b)
- `[physics/compute]` DiffPepBuilder gen + full-receptor AF2 fold on a GLP1R-scale complex fits on **one H100** and
  ran in **~hours** already. A fresh batch of 100–300 in disulfide-staple mode on the corrected single-hotspot R299
  ("vest2") target, folded and gated, is **≪10 days** even on 1–4 idle GPUs at zero paid cost.

### Inferences & [HYP] (c)
- `[HYP, yield]` Expect a **low but non-zero clean yield**: of 117 DPB peptides only ~19 were disulfide-capable and
  only ~4/12 EvoBinds self-formed a clean intramolecular disulfide (~3–17%), and the clean set must also pass
  R299-aim (~5 Å, reachability wall), eligibility (≤30% id, ≤3-aa overlap, no graft) and developability. **Realistic
  outcome: ~1–3 clean eligible disulfide-constrained R299-aimers** from a few-hundred batch — enough for 1–3 slots,
  not a flood.
- `[HYP, design rule]` Instruct the generator/post-filter to place the disulfide **away from the N-terminal message
  tip** (Q2/Q3), require **exactly one formable non-vicinal pair**, and **reject any lone Cys** (fail-loud) to avoid
  the free-thiol own-goal.

### Gaps
- DiffPepBuilder reports **no quantitative** stapling success/benefit rate; "binding performance" improvement is
  MD-only and qualitative. No tool reports a disulfide-constrained **class-B-pocket** result.

---

## Key Question 5 — VERDICT (d)

### Verdict: primarily **(c)** — run a small, cheap disulfide-constrained R299-aimed generation — resolving into a targeted **(b)** swap if it yields clean candidates, with **(a) keep-v5b as the bounded fallback.**

**Decision.** v5b is **mildly mis-weighted** toward linear peptides on a *rankable-prior* axis (15/17 win-path
linear vs the sole precedent cyclic; only 2 of 20 carry any conformational constraint), and the fix is
**near-free** (clean MIT/BSD tools + idle H100s). It is **not** mis-weighted in a way that costs the win, because
the firewall means topology is a prior, not proof, and **there is no evidence linear peptides are worse agonists**
(EvoBind offers no linear-vs-cyclic comparison). So the move is to **add**, not to gut the linear arm.

**Concrete plan & counts:**
1. **Generate (option c).** Run DiffPepBuilder in **disulfide-staple mode** on the corrected single-hotspot
   **R299 "vest2"** target (the already-validated pipeline; MIT; ≤4 idle H100s; hours; ≪10 days). Batch ~100–300.
2. **Hard-gate** each candidate for: (i) **exactly one non-vicinal, self-forming intramolecular disulfide**
   (reject lone Cys / vicinal CC / ≥2-pair mispairing — fail-loud); (ii) disulfide placed **away from the N-terminal
   message tip**; (iii) **R299 aim ≤~5 Å** minD on ≥1 full-receptor fold; (iv) eligibility (**≤30 % id, ≤3-aa
   contiguous incretin overlap, no graft**); (v) clean developability (instability, GRAVY, no Met/Trp oxidation
   hotspots).
3. **Swap (option b), only if ≥1 clean candidate survives.** Swap **1–3** of the **weakest-aim PepGLAD slots**
   (`glp1r_12/13/14/16/17_ago` — the ~26–33 Å-from-R299 picks carried on **novelty/dev/diversity only, not verified
   aim**) for the new disulfide-constrained R299-aimers. This raises constrained/pre-organized designs from **2 → 4–5**
   (~20–25 % of the win-path, **mirroring the n=1 cyclic precedent's topology**) **and** trades up on the **R299-aim**
   axis — a strict improvement on **two** rankable axes at once, zero paid cost.
   - **Keep** the 2 existing disulfide designs (slot 04 `eb_prod_l32`, slot 15 `pglad_048`).
   - **Do NOT displace** the clean linear ~5 Å DiffPep R299-aimers (slots 05–10) — they are the closest-to-the-wall
     *aim* evidence and the best-defensible linear shots.
   - **Keep** ≥1 ECD binding hedge.
   - **Cap at ~4–5 constrained** of 17 win-path: the disulfide mispairing/free-thiol liability must stay rare and
     clean, and over-rotating to cyclic would be an unforced monoculture in the other direction.
4. **Fallback (option a).** If the generation yields nothing clean+aimed+eligible in the window, **keep v5b as-is.**
   The downside of staying topology-light is **bounded** — a modest prior, not the verdict.

**Firewall-honest rationale (must accompany any swap).** This improves **rankable priors** — pre-organization
(ceiling ≈ up to ~1 order of magnitude in K_d *if* conformation-matched; realistically often ~0, Q1), protease
resistance, foldability — and **better hedges the topology axis toward the one precedent**. It is **not**, and
**cannot be**, evidence of agonism; the disulfide-constrained designs are **additional independent clean shots**,
not a claimed agonist. **Only the cell-based cAMP/CRE-SEAP assay decides.**

### Gaps on the verdict
- The realized pre-organization benefit for a GLP1R threader is unmeasurable in silico and plausibly ~0 (Q1), so
  the *expected* gain from this swap is a **cleaner, better-hedged portfolio on rankable axes**, not a higher
  modeled agonism (which does not exist). If the disulfide generation's clean yield is 0, option (a) is correct and
  **no bytes should change** just to hit a topology quota.
