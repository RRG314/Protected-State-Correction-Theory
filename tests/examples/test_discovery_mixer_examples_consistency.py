from __future__ import annotations

import json
from pathlib import Path

from ocp.discovery_mixer import discovery_mixer_demo_reports


REPO_ROOT = Path(__file__).resolve().parents[2]
SUMMARY_PATH = REPO_ROOT / 'data' / 'generated' / 'discovery_mixer' / 'discovery_mixer_summary.json'


def test_discovery_mixer_generated_summary_matches_source() -> None:
    saved = json.loads(SUMMARY_PATH.read_text(encoding='utf-8'))
    current = discovery_mixer_demo_reports()
    assert saved['summary'] == current['summary']
    assert {key: value['regime'] for key, value in saved['demos'].items()} == {key: value['regime'] for key, value in current['demos'].items()}
