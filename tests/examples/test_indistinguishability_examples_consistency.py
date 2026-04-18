from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path('/Users/stevenreid/Documents/New project/repos/ocp-research-program')
DATA_DIR = ROOT / 'data/generated/indistinguishability'


def test_indistinguishability_artifacts_exist_and_have_expected_schema() -> None:
    metrics_path = DATA_DIR / 'indistinguishability_metrics.csv'
    summary_path = DATA_DIR / 'indistinguishability_summary.json'
    anomalies_path = DATA_DIR / 'indistinguishability_anomalies.csv'

    assert metrics_path.exists() and metrics_path.stat().st_size > 0
    assert summary_path.exists() and summary_path.stat().st_size > 0
    assert anomalies_path.exists()

    with metrics_path.open(newline='') as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
    assert rows, 'indistinguishability metrics must contain at least one system row'

    required_columns = {
        'system_id',
        'family',
        'rank',
        'max_fiber_size',
        'percent_mixed',
        'DLS',
        'kappa_0',
        'Gamma_r',
        'delta',
        'status_label',
    }
    assert required_columns.issubset(set(rows[0].keys()))
    assert all(row['status_label'] == 'EXPLORATION / NON-PROMOTED' for row in rows)

    families = {row['family'] for row in rows}
    assert {'restricted-linear', 'periodic-cfd', 'bounded-cfd', 'mhd-proxy'}.issubset(families)

    with summary_path.open() as handle:
        summary = json.load(handle)
    assert summary.get('status_label') == 'EXPLORATION / NON-PROMOTED'
    assert int(summary.get('system_count', 0)) == len(rows)
    assert isinstance(summary.get('correlations'), dict)
    assert isinstance(summary.get('plot_files'), list)


def test_indistinguishability_report_is_explicitly_non_promoted() -> None:
    report_path = ROOT / 'docs/research-program/indistinguishability_exploration.md'
    assert report_path.exists() and report_path.stat().st_size > 0
    text = report_path.read_text(encoding='utf-8')
    assert 'EXPLORATION / NON-PROMOTED' in text
    assert 'does not modify theorem status' in text

