# GLP1R mechanism-coverage moonshot → candidate v6 (owner decision)

**Date:** 2026-10-16 · Owner-authorized "full push (A+B+C+D)". Result: the flagship track (A, RFd3
message-address) produced the **first designs that fill the portfolio's one empty approach-geometry bin**,
built into a validated candidate **v6**. v5c stays the frozen, brutal-tested fallback. Upload USER-GATED.

## What was run (firewall-clean: coverage/diversity axes only; agonism remains unprovable/unrankable in-silico)

- **D (SOTA sweep) → no-go.** No 2025–26 license-clean generator natively makes this design class; 9 methods
  verified + rejected first-hand. No install warranted.
- **B (mechanism-coverage axis) → built.** A committed-style scorer over a 4-approach × 2-size lattice. v5c
  covers 3/4 approach bins; the **reader-proximal (<4.5 Å to R299) bin is EMPTY**. Admission rule: a design
  justifies a slot only by filling an empty bin, via an independent ≥2-fold geometric filter (never a rank,
  never agonism).
- **A (RFd3 message-address) → 3 bin-fillers.** 384 backbones (two variants, GPUs 4–7, foreign job isolated on
  0–3) → 48 MPNN'd → 384 sequences → band-pass 187 → **developability-clean 49** (most killed by hydrophobic
  GRAVY at the vestibule interface) → eligible/novel → **31 clean+novel survivors** → 20 folded (diversity-
  capped) → **3 reproduce consensus <4.5 Å to R299 under independent Boltz AND Chai folding of the designed
  sequence**. The RFd3 placement reach (378/384 <4.5 Å) is **circular** (RFd3 was told to orient at R299) and is
  NOT reported as a result; 17/20 fail the non-circular consensus test = the expected reachability wall (valid
  negative). The 3 that pass are lead-verified clean by the committed scorers.
- **C (2-disulfide "grenade") → queued, GPU-blocked.** Recipe prepared + config-dry-run-passed; the foreign job
  reclaimed all 8 GPUs, so a bounded watcher will launch it when a lane frees.

## The 3 coverage-fillers (lead-verified; all band-pass, dev-CLEAN, 0-Cys, eligible, natural-AA, single_chain)

| internal | len | id% | cov | lcs | Boltz minD_R299 | Chai minD_R299 | consensus |
|---|--:|--:|--:|--:|--:|--:|---|
| des_0039_m7 | 37 | 40 | 0.27 | 2 | 2.31 | 3.84 | both <4.5 |
| des_0047_m6 | 45 | 57 | 0.16 | 2 | 2.98 | 4.18 | both <4.5 |
| des_0039_m2 | 37 | 67 | 0.16 | 3 | 2.92 | 3.80 | both <4.5 (shares backbone w/ m7) |

**Honest caveats (why this is a coverage gain, not an activation claim):** (1) interface confidence is
weak/mixed (iPAE often high, iptm mixed) — the geometry reproduces across folders, the binding confidence does
not uniformly; (2) both folders are trained on natural incretin:GLP1R complexes, so a shared co-fold
memorization confound cannot be excluded — 2-fold agreement is a necessary condition, not proof; (3) filling
the bin does not move provable agonism odds — the cAMP/SEAP assay remains the only verdict.

## Candidate v6 (built + validated; NOT adopted — owner's call)

`submissions/glp1r_track3_v6.csv`, md5 `398bfb3006464811e8ce9ab57afb4dad`, 20 rows, validator **PASS** (0/0).
Built programmatically from v5c (18 retained rows byte-identical); byte-diff = drop slots 11 (`pglad_034`) + 17
(`pglad_001`) — the two most-redundant outer-surface PepGLAD per the F2-07 analysis — and append the two
distinct-backbone reader-proximal designs `glp1r_21_ago` (= des_0039_m7) + `glp1r_22_ago` (= des_0047_m6).

- **Mechanism coverage: 3/4 → 4/4 approach bins** (the reader-proximal bin now holds 2 members).
- **Generative priors: 4 → 5** (adds RFd3 message-address).
- **Developability: 17/20 clean**, same forced 3-liability floor (slots 3/4 instab, slot 20 polyrun; the two
  additions are CLEAN). PepGLAD 6 → 4 (still well-represented); all other diversity preserved.
