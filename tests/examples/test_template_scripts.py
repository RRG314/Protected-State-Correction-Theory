from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path('/Users/stevenreid/Documents/New project/repos/ocp-research-program')
SCRIPTS = {
    'restricted_linear': ROOT / 'scripts/templates/restricted_linear_recovery_template.py',
    'functional_observability': ROOT / 'scripts/templates/functional_observability_template.py',
    'periodic_projection': ROOT / 'scripts/templates/periodic_projection_template.py',
    'ambiguity_witness': ROOT / 'scripts/templates/ambiguity_witness_template.py',
    'no_go_detection': ROOT / 'scripts/templates/no_go_detection_template.py',
    'minimal_information': ROOT / 'scripts/templates/minimal_information_sweep_template.py',
    'asymptotic_observer': ROOT / 'scripts/templates/asymptotic_observer_template.py',
    'exact_projector': ROOT / 'scripts/templates/exact_projector_template.py',
}


def _run(path: Path) -> dict[str, object]:
    completed = subprocess.run(
        ['python3', str(path)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(completed.stdout)


def test_template_scripts_emit_expected_payloads() -> None:
    restricted = _run(SCRIPTS['restricted_linear'])
    assert restricted['exact_recoverable'] is False
    assert restricted['minimal_added_measurements'] == 1

    functional = _run(SCRIPTS['functional_observability'])
    assert functional['exact_rows']
    assert functional['observer_reports']

    periodic = _run(SCRIPTS['periodic_projection'])
    assert periodic['minimal_exact_cutoffs']['low_mode_sum'] == 2
    assert periodic['minimal_exact_cutoffs']['bandlimited_contrast'] == 3

    witness = _run(SCRIPTS['ambiguity_witness'])
    assert witness['protected_gap'] > 0.1

    no_go = _run(SCRIPTS['no_go_detection'])
    assert no_go['exact_recoverable'] is False
    assert no_go['nullspace_protected_gap'] > 0.1

    minimal = _run(SCRIPTS['minimal_information'])
    assert minimal['minimal_exact_horizons']['three_active'] == 3

    observer = _run(SCRIPTS['asymptotic_observer'])
    assert observer['spectral_radius'] < 1.0
    assert observer['protected_error_history'][-1] < observer['protected_error_history'][0]

    projector = _run(SCRIPTS['exact_projector'])
    assert projector['recovery_error'] < 1e-10
