# METHODS — validation playbook

Grows as stages run; each claim lands here with its command + evidence. Governing principles first.

## Principles

1. **Two scores, never conflated.** *Binding-assay passage* is scored against the inactive/apo **24–432 construct
   model**; *agonism* is scored against the WT **active state (6X18)**. An off-state-only binder is **demerited**.
2. **No in-silico proof of agonism.** Computation yields a *credible active-state binder* hypothesis at most;
   the **cAMP/SEAP assay is the only verdict**. Every agonism number is labeled LOW-confidence.
3. **Calibrate on controls, not absolute cutoffs.** Per folder, run positives (GLP-1(7-36), exendin-4, orforglipron,
   Boc5) and scrambled negatives; set gates relative to those distributions.
4. **Re-validate the exact submitted sequence** end-to-end (submit == folded == scored); natural AAs; linear/disulfide.
5. **Devil's-advocate each design:** does the message truly reach the vestibule, or does it drift to the ECD (→ antagonist)? Is it de-novo? Will it open TM6?

## Stage methods (filled on execution)

- **S0 target prep (F2) — DONE:** fetched 6X18; cleaned chain R → full-atom **active-state design target** (gaps
  130–135, 339–343 modeled; C-tail disordered); built a WT/apo **24–432 construct model** for binding scoring; dumped
  **hotspot selections** (`data/target/hotspots.json`: `ecd_groove`, `tm_message_reader`); positive/negative **control
  complexes**; **glycan (N63/N82/N115) + tag exclusion zones**. CPU/light; `data/target` + checksummed manifest.
- **S1 generate (F3) — RUN (hedged outcome):** RFdiffusion-1 + RFdiffusion-3 (all-atom) vestibule, LigandMPNN-seqed,
  af2ig-gated → **NON-VIABLE** (a folded de-novo binder can't reach the membrane-blind 7TM vestibule: RFd1 rim-perch
  floors af2ig at pae 23.5; RFd3 lipid-wraps the bundle). RFd **ECD-groove** sweep → viable binders (see S3). **EvoBind**
  (conda env `evobind`, AF2 `model_1_ptm`, ColabFold receptor MSA) linear threading peptides, 8×200 iters → agonism bet,
  **in-silico weak** (if_dist floored ~5 Å; `gen_evobind.sh`). Geometry truth: buried hotspots (<20 Å² SASA) are
  undesignable; a folded bundle perches on the accessible rim. [[lesson-denovo-binder-cant-reach-buried-pocket]]
- **S2 sequence (F4) — RUN:** **LigandMPNN** (`seq_mpnn.sh`, chain R fixed / binder redesigned, `--omit_AA C` = 0 Cys).
  Filter backbones by geometry BEFORE MPNN (small-interface rim backbones → degenerate poly-Ala). EvoBind peptides are
  direct sequence output (no MPNN).
- **S3 binding (F5) — RUN; af2ig is the PRIMARY gate:** af2ig (`dl_binder_design`, `parse_af2ig.py`) — pae_interaction
  <10, plddt_binder >80, binder_aligned_rmsd <2. Boltz-2 co-fold is calibrated (below) but **OVER-DOCKS this isolated,
  membrane-blind target** → used only where its ECD-anchor/iPAE gate separates binders from junk, never for the vestibule.
  - **Calibration (2026-10-13, `scripts/iface_score.py`, Boltz-2):** global **ipTM/pTM FAIL** (scramble ties
    native, AUC~0.5 — never rank on them). **ECD-groove anchor count (>=5)** + **iPAE_min (<=4.0)** separate
    native-like binders from SCRAMBLES at **per-seed 83% sens / 96% spec** (the AUC=1.00 I first quoted was a
    3-seed-MEAN artifact — corrected). **Antagonist test** (exendin(9-39), GLP-1(9-37), GLP-1(15-36)): antagonists
    **PASS** (56% vs agonists 83%, scrambles 4%) → the gate is a **SPECIFIC-BINDER-vs-JUNK filter, NOT an agonism
    selector**. Use it to reject non-binders; agonism rests on mechanism rationale + the wet-lab assay. Compact
    RFd generation target cluster from 6X18 = {190,194,233,234,237}.
- **S4 agonism hypothesis (F6):** active-state co-fold vs 6X18; message-in-vestibule contacts; optional GaMD TM6-opening.
  **Geometry feasibility gate (DONE):** in 6X18 chain R, the accessible upper vestibule (R197/R299, orforglipron region)
  is ~14–20 Å from the ECD-groove anchor (R32) → reachable by a ~10–14-residue extension; the deep orthosteric pocket
  (R363/364/394) is 35–38 Å + buried → unreachable. So an ECD-anchored design can present a message only to the
  accessible vestibule (an ago-PAM/orforglipron-grounded bet), not the deep peptide-N-term pocket.
- **S5 novelty + liabilities (F7) — RUN (eligibility + developability):** **eligibility** (`eligibility_check.py`,
  local Smith-Waterman id vs `data/novelty/known_agonists.fasta`; FLAG id>30% AND cov≥0.5) — 14/15 OK, eb_accv_l32
  dropped. **developability** (`developability.py`: unpaired Cys, low-complexity/poly-X, GRAVY, instability index) —
  3 clean ECD binders + 1 clean peptide. **Structural novelty** (FoldSeek vs PDB100, `runs/novelty/pdb_hits.m8`, query
  = af2ig binder fold): 7/7 ECD binders are sequence-novel but structurally common helical bundles (max TM 0.87–0.92;
  `des_8_7` most novel 0.70) → ~3/4 on the novelty axis. AFDB skipped (disk). NOTE (2026-10-15): the Challenge-3
  upload portal has NO novelty score (format/parse only) — novelty is locked up-front with these local screens, not a portal recheck.
- **S6 rank + select (F8):** five scorecards → ≤20, best-first, diversity-capped (≤2/lineage); validator exit 0; md5
  recorded. Input = `data/candidates/candidates.csv` (filter `status==keep` & `eligible==True`; rank WITHIN arm, since
  `binding_value`/`plddt` are arm-specific and not cross-comparable).

## Candidate register (single source of truth)

`scripts/build_candidate_register.py` joins the three tool outputs — `parse_af2ig.parse_scores` (af2ig pae/plddt/rmsd),
`developability.analyze`, `eligibility.score_design` — into `data/candidates/{candidates.csv,register.md}`. Never
hand-edit; re-run to refresh. The CSV is the machine-readable authority (`status`, `eligible`, `binding_model` columns).
