# GLP1R Challenge-3 — brutal stress test of the final submission → v5c confirmed

**Date:** 2026-10-16 · **Verdict:** `v5c_stands` (md5 `61c2d9e4d806b799a278efe7efb31063`, 20 designs,
byte-frozen). **Not one design is rejected; no slot changes.** This is the result of an explicitly brutal,
reject-everything-allowed audit — the conclusion that v5c is already at the achievable rankable-axis frontier
is an *earned* one, not complacency.

## Method

A 48-agent adversarial workflow (`glp1r-brutal-stress-test`, ultracode) attacked every v5c design and the
selection logic itself on six fronts, then independently refuted + firewall-checked every finding:

1. **Per-design teardown** (all 20 scored on every committed axis; keep / weak-keep / reject).
2. **Composition challenge** (the *fixed* 4/6/1/6/3 lineage budget + the 13/20 reader-aimer concentration).
3. **Pool re-optimization** (best-achievable 20 over the full pool incl. PepMLM + BoltzGen, lineage floating).
4. **Aggregation / solubility / synthesizability** (the "will this shot even survive to be tested" axis).
5. **Novelty hardening** (sequence + structure; folds the two v5c-specific slots the stale table missed).
6. **Firewall red-team + 2026 SOTA micro-sweep.**

66 findings; 33 survived as CONFIRMED + firewall-safe. **Every surviving per-slot finding concluded KEEP.**
The two strongest pro-change claims were REFUTED in verification (F2-05 "PepMLM is the most defensible
diversity lever" → a trade, not a net win; F3-04 mislabels a diversity ceiling as a developability floor).
One finding was struck as firewall-unsafe (F1-09).

## Independently reproduced (coordinator re-ran the committed scorers — not trusted on the agents' word)

| Claim | Independent result |
|---|---|
| Byte-frozen pick intact | md5 `61c2d9e4d806b799a278efe7efb31063` ✓ |
| Format / portal-parse | `validate_submission --track 3` → **PASS**, rows=20, errors=0, warnings=0 ✓ |
| Strict-Pareto swaps | committed certificate → **0 swaps**; TRIPWIRE passed ✓ |
| Developability | 17/20 clean; exactly 3 liabilities: slot 3 (instab), slot 4 (instab), slot 20 (POLYRUN) ✓ |
| Structural novelty (completed) | 17/20 novel (maxTM<0.5); 3/20 ECD helical bundles capped (TM 0.70–0.92) ✓ |
| **Clean-floor (decisive)** | **max developability-clean 20 assemblable from ALL pools = 17 → a fully-clean 20 is mathematically impossible → forced min 3 liabilities → v5c sits AT the floor** ✓ |

### The clean-floor result (why a rebuild cannot win on developability)

Across every clean pool, counting band-passing AND liability-clean candidates, under the 35%-per-generator
diversity cap (≤7 of 20 from one generator):

| generator | band-pass ∧ clean | capped @7 |
|---|--:|--:|
| PepGLAD | 30 | 7 |
| DiffPepBuilder (linear+ss) | 27 | 7 |
| EvoBind | 2 | 2 |
| ECD | 1 | 1 |
| PepMLM | 0 | 0 |
| BoltzGen | 0 | 0 |
| **max clean assemblable** | | **17** |

17 < 20 ⇒ three slots *must* carry a liability. v5c carries exactly three (slots 3, 4, 20). A fully-clean 20
only exists if you drop the diversity cap and take ~10+10 from two generators — which collapses the portfolio
to 2 lineages (cousins), destroying the diversity that is the higher-value rankable axis for a wet-lab lottery.

## The one genuine decision point (surfaced for the owner; NOT recommended)

**F2-07** — *iff* the owner overrides and re-opens the byte-frozen submission, the single most-defensible
marginal move is **EvoBind 4 / DiffPepBuilder 6 / PepGLAD 4 / ECD 3 / PepMLM 3** (trim the 3 most
feature-redundant reader-aimer cousins — slots 8/11/17 — and add 3 PepMLM), which raises distinct generative
priors 4→5 and whole-portfolio min-pair dispersion 1.88→~2.22.

**Declined**, because it is a *trade*, not a strict improvement: it **worsens developability** (liabilities
3→6; 0 of 21 PepMLM band-passers are liability-clean, reproduced), it is **not a strict Pareto improvement**,
its stronger justification (F2-05) was **refuted**, PepMLM shares the ESM-2 base with DiffPepBuilder (so it is
a less-orthogonal prior than it appears), and — like every in-silico move — it buys **zero** provable agonism
odds. Keeping the Pareto-efficient, developability-floor-optimal v5c dominates this trade on the rankable axes.

Also confirmed-but-not-adopted: **F1-21/F2-04** — the 3 ECDs (slots 18-20) are the portfolio's *entire*
structural-novelty liability (TM 0.70-0.92, 3/4-cap) and hold the worst-developability member (slot 20:
POLYRUN, 7× Ala), **but** they are the top-3 whole-portfolio diversity contributors and the only large-scaffold
regime (removing them craters log-det by −6.77), there is **no clean same-lineage ECD replacement** (ECD
clean pool = 1), and slot 20 is the *most* structurally-novel ECD — so dropping any worsens novelty/diversity.
**Keep all 3.**

## Firewall attestation

No change is proposed, so no change rests on a barred signal. The decision to keep all 20 rests only on
rankable/verifiable axes: format compliance, sequence novelty (0/20 exceed 30% id; max global id 23.1%; max
contiguous incretin overlap 3; 0 grafts), structural novelty (FoldSeek maxTM), developability (the reproduced
3-liability forced floor), de-novo/provenance cleanliness (no AF3/Protenix-v2/ESM-3/ESMC in any submitted
design), generative-prior diversity (4 priors / 5 lineage cells), and portfolio diversity. `minD_R299` entered
**only** as the committed not-worse Pareto gate, never as a ranker — and F6-09 (verified) shows all six
DiffPep-linear "R299-aimers" miss the 4.5 Å reach gate, so reachability did **no** selection work. No co-fold /
iPAE / ipTM / engagement / vestibule-contact / pLDDT-as-binding signal touched this verdict.

## Honest ceiling

No in-silico result proves *or* ranks agonism of class-B GLP1R; the wet-lab cAMP/CRE-SEAP assay is the only
verdict on activation. This stress test established that v5c is format-compliant, Pareto-efficient on every
rankable axis, sequence-novelty-locked, developability-optimal at the mathematically-forced clean floor,
provenance-clean, and maximally diverse within its budget. It did **not** and **cannot** establish anything
about binding, affinity, reachability or relative agonism — those are unrankable in-silico and were barred.
"The best 20 that dominate the challenge" has been achieved on every axis that *can* be ranked or verified;
the activation outcome belongs to the assay alone, and no further in-silico work — including a full rebuild —
can improve those odds. **Ship the frozen set.** Upload remains USER-GATED.
