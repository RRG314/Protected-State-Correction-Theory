from __future__ import annotations

import csv
import json
from pathlib import Path

import pytest

ROOT = Path('/Users/stevenreid/Documents/New project/repos/ocp-research-program')
SUMMARY_JSON = ROOT / 'data/generated/validations/professional_validation_summary.json'
KNOWN_CSV = ROOT / 'data/generated/validations/professional_known_results_matrix.csv'
ADVERSARIAL_CSV = ROOT / 'data/generated/validations/professional_adversarial_matrix.csv'
SNAPSHOT_JS = ROOT / 'docs/workbench/lib/generatedValidationSnapshot.js'
REPORT_PATH = ROOT / 'docs/app/professional-validation-report.md'


def _load_summary() -> dict[str, object]:
    if not SUMMARY_JSON.exists():
        pytest.skip(f'missing generated artifact: {SUMMARY_JSON}')
    return json.loads(SUMMARY_JSON.read_text(encoding='utf-8'))


def _load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        pytest.skip(f'missing generated artifact: {path}')
    with path.open(newline='', encoding='utf-8') as fh:
        return list(csv.DictReader(fh))


def test_professional_validation_counts_match_exported_csvs() -> None:
    summary = _load_summary()
    known_rows = _load_csv(KNOWN_CSV)
    adversarial_rows = _load_csv(ADVERSARIAL_CSV)

    assert summary['knownResults']['total'] == len(known_rows)
    assert summary['knownResults']['passed'] == sum(1 for row in known_rows if row['pass'] == 'yes')
    assert summary['adversarial']['total'] == len(adversarial_rows)
    assert summary['adversarial']['passed'] == sum(1 for row in adversarial_rows if row['pass'] == 'yes')


def test_generated_validation_snapshot_matches_summary_counts() -> None:
    summary = _load_summary()
    if not SNAPSHOT_JS.exists():
        pytest.skip(f'missing generated snapshot: {SNAPSHOT_JS}')
    text = SNAPSHOT_JS.read_text(encoding='utf-8')

    assert str(summary['knownResults']['passed']) in text
    assert str(summary['knownResults']['total']) in text
    assert str(summary['adversarial']['passed']) in text
    assert str(summary['adversarial']['total']) in text
    assert str(summary['workflows']['passed']) in text
    assert str(summary['workflows']['total']) in text


@pytest.mark.parametrize('path', [ROOT / 'README.md', ROOT / 'FINAL_REPORT.md', ROOT / 'SYSTEM_REPORT.md', REPORT_PATH])
def test_reports_link_professional_validation_surface(path: Path) -> None:
    text = path.read_text(encoding='utf-8')
    assert 'professional-validation-report.md' in text or path == REPORT_PATH
