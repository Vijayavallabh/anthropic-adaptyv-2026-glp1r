# PepMLM pilot — GLP1R de-novo (diversity / lottery-ticket hedge)

_Generator: PepMLM-650M (authors' exact HF-Space generate). PepMLM-650M == ESM-2 650M fine-tuned (MIT base). Target-sequence-conditioned (UniProt P43220 construct 24-432, full 409 aa). This is a DIVERSITY hedge, NOT a win-path. No agonism is claimed or ranked; agonism is unprovable in-silico and only the wet-lab cAMP/CRE-SEAP assay decides._

## Counts

- generated: **105**
- eligible (eligibility not flagged): **89**
- graft-free (graft lcs <= 3): **100**
- band-passing / KEPT (entropy>=2.81, run<=2, A+G<=0.36, even non-vicinal Cys, lcs<=3, eligibility pass): **21**

## Strict-Pareto verdict vs v5c (committed diversity_certificate.pareto_dominates)

**None.** No kept PepMLM candidate strictly Pareto-dominates any v5c member.

- Of the 20 v5c members, only **7** are even dominable by an aim-less de-novo candidate: the committed `pareto_dominates` refuses to let a candidate without a verified minD_R299 correct-aim prior displace a member that has one (lineages DiffPep / PepGLAD / DiffPep-ss carry that prior). The dominable members are the EvoBind + ECD slots (aim-less).
- For those, no kept candidate was simultaneously no-worse on novelty-id, coverage, graft-lcs, Cys-count and liability-subset while strictly better on >=1. (PepMLM peptides are short, mostly 0-Cys, low graft-lcs, and already pass eligibility, so they rarely beat a member on a RANKABLE quality axis without also changing an axis the gate protects.)

## Kept candidates (top by PepMLM pseudo-perplexity — generator confidence ONLY, never agonism/affinity)

| name | sequence | len | nCys | entropy | A+G | lcs | elig_id% | ppl |
|---|---|--:|--:|--:|--:|--:|--:|--:|
| pepmlm_L17_06 | `VTTGLDDSLPFLLDIIK` | 17 | 0 | 3.10 | 0.06 | 2 | 43 | 9.20 |
| pepmlm_L12_02 | `DRTYLLPLLHIS` | 12 | 0 | 2.92 | 0.00 | 2 | 67 | 14.41 |
| pepmlm_L18_01 | `VYTTLLDSGLTFALDIAT` | 18 | 0 | 3.06 | 0.17 | 3 | 57 | 15.28 |
| pepmlm_L24_00 | `THFPCILLSRGLLRCKECIAACKK` | 24 | 4 | 3.47 | 0.12 | 2 | 80 | 15.63 |
| pepmlm_L17_04 | `VTTGLLPLLRFLCLIPC` | 17 | 2 | 2.82 | 0.06 | 2 | 33 | 18.76 |
| pepmlm_L19_01 | `VVYQLGLAGYSPFFADIIS` | 19 | 0 | 3.41 | 0.21 | 2 | 33 | 20.13 |
| pepmlm_L22_00 | `KPPESLSRRLSLSGEAACICLL` | 22 | 2 | 3.11 | 0.14 | 3 | 67 | 20.87 |
| pepmlm_L18_03 | `VYTTFLLSPLTFLLDIPK` | 18 | 0 | 3.04 | 0.00 | 2 | 50 | 21.35 |
| pepmlm_L19_00 | `VKPQSRLSSYYTFFADIAI` | 19 | 0 | 3.58 | 0.10 | 3 | 50 | 21.47 |
| pepmlm_L16_02 | `SQRTLGSLRSFCMGPC` | 16 | 2 | 3.20 | 0.12 | 2 | 57 | 22.36 |
| pepmlm_L23_05 | `LFRISLLYSGLPHSSLAIIALIT` | 23 | 0 | 3.07 | 0.13 | 2 | 45 | 22.67 |
| pepmlm_L22_02 | `KPPQCLLRSASPLLIKICLLYS` | 22 | 2 | 3.05 | 0.04 | 2 | 67 | 24.69 |

## Firewall / provenance notes

- Eligibility, developability and stress metrics are the COMMITTED project scorers (scripts/eligibility_check.py, developability.py, stress_liab.py) via diversity_certificate.featurize.
- Pareto test is the COMMITTED scripts/diversity_certificate.pareto_dominates (Cys-count-aware, aim-not-worse, liability-subset), reused verbatim.
- Natural-AA-only + length 12-26 + linear single_chain enforced at generation (rejection resampling).
- No submission file was modified; no git action taken.
