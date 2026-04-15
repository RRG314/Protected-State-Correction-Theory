#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'src'))

from ocp import functional_observability_sweep


def main() -> None:
    report = functional_observability_sweep(
        epsilon_values=(0.0, 0.1, 0.2, 0.5),
        horizons=(1, 2, 3),
    )
    rows = report['rows']
    summary = {
        'exact_rows': [row for row in rows if row['exact_recoverable']],
        'observer_reports': report['observer_reports'],
    }
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
