# TOOLS — the GLP1R design/scoring stack

Machine-readable matrix with licenses + install status: **`configs/tools.yaml`**. Full reconciliation +
primary-source license evidence: `research_notes/.../07_tool_availability_licenses_hardware.md`.

**License hygiene (load-bearing):** submitted sequences are published under **ODC-BY**. Keep
**AlphaFold3 / Protenix-v2 / ESM-3 / ESMC-600M OUT of any submitted-design provenance** (gated / non-commercial /
attribution-encumbered output terms). The permissive core (MIT / Apache-2.0 / BSD-3 / CC-BY) is clean to release.
GPL (FoldSeek/MMseqs2) binds the software, not the outputs → results are fine to publish.

## Stack by stage (all installed unless noted)

- **Generate** (S1/S2): RFdiffusion, RFdiffusion3, RFpeptides (use linear/disulfide outputs), BindCraft, BoltzGen,
  Genie3, PXDesign. **EvoBind** — top generator for blind peptide agonists; **CONFIRM/INSTALL + verify a linear mode + license** before use.
- **Sequence:** ProteinMPNN, LigandMPNN, Caliby (MIT/Apache).
- **Fold/score (binding):** AF2-initial-guess, Boltz-2 (2.2.1), Chai-1 (0.6.1), OpenFold3, **Protenix v0.5.0/PXDesign weights** (NOT v2), DockQ (2.1.3), voronota-lt (1.1.479). Rank by **ipSAE_min**, calibrated vs controls.
- **Agonism hypothesis:** active-state co-fold on **6X18**; optional explicit-state **GaMD (OpenMM)** for TM6-opening — hypothesis-only.
- **Novelty/dev:** **FoldSeek + MMseqs2** (installed to `tools/`), ESMFold2 (monomer pLDDT = expression), ESM-2 / ESMC-300M (naturalness), anarcism (antibody format).

## Environment policy

`uv` only for the core env; **heavy tools live in isolated per-tool venvs** (reuse the sibling repos' `.venv-*`
and the Anthropic `third_party/uplifting-biomolecular-modeling` kit — byte-pinned, `--det 1` for reproducible
submitted artifacts). Reuse weight caches (`~/.boltz`, `chai_downloads`, `protenix_cache`, `hf_cache`). One process
per GPU; default 4 GPUs; burst to 8 only in idle windows.
