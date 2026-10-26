# GLP1R Track-3 — v12 (gate-max + diversity best-20) = FINAL

**Recommendation (2026-10-26):** `submissions/glp1r_track3_v12.csv` (md5
`ae879c9738ca02882faeb29fb4e48c57`, validator PASS 20/0/0, all `single_chain`,
portal-parse-confirmed). This supersedes v14 (see "Why v12, not v14" below).
Upload is **USER-GATED**. Fallbacks: v15 (`39f3cf00…`, a higher-ipSAE but
cousin-heavier alternative, below), v11 (`fc3653c4…`), v10 (`6769ef67…`), v9 (`419c57ff…`).

## What v12 is

The **gate-max + lineage-diversity** best-20: the strongest designs on the organizers'
reproduced picker rubric (bare design + WT GLP1R 24-432; Boltz+Chai ipSAE/ipTM, ESMFold2
pLDDT, Kyte-Doolittle gravy, 2-folder R299 reach), subject to a hard **2-folder-robust**
reach gate (anti single-folder-artifact) and **≤4-per-lineage** diversity caps.

- **8 generator families:** BoltzGen 4, RFd4 4, PepGLAD 3, DiffPep 4, ECD 2, EvoBind 1,
  RFd3 1, PepMLM 1. 0-Cys. 17/20 are 2-folder-robust reachers.
- **Row order best-first** (picker takes top-10 by row order; rank-1 screen-protected):
  rank-1 `glp1r_25` is a 30 aa, 2f-robust, pLDDT-92 **length-honest** robust reacher, not a
  length-inflated long mini.

## Why v12, not v14 (the reversal)

v14 (the earlier "agonist-mechanism moonshot") front-loaded 3 designs seated on an
**R190 deep-switch engagement** signal. A cold devil's-advocate — then direct checks
against the project's own control data — proved that signal is **null**:

- `runs/rfd4/ctrlpanel/scorecard_2folder.csv`: **scrambled-GLP-1 negatives** engage the
  same central-polar residues (`190|363|364`, `190|364`) as the agonists *and* the
  antagonist exendin(9-39). R190 engagement does **not** discriminate.
- The deep-core spec was just the vestibule spec **with the R299 hotspot deleted**, so the
  "3%→24% switch-engagement" was an R299-deletion artifact; total central-polar engagement
  was flat (61.5% vs 60.0%).

So v14's distinctive premise does not survive its own negative controls. The honest
portfolio ranks on **measurable binding + expression + diversity only** — which is v12.
(Full checks: `data/candidates/v14_cross_metric_scorecard.md` and the session record.)

## What the final-day GPU confirmation added (and why it did not change v12)

With all 8 GPUs free (deadline −4.6h), a **multi-seed confirmation fold** re-folded the 36
top binding contenders (the v12/pool leaders + the deep-core designs incl. the v14 flagship)
bare+WT at **6 Boltz + 4 Chai seeds** (`runs/picker/confirm15_*`). Findings:

- **v12's strongest members are robust at the higher seed count:** `glp1r_32` (vest_76)
  ipSAE 0.61/0.79, R299 5/4; `glp1r_34` (v2_deep_060_1) 6/4; `glp1r_35` (vest_91) 5/2;
  `glp1r_30/31` 2f-robust. The gate ranking holds.
- **The v14 flagship (`mini_101`) never makes the 2f-robust cut** even at 6/4 seeds (reaches
  R299 in only 1 Chai seed) — independently confirming it was not a special design.
- **Re-allocating over the complete pool over-concentrates length-favored cousins**
  (6 BoltzGen incl. near-twins `v2_deep_060_0/1` + 5 RFd4; only 6 families) — a
  length-confounded ipSAE bump at the cost of diversity. That set is kept as **v15**
  (`39f3cf00…`, validated) for reference, but it is *not* preferred: v12's 8-family,
  length-honest composition is the better bet for both the displayed-affinity axis and the
  agonism-coverage bonus.

Net: the confirmation fold **validated v12 and killed v14's premise** — exactly what a
rigorous final-hours pass should do (confirm, don't churn).

## Firewall (unchanged)

No in-silico score proves or ranks agonism for a class-B GPCR. ipSAE/ipTM/reach are
**necessary-condition binding/expression proxies** on the stated vestibule epitope; the 20
are ordered by those + lineage diversity, **never by an agonism score**. Agonism is the
**wet INDIGO CRE/luciferase** verdict. All 20 are de-novo, graft-free (≤3-aa contiguous
incretin overlap), 0-Cys, `single_chain`. The paired-disulfide design `dpbss_007` remains an
optional owner-gated +1 (organizer Q&A §7 permits paired disulfides); it is not in v12.
