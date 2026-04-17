from __future__ import annotations

import json
from pathlib import Path
import subprocess

import numpy as np

from ocp.decision_layer import decision_layer_example_report

ROOT = Path('/Users/stevenreid/Documents/New project/repos/ocp-research-program')


def _load() -> dict[str, object]:
    path = ROOT / 'data/generated/unified-recoverability/decision_layer_summary.json'
    subprocess.run(
        ['python3', 'scripts/compare/run_decision_layer_examples.py'],
        cwd=ROOT,
        check=True,
    )
    return json.loads(path.read_text())


def test_decision_layer_summary_matches_recomputed_examples() -> None:
    saved = _load()
    report = decision_layer_example_report()

    assert saved['recommended_scope'] == report.recommended_scope
    assert saved['belongs_in_branch'] == report.belongs_in_branch
    assert saved['deserves_new_branch'] == report.deserves_new_branch
    assert saved['strongest_value'] == report.strongest_value
    assert saved['strongest_failure'] == report.strongest_failure

    saved_rows = {(row['family'], row['scenario']): row for row in saved['rows']}
    assert len(saved_rows) == len(report.rows)
    for row in report.rows:
        saved_row = saved_rows[(row.family, row.scenario)]
        assert saved_row['action'] == row.action
        assert saved_row['status'] == row.status
        assert tuple(saved_row['supporting_claims']) == row.supporting_claims
        assert saved_row['current_regime'] == row.current_regime
        assert saved_row['rationale'] == row.rationale
        if saved_row['notes'] != row.notes:
            # Tiny residual values in notes can jitter at machine epsilon scale.
            if ' = ' in saved_row['notes'] and ' = ' in row.notes:
                saved_prefix, saved_value = saved_row['notes'].rsplit(' = ', 1)
                row_prefix, row_value = row.notes.rsplit(' = ', 1)
                assert saved_prefix == row_prefix
                assert np.isclose(float(saved_value), float(row_value), atol=1e-12)
            else:
                assert saved_row['notes'] == row.notes
        assert saved_row['adds_value_beyond_regime'] == row.adds_value_beyond_regime
