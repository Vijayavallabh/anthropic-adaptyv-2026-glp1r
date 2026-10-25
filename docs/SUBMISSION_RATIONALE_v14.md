# GLP1R Track-3 — v14 (agonist-mechanism moonshot portfolio)

**Recommendation (owner-adopted 2026-10-25):** `submissions/glp1r_track3_v14.csv`
(md5 `1f25ed31bbab4181d3a606cd1e2625fc`, validator PASS 20/0/0, all `single_chain`).
Portal-confirmed + byte-verified 20/20 (`data/candidates/portal_parse_v14_2026-10-25.txt`).
Upload is **USER-GATED**. Fallbacks (all portal-/validator-clean): **v12** gate-max
(`ae879c97…`), **v11b** balanced (`3f4b5bf0…`), **v11** portal-confirmed reorder
(`fc3653c4…`), then v10 (`6769ef67…`) / v9 (`419c57ff…`) byte-frozen.

## What this is and why

v14 is the **mechanism-hedged, agonism-biased** portfolio produced by the "push moonshots"
campaign. The win condition is **activation**, not binding; every prior version front-loaded
the measurable **binding gate** (R299 vestibule reach) because that is all computation can
score. v14 adds, at the top, three designs selected for a **deeper, activation-relevant pose**
— engagement of the **R190 central polar hub** and the TM6/TM7 switch residues in **both
co-folders** — produced by a new generation lever, while keeping 13 strong binders to clear
the organizers' picker gate.

**The deep-core generation lever (the moonshot).** RFd4-Proteina was re-run with the R299 ECL2
**rim** hotspot *dropped* and the binder forced onto the **deep activation switch only**
(R190 / H363 / E364 / Q394; specs `runs/rfd4/specs/deepcore_{pep,mini}.yaml`). This lifted
Boltz switch-engagement (`central_polar`) from **~3% (base pool) to ~24% (217/912)**; after the
independent Chai fold, **16/80 were two-folder switch-engagers and 7 reached R190 in both
folders** — the first firewall-legal enrichment for the *activator pose* this project has found.

## Composition (20 designs, 8 generator families, 0-Cys)

1. **Rows 1-3 — agonist arm (R190 both folders):** `glp1r_42_mini` (RFd4 deep-core mini, 49 aa,
   ipSAE_min 0.55, pLDDT 87, N-term-in-7TM 4/3 — the flagship, seated at **screen-protected
   rank-1**), `glp1r_43_ago` (RFd4 deep-core peptide, 25 aa, R190 both, 2f-robust),
   `glp1r_44_ago` (BoltzGen deep `v2_deep_087`, 25 aa, R190/E364). Distinct modalities
   (mini / peptide / BoltzGen); pairwise identity 0.48 / 0.40 / 0.0.
2. **Rows 4-16 — gate core (13 strong binders, from the v12 gate-max set):** `glp1r_28, 30, 25,
   29, 23, 10, 33, 27, 36, 08, 26, 38, 31` — the 2f-robust vestibule reachers / high-pLDDT
   expressers that hold the picker's "gets tested" bar.
3. **Rows 17-20 — tail hedge:** `glp1r_19, 37, 21, 39` (ECD-groove + weaker reachers; diversity
   and a format-safe floor).

## Why this ordering (and the honest trade vs v12/v11)

The organizers' picker takes up to the **top-10 of each submission's row order**, treats
**rank-1 as screen-protected** (guaranteed tested), and reserves a few slots for
**hardest-goal evidence / long shots**. v14 spends exactly those protected + long-shot slots on
the agonist-pose bets, and fills the rest of the top-10 with the gate-max binders so the
submission still clears the binder/expresser gate.

**This is a deliberate trade, not a free win.** v12 (gate-max) and v11 (portal-confirmed reorder)
score **higher on the pure binding-gate ranking**; v14 gives up a little of that ranking to seat
three activator-pose designs where they are most likely to be tested. A relayed side-agent note
(agonist moonshots bind weaker → the binding-ranked contest may test them less) was **affirmed,
not dismissed**, and is the reason the moonshots are *mixed in* (rank-1 + long-shot slots + 13
gate binders) rather than allowed to crowd out the tested slots. If the owner prefers to optimize
the binding gate instead, **v12 is the drop-in gate-max alternative** (same validation, portal-clean).

## Firewall (load-bearing — unchanged)

**No in-silico score proves or ranks agonism for a class-B GPCR.** R190 / deep-core engagement in
both folders is a **necessary-condition pose enrichment** for the active state — a membrane-blind
co-fold that biases *toward* the activator pose — **never a proof or a rank of agonism**. The three
agonist-arm designs are seated as **diverse independent shots** (coverage / P(≥1 activates)), not
as ranked "agonists." The **wet INDIGO CRE/luciferase functional assay is the only verdict.**

## Provenance + eligibility

All 20 are **de-novo / zero-shot**, graft-free (**longest contiguous incretin overlap ≤3 aa**:
the three new designs 3/2/2), **0-Cys**, 13-80 aa, `single_chain`. Validator PASS 20/0/0;
md5 `1f25ed31…`; portal-parse-confirmed + byte-verified 20/20. The disulfide-staple arm
(`dpbss_007`) remains an option pending the owner's Slack confirmation of paired-disulfide
eligibility (`docs/ORGANIZER_QA_2026-10-23.md`); it is **not** in v14. Internal diversity: the
only same-length pair ≥0.5 identity in the 20 is `glp1r_28`~`glp1r_25` at 0.57 (inherited from
v12, borderline-acceptable). Provenance table: `data/candidates/v14_provenance.csv`.
