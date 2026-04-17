#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from dataclasses import asdict, is_dataclass
from pathlib import Path

from ocp.decision_layer import decision_layer_example_report

ROOT = Path('/Users/stevenreid/Documents/New project/repos/ocp-research-program')
OUT = ROOT / 'data/generated/unified-recoverability'


def _serialize(value):
    if is_dataclass(value):
        return {key: _serialize(item) for key, item in asdict(value).items()}
    if isinstance(value, dict):
        return {str(key): _serialize(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_serialize(item) for item in value]
    return value


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        return
    with path.open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    report = decision_layer_example_report()

    summary = _serialize(report)
    (OUT / 'decision_layer_summary.json').write_text(json.dumps(summary, indent=2))

    write_csv(
        OUT / 'decision_layer_examples.csv',
        [
            {
                'family': row.family,
                'scenario': row.scenario,
                'action': row.action,
                'status': row.status,
                'supporting_claims': ' '.join(row.supporting_claims),
                'current_regime': row.current_regime,
                'rationale': row.rationale,
                'notes': row.notes,
                'adds_value_beyond_regime': row.adds_value_beyond_regime,
            }
            for row in report.rows
        ],
    )

    print(f'wrote {OUT / "decision_layer_summary.json"}')
    print(f'wrote {OUT / "decision_layer_examples.csv"}')


if __name__ == '__main__':
    main()
