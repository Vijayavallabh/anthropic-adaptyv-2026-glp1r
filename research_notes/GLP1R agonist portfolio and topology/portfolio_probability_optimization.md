# GLP1R agonist portfolio: probability optimization of 20 unrankable shots

**Scope.** A quantitative decision: how to allocate the 20 Track-3 submission slots to **maximize
P(≥1 functional cAMP/CRE-SEAP agonist)** under the hard **firewall** that individual agonism cannot be
ranked or proven in-silico for a class-B GPCR. This is a *diversification-of-unrankable-shots* problem,
**not** an agonism-prediction problem. Nothing here proves, predicts, or ranks agonism; the wet-lab
functional assay is the only verdict. Analysis date 2026-10-15; optimizes the current submission
`submissions/glp1r_track3_v5b.csv` (md5 `b10571b40613d32ad36cbc9859890df7`).

Tags used: **[FACT]** = sourced external fact with citation · **[math]** = derivation · **[HYP]** =
assumed prior (illustrative; agonism is unrankable so all per-design/lineage probabilities are
assumptions, not measurements) · **[in-silico]** = computational observation that the firewall bars from
ranking agonism.

Reproducible numbers: `scratchpad/portfolio_calc.py` (all tables below are its output).

---

## 0. Setup, notation, and what the firewall does/does not allow

**The portfolio (v5b), confirmed from the CSVs.** 20 designs across 4 generator *lineages* + a topology split:

| lineage ℓ | count n_ℓ | in-silico aim [in-silico] | role |
|---|---|---|---|
| EvoBind (EB) | 4 | R299-aimed, reach ~5 Å; the only de-novo precedent family (cyclic) | win-path |
| DiffPepBuilder (DPB) | 6 | R299-aimed, reach 4.73–5.62 Å | win-path |
| PepGLAD (PG) | 7 | sit ~26–33 Å from R299 = **no verified aim**; novelty/diversity | win-path |
| ECD mini-proteins | 3 | validated **binders**, antagonist-leaning, ≈0 agonism prob | binding hedge |

So the current mix is **4/6/7/3** = **17 win-path + 3 ECD hedge**; lengths 13–74; only **2/20
disulfide-constrained**, **15/17 win-path linear**; max generator share 35%.
(Source: `glp1r_track3_v5b.csv`, `glp1r_track3_v5b_eligibility.csv`,
`reports/GLP1R v5 brutal stress test and best20 rebuild.md`.)

