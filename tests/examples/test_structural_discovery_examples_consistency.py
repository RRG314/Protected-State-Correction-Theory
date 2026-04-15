from __future__ import annotations

import json
from pathlib import Path
import subprocess

import numpy as np

from ocp.structural_discovery import structural_discovery_demo_reports

ROOT = Path('/Users/stevenreid/Documents/New project/repos/ocp-research-program')


def _load() -> dict[str, object]:
    path = ROOT / 'data/generated/structural_discovery/structural_discovery_summary.json'
    if not path.exists():
        subprocess.run(
            ['python3', 'scripts/compare/run_structural_discovery_examples.py'],
            cwd=ROOT,
            check=True,
        )
    return json.loads(path.read_text())


def test_structural_discovery_examples_match_recomputed_demo_reports() -> None:
    saved = _load()
    recomputed = structural_discovery_demo_reports()
    assert saved['summary'] == recomputed['summary']

    for demo_name, report in recomputed['demos'].items():
        saved_report = saved['demos'][demo_name]
        assert saved_report['family'] == report['family']
        assert saved_report['current_regime'] == report['current_regime']
        assert saved_report['failure_modes'] == list(report['failure_modes'])
        assert saved_report['missing_structure'] == report['missing_structure']
        assert saved_report['weaker_targets'] == list(report['weaker_targets'])
        for key, value in report['metrics'].items():
            saved_value = saved_report['metrics'][key]
            if isinstance(value, float):
                assert np.isclose(saved_value, value)
            else:
                assert saved_value == value
        assert saved_report['chosen_fix'] == report['chosen_fix']
        assert saved_report['comparison'] == report['comparison']
