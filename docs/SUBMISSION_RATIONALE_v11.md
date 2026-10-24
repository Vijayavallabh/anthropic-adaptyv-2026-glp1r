# GLP1R Track-3 — v11 (picker-rubric reorder of v10)

**Recommendation:** `submissions/glp1r_track3_v11.csv` (md5 `fc3653c4…`, validator PASS 20/0/0, all `single_chain`).
It is **v10's exact 20 sequences, reordered** (SET == v10, byte-verified; nothing added or removed). **v10
(`6769ef67…`) is kept byte-frozen as the fallback.** Upload is USER-GATED.

## What this is and why

The owner supplied the organizers' **published design-selection prompt** (the "picker") and asked for the best-20
on its rubric. We reproduced the picker's exact method — fold each **bare submitted design (tags off)** against
**WT GLP1R 24-432** and score **ipSAE + ipTM** (co-fold interface), **ESMFold2 monomer pLDDT**, and **mean
Kyte-Doolittle** — on our full eligible pool (1,607 designs → 221 cheap-screen shortlist + a 271 un-folded
expansion), using **two co-folders** (Boltz, Chai) for robustness. Pipeline: `scripts/picker/`.

**The re-score's real value is the row-order lever, not a swap.** The picker takes up to the **top-10 of each
submission's row order**; v10 was not ordered by picker-strength (its best bare+WT design, `glp1r_25`, sat at row 6).
Reordering v10 captures the picker gain at **zero import risk**.

## Why NOT a wholesale replacement (cold-adversary verdict: MISTAKE, P≈0.70)

A draft that replaced 13/20 was stress-tested by an independent devil's-advocate and **refuted**, verified against
our own files + ledger:
- **The both-folder R299-reach gate is agonism-blind** — our own logged lesson (`lesson-cofold-reach-bar-cheaply-
  clearable-agonism-blind`: the antagonist exendin(9-39) passes it). Raising a binding-*gate* proxy while deleting
  13 mode/reference-diverse **agonism** bets optimizes the wrong objective; the prize is activation, the picker is
  only a binder/expresser gate, and v10 already clears it (portal-format-confirmed).
- **Margin-fragile:** 7 of the draft's 17 "2f-robust" designs sit exactly at `chai_r299==2` (one reseed from
  failing) — within tiny-n reseed noise.
- **In-hand diversity violation:** the draft contained a 0.75-identity near-duplicate pair (`v5_short_143_0/1`) that
  a k-mer screen missed; the incoming pool designs were also un-re-checked for novelty/developability.
- The 2f gate even **excludes** the pool designs with the highest *single-folder* ipSAE/pLDDT — i.e. the ones the
  picker's one folder would most reward.

Conclusion: keep v10's validated, diverse 20; **reorder** to front-load picker-strength; do not import unvetted
designs one day before deadline.

## The reorder (tiered by activation-relevant engagement, then bare+WT composite)

Firewall-clean: ordered by **measurable** binding/reach/expression on the stated **vestibule/R299** epitope
(the organizers note "ECD binding ≠ activation"), never by an agonism score.

1. **Rows 1-6 — 2f-robust vestibule reachers** (reach R299 in ≥2 seeds in BOTH folders): `glp1r_25, 23, 24, 10,
   08, 21`. Rank-1 `glp1r_25` (bare+WT composite 1.0, ipSAE 0.44, pLDDT 92) is the screen-protected top pick.
2. **Rows 7-15 — single-folder vestibule reachers** (agonism arm): `glp1r_05, 13, 07, 09, 01, 06, 16, 12, 14`.
3. **Rows 16-17 — weak/non-reaching message peptides**: `glp1r_04, 02` (demoted from v10 rows 3/16 — weak on the
   picker's bare+WT method).
4. **Rows 18-20 — ECD-groove binders** (antagonist-leaning binding hedge, distinct epitope/class): `glp1r_19, 18, 20`.

Per-design three-screen evidence: `data/candidates/v11_picker_screens.csv`.

## Firewall + provenance

Agonism is never scored or ranked (unprovable in-silico; the wet INDIGO CRE/luciferase assay is the only verdict).
`ipSAE`/`ipTM`/reach are necessary-condition **binding** proxies; the vestibule/R299 engagement is a stated
binding-site. All 20 are de-novo, graft-free (≤3-aa contiguous incretin overlap), 13-74 aa, `single_chain`,
portal-format-confirmed (as v10). The disulfide-staple arm (`dpbss_007`) remains an option pending the owner's
Slack confirmation of paired-disulfide eligibility (`docs/ORGANIZER_QA_2026-10-23.md`); it is NOT in v11.
