#!/bin/bash
# Local novelty pre-screen (sequence + structure) = relative-rank / risk-flag ONLY.
# The Proteinbase portal novelty score is the AUTHORITY — always re-check it before upload (AGENTS.md).
# Full run needs reference DBs (SwissProt/PDB/AFDB) built in Stage 5 (F7); this checks tool availability
# and prints the intended commands until those DBs exist.
set -euo pipefail
cd "$(dirname "$0")/.."
FOLDSEEK=tools/foldseek/bin/foldseek
MMSEQS=tools/mmseqs/bin/mmseqs

if [ -x "$MMSEQS" ]; then "$MMSEQS" version; else echo "mmseqs MISSING -> scripts/setup_tools.sh novelty"; fi
if [ -x "$FOLDSEEK" ]; then "$FOLDSEEK" version; else echo "foldseek MISSING -> scripts/setup_tools.sh novelty"; fi

cat <<'EOF'
Novelty gate (Stage 5 / F7), eligibility thresholds from configs/filters.yaml:
  sequence : mmseqs easy-search designs.fasta <SwissProt+PDB+patents+AbDB DB> hits tmp --min-seq-id 0.3
             -> any hit >30% id to a known protein (esp. GLP-1/exendin/glucagon/semaglutide) = FLAG
  structure: foldseek easy-search designs_pdb/ <PDB/AFDB DB> aln tmp --alignment-type 1
             -> max TM >= 0.5 (moderate) = FLAG (helical bundles may cap at level 3 structurally)
Authority = the Proteinbase portal novelty score. Re-check every design before the (user-gated) upload.
EOF
