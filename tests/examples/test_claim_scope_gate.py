from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GATE_PATH = ROOT / 'scripts' / 'validate' / 'check_claim_scope.py'


def _load_gate_module():
    spec = importlib.util.spec_from_file_location('claim_scope_gate', GATE_PATH)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_forbidden_phrase_is_flagged() -> None:
    gate = _load_gate_module()
    out = gate.line_violations('docs/theorem-core/example.md', 'This is a new theory of information.')
    assert any('forbidden claim phrase' in row for row in out)


def test_negated_universal_phrase_is_allowed() -> None:
    gate = _load_gate_module()
    out = gate.line_violations('docs/theorem-core/example.md', 'This is not a universal scalar invariant claim.')
    assert out == []


def test_unscoped_universal_phrase_is_flagged() -> None:
    gate = _load_gate_module()
    out = gate.line_violations('docs/restricted-results/example.md', 'We found a universal scalar invariant.')
    assert any('unscoped universal phrasing' in row for row in out)


def test_universal_law_of_information_phrase_is_flagged() -> None:
    gate = _load_gate_module()
    out = gate.line_violations('docs/theorem-core/example.md', 'This establishes a universal law of information.')
    assert any('unscoped universal phrasing' in row for row in out)


def test_sds_unguarded_in_theorem_lane_is_flagged() -> None:
    gate = _load_gate_module()
    out = gate.line_violations('docs/theorem-core/example.md', 'SDS theorem package extends all core results.')
    assert any('SDS mention in theorem/restricted lane without scope guard' in row for row in out)


def test_sds_guarded_line_is_allowed() -> None:
    gate = _load_gate_module()
    out = gate.line_violations('docs/restricted-results/example.md', 'SDS is ANALOGY ONLY and not theorem-core.')
    assert out == []


def test_forbidden_fundamentalism_phrase_is_flagged() -> None:
    gate = _load_gate_module()
    out = gate.line_violations('README.md', 'Information is fundamental.')
    assert any('forbidden claim phrase' in row for row in out)
