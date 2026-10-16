# session handoff

## Where things stand (2026-10-16 — PICK = v6, OWNER-ADOPTED; v5c byte-frozen fallback; upload USER-GATED)

**Pipeline F0–F9 COMPLETE; v5c survived a brutal reject-everything audit; a mechanism-coverage moonshot then
produced v6, which the owner ADOPTED as the recommended pick (2026-10-16).** **The remaining action is the
owner's USER-GATED upload of v6 — never auto-upload.** Autonomous-to-deadline (deadline 2026-10-25 23:59 AoE).
Compute ceiling = **8 H100s + 500 GB**. **PICK = v6** `submissions/glp1r_track3_v6.csv` (md5
`398bfb3006464811e8ce9ab57afb4dad`, validator PASS 20/0/0); **v5c** (`61c2d9e4…`) byte-frozen fallback; **v5b**
(`b10571b4…`) + **v1** (`1ce4e943…`) deeper fallbacks. **Track-C (watcher `bem3nan8r`) has RUN and resolved
NEGATIVE — no v7**; all owner-approved moonshot tracks (A/B/C/D) are now resolved and no GPU work is pending.

- **2026-10-16 MECHANISM-COVERAGE MOONSHOT (owner: "full push A+B+C+D") → candidate v6 built + validated.**
  Report: `reports/GLP1R mechanism-coverage moonshot.md`. D(SOTA)=no-go; B(coverage axis)=built (v5c covers 3/4
  approach bins, reader-proximal <4.5Å bin EMPTY); A(RFd3 message-address)=384 backbones → 31 clean+novel → 20
  folded → **3 reproduce consensus <4.5Å to R299 under independent Boltz+Chai** (lead-verified clean; the RFd3
  placement reach is CIRCULAR and not counted; 17/20 fail the non-circular test = reachability wall, valid
  negative); C(2-SS)=RAN→**NEGATIVE** (watcher caught a GPU-6 window; of 42 built structures only 2 realize two
  real disulfides and both fail the committed gates; the 3 clean+band+eligible ones realize only 1 real SS + 2
  free thiols, duplicating `dpbss_010` — no clean double-staple exists; no v7). **v6** `submissions/glp1r_track3_v6.csv` md5
  `398bfb3006464811e8ce9ab57afb4dad`, validator PASS 20/0/0, 17/20 clean (same forced 3-liability floor) =
  v5c minus slots 11(`pglad_034`)+17(`pglad_001`) (most-redundant outer PepGLAD) plus `glp1r_21_ago`
  (des_0039_m7, DFYFDAAMVYLYTKLANPDPKVLEELKKQIALSLIVD) + `glp1r_22_ago` (des_0047_m6,
  WWLEPSDDPKLQELHAQALADWADVIFEETIDFILSLVVRVLLYL) = 2 distinct-backbone RFd3 reader-proximal fillers.
  v6 raises mechanism-coverage 3/4→4/4 + generative priors 4→5 (PepGLAD 6→4). **It is a coverage/robustness
  TRADE, not a strict Pareto win**; caveats = weak/mixed interface confidence + co-fold memorization confound;
  agonism still unprovable (assay-only). Candidates committed: `data/candidates/msgaddr_waveA_candidates.csv`.
  **OWNER ADOPTED v6 as the recommended pick (2026-10-16 via AskUserQuestion); v5c (`61c2d9e4`) byte-frozen
  fallback.** Firewall held (minD_R299/2-fold consensus = necessary-condition coverage filter only, never an
  agonism rank). **Track-C (watcher `bem3nan8r`) has since RUN and resolved NEGATIVE** — first-hand Sγ–Sγ
  verification shows no clean double-stapled "grenade" exists (2-SS realization ≈ 0; the clean candidates carry
  unpaired free thiols and duplicate the `dpbss_010` topology class); v6 unchanged, no v7. Full write-up in the
  Track-C resolution section of `reports/GLP1R mechanism-coverage moonshot.md`.

