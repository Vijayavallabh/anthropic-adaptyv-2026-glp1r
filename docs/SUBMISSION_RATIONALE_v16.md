# GLP1R Track-3 — v16 = v12 with 2 confirmed-dead reserve slots upgraded

**Recommendation (2026-10-26, deadline day):** `submissions/glp1r_track3_v16.csv`
(md5 `ca321795cb58b0c6922c5cca54b951ec`, validator PASS 20/0/0, all `single_chain`).
A **strict, surgical improvement over v12** — identical tested top-10, 2 dead reserve
slots replaced by confirmed-robust binders. Fallback: **v12** (`ae879c97`, portal-confirmed;
byte-identical tested-10, so near-equivalent and zero re-parse if preferred).

## What changed vs v12 (only rows 14 and 16)

A final-day **mining pass** Chai-confirmed 38 Boltz-strong, R299-reaching designs that had
never received the 2-folder gate (6 Boltz + 4 Chai seeds; `runs/picker/mine_*`). It also
re-confirmed that two v12 reserve members are **not** 2-folder-robust at the higher seed count:

- `glp1r_08_ago` (DiffPep, 15 aa): Boltz R299 **0/6** — does not reach the vestibule on Boltz.
- `glp1r_37_ago` (EvoBind, 14 aa): Boltz R299 **1/6** — not robust.

These two **reserve** slots (v12 rows 14, 16) were replaced with the best **length-honest,
high-pLDDT, 2-folder-robust, non-cousin** mining winners:

- `glp1r_50_ago` = `v4_reader_101_0` (BoltzGen, 21 aa, R299 **6/3**, ipSAE 0.40/0.26, pLDDT 87).
- `glp1r_51_ago` = `v4_reader_069_0` (BoltzGen, 22 aa, R299 **6/2**, ipSAE 0.50/0.22, pLDDT 90).

Both are de-novo (longest contiguous incretin overlap 3/2 aa), 0-Cys, single_chain.

## Why only these two (and not a wholesale re-allocation)

Re-allocating the full pool over the mining winners **over-concentrates the one dominant
BoltzGen architecture** (allocator output: 6 BoltzGen + 5 RFd4, 6 families; length-confounded
long minis promoted to the top; rank-1 pLDDT dropped to 67) — a length-confounded ipSAE bump at
the cost of v12's 8-family diversity and its strong length-honest rank-1 (`glp1r_25`, pLDDT 92).
That is the documented cousin-pile trap, not an improvement.

So v16 keeps everything that made v12 the honest best — the **diverse, proven tested top-10 is
byte-identical** — and spends the two genuinely-dead reserve slots on confirmed real binders.
It is a small but strict upgrade: +2 robust binders in the 20, zero change to the tested set.

## Firewall (unchanged)

Ranked on measurable binding/expression + lineage diversity, **never agonism** (the in-silico
agonism-pose signal was tested earlier this session against matched negative controls and found
non-discriminating — scrambles pass it). The wet **INDIGO CRE/luciferase** assay is the only
agonism verdict. Full method + the v14→v12 reversal: `docs/SUBMISSION_RATIONALE_v12.md`.
