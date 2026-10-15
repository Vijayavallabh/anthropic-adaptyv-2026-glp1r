# BoltzGen GLP1R vestibule mini-binder pilot — gating + Pareto report

_Isolated DIVERSITY / method hedge. BoltzGen = distinct generative method + independent clean ticket. NOT a win-path/agonism claim: agonism is UNPROVABLE in-silico for class-B GLP1R; the wet-lab cAMP/CRE-SEAP assay is the only verdict. No co-fold / engagement / iPAE / ipTM is used or ranked here._

## Provenance
- Generator: BoltzGen (Apache-2.0 Anthropic wrapper + MIT upstream BoltzGen); no ESM-3/ESMC/Protenix/AF3 in the generation or sequence path (BoltzGen's own inverse-folding head).
- Target: 6X18 chain R active-state, vestibule window author 140-338 (RFd3 committed window); binding hotspots author 190,194,233,234,237 (= parsed positions 156,160,199,200,203, residue-name cross-checked).

## Counts
- Generated (sequences extracted): **30**
- Eligible (natural AA, len 10-80, incretin lcs<=3, not id-flagged): **28**
- Graft-free (incretin contiguous overlap lcs<=3): **29**
- Win-path band-passing (entropy>=2.81, longest-run<=2, (A+G)/len<=0.36, even non-vicinal Cys, graft lcs<=3, eligibility pass): **3**

## Band-passing candidates (adoption-eligible pool)

| name | len | n_cys | entropy | A+G | run | elig_id% | elig_cov | lcs | dev_flags |
|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| bg_glp1r_vestibule_bg_26 | 39 | 0 | 3.10 | 0.18 | 2 | 24 | 0.54 | 2 | hydrophobic |
| bg_glp1r_vestibule_bg_28 | 39 | 0 | 3.06 | 0.26 | 2 | 24 | 0.54 | 3 | lowcplx(L31%),hydrophobic,instab>40 |
| bg_glp1r_vestibule_bg_25 | 39 | 0 | 3.05 | 0.23 | 2 | 44 | 0.23 | 3 | hydrophobic,instab>40 |

## Strict-Pareto dominance vs v5c (reusing diversity_certificate.pareto_dominates verbatim)

_Gated axes (dominator no worse on every one, strictly better on >=1): sequence-novelty id, coverage, graft lcs, correct-aim minD_R299 prior (a v5c member with verified aim CANNOT be displaced by a candidate without it — so BoltzGen candidates can only reach the aim-free EvoBind/ECD members), n_cys (not increased), developability liability-set (subset). Aim is a not-worse GATE only, never a justification._

**VERDICT: NONE.** No band-passing BoltzGen candidate strictly Pareto-dominates any v5c member on all committed rankable axes. v5c stands unchanged; BoltzGen contributes a distinct generative method + independent clean ticket for the diversity hedge, not a submission swap.

