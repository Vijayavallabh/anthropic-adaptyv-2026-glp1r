#!/bin/bash
# Install auxiliary tools into tools/ (gitignored). Idempotent. Static binaries, no compile.
#   scripts/setup_tools.sh novelty   # FoldSeek + MMseqs2 (the novelty gate; absent from the base install)
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p tools

case "${1:-}" in
  novelty)
    if [ ! -x tools/foldseek/bin/foldseek ]; then
      echo "=== downloading FoldSeek (static, avx2) ==="
      curl -fsSL https://mmseqs.com/foldseek/foldseek-linux-avx2.tar.gz -o tools/foldseek.tar.gz
      tar -xzf tools/foldseek.tar.gz -C tools/ && rm -f tools/foldseek.tar.gz
    fi
    tools/foldseek/bin/foldseek version
    if [ ! -x tools/mmseqs/bin/mmseqs ]; then
      echo "=== downloading MMseqs2 (static, avx2) ==="
      curl -fsSL https://mmseqs.com/latest/mmseqs-linux-avx2.tar.gz -o tools/mmseqs.tar.gz
      tar -xzf tools/mmseqs.tar.gz -C tools/ && rm -f tools/mmseqs.tar.gz
    fi
    tools/mmseqs/bin/mmseqs version
    echo "=== novelty tools ready in tools/ (gitignored) ==="
    ;;
  *)
    echo "usage: scripts/setup_tools.sh novelty"
    exit 2
    ;;
esac
