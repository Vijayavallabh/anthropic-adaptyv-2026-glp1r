# GLP1R — construct-reality probes + BoltzGen active-state generation arm (2026-10-19)

**BLUF.** A full "dominate" push on 8×H100: (1) a 4-thread deep-research sweep re-confirmed the firewall from every independent angle; (2) construct-reality probes showed the Adaptyv production construct (retained N-terminal (f)Met + C-terminal GFP11/Twin-Strep tag) disrupts v6's vestibule reach for most designs; (3) a diverse BoltzGen active-state sweep → depth-gate → independent cross-fold → novelty → 5-pose stability yielded **3 de-novo, eligibility-clean, production-robust, pose-robust deep-inserting candidates** that exceed v6 on the one geometric necessary-condition we can measure. A proposed v7 validated PASS 20/0/0 (md5 `f38c06df`) — **but a subsequent 2-folder (Chai) cross-predictor check REFUTED it: 0/21 candidates clear the Boltz∧Chai construct bar that GLP-1(7-36) clears, so the BoltzGen deep-insertion signal is largely Boltz-family-specific (the tool-specific artifact the 2-folder guard exists to catch).** FIREWALL HELD throughout: all metrics are necessary-condition geometry, never agonism. **VERDICT: HOLD v6 (`398bfb30`, adopted + byte-frozen) — do NOT adopt v7.** The extensive push was a rigorously-executed NEGATIVE; the cross-predictor guard did its job (see §6).

## 1. Firewall re-confirmed (deep research, reports/BindCraft2 and 2026 agonist design tools.md)
- **Baker/Norn/Tate/Sexton/Wootten, *Nature* 656:1044 (2026-05-21, PMID 42168559, verified via PubMed):** de-novo miniprotein agonists only for a **class-A** receptor (MRGPRX1); **GLP1R + all class-B siblings → antagonists**. No de-novo class-B agonist of any modality exists.
- The entire eligible 2026 toolscape (BoltzGen MIT, RFdiffusion3 BSD-3, BoltzDesign1 MIT, PXDesign Apache; NO-GO anything AF3/ESM-3-in-loop, Chai-2, AlphaProteo) conditions on a **supplied, ~rigid** target — none induces or scores activation. BindCraft2 v1.0.4 (AF2+ProteinMPNN, ODC-BY-clean) "induced_fit" is **binder-side**, not receptor activation.
- Activator-vs-antagonist discriminator = **insertion DEPTH + microswitch (ECL3 / central polar network R190^2.60b) engagement**; "a static co-fold pose cannot be read as active" (Cary/Sexton/Wootten, PNAS 2025). Natural-AA potency lever = N-terminal helix pre-organization (the Aib/Bip/disulfide tricks are off-limits here).

## 2. Construct reality (organizer-clarified; data/candidates/v6_met_probe_*, v6_construct_probe_*)
Adaptyv **cell-free expresses** designs (not synthesized): initiator **Met added & not removed** (some formylated); C-terminus carries **linker–GFP11–linker–Twin-Strep, on during the activation assay**; **disulfide formation unconfirmed ("linear only")**. ⇒ both natural termini are compromised; a de-novo activator must keep its message **internal** with disposable termini and **no disulfide dependence**.
- Met-probe (paired bare vs +Met, sepiq-Boltz single-seed): of 9 v6 designs that insert bare, **3 lose insertion to the Met** (glp1r_07/10/15); calibration caveat — exendin-4/glucagon/oxyntomodulin also score reach=False, so reach is a positive indicator, **never a disqualifier**.
- Full-construct probe (+Met+tag): the tag kills reach for glp1r_07/15/19/21 and strips R299 from 01; only **glp1r_06/09** survive as construct-robust reader-engagers (weak, fold-fragile prior). The reach proxy is engine/seed/construct-fragile (glp1r_04 flips between folders).

