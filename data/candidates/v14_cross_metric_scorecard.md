# v14 cross-metric scorecard + gate-vs-agonism decision (2026-10-25)

Judge = the organizers' picker rubric reproduced in `scripts/picker/` (bare design + WT GLP1R
24-432, Boltz+Chai; ipSAE/ipTM/ESMFold-pLDDT/gravy/2f-reach), scored over the full eligible pool
(`runs/picker/allocF42_ranked_all.csv`, 191 designs). **FIREWALL: no column ranks agonism.** The
R190-both column is a *necessary-condition pose enrichment* (membrane-blind co-fold biased toward
the activator pose), NOT an agonism rank; the wet INDIGO CRE/luciferase assay is the only verdict.

`gate#` = rank on the gate composite among the 191-design pool (lower = stronger binder/expresser).
† = scored on the active-state deep-core axis, not the bare+WT picker axis (bare+WT re-fold pending an idle GPU).

| row | name | family | L | gate# | ipSAE_2f | ipTM_2f | pLDDT | 2f-rob | R190-both | role |
|----:|------|--------|--:|------:|---------:|--------:|------:|:------:|:---------:|------|
| 1 | glp1r_42_mini | RFd4-deepcore | 49 | —† | 0.82/0.55† | 0.975† | ~87 | Y† | yes(dc) | AGONIST-ARM R190-both |
| 2 | glp1r_43_ago | RFd4-deepcore | 25 | —† | 0.34/0.23† | 0.951† | ~87 | Y† | yes(dc) | AGONIST-ARM R190-both |
| 3 | glp1r_44_ago | BoltzGen | 25 | 26 | 0.383 | 0.842 | 89.0 | Y | no | AGONIST-ARM R190-both |
| 4 | glp1r_28_ago | BoltzGen | 30 | 2 | 0.505 | 0.902 | 92.0 | Y | yes | gate-core |
| 5 | glp1r_30_mini | RFd4 | 80 | 4 | 0.684 | 0.891 | 83.0 | Y | n/a | gate-core |
| 6 | glp1r_25_ago | BoltzGen | 30 | 1 | 0.445 | 0.901 | 92.0 | Y | yes | gate-core |
| 7 | glp1r_29_ago | BoltzGen | 23 | 3 | 0.436 | 0.891 | 68.0 | Y | yes | gate-core |
| 8 | glp1r_23_ago | PepGLAD | 15 | 49 | 0.336 | 0.837 | 85.0 | Y | yes | gate-core |
| 9 | glp1r_10_ago | DiffPep | 23 | 85 | 0.271 | 0.718 | 68.0 | Y | no | gate-core |
| 10 | glp1r_33_ago | DiffPep | 14 | 92 | 0.256 | 0.715 | 73.0 | Y | no | gate-core |
| 11 | glp1r_27_ago | PepGLAD | 13 | 106 | 0.262 | 0.595 | 70.0 | Y | yes | gate-core |
| 12 | glp1r_36_ago | DiffPep | 22 | 107 | 0.236 | 0.695 | 91.0 | Y | yes | gate-core |
| 13 | glp1r_08_ago | DiffPep | 15 | 117 | 0.242 | 0.632 | 72.0 | Y | yes | gate-core |
| 14 | glp1r_26_ago | PepGLAD | 17 | 131 | 0.235 | 0.592 | 68.0 | Y | yes | gate-core |
| 15 | glp1r_38_bind | ECD | 77 | 78 | 0.595 | 0.763 | 87.0 | - | no | gate-core |
| 16 | glp1r_31_mini | RFd4 | 79 | 10 | 0.616 | 0.875 | 84.0 | Y | n/a | gate-core |
| 17 | glp1r_19_bind | ECD | 74 | 125 | 0.359 | 0.738 | 89.0 | - | no | tail-hedge |
| 18 | glp1r_37_ago | EvoBind | 14 | 143 | 0.220 | 0.625 | 70.0 | Y | yes | tail-hedge |
| 19 | glp1r_21_ago | RFd3 | 37 | 167 | 0.100 | 0.581 | 81.0 | Y | no | tail-hedge |
| 20 | glp1r_39_pm | PepMLM | 20 | 150 | 0.272 | 0.853 | 91.0 | - | yes | tail-hedge |

## The trade, quantified (v14 vs the allocator's pure gate-max 20, `allocF42_submission`)

- v14's top-7 rows are strong on **both** axes (gate ranks 1-4 at rows 4-7; flagship `glp1r_42` deep-core ipSAE 0.82/0.55 + R190-both) → rank-1 is NOT a weak-binder bet, and v14 clears the picker's 'gets tested' bar.
- v14 trades **6 gate-max slots** (dropped: `v2_deep_060_1`#5, `rfd4_mini_g7_76`#13, `rfd4_mini_g5_91`#14, 3 BC2 peptides #66/#94/#103) for **3 agonist-arm deep-core designs** (rows 1-3: R190-both) + **3 diverse tail hedges** (gate #143/#150/#167).
- So on the **pure gate composite v14 is NOT the max** — the gate-max is `allocF42`/v12. v14 is a deliberate agonism+diversity hedge.

## Dominance check — are there strictly-better unseated designs? (adversarial)

Many unseated pool designs are high-gate (#5-#60) AND R190-both — apparent free upgrades over v14's weak tail (`glp1r_21`#167, `glp1r_19`#125). **They are a trap, not a win:**
- All are the **BoltzGen deep-motif family** (`…RRQYIED…[WL]DTLSL…`); **15/30 of the gate-top is this one architecture**. Seating several = a cousin pile vs the ~2/lineage diversity cap (v14 already has 4 BoltzGen).
- Their R190-both + gate strength is exactly the **agonism-blind** reach/over-docking signal (antagonist exendin passes the same bar). Promoting them = re-ranking by a firewall-barred proxy.
- Prior waves proved this family is **length-confounded** and collapses to ~one substitution-aware cluster.
- **Conclusion: no firewall-legal swap improves v14.** The only way to raise the gate score is to abandon the mechanism bet → that portfolio already exists as **v12 / gate-max**.

## Decision (owner's dial — this is a reserved call)

`P(win) = P(selected) × P(express+bind) × P(agonist)`. The gate scores the first two; **no metric scores the third** (firewall).

- **v14 (adopted) — maximize P(win):** top rows clear the gate; rank-1 guaranteed-tested AND R190-engaging; rows seat diverse R190 mechanism bets. Best when you believe the prize (agonism) needs the mechanism arm, since the gate is agonism-blind.
- **v12 / gate-max — maximize P(selected)×P(bind):** the 20 highest gate-composite designs (cap-aware). Best only if you weight 'gets tested' over 'activates'; but it is agonism-blind (Baker-prior antagonist-leaning) so it spends every slot on the one factor that does not win.

**Recommendation: keep v14.** The gate-max alternative optimizes the one factor that cannot win the challenge; v14 keeps the tested-top gate-strong while spending the protected/long-shot slots on the only firewall-legal activator-pose enrichment found. v12 remains the drop-in if you decide to weight the gate.

## One open verification (cheap, GPU-blocked now)
Re-fold `glp1r_42`/`glp1r_43` on the bare+WT 24-432 picker axis so the flagship sits on the same axis as the pool (its deep-core ipSAE 0.82/0.55 already looks strong, but that is the active-state axis). Blocked now: all 8 GPUs occupied by a foreign job — never clobbered. Can queue a non-clobbering idle-GPU watcher on request (writes only to `runs/`).
