from __future__ import annotations

import json
from pathlib import Path
import subprocess

import numpy as np

from ocp.design import linear_recoverability_design_report

ROOT = Path('/Users/stevenreid/Documents/New project/repos/ocp-research-program')


OBSERVATION = np.array(
    [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 1.0],
    ]
)
CANDIDATES = [
    np.array([0.0, 1.0, 0.0]),
    np.array([0.0, 0.0, 1.0]),
    np.array([1.0, 1.0, 0.0]),
]


def _load() -> dict[str, object]:
    path = ROOT / 'data/generated/design/design_template_examples.json'
    if not path.exists():
        subprocess.run(
            ['python3', 'scripts/compare/run_design_examples.py'],
            cwd=ROOT,
            check=True,
        )
    return json.loads(path.read_text())


def _normalize(report) -> tuple[bool, int | None, tuple[tuple[int, ...], ...]]:
    return (
        bool(report.exact_recoverable),
        report.minimal_added_measurements,
        tuple(tuple(int(index) for index in combo) for combo in report.candidate_exact_sets),
    )


def test_design_examples_json_matches_linear_reports() -> None:
    data = _load()

    tail_pair = linear_recoverability_design_report(
        OBSERVATION,
        np.array(
            [
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 1.0],
            ]
        ),
        candidate_rows=CANDIDATES,
    )
    x3_only = linear_recoverability_design_report(
        OBSERVATION,
        np.array([[0.0, 0.0, 1.0]]),
        candidate_rows=CANDIDATES,
    )
    weaker_sum = linear_recoverability_design_report(
        OBSERVATION,
        np.array([[0.0, 1.0, 1.0]]),
        candidate_rows=CANDIDATES,
    )

    assert _normalize(tail_pair) == (
        data['linear_tail_pair']['report']['exact_recoverable'],
        data['linear_tail_pair']['report']['minimal_added_measurements'],
        tuple(tuple(combo) for combo in data['linear_tail_pair']['report']['candidate_exact_sets']),
    )
    assert _normalize(x3_only) == (
        data['linear_x3_only']['report']['exact_recoverable'],
        data['linear_x3_only']['report']['minimal_added_measurements'],
        tuple(tuple(combo) for combo in data['linear_x3_only']['report']['candidate_exact_sets']),
    )
    assert _normalize(weaker_sum) == (
        data['linear_weaker_sum']['report']['exact_recoverable'],
        data['linear_weaker_sum']['report']['minimal_added_measurements'],
        tuple(tuple(combo) for combo in data['linear_weaker_sum']['report']['candidate_exact_sets']),
    )
    assert data['linear_weaker_sum']['report']['exact_recoverable'] is True
    assert data['linear_tail_pair']['report']['exact_recoverable'] is False
