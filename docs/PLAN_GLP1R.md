# PLAN — De-novo GLP1R agonist (Anthropic × Adaptyv 2026, Challenge 3 / Track 3)

The 10 initial deliverables from the brief, grounded in the research wave (`reports/GLP1R de novo agonist
design.md` + `research_notes/.../01–08`, all verified against live sources on **2026-10-13**). Supplied facts,
verified evidence, hypotheses, and in-silico predictions are kept distinct; **binding is kept separate from
activation** throughout. No organizer threshold, reference agonist, or result is invented.

---

## 1 · Objective and hard constraints

**Objective.** Design ≤20 **de-novo** molecules that **bind *and activate*** human GLP1R (UniProt **P43220**).
Judged on predicted quality + **design novelty + method novelty**; "selection will not rely on a single in-silico metric." Experimental testing not guaranteed (Track 3 has no reserved allocation).

**Hard constraints (verified live):** target P43220 (ECD 24–139; 7TM 140–404). Binding construct = Sino
13944-H18H-DD, residues **24–432**, DDM/CHS, N-FLAG/C-His, HEK293, **proprietary thermostabilizing mutations**.
Functional assay = cell-surface Gαs→cAMP→CRE-SEAP. Formats: protein (10–250 aa), nanobody, scFv, Fab. **De-novo /
zero-shot**; no modifying GLP-1/exendin/semaglutide/known binders. **Linear or disulfide-cyclized, natural AAs only.**
Deadline **2026-10-25 23:59 AoE**. Submissions (incl. negatives) published **ODC-BY**; names published verbatim.

## 2 · Binding ≠ activation (the crux)

GLP1R is a **class B1 GPCR**: the ECD captures the ligand C-terminal "address"; the N-terminal **"message"
inserts into the 7TM core and drives the TM6 kink (~18 Å swing)** that opens the Gαs cavity (His7-imidazole
*charge* is the decisive activation element). Consequences, now evidence-backed:
- A surface/ECD binder **antagonizes** (Baker's de-novo GLP1R binders were antagonists; our own structure stream
  confirms ECD-only = block). Activation **requires reaching the 7TM vestibule** (the orforglipron site is sufficient).
- The **thermostabilized construct is likely inactive-biased** → it can *reward off-state binders*. Therefore:
  **score agonism against the WT active state (6X18); score binding-assay passage against the inactive 24–432 model;
  demerit off-state-only binders.**
- **No in-silico score proves agonism** (co-folders default inactive, ignore the membrane; no validated activation
  oracle). Computation gates a *credible active-state binder* only; the cAMP/SEAP assay is the sole verdict.

## 3 · Literature synthesis, cutoff, gaps

Full cited synthesis: **`reports/GLP1R de novo agonist design.md`** (26-row evidence register, 80 citations);
per-topic notes `research_notes/.../01–08`. **Search cutoff: 2026-10-13.** Load-bearing results verified first-hand:
- **Baker/IPD** (bioRxiv 2025.03.23.644666 → *Nature* 2026): de-novo agonists **only for class A** (MRGPRX1); **GLP1R →
  binders/antagonists, zero agonists** (down to 5.3 nM). Agonism "particularly difficult (conformational selectivity)."
- **EvoBind** (bioRxiv 2025.06.06.658268): the **only** direct de-novo GLP1R agonist — 18-mer **cyclic** peptide,
  **EC50 31.9 nM**, Gs-biased, no similarity to known agonists; but n=3, cross-activity (designed vs GCGR), cyclic.
- **No standalone designed protein/antibody has agonized any class B GPCR** (agonist-antibody precedents are class A:
  TSHR M22, apelin JN241-9, MC4R pN162; class-B "biologic agonists" are nanobody–**peptide** conjugates).

**Evidence gaps (organizer-unspecified or unknown):** numeric EC50/affinity/agonism/min-novelty thresholds; the
reference agonist; novelty DB versions/params; exact macrocycle & motif-scaffolding policy; the selection-prompt weighting.

## 4 · Strategy comparison (format × epitope × mechanism)

| # | Strategy | Mechanism | Evidence | Novelty | Primary failure mode | Required validation |
|---|----------|-----------|----------|---------|----------------------|---------------------|
| **S1** (primary) | de-novo **message micro/mini-protein** (<40–100 aa, linear/disulfide) → 7TM vestibule | orthosteric active-state stabilization | EvoBind (class B, peptide) + MRGPRX1 (class A) + Boc5 | High | binds but doesn't open TM6; ECD-drift → antagonist | active-state co-fold vs 6X18 + message-in-vestibule contacts |
| **S2** | de-novo **two-domain (address+message)** mini-agonist | reconstruct native mechanism | mechanism T1; no class-B de-novo precedent | **Highest** | fold/present-message failure | both domains fold; message reaches vestibule |
| **S3** | **TM-exoframe ago-PAM** (GEM-style) | allosteric active-state bias | GEMs restored a class-A mutant (Nature 2026) | High (moonshot) | membrane-embedded epitope; may need endogenous GLP-1 | exoframe binding + PAM rationale |
| **S4** | ECD/ECL **clamp** (control) | hold active ECD pose | weak — Baker ECD binders = antagonists | Moderate | **antagonist trap** | only with active-state target + functional gate; ≤1–2 slots |

