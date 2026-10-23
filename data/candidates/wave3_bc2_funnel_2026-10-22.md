# Wave-3 — BindCraft2 v1.0.4 active-state moonshot → 2-folder construct bar (2026-10-21/22)

**Firewall:** class-B GLP1R agonism is UNPROVABLE/UNRANKABLE in-silico. Everything below is
necessary-condition GEOMETRY + interface-confidence (R299 reach, iPAE, insertion depth) on the
inactive `construct_24_432` binding model. No design is or ranks as an agonist; the wet cAMP/SEAP
assay is the only verdict. This wave sought a NEW, decorrelated deep-insertion lineage, never agonism.

## Why BC2 (the one genuinely-new lever)
BindCraft2 v1.0.4 (released 2026-10-19; AF2 + ProteinMPNN/HyperMPNN; ODC-BY-clean) is the first
**AF2-based** generator applied here — architecturally orthogonal to the Boltz-family (BoltzGen) and
RFd3 designs already in v9. The hypothesis: an AF2-designed peptide/miniprotein that clears the
*independent* Boltz∧Chai 2-folder construct bar would be the first cross-family-robust deep reacher
this campaign has produced (the 2026-10-19 BoltzGen arm went 0/21 on that exact bar).

## Funnel validation (positive controls, bare peptide vs construct_24_432)
Rebuilt pipeline (Boltz `.venv-boltz` + Chai `.venv-chai` → `iface_score.py` → `apply_bar.py`)
reproduces the prior calibration almost exactly and PASSES all 4 native agonists:
| ctrl | Boltz reach-iPAE | Chai reach-iPAE (cal.) | R299 both | PASS |
|---|--:|--:|:--:|:--:|
| GLP-1(7-36) | 4.77 | 4.40 (4.49) | ✓ | ✓ |
| glucagon | 2.84 | 2.85 (2.84) | ✓ | ✓ |
| liraglutide | 2.19 | 3.67 (3.69) | ✓ | ✓ |
| exendin-4 | 2.73 | 3.63 (3.73) | ✓ | ✓ |
Bar (GLP-1-calibrated): R299 in ≥2/4 seeds BOTH folders; reaching-pose iPAE Boltz ≤6.0, Chai ≤5.5.
(Caveat: this is a REACH/binding necessary-condition gate — it passes native agonists AND would pass
a known antagonist that reaches R299; it is not an agonism selector.)

## Wave-3a — forced-deep targeting → 0 yield (reachability wall)
4 arms (deepcore / construct-robust / polarnet / deep-helix), `forced_targeting` onto the deep
vestibule cluster (R190/N240/Y242/W243) or polar net (R190/R299/H363/E364), peptide modality,
~1,988 trajectories. **0 accepted, 0 even refolded** — every trajectory rejected at the fold-screen
(pLDDT): AF2 cannot confidently fold a lone de novo *linear peptide* forced into the deep class-B
vestibule. Same wall as BoltzGen, from the AF2 side. (NOTE: initial run throttled to 1 worker/GPU to
coexist with a foreign TfR1 Chai job; 2 arms hit a CUDA-graph contention crash. Re-run at full
throughput after TfR1 finished — still 0/1,988.)

## Wave-3b — ordinary targeting + miniproteins → 12 designs, 0/11 pass the bar
Dropping the coercive forced-deep targeting (which kills fold confidence) yielded designs:
E (ordinary reader peptide) 6, F (ordinary deep peptide) 1, H (ordinary 0-Cys miniprotein 40-70aa) 5,
G (forced miniprotein) 0. 12 accepted total; eligibility dropped 1 (`bc2H…l65`: 4-aa "MEEE" overlap
with exendin-4). **11 eligible → two-stage funnel (Boltz-screen → 4 Boltz R299-reachers → Chai-confirm
construct) → 0/11 PASS the 2-folder construct bar.**

The 3 closest (reach R299 in BOTH folders but fail Chai interface confidence — identical to BoltzGen):
| design (arm) | Boltz reach-iPAE / R299 | Chai reach-iPAE / R299 | central-polar | PASS |
|---|--:|--:|--|:--:|
| bc2E_pep_reader (pep) | 6.36 / 3-4 | **11.24** / 3/4 | 190,364 | ✗ |
| bc2E_pep_reader (pep) | 6.09 / 3/4 | **12.02** / 4/4 | 190,363,364 | ✗ |
| bc2H_mini_ord (mini) | 9.00 / 3/4 | **18.49** / 4/4 | 190,364 | ✗ |
All three *touch* R299 in both folders (a geometric near-miss) but dock at Chai iPAE 11–18 vs the
native-comparable ≤5.5 (GLP-1 4.4) — a 2–3× interface-confidence gap, i.e. NOT native-comparable, and
worse than the existing v9 robust reachers (Chai iPAE 2.5–4.6). Failure is interface-fundamental.

