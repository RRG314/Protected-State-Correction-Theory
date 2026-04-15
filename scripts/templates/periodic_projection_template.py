#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'src'))

from ocp import periodic_functional_complexity_sweep


def main() -> None:
    report = periodic_functional_complexity_sweep(
        cutoffs=(0, 1, 2, 3, 4),
        functionals={
            'low_mode_sum': (1.0, 1.0, 0.0, 0.0),
            'bandlimited_contrast': (0.0, 1.0, -1.0, 0.0),
            'full_weighted_sum': (1.0, -0.5, 0.75, 0.25),
        },
    )
    rows = report['rows']
    cutoffs = {}
    for row in rows:
        if row['exact_recoverable'] and row['functional_name'] not in cutoffs:
            cutoffs[row['functional_name']] = row['cutoff']
    print(json.dumps({'minimal_exact_cutoffs': cutoffs, 'rows': rows}, indent=2))


if __name__ == '__main__':
    main()
