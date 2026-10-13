"""Submission-contract tests (schema, length, format, uniqueness, caps, byte-repro)."""
from __future__ import annotations

from pathlib import Path

from adaptyv_glp1r.submission import (
    LEN_MAX,
    LEN_MIN,
    canonicalize_molecule_class,
    length_category,
    validate_csv,
    validate_rows,
    write_submission,
)

# A well-formed single-chain row (natural AAs, in-range length, de-novo-looking).
_GOOD = "DEEKLAKELAEKLEEAGVSEEEIKKAIELFKKAGADEEEIKKLAEELGLSEEEAKKFLE"  # 58 aa
_GOOD2 = "SPEDLKRALEELKRRGFSPEEIEKALELFKEHGVDPEEIKKLAEELGISEEELKKAFKD"  # 58 aa


def _rows(*triples):
    return [{"name": n, "sequence": s, "molecule_class": m} for (n, s, m) in triples]


def test_good_single_chain_passes():
    rep = validate_rows(_rows(("d1", _GOOD, "protein"), ("d2", _GOOD2, "protein")), track=3)
    assert rep.ok, rep.errors + [e for r in rep.rows for e in r.errors]


def test_single_chain_alias_accepted():
    # Both 'protein' and 'single_chain' are accepted single-chain aliases.
    for cls in ("protein", "single_chain"):
        rep = validate_rows(_rows(("d", _GOOD, cls)), track=3)
        assert rep.ok, (cls, rep.errors)


def test_canonicalize_alias():
    assert canonicalize_molecule_class("single_chain") == "protein"
    assert canonicalize_molecule_class("protein") == "protein"
    assert canonicalize_molecule_class("nanobody") == "nanobody"


def test_bad_molecule_class_fails():
    rep = validate_rows(_rows(("d", _GOOD, "peptide")), track=3)
    assert not rep.ok


def test_nonstandard_residue_fails():
    rep = validate_rows(_rows(("d", _GOOD[:-1] + "X", "protein")), track=3)
    assert not rep.ok


def test_length_bounds():
    short = "A" * (LEN_MIN - 1)
    long = "A" * (LEN_MAX + 1)
    assert not validate_rows(_rows(("s", short, "protein")), track=3).ok
    assert not validate_rows(_rows(("l", long, "protein")), track=3).ok


def test_length_category():
    assert length_category(30) == "protein_microbinder"
    assert length_category(70) == "protein_minibinder"
    assert length_category(180) == "large_protein"


def test_fab_requires_single_colon():
    # single-chain class must NOT contain ':'
    assert not validate_rows(_rows(("x", _GOOD + ":" + _GOOD2, "protein")), track=3).ok
    # fab must contain exactly one ':'
    assert not validate_rows(_rows(("x", _GOOD, "fab_kappa")), track=3).ok


def test_duplicate_name_and_sequence_fail():
    assert not validate_rows(_rows(("dup", _GOOD, "protein"), ("dup", _GOOD2, "protein")), track=3).ok
    assert not validate_rows(_rows(("a", _GOOD, "protein"), ("b", _GOOD, "protein")), track=3).ok


def test_track_cap():
    rows = _rows(*[(f"d{i}", _GOOD[:LEN_MIN] + ("A" * i), "protein") for i in range(21)])
    assert not validate_rows(rows, track=3).ok  # 21 > 20


def test_write_submission_byte_reproducible(tmp_path: Path):
    rows = _rows(("d1", _GOOD, "single_chain"), ("d2", _GOOD2, "protein"))
    p1 = write_submission(rows, tmp_path / "a.csv")
    p2 = write_submission(rows, tmp_path / "b.csv")
    b1, b2 = p1.read_bytes(), p2.read_bytes()
    assert b1 == b2
    # canonicalization rewrote the 'single_chain' alias to 'protein'
    assert b"single_chain" not in b1 and b"protein" in b1
    # round-trips through the validator
    assert validate_csv(p1, track=3).ok


def test_example_fixture_passes():
    ex = Path(__file__).resolve().parents[1] / "submissions" / "example_track3.csv"
    if ex.exists():
        assert validate_csv(ex, track=3).ok
