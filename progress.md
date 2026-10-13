# progress

**Project:** anthropic-adaptyv-2026-glp1r — de-novo human GLP1R **agonist** (Challenge 3, Track 3)
**Deadline:** 2026-10-25 23:59 AoE · **Updated:** 2026-10-13

## Status

- **F1 Research — DONE.** 8-stream wave + cited synthesis (`reports/`, `research_notes/`); load-bearing claims
  verified first-hand. Strategy (user-approved): **mechanism-hedged portfolio S1–S4**.
- **F0 Harness + env — DONE.** `init.sh` gate PASSES (uv sync + compile + 12 tests + validator). FoldSeek/MMseqs2
  installed. Private repo pushed: `Vijayavallabh/anthropic-adaptyv-2026-glp1r` (commit `91ded84`).
- **F2 Stage 0 target prep — DONE.** 6X18 active-state target (chain R; gaps 130–135 + 339–343 confirmed) + GLP-1(7–36)
  message geometry (chain P) extracted; WT `24–432` construct model (409 aa); hotspots + positive controls + checksummed
  `data/target/manifest.json`. CPU/light.
- **Scoring CALIBRATION — DONE (key result, corrected after /code-review).** Boltz-2 co-fold: global
  **ipTM/pTM do NOT discriminate** (AUC~0.5). **ECD-groove-anchor (>=5) + iPAE_min (<=4.0)** separate native-like
  binders from scrambles (per-seed **83% sens / 96% spec**; the AUC=1.00 was a 3-seed-MEAN artifact). **Antagonist
  test: exendin(9-39)/GLP-1(9-37) PASS the gate (56%)** → it's a **binder-vs-JUNK filter, NOT an agonism selector**.
  Gate in `configs/filters.yaml`; `scripts/iface_score.py`. Agonism rests on mechanism + wet-lab. Compact RFd
  target cluster {190,194,233,234,237} from 6X18.
- **/code-review hardening — DONE.** 15 findings; the 2 scientific ones (mean-vs-per-seed overclaim; scramble≠
  antagonist negative) corrected above; code bugs fixed (scorer emits `ecd_groove_anchor_count` + distance-gated
  nterm + bool/round casts; shard script: fail-loud on empty input, clear stale inputs, OMP cap, set-u-safe, accept
  name/design); stale docs reconciled (ipSAE_min → the engagement gate). cofold_boltz.sh now a thin wrapper.

## Feasibility (honest)

**Frontier moonshot.** No standalone designed protein has agonized a class B GPCR; only direct GLP1R-agonist precedent
is EvoBind (preprint, n=3, cyclic). **Win = activation (cAMP/SEAP), not binding.** No in-silico score proves agonism.

## F3 generation — STARTED (owner approved "proceed with the first generation wave")

### RFd validation wave 1 (`val_vest`, deep message hotspots {190,194,233,234,237}) — DONE, DIAGNOSTIC
`scripts/gen_rfd.sh val_vest "R140-338/0 60-90" ... 8 1` → rc=0, **8 clean backbones**, RFd plddt **0.88–0.92**,
helix **0.92–1.0** (RFd generator works great). BUT (`scripts/check_rfd_geom.py` + diag):
- **3 of 5 deep hotspots are BURIED** (R190 18.6 Å², R194 15.7, R234 15.4 — all <20 Å² SASA in the crop) →
  a compact de-novo binder physically **cannot contact them**.
- All 8 designs **self-docked to the accessible vestibule RIM**, two clusters: TM1-tip {144,148,151,152,155}
  and TM5-tip {298,299,300,301} — real GLP-1-contact residues, but shallow, **tiny 1–7-residue interfaces**.
- **GLP-1 itself grips 55 receptor residues** (29 in the crop) — a deep interface a *threaded 30-mer* fills.

