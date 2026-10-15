# GLP1R portfolio — diversity-selection certificate (M1)

_Zero-GPU, deterministic. Firewall GUARD-A: the objective uses only clean sequence / physicochemical / novelty features — no minD_R299, engagement, iPAE, ipTM or consensus signal. GUARD-B: every number below is a RANKABLE coverage/decorrelation measure, never an agonism claim._

- Clean features in the objective (12): `length, entropy, maxfrac, ag_frac, longest_run, n_cys, arom, gravy, charge, elig_pid, elig_cov, lcs` + lineage partition-matroid.
- Win-path band pre-filter: entropy>=2.81, longest-run<=2, A+G<=0.36, graft-lcs<=3, even non-vicinal Cys, eligibility pass.
- **TRIPWIRE PASSED**: all 8 PepFlow/pepx pool rows are rejected by the band (confirms the optimizer cannot select the rejected low-complexity outliers).

## Per-lineage dispersion: v5c subset vs the unconstrained max-min upper bound

_The 'frontier' column is a greedy max-min / log-det **upper bound that is outlier-seeking**: it maximizes raw feature spread, so it preferentially grabs the compositional extremes of each band (longest / most-charged / highest-entropy members). It is a DIAGNOSTIC CEILING, not a target — a gap to it means v5c spends some raw dispersion to buy the aim / developability / validated-binding priors those extremes lack, which is the intended engineering trade, not a deficiency. The decision-relevant test is the strict-Pareto scan below, not this gap._

| Lineage | budget | pool (band-pass) | v5c min-pair | max-min ceiling | head-room | v5c logdet | ceiling logdet |
|---|--:|--:|--:|--:|--:|--:|--:|
| EvoBind | 4 | 4 | 2.870 | 3.568 | 19.6% | 8.573 | 9.323 |
| DiffPep-linear | 6 | 54 | 2.605 | 5.118 | 49.1% | 12.248 | 16.139 |
| DiffPep-ss | 1 | 12 | n/a | 5.469 | 0.0% | 2.375 | 5.072 |
| PepGLAD | 6 | 47 | 2.126 | 4.577 | 53.6% | 10.917 | 14.601 |
| ECD | 3 | 0 | 4.874 | 4.874 | 0.0% | 10.845 | 10.845 |

## Strict-Pareto swap candidates

_Gated axes (a dominator must be no worse on every one, strictly better on >=1): sequence-novelty id, coverage, graft lcs, structural-novelty TM (when known), **correct-aim minD_R299 prior** (geometric, not agonism; a member with verified aim cannot be displaced by one without it), and developability liability-set (subset). Aim is used ONLY here, never in the diversity kernel._

| lineage | v5c member (slot) | dominated by | margin |
|---|---|---|---|
| DiffPep-linear | glp1r_06_ago (slot 6) | dpbv2_005 | id 60<= 60, cov 0.25<= 0.33, lcs 2<= 2, liab []⊆[] |

**Assessment (not an auto-adopt):** the swap(s) above are non-harmful strict improvements, but each must clear the cost of re-opening the byte-frozen, portal-parsed-20/20 v5c submission. A swap whose ONLY strict gain is a within-eligibility coverage delta (both members already pass the id<=30%/cov<0.5 novelty gate, and the upload portal has NO novelty score) is a marginal local-screen gain, not a portal- or prize-visible one; the convergent portfolio math puts same-lineage member reshuffling at <0.03 of P(>=1 hit) with sign-uncertain direction. Recommend KEEPING v5c frozen unless the owner wants the marginally-more-novel variant built (v5d), in which case it is a one-slot rebuild + full re-validation, with v5c retained as fallback.

## Band-marginal v5c members (audit transparency)

| slot | name | lineage | entropy | longest-run | A+G | liabilities |
|--:|---|---|--:|--:|--:|---|
| 20 | glp1r_20_bind | ECD | 2.78 | 7 | 0.44 | ['POLYRUN'] |
| 7 | glp1r_07_ago | DiffPep-linear | 2.81 | 2 | 0.07 | CLEAN |
| 13 | glp1r_13_ago | DiffPep-ss | 3.20 | 3 | 0.22 | CLEAN |
| 18 | glp1r_18_bind | ECD | 3.46 | 5 | 0.34 | CLEAN |
| 3 | glp1r_03_ago | EvoBind | 3.77 | 2 | 0.12 | ['instab'] |
| 4 | glp1r_04_ago | EvoBind | 3.95 | 2 | 0.12 | ['instab'] |

_Note: band-marginal v5c members are retained where they carry an irreplaceable rankable value (e.g. the most structurally-novel ECD) that no cleaner pool member matches — a strict-Pareto swap, not a band threshold, governs replacement._
