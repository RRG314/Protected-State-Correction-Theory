from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path('/Users/stevenreid/Documents/New project/repos/ocp-research-program')


def _load_json(path: Path) -> dict[str, object]:
    if not path.exists():
        pytest.skip(f'missing generated artifact: {path}')
    return json.loads(path.read_text())


def test_workbench_examples_json_contains_consistent_mixer_examples() -> None:
    data = _load_json(ROOT / 'data/generated/validations/workbench_examples.json')

    structured = data['mixerStructuredLinear']
    assert structured['family'] == 'linear'
    assert structured['mode'] == 'structured'
    assert structured['regime'] == 'impossible'
    assert structured['chosenRecommendation']['patch']['mode'] == 'structured'
    assert structured['chosenRecommendation']['patch']['family'] == 'linear'

    periodic = data['mixerPeriodicDemo']
    assert periodic['family'] == 'periodic'
    assert periodic['mode'] == 'structured'
    assert periodic['regime'] == 'impossible'
    assert periodic['comparison']['afterRegime'] == 'exact'

    custom = data['mixerCustomLinear']
    assert custom['family'] == 'linear'
    assert custom['mode'] == 'custom'
    assert custom['regime'] == 'impossible'
    assert custom['comparison']['afterRegime'] == 'exact'

    boundary = data['mixerBoundary']
    assert boundary['family'] == 'boundary'
    assert boundary['regime'] == 'impossible'
    assert boundary['comparison']['afterRegime'] == 'exact'
