# GLP1R Track-3 — uniform 2-folder reach validation of v6 (2026-10-19)

**Trigger:** owner "dominate at all costs" on a free 8-GPU window. **Method:** the first *uniform* 2-folder
(Boltz-2 + Chai-1, single-seq, 1 seed each) cofold of the EXACT v6 twenty + 15 top non-v6 "reach" candidates
(DiffPepBuilder linear/disulfide, strongest existing minD_R299) + 8 native controls, all vs the 409-res 24–432
construct (scorer-compatible numbering), scored by the UNCHANGED `scripts/iface_score.py`
(N-term-in-7TM-vestibule, vestibule hits, R299 contact, iPAE). Inputs: `scratchpad/dominate/{foldset.csv,
boltz_scores.json, chai_scores.json}`; folds `runs/boltz_domfold3/`, `scratchpad/dominate/chai_out/`.

## Firewall (upheld)
Agonism is unprovable/unrankable in-silico; the cAMP/SEAP assay is the only verdict. Reach/vestibule geometry is
a weak **rankable prior** (necessary-ish, not sufficient), NOT an agonism score. This run ranks/validates reach;
it makes no activation claim.

## The decisive result — the metric does NOT separate agonists (empirical firewall)
Control calibration (robust = reaches R299 in BOTH folders): only the native **GLP1_7-36 scores AGREE:agonist**;
every other control — including potent agonists **exendin-4** (SPLIT, R299 0/1) and **liraglutide** (SPLIT
b=weak/c=agonist) — misses the 2-folder agonist bar, while the **antagonist exendin(9-39)** (AGREE:weak) and
agonist **oxyntomodulin** (rob 0) overlap the low end. So the "agonist-like" class does **not** discriminate
agonists from antagonists/weak binders. This is direct empirical confirmation that no in-silico re-ranking of
this portfolio for agonism is valid — exactly the standing firewall.

## v6 findings
- **4 robust 2-folder R299 reachers**: `glp1r_04` (SPLIT b=weak/c=agonist, iPAE 3.5/4.6 — **matches the
  liraglutide control exactly**), `glp1r_10`, `glp1r_21` (RFd3), `glp1r_22` (geometric reach both, but high iPAE).
  So v6's win-path does contain mechanistically-reasonable, independently-reproduced reader-engagers.
- The remaining agonism members are weaker on this proxy (single-folder reachers or AGREE:scramble), and the 3
  ECD binders score scramble-like on the vestibule metric **as expected** (they bind the extracellular domain,
  not the 7TM vestibule). Because the proxy cannot rank agonism (controls above), "weak on proxy" is NOT "bad
  bet"; v6 was deliberately selected for lineage/topology DIVERSITY (cell count), the only regime-robust lever.

## Swap check → NEGATIVE
No non-v6 candidate dominates any v6 member. The DiffPepBuilder "reachers" (`dpbss_*`, `dpbv2_*`) that aimed
<5 Å in DiffPepBuilder's own pose **do not reproduce reach under either independent folder** (vestibule 0,
iPAE 10–20) — the reachability wall holds. The two that reach R299 geometrically (`dpbv2_002/003`) are antag/
scramble class (no N-term insertion, high iPAE), not better than v6's reachers.

## Conclusion
**v6 (`398bfb30`, 20/20, validator PASS) is confirmed sound and unchanged.** All members fold; 4 agonism members
are robust 2-folder R299 reachers (one at liraglutide level); no swap is justified; and the controls empirically
re-prove the firewall. This hardens the evidence behind v6 without altering it. Caveats: single seed, single
(inactive 24–432) construct, confounded class — reach is a weak prior only. Upload remains USER-GATED.
