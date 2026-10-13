"""Fetch a receptor MSA (a3m) from the public ColabFold MMseqs2 API for a PUBLIC
protein sequence (GLP1R P43220 — not proprietary; the undisclosed construct
mutations are NOT used, we send WT). This is the lightweight alternative to the
~50 GB uniclust30 + hh-suite install that EvoBind's design_local.sh assumes
(absent here). HTTPS only (env constraint). Writes <out>.a3m.

Usage: uv run python scripts/fetch_msa_colabfold.py <fasta_in> <a3m_out> [mode=env]
"""
from __future__ import annotations

import os
import sys
import tarfile
import time
import urllib.parse
import urllib.request

HOST = "https://api.colabfold.com"
UA = {"User-Agent": "glp1r-design/1.0"}


def _post(path, data):
    req = urllib.request.Request(HOST + path, data=urllib.parse.urlencode(data).encode(),
                                 headers=UA, method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode()


def _get(path):
    req = urllib.request.Request(HOST + path, headers=UA)
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


def read_seq(fasta):
    seq = []
    for ln in open(fasta):
        if ln.startswith(">"):
            continue
        seq.append(ln.strip())
    return "".join(seq)


def main():
    fasta, out = sys.argv[1], sys.argv[2]
    mode = sys.argv[3] if len(sys.argv) > 3 else "env"
    seq = read_seq(fasta)
    query = f">query\n{seq}\n"
    print(f"[msa] submit len={len(seq)} mode={mode}", flush=True)
    import json
    sub = json.loads(_post("/ticket/msa", {"q": query, "mode": mode}))
    tid = sub["id"]
    print(f"[msa] ticket={tid} status={sub.get('status')}", flush=True)
    # poll
    for i in range(240):  # up to ~20 min
        st = json.loads(_get(f"/ticket/{tid}").decode())
        s = st.get("status")
        if s == "COMPLETE":
            break
        if s in ("ERROR", "MAINTENANCE", "UNKNOWN"):
            raise SystemExit(f"[msa] server status {s}")
        time.sleep(5)
    else:
        raise SystemExit("[msa] timed out")
    print("[msa] COMPLETE -> downloading", flush=True)
    tgz = out + ".tar.gz"
    with open(tgz, "wb") as f:
        f.write(_get(f"/result/download/{tid}"))
    # extract the uniref/env a3m(s); concatenate into one a3m
    a3ms = []
    with tarfile.open(tgz) as t:
        for m in t.getmembers():
            if m.name.endswith(".a3m"):
                a3ms.append((m.name, t.extractfile(m).read().decode()))
    if not a3ms:
        raise SystemExit("[msa] no a3m in result tar")
    # prefer a single merged a3m; colabfold returns uniref.a3m (+ bfd.mgnify...). Concatenate unique.
    merged = max(a3ms, key=lambda kv: len(kv[1]))  # the largest a3m = the full MSA
    with open(out, "w") as f:
        f.write(merged[1])
    nseq = merged[1].count(">")
    print(f"[msa] wrote {out} from {merged[0]} ({nseq} sequences). members={[a[0] for a in a3ms]}", flush=True)
    os.remove(tgz)


if __name__ == "__main__":
    main()