- **2026-10-16 BRUTAL STRESS TEST (owner: "reject all 20 if a better set exists") → `v5c_stands`, independently
  verified.** A 48-agent adversarial workflow (`glp1r-brutal-stress-test`) attacked every design + the selection
  logic on 6 fronts (per-design teardown / composition challenge / full-pool re-optimization incl. PepMLM+BoltzGen
  / aggregation-synthesizability / novelty hardening / firewall red-team+SOTA), then refuted + firewall-checked
  every finding. 66 findings, 33 CONFIRMED+firewall-safe, **every per-slot finding = KEEP; 0 designs rejected;
  2 pro-change claims REFUTED**. Coordinator re-ran the committed scorers first-hand (not on the agents' word):
  md5 `61c2d9e4` ✓; validate PASS 20/0/0 ✓; certificate **0 Pareto swaps** ✓; **17/20 dev-clean, 3 forced
  liabilities = slots 3/4 (instab) + 20 (POLYRUN)** ✓; **CLEAN-FLOOR = 17** (max dev-clean 20 assemblable from
  ALL clean pools incl. pilots, under the 35%/generator cap, is only 17: PepGLAD 7 + DiffPepBuilder 7 + EvoBind 2
  + ECD 1 + PepMLM 0 + BoltzGen 0) → **a fully-clean 20 is mathematically impossible; v5c's 3 liabilities are the
  FORCED FLOOR, not a defect** ✓. Report: `reports/GLP1R brutal stress test v5c confirmation.md`. Record-hygiene:
  `data/candidates/v5c_struct_novelty.csv` written (corrected for the ACTUAL v5c slots 11=pglad_034 pLDDT60 /
  13=dpbss_010 pLDDT68, both maxTM 0.000 novel; stale v5_struct_novelty.csv mislabeled those two). **One genuine
  decision point surfaced + DECLINED (F2-07):** iff owner re-opens the submission, trim slots 8/11/17 + add 3
  PepMLM (priors 4→5, min-pair 1.88→2.22) — but it WORSENS developability (liab 3→6; 0/21 PepMLM band-passers
  clean), is not a strict Pareto win, and PepMLM shares ESM-2 with DiffPepBuilder (non-orthogonal). KEEP v5c.
  Firewall held: minD_R299 used only as the not-worse gate (all 6 DiffPep-linear aimers miss the 4.5Å gate → did
  no selection work); no agonism/binding signal touched the verdict.

- **EIGHT submission files staged (all validate PASS, all ≤20, all `molecule_class=single_chain`):**
  - **PICK = v6** `submissions/glp1r_track3_v6.csv` — **20 designs**, md5 `398bfb3006464811e8ce9ab57afb4dad`,
    **OWNER-ADOPTED 2026-10-16**. = v5c − slots 11/17 (most-redundant outer PepGLAD) + 2 distinct-backbone RFd3
    reader-proximal coverage-fillers `glp1r_21_ago` + `glp1r_22_ago`; mechanism coverage 3/4→4/4, generative
    priors 4→5, same forced 3-liability floor (the 2 additions clean/0-Cys/eligible). Validator PASS 20/0/0.
    Report `reports/GLP1R mechanism-coverage moonshot.md`.
  - **v5c** `submissions/glp1r_track3_v5c.csv` — **20 designs**, md5 `61c2d9e4d806b799a278efe7efb31063`.
    **Byte-frozen FALLBACK** (brutal-tested Pareto-optimal, portal-parsed 20/20). = v5b with ONE swap (slot 13
    `pglad_053` → `dpbss_010`, a fresh clean DiffPepBuilder disulfide-stapled
    R299-aimer: `RNAAYYAYCEIDCIDQLLLAAYF`, Cys9-Cys13 internal, minD_R299 4.76 Å, id42.9/cov0.30, lcs3, dev CLEAN).
    Raises win-path constrained-topology count 2→3; max generator share 35% (unchanged). Validator PASS; stress
    17 clean/3 soft/0 FATAL; v5b rebuilds byte-identical (assembler edit backward-safe); diff vs v5b = slot 13 only;
    ESMFold+FoldSeek on dpbss_010 = 0 PDB hits. Build: `scripts/assemble_portfolio.py data/candidates/portfolio_v5c_order.txt submissions/ v5c`.
    **Portal-parsed 20/20 "Single chain / Passed" (byte-verified against the committed file).**
  - **v5b** `glp1r_track3_v5b.csv` — 20, md5 `b10571b4…`. **Byte-frozen FALLBACK.** = v5 with the pglad_029→pglad_034
    novelty swap. Portal-parsed 20/20.
  - **v5** `glp1r_track3_v5.csv` — 20, md5 `4c87e1bd…`. Brutal-gauntlet best-20 (13-agent adversarial rebuild).
    Portal-parsed 20/20. Report: `reports/GLP1R v5 brutal stress test and best20 rebuild.md`.
  - **v4** `…_v4.csv` (945b30b3), **v3** `…_v3.csv` (6b846b83), **v2** `…_v2.csv` (66cefdcf) — superseded.
  - **v1** `glp1r_track3.csv` — 19, md5 `1ce4e943…`. **ZERO-RISK FALLBACK** (12 EvoBind + 7 ECD).
- **This session's extension pass (report `reports/GLP1R agonist portfolio and topology.md`, notes in
  `research_notes/GLP1R agonist portfolio and topology/`):** 3 agents (portfolio-probability math / topology-preorg
  chemistry / reachability re-challenge) converged → the only regime-robust, firewall-compatible lever is raising the
  win-path's constrained-topology / lineage-cell count. REJECTED on evidence: **PepFlow 5th-method cell** (all `pepx_*`
  are low-complexity outliers vs the v5b band), **deep-pocket insertion** (reachability wall holds), and
  **non-orthosteric/ago-PAM/exoframe** peptide mechanisms (sites intracellular/membrane → CLOSED). Portfolio math
  says **do NOT churn the 4/6/7/3 mix** (<0.03, sign-uncertain). Executed: fresh DiffPepBuilder disulfide-staple
  generation (idle GPUs, zero cost) → 16 clean-gated graft-free R299-aimers (pool `data/candidates/diffpep_ss_vest2.csv`,
  `dpbss_*`) → one swapped into v5c.
