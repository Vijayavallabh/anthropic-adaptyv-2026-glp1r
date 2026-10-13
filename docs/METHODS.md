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

## Stage methods (planned; filled on execution)

- **S0 target prep (F2, next):** fetch 6X18; clean chain R → full-atom **active-state design target** (note gaps
  130–135, 339–343; C-tail disordered); build a WT/apo **24–432 construct model** for binding scoring; dump
  **hotspot selections** (ECD groove + 7TM vestibule from `configs/target.yaml`); assemble positive/negative **control
  complexes**; record **glycan (N63/N82/N115) + tag exclusion zones**. CPU/light; outputs to `data/target` + `data/controls`.
- **S1 generate (F3):** vestibule-hotspot-targeted, active-state-conditioned de-novo per S1–S4; provenance (tool/version/seed); eligibility pre-screen.
- **S2 sequence (F4):** ProteinMPNN/LigandMPNN; 0 unpaired Cys unless intended.
- **S3 binding (F5):** multi-folder co-fold + the CALIBRATED engagement gate vs controls on the construct model.
  - **Calibration (2026-10-13, `scripts/iface_score.py` on 4 agonists vs 8 scrambles x3 seeds, Boltz-2):**
    global **ipTM/pTM FAIL** (scramble ties native, AUC~0.5 — never rank on them). The discriminators that
    separate native-agonist-LIKE engagement: **ECD-groove anchor count >=5 (AUC 1.00)** and **iPAE_min <=4.0
    (AUC 0.88)**. Gates binding MODE, not agonism. Compact message-site hotspots from 6X18 = {190,194,233,234,237}.
- **S4 agonism hypothesis (F6):** active-state co-fold vs 6X18; message-in-vestibule contacts; optional GaMD TM6-opening.
- **S5 novelty + liabilities (F7):** FoldSeek/MMseqs2 (seq≤30% / TM<0.5); ESMFold-monomer pLDDT; SAP/Cys; ANARCI for antibodies.
- **S6 rank + select (F8):** five scorecards → ≤20, best-first, diversity-capped; validator exit 0; md5 recorded.
