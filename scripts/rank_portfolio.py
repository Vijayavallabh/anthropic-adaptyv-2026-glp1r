"""F8 - rank the keep-candidates best-first and select <=20 for the Track-3 submission.

The scoring formula the organizer uses is UNSPECIFIED (do not invent it). This is our OWN
disclosed internal ranking, not presented as the organizer's. Priority order from AGENTS.md:
agonism (the only win condition) > binding (the gate) > novelty/developability. Because binding-
only ECD designs lean antagonist and cannot win the functional assay, the agonism peptides are the
win-path and lead; within each arm we order by a quality composite. Everything is LOW-confidence on
agonism (no in-silico score proves it). Diversity cap: <=2 per lineage (ECD backbone / peptide run).

Composite (disclosed weights):
  0.40*arm_prize + 0.10*binding_norm(within-arm) + 0.25*dev_score + 0.25*elig_safety
  arm_prize   : agonism-peptide=1.0, binding-hedge=0.0   (encodes the prize priority)
  binding_norm: within-arm min-max of the binding proxy (if_dist / pae; lower=better -> higher norm).
                Low weight on purpose: the peptide if_dist band is narrow (5.0-6.3) and a weak proxy.
  dev_score   : 1.0 minus GRADED developability penalties from the numeric columns (instability
                magnitude, low-complexity fraction, unpaired Cys, hydrophobicity)
  elig_safety : 1 - coverage-gated known-agonist concern (same cov-gating as the eligibility gate:
                a high id over tiny coverage is spurious/safe; a high id over >=50% coverage is a real
                compliance risk). Weighted heavily - accidental incretin resemblance is the key risk.

Usage: uv run python scripts/rank_portfolio.py [max_designs=20]
Writes runs/portfolio/ranked.csv (full, with scores) + prints the ranked table.
"""
from __future__ import annotations
import csv, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(REPO, "data/candidates/candidates.csv")
OUT = os.path.join(REPO, "data/candidates/ranked.csv")
LINEAGE_CAP = 2
COV_MIN = 0.50   # matches eligibility_check.COV_MIN
W = {"arm_prize": 0.40, "binding": 0.10, "dev": 0.25, "elig": 0.25}


def dev_score(r):
    """Graded developability score from the numeric columns (not the flag string, which loses magnitude)."""
    s = 1.0
    instab = float(r.get("instability") or 0)
    maxfrac = float(r.get("max_aa_frac") or 0)
    cys = int(r.get("cys") or 0)
    gravy = float(r.get("gravy") or 0)
    if instab > 40:
        s -= min(0.45, (instab - 40) / 100.0)   # 42->0.02, 60->0.20, >=85->0.45 cap (123 is awful)
    if maxfrac > 0.30:
        s -= min(0.30, (maxfrac - 0.30) * 2.0)   # poly-X low complexity
    if cys % 2 == 1:
        s -= 0.15                                # unpaired Cys liability
    if gravy > 0.5:
        s -= 0.15                                # too hydrophobic
    return max(0.0, round(s, 3))


def elig_safety(r):
    """1 - coverage-gated concern. High id over tiny coverage is spurious (safe); high id over
    >=COV_MIN coverage is a real incretin-resemblance / compliance risk."""
    pid = float(r["elig_id_pct"]); cov = float(r["elig_cov"])
    concern = pid if cov >= COV_MIN else pid * cov / COV_MIN
    return max(0.0, 1.0 - concern / 100.0)


def lineage(r):
    if r["arm"] == "binding-hedge":
        core = r["name"][4:] if r["name"].startswith("ecd_") else r["name"]
        parts = core.split("_")
        return f"ecd_{parts[1]}" if len(parts) > 1 else core   # backbone index: des_2_4 & des_2_6 -> ecd_2
    return r["name"]                                            # each peptide run is its own lineage


def main():
    max_designs = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    rows = [r for r in csv.DictReader(open(CSV)) if r["status"] == "keep" and r["eligible"] == "True"]
    # within-arm min-max of the binding proxy (lower value = better -> norm 1)
    for arm in {r["arm"] for r in rows}:
        vals = [float(r["binding_value"]) for r in rows if r["arm"] == arm]
        lo, hi = min(vals), max(vals)
        for r in rows:
            if r["arm"] == arm:
                r["binding_norm"] = 1.0 if hi == lo else (hi - float(r["binding_value"])) / (hi - lo)
    for r in rows:
        r["dev_sc"] = dev_score(r)
        r["elig_safety"] = round(elig_safety(r), 3)
        r["arm_prize"] = 1.0 if r["arm"] == "agonism-peptide" else 0.0
        r["composite"] = round(W["arm_prize"] * r["arm_prize"] + W["binding"] * r["binding_norm"]
                               + W["dev"] * r["dev_sc"] + W["elig"] * r["elig_safety"], 4)
    rows.sort(key=lambda r: -r["composite"])
    # enforce lineage cap, take up to max_designs
    picked, seen = [], {}
    for r in rows:
        lin = lineage(r)
        if seen.get(lin, 0) >= LINEAGE_CAP:
            r["_skipped"] = f"lineage-cap({lin})"
            continue
        seen[lin] = seen.get(lin, 0) + 1
        picked.append(r)
        if len(picked) >= max_designs:
            break

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    cols = ["rank", "name", "arm", "composite", "arm_prize", "binding_norm", "dev_sc", "elig_safety",
            "binding_metric", "binding_value", "dev_flags", "struct_nov_maxTM", "molecule_class", "sequence"]
    with open(OUT, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for i, r in enumerate(picked, 1):
            r["rank"] = i
            r["binding_norm"] = round(r["binding_norm"], 3)
            w.writerow(r)

    print(f"# ranked {len(picked)} / {len(rows)} keep-eligible (cap {LINEAGE_CAP}/lineage, max {max_designs})")
    print(f"{'#':>2} {'name':<14}{'arm':<16}{'comp':>6}{'bindN':>7}{'dev':>5}{'elig':>5}  {'metric':<16}{'flags'}")
    for i, r in enumerate(picked, 1):
        print(f"{i:>2} {r['name']:<14}{r['arm']:<16}{r['composite']:>6}{r['binding_norm']:>7}{r['dev_sc']:>5.2f}"
              f"{r['elig_safety']:>5.2f}  {r['binding_metric']+'='+r['binding_value']:<16}{r['dev_flags']}")
    print(f"# wrote {OUT}")


if __name__ == "__main__":
    main()
