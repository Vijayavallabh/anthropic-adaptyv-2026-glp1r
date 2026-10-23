# Submission rationale — v10 (2026-10-23)

**FINAL = `submissions/glp1r_track3_v10.csv`** (md5 `6769ef67789319510015442e4f8378ea`, 20 designs, validator PASS 20/0/0, `molecule_class=single_chain`).

## What changed from v9
v10 = **v9 (`419c57ff`) with exactly one change**: `glp1r_04_ago` → its 0-Cys **C9S/C29S** variant
(`HIDFSAIHCAVYASDGNQPLQPFVKWVVCKMI` → `HIDFSAIHSAVYASDGNQPLQPFVKWVVSKMI`). Row order and all 19 other
sequences are byte-identical to v9; `molecule_class` stays `single_chain` for all 20. Diff-verified: the only
content change is `glp1r_04`'s sequence.

## Why (compliance hardening under the verified rules)
The organizers confirmed the design space **definitively** (relayed by owner, 2026-10-23):
> "We are not supporting cyclic peptides in this competition, only linear ones."
> "10 to 250 standard amino acid residues per chain."

with `molecule_class ∈ {single_chain, nanobody, scfv, fab_kappa, fab_lambda}`.

A compliance audit of all 20 v9 designs vs these rules found **19/20 unambiguously clean** (length 13–74 ∈
10–250; all 20 standard AAs, zero non-standard; graft overlap ≤3 contiguous vs GLP-1/exendin/glucagon/GIP;
names + sequences unique). The lone flag was **`glp1r_04`** — the only design carrying 2 Cys
(disulfide-capable), which in a **linear-only** competition is a latent "cyclic"/free-thiol ambiguity.

A fold through the committed 2-folder pipeline (`glp1r_04` vs its C9S/C29S mutant + agonist/antagonist anchors)
showed the **two Cys are not load-bearing**: the mutant reaches R299 identically (Boltz 0/4, Chai 4/4, same
central-polar contacts `190|363|364|394`). So removing them is a **behaviour-preserving** fix that eliminates
the only disulfide ambiguity at zero cost. Evidence: `runs/finalize/` (audit, candidate, `glp1r04_swap/` fold).

## Firewall
This is compliance / necessary-condition hardening, **never an agonism claim**. Reach/engagement are
necessary-condition proxies, length-biased, and agonism-blind (a deep-reader Q234/V237 discriminator was
**refuted by its own matched controls** this session — the inactive metabolite GLP-1(9-36) passes it as
strongly as the agonists). Class-B agonism remains unprovable in-silico; the wet cAMP/CRE-SEAP assay is the
only verdict.

## Fallback
**v9 (`419c57ff`)** is the immediate byte-frozen fallback — itself fully compliant (its only blemish was
`glp1r_04`'s 2 Cys; `molecule_class=single_chain` was correct all along). Deeper fallbacks: v8 `3b7d2581`,
v7 `9ee8df5b`, v6b `32819e6f`, v6 `398bfb30`.

Upload is **USER-GATED**; deadline **Sun 2026-10-25 23:59 AoE**.