**Format ranking for agonism:** small peptide/micro-protein ≫ mini-protein ≫ antibody/large (Ig fold can't reach
the 7TM → antagonist-prone). Clustering/dimerization agonism (de-novo IL-2/DR5 etc.) **does not transfer** (GLP1R is
monomeric). **User-approved plan (2026-10-13): mechanism-hedged portfolio across S1–S4.**

## 5 · Initialization / repo / GPU plan

- **Harness** (this repo, via `harness-creator`, mirroring the TNF/sepiq convention): AGENTS/CLAUDE invariants,
  `feature_list.json`, `configs/{target,filters,tools}.yaml`, `src/adaptyv_glp1r` validator + stage skeleton, tests,
  `init.sh` gate (**PASSES**: uv sync + compile + 12 tests + validator). FoldSeek/MMseqs2 installed (`tools/`, gitignored).
- **Repo:** private `Vijayavallabh/anthropic-adaptyv-2026-glp1r`; repo-local identity; no-AI-attribution commits;
  gitignore weights/runs/envs/third_party/data-raw; submission CSVs user-gated.
- **Env:** uv core (CPU); heavy tools in isolated venvs reusing sibling repos + the Anthropic uplifting kit; clean
  ODC-BY stack (AF3/Protenix-v2/ESM-3 excluded from submitted-design provenance).
- **GPU:** 8× H100 (idle). Default **4**; one process/GPU; `OMP` capped; **burst to 8 only in idle windows**; `nvidia-smi`
  before launch; never clobber foreign jobs. **No GPU design job runs without a specific owner OK.**

## 6 · Staged workflow + separate binding/agonism ranking

**Pipeline.** S0 target prep → S1 generate (vestibule-hotspot-targeted, active-state-conditioned) → S2 sequence
(ProteinMPNN/LigandMPNN) → S3 **binding** fold/score (Boltz-2/Protenix-v0.5.0/Chai-1/af2ig; ipSAE_min vs controls) →
S4 **agonism-hypothesis** gate (active-state co-fold + message-in-vestibule + optional GaMD TM6; LOW-confidence) →
S5 novelty+liabilities (FoldSeek/MMseqs2 + ESMFold-monomer + SAP/Cys + ANARCI) → S6 rank & pick ≤20 for diversity.

**Five separate scorecards (never conflated):** (A) predicted **binding**; (B) **hypothesized agonism** (explicitly
low-confidence, active-state only); (C) **novelty & compliance**; (D) **developability**; (E) **portfolio diversity**
(cap 2/lineage; spread mechanism×fold×method). No single-metric gate. Internal weights **disclosed**, never presented
as the organizer's formula. Calibrate every binding/agonism threshold against positive controls + scrambles, per folder.

**Stopping criteria:** a design advances only with recorded evidence on its scorecards; portfolio locks at ≤20 when
diversity + compliance + validator(exit 0) are satisfied; generation stops when the hedged portfolio is filled or the
research-refresh (below) flags a superior method.

## 7 · Verified Track-3 compliance checklist

✓ ≤20 designs; Oct-25 AoE; de-novo/zero-shot/not-modified; natural AAs; unique names+sequences; names non-identifying;
Fab `VH:VL` (heavy first); antibody formats ANARCI-parseable; biosecurity-screened; ODC-BY publication; eligibility
(jurisdiction) — user has submitted prior challenges. **Validator (`scripts/validate_submission.py --track 3`) enforces
format/length/uniqueness/ANARCI and exits 0 as the definition-of-done gate.**
⚠ **Must re-verify at upload:** `molecule_class` live value (`protein` vs `single_chain` — validator accepts both,
emits `protein`); macrocycle/non-canonical policy (assume linear/disulfide); de-novo motif-scaffolding permissibility.

## 8 · Submission outline + placeholder CSV

Ranked CSV, rows best-first (template — **not a candidate**):
```csv
name,sequence,molecule_class
DESIGN_PLACEHOLDER,SEQUENCE_PLACEHOLDER,protein
```
Dossier (in-repo; large artifacts out-of-git with manifests+checksums): per-design mechanism & activation rationale,
methods + provenance (tool/version/seed), novelty evidence, **actual** computed predictions, the internal ranking
(weights/normalization/missing-data disclosed), uncertainty, reproducibility, research cutoff, tool/license attribution.

## 9 · Unresolved facts / essential inputs

Organizer-unspecified (never invented): scoring formula/weights, affinity & activation thresholds, reference agonist,
binding-assay modality. To confirm at the portal: `molecule_class` string, macrocycle/motif-scaffolding policy. Owner-gated
inputs: portal upload + team name (submission time); authorization for >4 GPUs; any setup change beyond the approved init.

## 10 · Bounded research-refresh plan

Refresh (time-boxed, ≤1 focused pass each) **before**: final tool lock (F3), major strategy change, and final selection
(F8). Near the deadline, re-check the live Challenge-3 page + the Proteinbase novelty portal. Keep the evidence register
versioned (date every entry). Trigger an ad-hoc refresh only if a load-bearing assumption breaks (e.g., a new de-novo
class-B agonist method appears). Bound all refreshes by the Oct-25 deadline.