**Load-bearing geometric truth (first-hand):** a folded bundle perches on the vestibule rim (antagonist-leaning);
it cannot insert the "message" into the deep site. → **RFd arm = vestibule-RIM binders** (strong-binder hedge, passes
the binding gate, mechanistically antagonist-leaning); **the agonism bet is EvoBind threading linear peptides** (the
only direct precedent). Matches research note 04 and the approved S1–S4 hedge; does not break it.

### RFd validation wave 2 (`val_tm5tip`, ACCESSIBLE cluster {298,299,300,306}, dmax 11 Å, SASA 57) — RUNNING
Single-variable retarget to the one compact+exposed rim cluster. Expect larger on-target interfaces; if so, scale the
RFd rim-binder lineage. `runs/rfd_val_tm5tip.log`.

### Pipeline built + running (2026-10-13)
- `scripts/check_rfd_geom.py` — RFd backbone geometry gate (hotspot contact, footprint, Rg, helix, plddt).
- `scripts/seq_mpnn.sh` — **LigandMPNN** binder design (chain R fixed, chain A redesigned, `--omit_AA C` = 0 Cys);
  extracts `variants.csv`. VERIFIED working (pilot on `val_tm5tip`, 32 seqs). **Observation:** geometry-PASS
  backbones → reasonable charged seqs; geometry-FAIL → degenerate poly-Leu/Ala (binder on hydrophobic TM) →
  **FILTER backbones by geometry BEFORE MPNN/co-fold**; watch interface hydrophobicity (membrane-proximal).
- `scripts/gen_sweep.sh` — RFd production sweep (tm5tip / ecl2 / ecd × mini 60-90, 24 each). RUNNING (GPUs 1/3/5).
- `scripts/gen_evobind.sh` + `scripts/fetch_msa_colabfold.py` — **EvoBind agonism flagship READY**: conda env
  `evobind`, receptor MSA fetched via ColabFold (`glp1r_construct.a3m`, 6085 seqs, query==construct VERIFIED),
  linear peptides steered to the deep vestibule message site (`receptor_if_residues`, fasta idx = UniProt-23).
  **Needs a genuinely FREE GPU** (full AF2 on ~430 res); deferred until the TNF job frees memory.

### FIRST SCORED WAVE (2026-10-13, af2ig = primary gate) — vestibule RFd arm is NON-VIABLE
- **Full control re-score** (runs/boltz_panel/out, seed-mean): ECD-anchor>=5 AND iPAE_min<=4 → agonists 3/4,
  antagonists 1/3, **scrambles 0/8** = validated binder-vs-junk filter *for two-domain/ECD designs*. But
  vestibule_hits does NOT separate (Boltz over-docks) → **af2ig is the primary gate** for 7TM-only binders.
- **af2ig on RFd vestibule binders (pass_v1 = 6 geometry-passers x8 MPNN):** **BEST pae_interaction 23.5, ALL
  fail the <10 gate.** Binders FOLD well (plddt ~90, rmsd 0.4) but make NO confident interface. The RFd
  folded-binder→vestibule arm **floors af2ig** → NON-VIABLE as-is (matches TNF `lesson-denovo-wall-flat-polar-target`
  + the buried-pocket geometry). Do NOT scale RFd vestibule binders.
- MPNN caveat confirmed: small-interface rim binders → degenerate poly-Ala seqs at temp 0.2.

### ECD arm: VIABLE binder hedge — 7 designs PASS af2ig (full 192, complete)
**BEST pae_interaction 6.22** (des_20_7, plddt 89.8, rmsd 0.59 = STRONG de-novo binder); 7 PASS (pae<10,plddt>80,
rmsd<2): des_20_7(6.22) des_8_7(7.03) des_10_6(7.68) des_2_4(7.82) des_2_6(8.21) des_4_3(8.60) des_18_5(9.55);
several more 10-14. The soluble ECD IS designable. **These are ANTAGONIST-leaning (ECD-only, no message) → the
BINDING hedge**, not agonism. (The earlier "best 10.4" was a cuBLAS-race-truncated run; staggered re-run complete.)
`runs/af2/ecd_mini/sharded`.