- **Agonism is UNPROVABLE/UNRANKABLE in-silico** (class-B GLP1R) — v5→v5c improvements are RANKABLE-PRIOR + coverage
  only, NOT agonism gains. Win = the wet-lab cAMP/CRE-SEAP assay, the ONLY verdict.
- **2026-10-15b moonshot re-attack (8-agent adversarial vetting + 2026 SOTA sweep):** the firewall HELD against the
  whole sweep (no new activation oracle survives as a ranker; no new generator breaches the reachability wall;
  nothing post-2026-10-01 changes the board). M2 (structural-novelty max) + M4 (fly-casting/low-pLDDT rescue) KILLED
  on byte-verified evidence. **M1 (principled diversity selection) EXECUTED** → `scripts/diversity_certificate.py`
  + `reports/GLP1R diversity selection certificate.md`: firewall-guarded (GUARD-A no engagement/aim in the kernel),
  TRIPWIRE confirms the band rejects all PepFlow rows, and **v5c is Pareto-efficient / diversity-consistent** under
  the fixed 4/6/1/6/3 matroid. An initial flag (`dpbv2_005`→slot 6) was REFUTED on build — `dpbv2_005` is a
  2-disulfide design (`has_ss`, 4 Cys), not a clean linear upgrade; the Cys-count-hardened certificate now finds
  **0 valid swaps** → v5c confirmed Pareto-optimal (v5d built on owner request, refuted, removed). Firewall citations added to docs/METHODS.md
  (Muratspahić/Baker Nature 2026; Junker & Schoeder PLoS One 2026; Fonteyne RSC Dig. Disc. 2026 — all verified first-hand).

## Do next

1. **Owner's call at upload — PICK = `v5c` (recommended); `v5b` is the byte-frozen fallback; `v1` the zero-risk set.**
   The upload click is **USER-GATED** — never auto-upload. v5c and v5b both parse 20/20 at the portal.
