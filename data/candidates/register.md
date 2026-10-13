# Candidate register — GLP1R agonist (Challenge 3)

**Generated** by `scripts/build_candidate_register.py` from the tool outputs (af2ig `.sc`,
EvoBind `metrics.csv`, `developability.analyze`, `eligibility.score_design`) — **do not hand-edit;
re-run to refresh.** `candidates.csv` (this dir) is the machine-readable authority: filter on
`status == keep` and `eligible == True` before selection. `binding_value` is arm-specific
(`binding_model`/`binding_metric` columns): af2ig `pae_interaction` (lower=better) for binders,
EvoBind `if_dist_peptide` (lower=better) for peptides; `plddt` is likewise the design-confidence
from that arm's model and is NOT comparable across arms. No in-silico score proves agonism; the
agonism arm is explicitly LOW-confidence. Proteinbase portal is the authority for
novelty/eligibility — re-check every pick before any (USER-GATED) upload.

## Arm A — agonism bet: EvoBind threading peptides (LOW confidence)

Only direct de-novo GLP1R-agonist precedent is a threading peptide (Li/Bryant 2025, cyclic). 8 runs
× 200 iters (linear, submittable). Result: **did not converge** — best-pose `if_dist_peptide` floored
~5–7.6 Å (a genuine inserted contact is <4 Å), peptide plddt low; the accessible retarget did not beat
the deep one. No clean in-silico binding gate exists for this membrane-blind isolated-receptor pocket,
and agonism is unprovable in-silico. Mechanism-plus-precedent bets, not validated binders. `status=drop`
rows failed the de-novo eligibility gate (local id to a known agonist >30% over ≥50% coverage).

| name | status | len | if_dist (Å) | plddt | rmsd | instab | eligibility (id%/cov/nearest) | novTM(PDB) | dev |
|---|---|---|---|---|---|---|---|---|---|
| eb_accv_l14 | keep | 14 | 5.04 | 65.7 | - | 24.9 | OK 80.0%/cov0.36/exendin_4 | - | oddCys(1) |
| eb_prod_l20 | keep | 20 | 5.14 | 37.6 | - | 46.7 | OK 44.4%/cov0.45/exendin_4 | - | oddCys(1),instab>40 |
| eb_accv_l20 | keep | 20 | 5.35 | 39.0 | - | 123.2 | OK 75.0%/cov0.20/GIP_1_42 | - | instab>40 |
| eb_prod_l14 | keep | 14 | 5.52 | 46.3 | - | 41.7 | OK 66.7%/cov0.43/GLP1_7_37 | - | hydrophobic,instab>40 |
| eb_prod_l26 | keep | 26 | 5.77 | 57.4 | - | 35.6 | OK 50.0%/cov0.31/GLP1_7_37 | - | clean |
| eb_prod_l32 | keep | 32 | 5.93 | 61.3 | - | 59.8 | OK 36.4%/cov0.34/GLP1_7_37 | - | instab>40 |
| eb_accv_l26 | keep | 26 | 6.27 | 38.9 | - | 52.4 | OK 62.5%/cov0.31/exendin_9_39 | - | instab>40 |
| eb_accv_l36 | keep | 36 | 6.45 | 66.1 | - | 24.3 | OK 57.1%/cov0.19/GLP1_7_37 | - | clean |
| eb_prod_l40 | keep | 40 | 7.07 | 46.9 | - | 35.9 | OK 37.5%/cov0.20/exendin_4 | - | oddCys(3) |
| eb_accv_l32 | drop | 32 | 7.65 | 31.7 | - | 69.4 | FLAG 43.8%/cov0.50/GIP_1_42 | - | oddCys(1),instab>40 |
| eb_accv_l44 | drop | 44 | 7.86 | 29.3 | - | 18.8 | FLAG 30.3%/cov0.75/GIP_1_42 | - | clean |

## Arm B — binding hedge: ECD miniprotein binders (antagonist-leaning)

RFdiffusion→LigandMPNN→af2ig on the soluble ECD groove; all shown pass the binder gate
(pae<10, plddt>80, rmsd<2). Mechanistically ECD-only (no 7TM message) → expected to BIND and pass the
binding gate but lean antagonist, not agonist. All de-novo (eligibility OK; coverage ≪ 0.5).
**Structural novelty (FoldSeek vs PDB100, F7):** all are sequence-novel but structurally common helical
bundles (max TM 0.87–0.92 to PDB; `des_8_7` most novel at 0.70) → expect ~3/4 on the portal novelty axis
(sequence saves them). Query = the af2ig binder fold; the portal is the authority (it also compares AFDB).

| name | status | len | af2ig pae | plddt | rmsd | instab | eligibility (id%/cov/nearest) | novTM(PDB) | dev |
|---|---|---|---|---|---|---|---|---|---|
| ecd_des_20_7 | keep | 70 | 6.22 | 89.8 | 0.59 | 18.3 | OK 62.5%/cov0.11/GLP1_7_37 | 0.883 | clean |
| ecd_des_8_7 | keep | 66 | 7.03 | 85.9 | 1.62 | 27.1 | OK 37.5%/cov0.24/GLP1_7_37 | 0.705 | lowcplx(A39%) |
| ecd_des_10_6 | keep | 77 | 7.68 | 90.2 | 0.78 | 36.5 | OK 50.0%/cov0.21/exendin_9_39 | 0.924 | lowcplx(A40%) |
| ecd_des_2_4 | keep | 74 | 7.82 | 91.7 | 0.62 | 17.3 | OK 32.0%/cov0.34/exendin_4 | 0.910 | clean |
| ecd_des_2_6 | keep | 74 | 8.21 | 92.1 | 0.67 | 30.4 | OK 38.5%/cov0.18/GLP1_7_37 | 0.906 | clean |
| ecd_des_4_3 | keep | 64 | 8.60 | 86.7 | 1.08 | 36.2 | OK 33.3%/cov0.28/GLP1_7_37 | 0.895 | lowcplx(A31%) |
| ecd_des_18_5 | keep | 76 | 9.55 | 89.8 | 0.37 | 42.1 | OK 33.3%/cov0.28/exendin_4 | 0.873 | instab>40 |

## Arm C — two-domain agonist (S2) — TESTED, NO-GO (a folded binder won't span to the vestibule)

Mechanistically the strongest agonism idea (GLP-1 is bipartite: C-term address→ECD, N-term message→7TM), and the
geometry is permissive (accessible vestibule R197/R299 ~14–20 Å from the ECD anchor R32; deep pocket R363/364/394
35–38 Å + buried = unreachable). But a pilot of 24 RFdiffusion binders conditioned on a bridging ECD↔vestibule
hotspot set (R32,R197,R299; 80–140 aa) produced **0/24 two-site** designs (`scripts/check_s2_geom.py`): the binder
binds the large convex ECD surface and leaves the concave vestibule untouched (≤1 vestibule contact, ever). This is
the 4th independent confirmation of the reachability wall (RFd1 rim-perch, RFd3 lipid-wrap, EvoBind if_dist floor,
now S2 span) — a folded de-novo protein cannot engage this vestibule. NO-GO; not scaled. The agonism bet rests on
the Arm-A threading peptides (LOW-confidence); Arm-B is the binding hedge. (The pilot's 6 ecd_only designs are a
distinct large-ECD-binder lineage, available to af2ig-validate for hedge diversity if F8 wants it.)