### RFd3 all-atom vestibule — DEAD (non-physical)
32 backbones, huge interfaces (45-58 contacts) BUT only 30-39% of contacts on GLP-1's physical extracellular
face → CIRCUMFERENTIAL LIPID-FACING WRAP of the membrane-blind TM bundle (non-physical). Both RFd1 (rim perch,
af2ig floor) and RFd3 (lipid wrap) **fail to make a physical vestibule binder**; af2ig/AF2 are membrane-blind so
they can't even gate a lipid-wrap out → **folded-binder→vestibule approach is a dead end.**
[[lesson-denovo-binder-cant-reach-buried-pocket]]

### EvoBind agonism bet — DONE (8 runs × 200 iters), in-silico WEAK (honest)
All 8 complete (watcher `bxji9h2d0` was self-match-stuck → killed; read metrics directly). Best-pose
`if_dist_peptide` **floored 5.0–7.6 Å** (a genuine inserted contact is <4 Å), peptide plddt LOW (32–66); the
accessible-vestibule retarget (accv) did **not** beat deep (prod) — both floor ~5 Å. The threading-peptide
optimizer also cannot insert into this membrane-blind, isolated, inactive vestibule; **no clean in-silico binding
gate exists here**, and agonism is unprovable in-silico regardless. Best by if_dist: accv_l14 5.04/plddt66
`SLFINDWCETFDMM`; prod_l20 5.14; prod_l26 5.77 (**only fully-clean developability**). Eligibility 7/8 OK;
**accv_l32 FLAG** (44% id/cov0.50 vs GIP → dropped). Several carry *short* high-local-id motifs to GLP-1/exendin
at low coverage (accv_l14 80%/cov0.36 exendin4) → prefer low-id, portal re-check. Developability poor across the
board (short unoptimized peptides); only eb_prod_l26 clean. **→ Keep a DIVERSE 3–4 as LOW-confidence agonism bets
(labeled); do NOT scale** (floor is reachability, not iteration count). Full set + metrics/flags/labels in the
versioned register `data/candidates/{register.md,candidates.csv}` (15 candidates: 8 peptides, 7 ECD binders).

### Next (12 days runway to 2026-10-25)
1. **S2 two-domain agonist = the prize bet with the best mechanism** (GLP-1 is bipartite: C-term address→ECD,
   N-term message→7TM). Reuse the 7 validated ECD-binder backbones as the address; attempt a single chain that
   also reaches a vestibule message tip. FIRST devil's-advocate the geometry (ECD-epitope↔vestibule span in 6X18)
   before committing a wave; agonism stays unprovable in-silico → honest-labeled bets.
2. Portfolio = 3 clean ECD binders (binding hedge) + diverse EvoBind peptides (agonism bet) + any S2 (best-mechanism
   bet), diversity-capped (≤2/lineage), best-first, ≤20 designs.
3. F7 novelty/liabilities (vs GLP-1/exendin/glucagon/semaglutide; FoldSeek structural) → F8 rank (5 scorecards)
   → F9 package (validator exit 0). **USER-GATED upload.**

## Compute

**State 2026-10-13 (post-EvoBind):** my 8 EvoBind runs finished and released. GPUs **1,3,6,7 free**; **2,4,5** used
by my concurrent **SEPIQ session** (`boltz predict` ×4 + an `alchemy_ddg` FEP job, small) — do not clobber. GPU 0
holds a 4.7 GB orphaned allocation from an already-dead PID (not reclaimable by me; non-blocking). Default 4 GPUs;
burst to 8 only when genuinely idle. Heavy GPU work → the free 1/3/6/7.

## Gated (owner OK required)

Launching generation (F3); using >4 GPUs; portal upload; env/setup changes beyond the approved init.
