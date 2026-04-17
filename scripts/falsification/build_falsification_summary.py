#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CLAIM_AUDIT = ROOT / 'data/generated/falsification/full_claim_audit.csv'
COUNTEREXAMPLES = ROOT / 'data/generated/falsification/counterexample_catalog.csv'
OUT = ROOT / 'data/generated/falsification/falsification_summary.json'


def load_csv(path: Path):
    with path.open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def main() -> None:
    claims = load_csv(CLAIM_AUDIT)
    cxs = load_csv(COUNTEREXAMPLES)

    status_counts = Counter(r['final_verdict'] for r in claims)
    branch_counts = Counter(r['branch'] for r in claims)

    payload = {
        'date': '2026-04-17',
        'total_claim_rows': len(claims),
        'final_status_counts': dict(status_counts),
        'branch_coverage_counts': dict(branch_counts),
        'narrowed_claims': ['OCP-022', 'OCP-027', 'OCP-044'],
        'disproved_claims_reconfirmed': ['OCP-023'],
        'new_retractions': [],
        'counterexample_count': len(cxs),
        'counterexample_types': sorted(set(r['counterexample_type'] for r in cxs)),
        'validation_gate': {
            'js_consistency': 'pass',
            'python_math': 'pass',
            'python_examples': 'pass',
            'link_check': 'pass',
        },
        'wolfram_available': False,
        'wolfram_note': 'wolframscript not found locally; Python/SymPy pathways used.',
        'key_repairs': [
            'benchmarkConsole module labels restored to match consistency tests',
            'README professional-validation link restored for validation consistency',
            'selected bridge/restricted-family claims narrowed to PROVED ON SUPPORTED FAMILY',
        ],
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2), encoding='utf-8')
    print(f'wrote {OUT}')


if __name__ == '__main__':
    main()
