from __future__ import annotations

import csv
import json
import os
from pathlib import Path
import subprocess

ROOT = Path('/Users/stevenreid/Documents/New project/repos/ocp-research-program')


def _run_major_expansion() -> None:
    subprocess.run(
        ['python3', 'scripts/compare/run_major_expansion_candidate.py'],
        cwd=ROOT,
        check=True,
        env={**os.environ, 'PYTHONPATH': 'src'},
    )


def test_major_expansion_artifacts_exist_and_have_expected_schema() -> None:
    _run_major_expansion()

    ranking_path = ROOT / 'data/generated/discovery/major_expansion_lane_ranking.csv'
    anomalies_path = ROOT / 'data/generated/discovery/major_expansion_anomalies.csv'
    summary_path = ROOT / 'data/generated/discovery/major_expansion_summary.json'

    assert ranking_path.exists() and ranking_path.stat().st_size > 0
    assert anomalies_path.exists() and anomalies_path.stat().st_size > 0
    assert summary_path.exists() and summary_path.stat().st_size > 0

    with ranking_path.open() as handle:
        ranking_rows = list(csv.DictReader(handle))
    assert len(ranking_rows) == 5
    selected = [row for row in ranking_rows if row['selected_for_deep_development'] == 'True']
    assert len(selected) == 2

    with anomalies_path.open() as handle:
        anomaly_rows = list(csv.DictReader(handle))
    assert len(anomaly_rows) >= 5

    summary = json.loads(summary_path.read_text())
    assert summary['status'] == 'EXPLORATION / NON-PROMOTED'
    assert len(summary['selected_top2_lanes']) == 2
    assert summary['final_recommendation'] in {
        'INTEGRATE AS MAJOR NEW REPO LAYER',
        'KEEP AS CONDITIONAL MAJOR CANDIDATE',
        'KEEP AS BENCHMARK/APPLICATION LANE ONLY',
        'REJECT AS NOT SUBSTANTIAL ENOUGH',
    }


def test_major_expansion_report_and_support_docs_are_present() -> None:
    report_path = ROOT / 'docs/research-program/major_expansion_candidate_report.md'
    overview_path = ROOT / 'docs/research-program/context_invariant_recoverability_overview.md'
    theorem_path = ROOT / 'docs/research-program/context_invariant_recoverability_theorem_candidates.md'
    nogo_path = ROOT / 'docs/research-program/context_invariant_recoverability_no_go_candidates.md'
    plan_path = ROOT / 'docs/research-program/context_invariant_recoverability_validation_plan.md'

    for path in (report_path, overview_path, theorem_path, nogo_path, plan_path):
        assert path.exists(), f'missing expected output file: {path}'
        assert path.stat().st_size > 0, f'empty expected output file: {path}'

    report = report_path.read_text(encoding='utf-8')
    assert 'Status: **EXPLORATION / NON-PROMOTED**' in report
    assert '## 5. Stage 4 Falsification Counterattack' in report
    assert 'Final recommendation:' in report