- **Structural novelty (CPU ESMFold → FoldSeek vs local PDB DB; red-team audit 2026-10-17):** on the portal
  structural-novelty axis (distinct from the approach-bin *coverage* 3/4→4/4 above), `glp1r_22_ago` = **4-of-4**
  (0 PDB hits, no fold template) and `glp1r_21_ago` = **3-of-4** (top template 7m13, alnTM 0.85 / qTM 0.73 —
  same tier as the ECD helical-bundle hedges; still ≥3/4, passes). Previously unmeasured for the two v6
  additions; now recorded in `data/candidates/v6_filler_struct_novelty.csv`.

## The decision (v5c vs v6)

- **v5c** (`61c2d9e4`): brutal-tested, Pareto-optimal, byte-frozen, portal-parsed 20/20; every member
  validated-clean or at the forced floor. Its one gap: no reader-proximal design (mechanism-monoculture).
- **v6** (`398bfb30`): adds the one mechanistically-relevant geometry the portfolio lacked + a 5th prior, at the
  cost of 2 redundant members and accepting weak interface confidence + the co-fold confound on the additions.
  It is a **coverage/robustness TRADE, not a strict Pareto win**.

Both are valid 20-design single_chain submissions. v5c remains the frozen fallback regardless. If Track-C or an
optional Wave-B yields a higher-confidence filler before upload, v6 can be rebuilt from the better candidate.

## Track-C resolution (2026-10-16) → NEGATIVE; v6 unchanged

The bounded watcher caught a GPU window and ran one DiffPepBuilder L30–40 lane (the 2-SS zone) + the prepared
post-filter. The post-filter flagged 3 "grenade" candidates (`dpbss2_004/007/009`) as clean + band + eligible
with `n_ss_realized=2`. **First-hand verification refutes the double-staple premise:**

- The post-filter's `n_ss_realized`/`staple_spans` are a **naive sequential Cys-pairing** `(c0,c1),(c2,c3)` — it
  never read disulfide connectivity. Measuring actual Sγ–Sγ distances in the built structures shows all three
  "grenades" realize only **one** real disulfide (Sγ–Sγ ≈ 2.0 Å), leaving **2 unpaired free-thiol cysteines** each
  — a developability liability the sequence-level scorer cannot see, and *worse* than the existing clean single-SS
  member `dpbss_010` (2 Cys, 1 SS, no spare thiols), whose topology class they merely duplicate.
- A full scan of all 42 built structures: only **2** realize two real disulfides, and **both fail the committed
  gates** (band / eligibility; one carries a vicinal `ICC` pair). So **no clean, eligible, band-passing
  double-stapled design exists** — the 2-SS realization rate is ≈ 0, exactly as this track's low-yield prediction.

No independent 2-fold fold was warranted (the non-circular test was contingent on a clean, distinct double-staple
existing; none does). **Track-C yields no v7.** All owner-approved moonshot tracks (A / B / C / D) are now
resolved; v6 stands as the owner-adopted pick, v5c the frozen fallback, upload USER-GATED. Verification artifacts:
`scratchpad/moonshot/track-c-disulfide/{verify_grenades.py, stage2_dpbss_grenade.csv, watcher_C.log}`.

## Red-team + novelty audit (2026-10-17) → v6 stands

An adversarial workflow tasked only with breaking the "frontier exhausted / keep v6" conclusion returned **no
win-path lever.** Its own verifier refuted the one developability lever (the deamidation/isomerization motifs it
flagged are *surfaced-only* fields in `scripts/stress_liab.py`, not gated by `n_liab`). The sole real finding was
that the two v6 additions' **structural** novelty was unmeasured — now closed (see the "Structural novelty"
bullet above; `glp1r_22_ago` 4-of-4, `glp1r_21_ago` 3-of-4, within the ≥3/4 gate, no forced swap).

**Optional Wave-B (user-approved, idle-GPU-gated):** RFd3 motif-extension off the two proven reacher backbones
(des_0039/des_0047), armed as a no-clobber idle-window watcher. As of 2026-10-17 the DGX's 8 GPUs are held by a
foreign job (94% util); the watcher waits and never clobbers it. Wave-B is pure optional upside — it cannot change
v6 without the owner's explicit swap call. v6 (`398bfb30`) and the v5c fallback (`61c2d9e4`) are unchanged.