## Wave-3c — ordinary + termini_accessible → 0/8 (tag-clash hypothesis refuted)
Final BC2 config: ordinary targeting + both termini oriented away (so the retained Met and the
C-terminal GFP11/TwinStrep tag sit clear) — the construct-robustness lever Wave-3a arm B never
reached. I peptides (5 accepted) + J 0-Cys miniproteins (4); eligibility dropped 1 (another 4-aa
"MEEE" exendin overlap) → 8 eligible → funnel → **0/8 PASS**. 2 Boltz R299-survivors; the best
(bc2I_pep_termaway) reached R299 4/4 in Chai but at iPAE **12.44** (vs ≤5.5), the other 1/4. The
termini-away geometry did NOT close the Chai-iPAE gap — confirming the 3b failure is
interface-fundamental, not a tag-clash effect. The BC2 config space is exhausted.

## FINAL VERDICT — BC2/AF2 moonshot is a rigorous NEGATIVE; HOLD v9
No BC2 (AF2) design clears the 2-folder construct bar that the v9 robust reachers clear — **0 across
all three waves** (3a 0/1,988 accepted; 3b 0/11; 3c 0/8), ~5,000 trajectories, every config
(forced-deep / ordinary / miniprotein / termini-accessible). Combined with the 2026-10-19 BoltzGen
arm (0/21), **two orthogonal generators (Boltz-family and AF2) fail with an identical failure mode:**
de novo designs can *reach* R299 (geometric near-misses: several hit R299 in both folders) but do not
*dock* the class-B vestibule with native-comparable interface confidence in the independent folder
(Chai iPAE 10–18 vs native ≤5.5). This is the same reachability/confidence wall from both sides.
The in-silico frontier for this necessary condition is exhausted. **v9 (`419c57ff`) stands as FINAL,
unchanged;** no candidate v10. Firewall intact throughout — no agonism was claimed or ranked; the wet
cAMP/SEAP assay remains the only verdict. Owner's portal submit of v9 + the assay are all that remain.

## Addendum 2026-10-22 — apples-to-apples re-score (side-agent critique resolved)
A side agent correctly flagged that Wave-3 scored BC2 designs tag-ON (full expression construct) but
judged them against a bar calibrated on tag-OFF natives (GLP-1 bare Chai 4.5, cut ≤5.5) and compared
them to v9's tag-OFF numbers — not apples-to-apples. Valid. Re-folded the 14-design comparison set
BOTH bare and tag-on through one pipeline (runs/bc2/compare/scorecard_{bare,construct}.csv; Boltz+Chai,
4 seeds each).

Findings:
- The tag DOES inflate Chai iPAE heavily: GLP-1(7-36) bare 4.53 → tagged **8.2**; liraglutide 3.67→8.96;
  glucagon 2.86→9.06; glp1r_25 2.5→7.93. So the absolute ≤5.5 Chai cut is **TAG-OFF-ONLY**; the correct
  tag-ON reference (the tagged real agonists) is ~8–9.
- Corrected comparison still HOLDS the negative. Scored identically tag-ON, R299-both reachers rank by
  Chai reaching-iPAE: **glp1r_25_ago 7.93 (v9)** < GLP-1 8.2 (native) < **glp1r_18_bind 8.37 (v9)** <
  liraglutide 8.96 < **bc2E_pep_reader 11.2 (best BC2)** < **glp1r_19_bind 12.71 (v9)**. The best BC2
  design (11.2) is worse than 2 of the 3 v9 reachers (glp1r_25 7.93, glp1r_18 8.37) and far worse than
  tagged GLP-1 (8.2); it edges only the weak glp1r_19 (12.71). No BC2 design is tag-on GLP-1-comparable.
  (NB: `scorecard_construct.csv`'s PASS_2folder column used the tag-OFF 5.5 Chai cut, so it reads False for
  every row incl. native GLP-1 — read the iPAE VALUES above, not that PASS column. `compare_fold.sh` has
  since been fixed to use `--chai-cut 99` for construct mode.)
- The side agent's specific hypothesis — a BC2 R299-reacher could be a better hedge than the v9 ECD-hedges
  (18/19/20, believed not to reach R299) — is **REFUTED**. In the realistic tagged construct, v9's own
  glp1r_18_bind and glp1r_19_bind DO reach R299 in both folders (8.37 / 12.71), and glp1r_18 (8.37) ≈
  tagged GLP-1 (8.2) — better than every BC2 reacher. The earlier "hedges don't reach R299" was itself a
  tag-OFF artifact.

Net: the critique was methodologically correct (unfair comparison; the tag wrecks scores), but the
corrected apples-to-apples re-score **CONFIRMS the Wave-3 negative on sound footing** — and reveals v9 is
slightly STRONGER than recorded (its top reachers glp1r_25/glp1r_18 reach R299 in the tagged construct at
GLP-1-comparable Chai confidence). No BC2 design earns a v10 slot. v9 (`419c57ff`) stands, unchanged.