2. **No submission change is pending.** v5c is fully verified (validator PASS, 17/3/0, byte-regression-safe,
   portal-parsed, 0 PDB hits) and now additionally certified Pareto-efficient/diversity-consistent (M1). The
   in-silico win-path levers are exhausted; remaining *agonism* gains are **wet-lab only**.
   **Owner-approved pilots — BOTH RAN, lead-verified, 0 dominators (COMPLETE 2026-10-15).** PepMLM + BoltzGen were
   provenance-VERIFIED clean (PepMLM HF weights MIT & `gated=False` — a subagent's restrictive-license claim was a FALSE
   ALARM, corrected via HF+GitHub APIs; BoltzGen MIT + base Boltz-2 MIT, no ESM-3/ESMC/Protenix/AF3). GPU-blocked through
   watcher cycle 1 (`baopxnp26`, 4h@180s → `no_window`); cycle 2 (`brc0ev2tb`, 12h@600s) caught a durable idle window
   ~21:05 UTC when the foreign job finished and **ran both pilots to completion** (one process/GPU, nothing clobbered).
   Outcome (COMMITTED to `data/candidates/`: `pepmlm_pilot.csv`+`_report.md`, `boltzgen_pilot.csv`+`_report.md`):
   **PepMLM** 105 raw → 89 eligible → 21 band-passing → **0 strict-Pareto dominators vs v5c**; **BoltzGen** 30 raw →
   29 eligible → 3 band-passing → **0 dominators**. Both gates reuse the committed `diversity_certificate`
   (featurize/passes_band/pareto_dominates/load_v5c/AIM) verbatim; I **independently re-drove** those committed
   functions from the raw sequences in my own loop (`scratchpad/verify_pilots_pareto.py`) → confirmed **0 dominators**
   in both pools (0 even among ALL eligible, incl. non-band — no hidden dominator the band masked), and confirmed
   `load_v5c()` returns the frozen 20-member v5c (dpbss_010 at slot 13). **v5c stands UNCHANGED**, now additionally
   stress-tested against 135 fresh de-novo candidates from two independent SOTA lineages (ESM-2 + Boltz-2). The pilots
   were diversity/clean-ticket hedges, NOT a win-path — and no swap is justified (none dominates). **Watcher mission
   COMPLETE — do not re-arm** (both pilots have now executed). NeoPep/PPI-Diff CLOSED on license. **v5d** (owner-approved)
   refuted on inspection (swap-in `dpbv2_005` is a 2-disulfide design, not a clean upgrade) and removed. In-silico
   win-path levers are now fully exhausted; remaining *agonism* gains are wet-lab only (cAMP/CRE-SEAP).
3. If a future reason to change the roster arises: `assemble_portfolio.py` now resolves `dpbss_*` (disulfide pool) +
   `dpbv2_*`/`pglad_*`/`eb_*`/`ecd_*`; rebuild from an order file under `data/candidates/portfolio_*_order.txt`
   (byte-reproducible; v5b/v5c/… all rebuild identically).

## Invariants (full list in AGENTS.md)

- **Agonism ≠ binding.** Score agonism vs **6X18 active state**; binding vs the inactive 24–432 construct; keep
  separate; demerit off-state binders. **No in-silico score proves agonism** — only the cAMP/CRE-SEAP assay does.
- De-novo / zero-shot only; no GLP-1/exendin/glucagon/semaglutide/GIP identity (≤3 aa contiguous overlap);
  **linear/disulfide, natural AAs** (no head-to-tail macrocycle).
- **The Challenge-3 upload portal has NO novelty score** (format/parse "Single chain / Passed" only) — lock novelty
  up-front with the local sequence+structure screens, never a portal recheck.
- Keep AF3/Protenix-v2/ESM-3/ESMC out of submitted-design provenance (ODC-BY; DiffPepBuilder uses ESM-2 = clean;
  RFd3/RFdAA = BSD-3; Chai-1 Apache-2.0). Up to 8 GPUs (owner 2026-10-14); one process/GPU; never clobber a foreign job.

## Compute (2026-10-15)

Ceiling = **8 H100s + 500 GB**. This session: DiffPepBuilder disulfide-staple generation on GPU 0 + an ESMFold fold
on GPU 1, both released; a transient foreign ~1 GB job appeared on GPU 0 mid-pass (avoided). Verify idle with
`nvidia-smi` before launching; concurrent SEPIQ/TNF/AMP sessions often hold several GPUs; one process/GPU; never
clobber a running job. NOTE: `run_diffpep.sh` picks the GPU via `GPUtil` (physical ordinals) — pass the full visible
set (e.g. `"0,1,2,3,4,5,6,7"`) as its GPU arg so the `CUDA_VISIBLE_DEVICES` map is identity (a single masked index
can trigger `CUDA error: invalid device ordinal`).

## Gated (owner OK required)

Portal upload (USER-GATED account); creating/altering the GitHub repo or changing its visibility; env/setup changes
beyond the approved init. (GPU ceiling raised to 8 on 2026-10-14 — >4 GPUs no longer gated, but still use only free ones.)
Regular commits/pushes to the existing private repo are the normal checkpoint workflow (NOT gated).
