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

### Next
1. Finish sweep → geometry-filter → MPNN passers → `variants.csv`.
2. **When GPUs free:** (a) Boltz-2 co-fold pilot (`val_tm5tip` passers) + production variants → engagement gate;
   (b) EvoBind pilot (smoke test then production). **Recalibrate a VESTIBULE-engagement gate** (iPAE_min +
   7TM-contact) for 7TM-only binders — the ECD-anchor gate is for two-domain designs only (see below).
3. F7 novelty/liabilities → F8 rank (5 scorecards) → F9 package.

## Compute

**NOT idle right now:** my concurrent **TNF-challenge session** is running `af2ig` across **all 8 GPUs** (~61 GB each,
`boldA_af2ig`). Only ~15–19 GB free/GPU. RFd (~4 GB) and ProteinMPNN coexist fine and are proceeding; **heavy Boltz-2
co-fold is QUEUED until the TNF job frees memory** (honors "queue heavy GPU work into idle windows / never clobber").
Default 4 GPUs; burst to 8 only when genuinely idle.

## Gated (owner OK required)

Launching generation (F3); using >4 GPUs; portal upload; env/setup changes beyond the approved init.
