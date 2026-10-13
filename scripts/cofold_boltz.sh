#!/bin/bash
# Single-GPU Boltz-2 cofold — thin wrapper around the sharded workhorse (dedup; inherits its fixes).
# Usage: cofold_boltz.sh <csv> <target_seq_file> <tag> [gpu=0] [seeds=0]
exec bash "$(dirname "$0")/cofold_boltz_shard.sh" "${1:?csv}" "${2:?target_seq_file}" "${3:-cal}" "${4:-0}" "${5:-0}"
