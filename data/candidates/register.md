# Candidate register — GLP1R agonist (Challenge 3)

**Updated:** 2026-10-13 · Machine-readable: `candidates.csv` (this dir). All classes `protein` (micro/mini).
No in-silico score proves agonism; the agonism arm is explicitly LOW-confidence. Proteinbase portal is the
authority for novelty/eligibility — re-check every pick before any (USER-GATED) upload.

## Arm A — agonism bet: EvoBind threading peptides (LOW confidence)

The only direct de-novo GLP1R-agonist precedent is a threading peptide (Li/Bryant 2025, cyclic). 8 runs ×
200 iters (linear, submittable), deep- and accessible-vestibule targets. **Result: did not converge** —
best-pose `if_dist_peptide` floored 5.0–7.6 Å (a genuine inserted contact is <4 Å), peptide plddt low (32–66);
the accessible retarget did not beat the deep one. There is no clean in-silico binding gate for this
membrane-blind isolated-receptor pocket, and agonism is unprovable in-silico regardless. These are mechanism-
plus-precedent bets, not validated binders. **`eb_accv_l32` dropped** (eligibility FLAG 44% id / cov 0.50 vs GIP,
also worst binder). Several carry *short* high-local-identity motifs to GLP-1/exendin at low coverage (not copies;
EvoBind generated them de novo) — prefer low-id peptides and re-check on the portal.

| name | len | if_dist (Å) | plddt | instab | eligibility | dev | note |
|---|---|---|---|---|---|---|---|
| eb_accv_l14 | 14 | 5.04 | 65.7 | 24.9 | OK (80%/cov0.36 exendin4) | oddCys(1) | best if_dist; Cys + exendin motif → caution |
| eb_prod_l20 | 20 | 5.14 | 37.6 | 46.7 | OK (44%/cov0.45 exendin4) | oddCys, instab | |
| eb_accv_l20 | 20 | 5.35 | 39.0 | 123.2 | OK (75%/cov0.20 GIP) | instab123 | very high instability |
| eb_prod_l14 | 14 | 5.52 | 46.3 | 41.7 | OK (67%/cov0.43 GLP1) | hydrophobic, instab | |
| **eb_prod_l26** | 26 | 5.77 | 57.4 | 35.6 | OK (50%/cov0.31 GLP1) | **CLEAN** | only fully-clean peptide |
| eb_prod_l32 | 32 | 5.93 | 61.3 | 59.8 | OK (36%/cov0.34 GLP1) | instab (2 Cys) | lowest id |
| eb_accv_l26 | 26 | 6.27 | 38.9 | 52.4 | OK (62%/cov0.31 ex9-39) | instab | |
| ~~eb_accv_l32~~ | 32 | 7.65 | 31.7 | 69.4 | **FLAG** (44%/cov0.50 GIP) | oddCys, instab | DROPPED |

## Arm B — binding hedge: ECD miniprotein binders (antagonist-leaning)

RFdiffusion→LigandMPNN→af2ig on the soluble ECD groove. 7 pass the binder gate (pae<10, plddt>80, rmsd<2).
Mechanistically ECD-only (no 7TM message) → expected to BIND the construct and pass the binding gate, but lean
antagonist, not agonist. All de-novo (eligibility OK; coverage 0.11–0.34 ≪ 0.5). 3 are developability-clean.

| name | len | af2ig pae | instab | eligibility | dev | note |
|---|---|---|---|---|---|---|
| **ecd_des_20_7** | 70 | 6.22 | 18.3 | OK (62%/cov0.11) | **CLEAN** | strongest + clean |
| ecd_des_8_7 | 66 | 7.03 | 27.1 | OK (38%/cov0.24) | lowcplx A39% | poly-Ala (re-MPNN-able) |
| ecd_des_10_6 | 77 | 7.68 | 36.5 | OK (50%/cov0.21) | lowcplx A40% | poly-Ala |
| **ecd_des_2_4** | 74 | 7.82 | 17.3 | OK (32%/cov0.34) | **CLEAN** | clean |
| **ecd_des_2_6** | 74 | 8.21 | 30.4 | OK (38%/cov0.18) | **CLEAN** | clean |
| ecd_des_4_3 | 64 | 8.60 | 36.2 | OK (33%/cov0.28) | lowcplx A31% | poly-Ala |
| ecd_des_18_5 | 76 | 9.55 | 42.1 | OK (33%/cov0.28) | instab>40 | borderline |

## Arm C — two-domain agonist (S2) — PLANNED, not yet generated

Mechanistically the strongest agonism bet (GLP-1 is bipartite: C-term address→ECD, N-term message→7TM). Reuse
the Arm-B ECD binders as the address and attempt a single chain that also reaches a vestibule message tip.
Gated first on a geometric feasibility check (ECD-epitope↔vestibule span in 6X18). Honest-labeled bet regardless.