## 3. BoltzGen active-state generation arm (local-only; third_party/boltzgen, runs/ gitignored)
Tool: **BoltzGen 0.3.2** (PacesaLab; AF2+SolubleMPNN provenance = ODC-BY-clean; source-available license permits sharing outputs). Target: active-state **6X18** receptor, binding conditioned on deep vestibule sub-sites (label_seq, verified via viz CIF).
- **Sweep (all 8 GPUs, canary-guarded, ~700 designs, 4 conditions):** deep cluster (199/203/242/243/246), central-polar-net (199/372/373/403), reader-proximal (…/308), short "message-like" 10–16-mers. 1232 refolds.
- **Depth-gate** (N-term heavy-atom ≤5 Å to deep cluster; data/candidates/boltzgen_sweep_depthgate_*): **41 Cys-free N-term-deep inserters** (closest 1.99 Å), vs v6 which largely rim-perches.
- **Independent cross-fold** (sepiq-Boltz, a folder that did NOT design these, bare+construct vs 24–432): **21/41 independently reach R299 bare iPAE≤6** (vs 6/20 for v6 same pipeline); **4 survive the production construct** single-seed.
- **Novelty gate:** all deep-inserter winners ≤30% id to GLP-1/exendin/glucagon (de-novo).
- **5-pose stability** (data/candidates/boltzgen_posestab_*): single-seed over-called 3 of 4 (fold-luck); the robust set (deep+R299 in ≥3/5 poses in construct) = **3 designs**.

## 4. The 3 validated candidates + proposed v7 (USER-GATED)
| proposed name | sequence | len | novelty | pose-stab bare/cons | cons iPAE |
|---|---|---|---|---|---|
| glp1r_23_ago | LDLSNEMSEVLERKAVRRVLEMRRA | 25 | 12% (exendin4) | 0.8 / 0.8 | 4.5 |
| glp1r_24_ago | MFDELELVIG | 10 | 20% (GLP-1) | 1.0 / 0.6 | 3.29 |
| glp1r_25_ago | DFDELRHYIY | 10 | 20% (glucagon) | 0.6 / 0.8 | 4.25 |

All de-novo, natural-AA, linear, **Cys-free** (no disulfide dependence), short (synthesizable), acidic/charged N-termini (message-grammar-consistent), and a 4th generation lineage (BoltzGen) for mechanism diversity.

**Proposed v7** = v6 − {glp1r_03/12/14 (weakest: both-folder-scramble AND "neither reaches" in the construct probe)} + {glp1r_23/24/25}. Validator: **rows=20 errors=0 ANARCI=yes PASS**, md5 `f38c06df`. File: `runs/glp1r_track3_v7_PROPOSED.csv` (gitignored proposal).

## 5. Honest caveats / what this is NOT
- **Not agonism.** All metrics are necessary-condition GEOMETRY (insertion depth + reader proximity + fold/pose/construct robustness). The firewall stands: only the wet cAMP/SEAP assay decides.
- The candidates clear a **more rigorous bar than v6** (3 independent-context folds + 5-pose construct stability + novelty), but the base rate of de-novo class-B agonism is empirically ~0.
- **v6 stays the adopted, byte-frozen pick** unless the owner approves v7. The swap-out choice (03/12/14) is defensible on the measurable axes but is the owner's call.

## 6. 2-folder (Chai) cross-predictor validation → NEGATIVE (decisive)
v6's reach bar required TWO predictors (Boltz **and** Chai) to agree — a guard against one tool's pocket-fit quirk. §3–5 above checked the BoltzGen candidates on **Boltz-family only** (Chai was wiped in the disk cleanup); multi-pose stability is NOT a substitute for a second predictor. Restoring Chai (reused `sepiq/.venv-chai` + cached weights; no rebuild) and re-running candidates + controls on the identical 2-folder bar (`data/candidates/boltzgen_2folder_chai_2026-10-19.csv`):
- **Calibration OK:** GLP-1(7-36) reaches in Chai (iPAE 4.63, R299 ✓) — the bar detects a real deep reacher.
- **0 / 21** BoltzGen candidates clear the 2-folder *construct* bar (Boltz-pose-robust ∧ Chai-reach). `glp1r_23` (bg_v4_reader_24) is the lone partial — Chai confirms its **bare** reach (iPAE 4.14) but **not** in-construct (iPAE 8.64); `glp1r_24/25` Chai does not confirm at all (iPAE 15–19).
- v6's own `06/09` also fail Chai here (Boltz-leaning) — consistent; they were never 2-folder reachers either.
**Conclusion:** the BoltzGen deep-insertion result does **not** survive cross-predictor validation — a Boltz-specific artifact on the construct-reach axis. **HOLD v6; v7 not adopted.** An honest negative from a rigorously-executed, extensive-GPU push; the 2-folder guard worked exactly as designed. (My earlier "more rigorous than v6" framing was wrong on this axis and is retracted.)