**[FACT] The firewall is well-founded.** The challenge win condition is **functional activation**
(GLP1R→Gαs→cAMP→CRE-SEAP), not binding; "a design must be an agonist, confirmed in a functional assay,
to count," and binders that do not activate do not count
([GLP1R Challenge-3 page](https://proteinbase.com/competitions/anthropic-adaptyv-2026/challenges/glp1r)).
Selection is explicitly **multi-metric** and "will not rely on a single in silico metric"
([ibid.](https://proteinbase.com/competitions/anthropic-adaptyv-2026/challenges/glp1r)). Project
ground-truth (3 prior rounds + empirical tests): for class-B GPCRs agonism is **unprovable and
unrankable** by any co-fold / iPAE / ipTM / engagement score; the only de-novo GPCR-agonism precedent
is **EvoBind cyclic peptides** (best 18-mer EC50 ≈ 32 nM, n=3), and Baker's 2026 de-novo GLP1R binders
were **antagonists** (reachability wall: folded de-novo peptides reach ~4.7–5.6 Å from R299 and perch on
the rim). [in-silico] aim numbers (5 Å vs 29 Å) are therefore priors on *lineage viability only* — the
firewall forbids using them to rank individual designs.

**[math] Consequence for the optimizer.** Because we may not rank designs by p_i, the decision collapses
to: *how many distinct, weakly-correlated mechanism families do we buy, and how many shots in each?* The
objective is P(≥1), and the free variables are the **lineage counts** {n_ℓ} and the **number of distinct
lineages L**. Treat each p_i as unknown, bounded, and coarsely groupable by lineage.

---

## 1. Formal model: P(≥1), the correlation penalty, and the allocation numbers

### 1a. [math] Independence baseline — and why it makes allocation almost irrelevant

With independent per-design success probabilities p_i,

&nbsp;&nbsp;&nbsp;&nbsp;**P(≥1) = 1 − Π_i (1 − p_i) ≈ 1 − exp(−Σ_i p_i) = 1 − e^(−Λ)**, &nbsp; Λ ≡ Σ_i p_i = E[# hits].

The approximation uses 1−p ≈ e^(−p) for small p. **Under independence, P(≥1) depends only on the sum Λ**,
not on how the shots are distributed. So if every design had the same p regardless of lineage, *allocation
would not matter at all.* **Allocation matters only through two channels: (i) correlation structure, and
(ii) lineage-dependent means** (e.g., ECD having a much smaller agonism p than win-path). Channel (i) is
the dominant one here, and it is what the firewall's "shared generator failure mode" is about.

### 1b. [math][HYP] The shared-mode (latent lineage-viability) model

Positive intra-lineage correlation arises because designs from one generator share a failure mode
(same inductive bias, same binding sub-site, same topology, same "does this mechanism class even reach
the vestibule?"). Model it with a **latent lineage-viability** Bernoulli:

- For lineage ℓ: **Z_ℓ ~ Bernoulli(q_ℓ)** — "generator/mechanism ℓ is viable *at all* against this target."
- Given **Z_ℓ = 1**, each design in ℓ independently succeeds with prob **r_ℓ**; given **Z_ℓ = 0**, *all*
  designs in ℓ fail (p = 0). This encodes the shared failure mode exactly: if the whole mechanism is wrong
  (e.g., "all PepGLAD sit 29 Å from R299 and cannot deliver the message," or "folded peptides perch on the
  rim → antagonist"), the entire lineage dies together.

Then, per design, **marginal p_ℓ = q_ℓ·r_ℓ**, and for a lineage of n_ℓ designs:

&nbsp;&nbsp;&nbsp;&nbsp;**P(≥1 hit in lineage ℓ) = q_ℓ · [1 − (1 − r_ℓ)^(n_ℓ)]**  &nbsp; — *the master per-lineage term.*

This is **bounded above by q_ℓ no matter how many designs you add**: piling shots into one lineage can
never beat the probability that the lineage is viable at all. That cap is the mathematical statement of
"correlated failure limits the return to concentration."

Assuming near-zero cross-lineage correlation (distinct mechanisms fail for independent reasons — the
project's stated prior), lineage viabilities are independent, so:

&nbsp;&nbsp;&nbsp;&nbsp;**P(≥1 agonist) = 1 − Π_ℓ [ 1 − q_ℓ (1 − (1 − r_ℓ)^(n_ℓ)) ]**  &nbsp; — *the master formula.*

Sanity checks: q_ℓ = 1 ⇒ term = 1−(1−r_ℓ)^(n_ℓ) (independence recovered); r_ℓ = 1 ⇒ term = q_ℓ (one
viable design suffices, extra designs add nothing).

### 1c. [math][FACT] The explicit correlation/variance argument

Let X_i, X_j be success indicators of two designs in the same lineage ℓ. Under the shared-mode model:

- E[X_i] = p_ℓ = q_ℓ r_ℓ ; E[X_i X_j] = P(both) = q_ℓ r_ℓ² (need Z_ℓ=1, then both succeed).
- **Cov(X_i, X_j) = q_ℓ r_ℓ²(1 − q_ℓ) ≥ 0** (zero iff q_ℓ=1); cross-lineage Cov = 0.
- Var(X_i) = p_ℓ(1−p_ℓ). Hence the **intra-lineage correlation**
  **ρ_ℓ = r_ℓ(1 − q_ℓ) / (1 − q_ℓ r_ℓ)**. ρ_ℓ = 0 iff q_ℓ = 1 (no shared mode); ρ_ℓ ↑ as q_ℓ ↓.

Note the modeling insight: **"moderate ρ within lineage" corresponds to LOW lineage-viability q_ℓ and
moderate r_ℓ** — i.e., the dominant uncertainty is at the *mechanism* level ("does this class work at
all?"), not the individual-design level. That is exactly the firewall's claim. (E.g., q=0.15, r=0.30 →
ρ≈0.27; q=0.08, r=0.40 → ρ≈0.38.)

**Why positive correlation strictly reduces P(≥1) at fixed marginals.** Let S = Σ_i X_i = # hits.
E[S] = Λ is **invariant** to correlation, but Var(S) = Σ Var(X_i) + Σ_{i≠j} Cov(X_i,X_j) is **inflated**
by positive covariance. At fixed mean, extra variance pushes probability mass toward the tails — toward
S = 0 (all fail) and toward large S (redundant multi-hits) — raising P(S=0) and lowering P(S≥1). The
rigorous statement: the shared-mode indicators are **associated** random variables, and for associated
variables in [0,1], **P(≥1 success) = E[∐X_i] ≤ ∐E[X_i] = 1 − Π(1 − p_i)** — the independence value is an
**upper bound**; positive dependence can only reduce P(≥1).
**[FACT]** Association and this at-least-one inequality: Esary, Proschan & Walkup, "Association of Random
Variables, with Applications," *Ann. Math. Stat.* 38(5):1466–1474, 1967
([statement restated in Univ. Oslo STK3405 notes](https://www.uio.no/studier/emner/matnat/math/STK3405/h20/forelesningsnotater/week40-part2.pdf));
the same monotonicity (system failure probability ↑ with positive dependence) is standard in
correlated parallel-system reliability
([AAU structural-reliability ch. 12](https://vbn.aau.dk/ws/files/234837364/Chapter_12_Reliability_of_Structural_Systems_with_Correlated_elements.pdf)).

**Monotone in the correlation, with an explicit range.** Fix the marginal p = q·r and vary q from p
(perfect correlation, r=1) to 1 (independence, r=p). With f(q) = q[1 − (1 − p/q)^n],

&nbsp;&nbsp;&nbsp;&nbsp;df/dq = 1 − q^(−n)(q−p)^(n−1)[q + p(n−1)] > 0 for n ≥ 2, p small,

so P(≥1 in lineage) **increases monotonically as correlation falls**, between the two extremes:

&nbsp;&nbsp;&nbsp;&nbsp;perfect correlation (q=p): P = **p** (one effective shot, n is useless) &nbsp;≤&nbsp;
independence (q=1): P = **1 − (1 − p)^n** (n effective shots).

So a lineage's **effective number of independent shots** ranges from **1** (fully correlated) to **n**
(independent); positive ρ eats the difference. Concentrating many shots into one correlated lineage buys
far fewer effective shots than the headcount suggests.

### 1d. [math][HYP] Numbers for the candidate allocations

Master formula evaluated for the four candidate allocations, under three illustrative prior regimes
(all **[HYP]**; agonism is unrankable, so these are not measurements). "P≥1 indep" is the independence
upper bound at the same marginals; "penalty" = fraction of that upper bound lost to intra-lineage
correlation. Win-path lineages share (q,r) within a regime; ECD uses q≈0.02 (≈0 agonism); the
max-spread adds 3 hypothetical equally-clean lineages.

**Regime AGNOSTIC** (can't rank → all win-path equal; q=0.15, r=0.30, ρ≈0.27):

| allocation | **P(≥1 agonist)** | P≥1 indep | corr. penalty | E[hits] |
|---|---|---|---|---|
| **A1 current 4/6/7/3** | **0.346** | 0.551 | 37% | 0.78 |
| A2 even 5/5/5/5 | 0.341 | 0.514 | 34% | 0.71 |
| A3 concentrate 10/4/3/3 | 0.327 | 0.551 | 41% | 0.78 |
| **A4 max-spread (7 lineages)** | **0.469** | 0.569 | 18% | 0.82 |

**Regime HIGH-CORR** (q=0.08, r=0.40, ρ≈0.38):

| allocation | **P(≥1 agonist)** | P≥1 indep | corr. penalty | E[hits] |
|---|---|---|---|---|
| A1 current 4/6/7/3 | 0.217 | 0.435 | 50% | 0.56 |
| A2 even 5/5/5/5 | 0.216 | 0.404 | 46% | 0.51 |
| A3 concentrate 10/4/3/3 | 0.207 | 0.435 | 52% | 0.56 |
| **A4 max-spread (7 lineages)** | **0.329** | 0.450 | 27% | 0.59 |

**Regime TILTED [in-silico]** (aim prior: EB q=0.25, DPB q=0.22, PG q=0.06, extra L q=0.20; r=0.30):

| allocation | **P(≥1 agonist)** | P≥1 indep | corr. penalty | E[hits] |
|---|---|---|---|---|
| A1 current 4/6/7/3 | 0.391 | 0.580 | 33% | 0.84 |
| A2 even 5/5/5/5 | 0.396 | 0.573 | 31% | 0.83 |
| A3 concentrate 10/4/3/3 | **0.402** | 0.675 | 40% | 1.09 |
| **A4 max-spread (7 lineages)** | **0.555** | 0.654 | 15% | 1.03 |

**What the numbers say:**

1. **Re-splitting within the same 4 lineages barely moves P(≥1).** A1 vs A2 vs A3 differ by **< 0.03** and
   the ordering flips with the (unknowable) regime. **The 4/6/7/3 split is not a high-value decision
   variable.**
2. **The correlation penalty is large and grows with concentration.** It is 34–52% of the independence
   value, and A3 (concentrate) always carries the **highest** penalty (40–52%) because it piles the most
   shots into a single correlated cluster. The controlled comparison is **A1 vs A3**: they have *identical*
   marginals and *identical* independence value (0.551 agnostic), yet A1 (spread) = 0.346 beats A3
   (concentrate) = 0.327 **purely from the correlation term**. Concentration wins *only* in the TILTED
   regime, and only because it bets on an **[in-silico] aim prior the firewall forbids us to trust for
   ranking.**
3. **The one lever that moves P(≥1) robustly is the NUMBER OF DISTINCT LINEAGES.** A4 (7 lineages) beats
   every 4-lineage allocation in **every** regime, by **+0.11 to +0.16** — a far larger effect than any
   within-4-lineage reshuffle. Its correlation penalty is also the lowest (15–27%), because spreading
   minimizes redundant intra-lineage covariance.

### 1e. [math] Submodularity: why a new lineage beats a deeper one

Marginal gain of the (n+1)-th design **within** lineage ℓ:

&nbsp;&nbsp;&nbsp;&nbsp;**ΔP_ℓ(n) = q_ℓ r_ℓ (1 − r_ℓ)^n** — decreasing **geometrically** in n (diminishing returns),
and the lineage total is capped at q_ℓ.

Marginal gain of the **first** design in a fresh lineage ℓ′: **q_{ℓ′} r_{ℓ′} = p_{ℓ′}** — **undiscounted.**
At q=0.15, r=0.30 (agnostic):

| design # within a lineage | marginal ΔP | first shot in a NEW lineage |
|---|---|---|
| 1st | +0.0450 | +0.0450 |
| 4th | +0.0154 | +0.0450 |
| 6th | +0.0076 | +0.0450 |
| 7th | **+0.0053** | **+0.0450** |

So PepGLAD's **7th** design is worth **~8× less** to P(≥1) than the first design of a new mechanism family.
This is a textbook **submodular / diminishing-returns** structure, which is precisely what makes greedy
diversification near-optimal (§3a) and tells us where the slack is: the deep end of the most-saturated
lineage (PepGLAD at 7, which also has *no verified aim*).

---

## 2. Is the 17-win / 3-ECD split defensible for the agonism objective?

**[math] The 3 ECD contribute ≈0 to P(≥1 agonist).** At q_ECD ≈ 0.02 their whole-lineage term is
≤ 0.02. The sharper question is the **opportunity cost** of spending 3/20 slots on ~0-agonism designs.
Two reallocations, computed per regime:

| regime | current (17win+3ECD) | → deepen win lineages (6/7/7, no ECD) | → **open a 5th win lineage** (5/5/5 + L5·5) |
|---|---|---|---|
| AGNOSTIC | 0.346 | 0.355 (**+0.009**) | 0.413 (**+0.068**) |
| HIGH-CORR | 0.217 | 0.214 (**−0.002**) | 0.264 (**+0.047**) |
| LOW-CORR | 0.538 | 0.582 (+0.044) | 0.600 (+0.062) |
| TILTED [in-silico] | 0.391 | 0.412 (+0.021) | 0.488 (**+0.096**) |

**Reading.** The answer is **conditional on what the freed slots buy:**

- **vs. deepening the existing 3 win lineages:** the agonism gain is **tiny (+0.01, even −0.002)** — because
  those lineages are already near their q_ℓ cap at n=6–7 (§1e). On this comparison the 3 ECD are **not
  meaningfully "wasted"**: three more cousin-peptides in already-saturated lineages are worth ~1 point.
- **vs. opening a genuinely new mechanism lineage:** the agonism opportunity cost is **~5–10 points of
  P(≥1)** (+0.047 to +0.096). *This* is the real cost of the hedge.

**Does the multi-metric payoff cover it?** The 3 ECD are the **only designs with validated binding**
(af2ig pae 6.22; `reports/GLP1R v5 brutal stress test`), and the challenge **ranks on affinity AND
activation** and will **not rely on a single metric**
([Challenge-3 page](https://proteinbase.com/competitions/anthropic-adaptyv-2026/challenges/glp1r)). So the
ECD buy, on the *separately judged* axes: (i) the **binding-assay gate** — a design must bind to even
reach the functional readout, and the peptides' binding is unvalidated/weak; (ii) **method novelty**
(RFdiffusion+LigandMPNN+af2ig = a 4th generator); (iii) **structural novelty** (one TM 0.705 ECD) and
clean developability; (iv) **insurance** against the tail where *no* peptide binds at all (portfolio still
shows validated binders → partial credit on the affinity objective).

**[math] Verdict on the split.** The 3-ECD hedge is **defensible iff** (a) no clean, novel, validated
*5th win-path mechanism* can be fielded by the deadline, in which case the agonism cost of the hedge is
only the ~1-point "deepen" comparison and is comfortably covered by the binding-objective + method/structural-novelty
payoff; **and not fully defensible iff** a clean 5th lineage *is* available, in which case 2 of the 3 ECD
sit on a **~5–10-point P(≥1 agonist) opportunity cost**. The resolution is to **keep 1 ECD** (the
best-validated binder — captures the binding objective and method-novelty at near-zero agonism cost) and
**convert 2 ECD into a 5th mechanism lineage** if one exists. Keeping all 3 is a bet that the judged
affinity/novelty axes are worth ≥ ~0.05–0.10 of agonism probability — plausible given the explicit
multi-metric rubric, but it should be a *chosen* trade, not a default.

---

## 3. The decision mapped to five formal frameworks

Setup for all five: we get **one batch of 20**, evaluated **jointly on one 384-well plate**, with **no
feedback between designs** and — critically — **no in-silico signal to rank designs by agonism**
(the firewall). This specific structure (one-shot batch, no exploitable signal) is what each framework
keys on.

### (a) Max-coverage / submodular facility-location — *diversity as coverage of hypothesis space*

**[math]** Let the ground set be the **mechanism cells** by which a design could conceivably agonize
(which sub-site near R299 it engages × topology × generator inductive bias). Under the shared-mode model,
**P(≥1 agonist) is a monotone submodular set function** of the chosen designs (it is a coverage function:
you win if ≥1 chosen design lands in ≥1 viable cell; adding a design has diminishing returns, §1e).
**[FACT]** For monotone submodular maximization under a cardinality constraint (|S| ≤ 20), the **greedy**
algorithm achieves **≥ (1 − 1/e) ≈ 0.63** of the optimum, and this is **tight** for max-coverage
(Nemhauser, Wolsey & Fisher, *Math. Programming* 14:265–294, 1978
([result restated, UW EE596b notes](https://people.ece.uw.edu/bilmes/classes/ee596b_spring_2016/lecture15.pdf));
hardness/tightness: Feige, *JACM* 1998). **Prescribes:** greedily add the design that covers the *most
currently-uncovered* mechanism cell → **spread across distinct cells; never deepen a covered cell while an
uncovered one remains.** Directly favors raising the distinct-lineage count L and populating the empty
topology cell (cyclic).

### (b) Markowitz diversification — *unknown, correlated returns*

**[FACT]** Portfolio variance is a double sum over pairwise covariances, Var = Σ_i Σ_j w_i w_j σ_ij; for
two assets Var = w₁²σ₁² + w₂²σ₂² + 2w₁w₂σ₁₂, so risk is driven by **covariances, not just individual
variances**, and diversification works by combining **low/negatively-correlated** holdings (Markowitz,
"Portfolio Selection," *J. Finance* 7(1):77–91, 1952
([text](https://www.math.hkust.edu.hk/~maykwok/courses/ma362/07F/markowitz_JF.pdf))). **[math]** Map each
design's agonism outcome to a "return" with unknown mean and covariance. The firewall removes the *means*
(we cannot rank expected returns), so the mean-variance program **degenerates to the minimum-variance
portfolio** — and minimizing portfolio variance = minimizing total pairwise covariance = **equal-ish
weight across weakly-correlated lineages, with a cap on any single correlated cluster** (the positive
intra-lineage σ_ij is the dominant risk term; overweighting a lineage maximizes exactly the term you want
to minimize). **Prescribes:** spread to the min-variance/robust vertex; **cap cousins; do not overweight
any one generator.** (Formally this is the robust/ambiguity-averse case: unknown means + unknown q_ℓ →
max-min favors spreading, since a concentrated bet on a lineage whose q_ℓ turns out 0 yields P = 0.)

### (c) Bayesian experimental design / batch active learning — *one-shot batch*

**[FACT]** Naive top-k batch selection acquires **redundant, near-duplicate** points and can **underperform
even random** acquisition; scoring the **batch jointly** (a submodular mutual-information objective, greedy
with the 1−1/e guarantee) restores **diversity** and beats top-k (Kirsch, van Amersfoort & Gal,
"BatchBALD," *NeurIPS* 2019
([paper](https://proceedings.neurips.cc/paper/2019/hash/95323660ed2124450caaac2c46b5ed90-Abstract.html))).
Classical basis: maximize expected information gain of the design (Lindley, *Ann. Math. Stat.* 1956;
Chaloner & Verdinelli, *Stat. Sci.* 1995). **[math]** We have exactly BatchBALD's setting — one batch, no
intermediate feedback — so the right objective is the **joint** value of the 20, which rewards spread and
penalizes redundancy. **Prescribes:** choose the 20 jointly for diversity; **7 near-cousin PepGLAD is the
"near-duplicate" failure mode BatchBALD warns against** — a marginal-value sink (§1e).

### (d) Best-arm identification bandit — *a single pull per arm*

**[FACT]** In **fixed-budget** best-arm identification, the probability of selecting the wrong arm is
governed by the per-arm budget relative to the inter-arm gaps; with a *tiny* budget the problem is
dominated by pure exploration (Audibert, Bubeck & Munos, COLT 2010; Bubeck, Munos & Stoltz, 2009;
Lattimore & Szepesvári, *Bandit Algorithms*, 2020
([survey context](https://ar5iv.labs.arxiv.org/html/1609.02606))). **[math]** Arms = mechanism lineages;
a "pull" = testing one design; our budget is **≈ 1 pull per arm**, and — uniquely — we have **no in-silico
signal to rank outcomes even after pulling** (the firewall). With ~1 pull/arm there is **zero statistical
power to identify the best arm**: you cannot *exploit*, because exploitation requires a signal we are
forbidden to have. The optimal policy in the no-signal / pure-exploration limit is **uniform allocation
over arms** (round-robin coverage). **Prescribes:** **spread pulls uniformly across arms; concentrating
pulls is premature exploitation with no evidence** — the firewall is exactly "no evidence."

### (e) Determinantal point processes / optimal transport — *maximize portfolio diversity*

**[FACT]** A **k-DPP** selects a fixed-size subset with probability ∝ det of a quality×similarity kernel;
the determinant is a **volume**, maximized when items are simultaneously high-quality and **mutually
dissimilar**, giving a principled quality-vs-diversity trade-off and tractable selection (Kulesza & Taskar,
*Determinantal Point Processes for Machine Learning*, Found. & Trends ML 5(2–3), 2012; k-DPP: ICML 2011
([k-DPP paper](https://icml.cc/imls/conferences/2011/papers/611_icmlpaper.pdf))). **[math]** Under the
firewall the **quality term is flat** (agonism unrankable), so the k-DPP **reduces to a pure
volume/diversity sampler** = pick the 20 most mutually-dissimilar designs. Equivalently (optimal-transport
view), spread the 20 to minimize the Wasserstein distance between the portfolio's empirical distribution
over mechanism-space and a uniform target over plausibly-viable mechanisms. **Prescribes:** maximize spread
in sequence/structure/mechanism/topology space; **cap cousins.**

**[math] The five frameworks converge.** Submodular coverage, min-variance Markowitz, one-shot batch
active learning, pure-exploration bandits, and k-DPP/OT **all prescribe the same thing**: **spread across
the maximum number of distinct, weakly-correlated lineages/cells; cap any single cluster; do not
concentrate.** This convergence — from five independent formalisms — is itself the strongest result here,
and it is robust to the firewall (none of them needs a per-design agonism ranking; all of them *assume we
don't have one*).

---

## 4. VERDICT

**The math does not justify churning the 4/6/7/3 split, and it does not justify concentrating.** It
justifies **one** change: **raise the number of distinct, weakly-correlated lineage/topology cells.**

**Ranked conclusions (all [math], under [HYP] priors; never a claim of agonism):**

1. **Do NOT concentrate (reject A3 10/4/3/3).** It carries the highest correlation penalty (40–52%) and
   loses in every symmetric regime; it wins only under an **[in-silico] aim prior the firewall bars from
   ranking.** Concentration = premature exploitation with no evidence (framework d).
2. **Do NOT flatten to 5/5/5/5 (reject A2).** It spends a 5th slot on the ~0-agonism ECD lineage and
   slightly lowers P(≥1) vs current in two of three regimes.
3. **The 4/6/7/3 split itself is near-optimal among 4-lineage options and NOT worth re-tuning** (all
   within-4 reshuffles move P(≥1) by < 0.03, regime-dependent). Re-splitting a validated, byte-frozen
   submission for < 3 points of a [HYP] probability is churn; the firewall makes the sign uncertain.
4. **The single highest-value change is to increase L** (distinct lineage count), which robustly adds
   **+0.05 to +0.16** of P(≥1) across all regimes — an order of magnitude more than any within-4 reshuffle.
   The slack to fund it comes from the **lowest-marginal-value slots**: PepGLAD's 6th–7th designs
   (saturating *and* no verified aim) and 2 of the 3 ECD (≈0 agonism).

**Recommended 20-slot allocation — if a clean, novel, validated 5th mechanism cell can be fielded by
2026-10-25** (a distinct generator — e.g. BindCraft/RFpeptides/Chroma-class — *or* a mechanistically
distinct **disulfide-cyclic** sub-family; cyclic is the *only* precedented topology yet only 2/20 of the
current portfolio):

| lineage | count | rationale |
|---|---|---|
| EvoBind (R299-aimed; incl. ≥1–2 disulfide to seat the cyclic cell) | 4 | precedented family; keep |
| DiffPepBuilder (R299-aimed, distinct generator) | 6 | strongest aim diversity; keep |
| PepGLAD (novelty, no verified aim) | **5** | **trim 7→5**; most-saturated + unaimed = lowest marginal |
| **New 5th cell** (distinct generator or distinct cyclic topology) | **3** | **undiscounted first-shots**; raises L 4→5 |
| ECD binding hedge | **2** | **trim 3→2**; keep best-validated binder + the structurally-novel one |

Total = **4 + 6 + 5 + 3 + 2 = 20**; effective lineage count **L: 4 → 5**; the empty **cyclic topology
cell** gets populated. Expected **+0.05 to +0.10 P(≥1 agonist)**, regime-robust, at **zero cost** on the
judged binding/novelty axes (one validated ECD retained; a new generator *adds* method novelty).

**If NO clean 5th cell can be fielded in time:** **keep 4/6/7/3 as-is** (it is near-optimal among 4-lineage
allocations and already byte-frozen/validated), and make the **one coverage improvement that needs no new
generator**: promote **≥1 additional disulfide-cyclic design into the win-path** (from an existing lineage's
clean disulfide-formable members), because **cyclic is the only de-novo GPCR-agonism precedent** and the
portfolio is topology-thin (2/20). This is a **coverage** move (cover the one precedented topology cell),
**not** an agonism ranking — fully firewall-compatible.

**Framing guardrail.** Every number above optimizes the **diversification of unrankable shots** and the
**robustness** of the bet; **none proves, predicts, or ranks agonism.** The cAMP/CRE-SEAP assay is the only
verdict. The result is a prescription to **buy the most, cleanest, most mechanism-diverse lottery tickets**,
which is all in-silico analysis can legitimately do for a class-B GPCR agonist.

---

## Sources
- GLP1R Challenge-3 brief (win = functional activation; multi-metric selection; affinity + activation
  ranked) — https://proteinbase.com/competitions/anthropic-adaptyv-2026/challenges/glp1r
- Esary, Proschan & Walkup 1967, association + at-least-one inequality (positive dependence ⇒ P(≥1) ≤
  independence value) — https://www.uio.no/studier/emner/matnat/math/STK3405/h20/forelesningsnotater/week40-part2.pdf
- Correlated parallel-system reliability (failure prob ↑ with positive dependence) — https://vbn.aau.dk/ws/files/234837364/Chapter_12_Reliability_of_Structural_Systems_with_Correlated_elements.pdf
- Nemhauser, Wolsey & Fisher 1978, submodular greedy (1−1/e) — https://people.ece.uw.edu/bilmes/classes/ee596b_spring_2016/lecture15.pdf
- Markowitz 1952, Portfolio Selection (variance = Σ w_i w_j σ_ij; diversify via covariance) — https://www.math.hkust.edu.hk/~maykwok/courses/ma362/07F/markowitz_JF.pdf
- Kirsch, van Amersfoort & Gal 2019, BatchBALD (joint batch, diversity, 1−1/e; top-k picks redundant points) — https://proceedings.neurips.cc/paper/2019/hash/95323660ed2124450caaac2c46b5ed90-Abstract.html
- Fixed-budget best-arm identification / pure exploration (Audibert–Bubeck–Munos 2010; Bubeck–Munos–Stoltz 2009; Lattimore–Szepesvári 2020) — https://ar5iv.labs.arxiv.org/html/1609.02606
- Kulesza & Taskar, k-DPP (fixed-size diverse subset; volume = diversity) — https://icml.cc/imls/conferences/2011/papers/611_icmlpaper.pdf
- Reproducible computation — `scratchpad/portfolio_calc.py`

## Caveats / Gaps
- **All per-design/lineage probabilities (q_ℓ, r_ℓ, p_i) are [HYP]**, not measurements — agonism is
  unrankable, so the tables illustrate *structure and sign*, not calibrated magnitudes. The robust
  conclusions (spread > concentrate; L is the dominant lever; the 4/6/7/3 vs 5/5/5/5 vs 10/4/3/3 choice is
  within prior noise) hold across every regime tested; the exact numbers do not.
- **The "new 5th lineage" recommendation is conditional on availability.** The v5 report lists clean
  *within-lineage* alternates and ~24 unused clean PepGLAD, but does **not** confirm a clean/novel/validated
  **distinct 5th generator** ready by the deadline. If none exists, the fallback (keep 4/6/7/3 + add a
  cyclic win-path design) applies. Owner/repo must confirm what clean 5th-cell designs actually exist.
- **Cross-lineage ρ ≈ 0 is assumed.** If two generators share a failure mode (e.g., both perch on the
  ECD rim), their cross-correlation is > 0 and the diversification benefit of counting them as "distinct"
  shrinks. Distinctness should be mechanistic (sub-site/topology), not merely tool-name.
- **The multi-metric selection weights are unpublished** (quality vs novelty vs method-novelty vs
  developability vs diversity), so the exact point at which the ECD binding/novelty payoff offsets the
  agonism opportunity cost cannot be computed — only bounded (~0.05–0.10 in the favorable regime).
- Independence-vs-shared-mode is the modeling choice that drives everything; a richer model (continuous
  latent viability, partial cross-lineage coupling) would change magnitudes but not the ranking of
  allocations, because the association upper bound (§1c) holds for *any* positively-associated structure.
</content>
</invoke>
