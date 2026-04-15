#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'src'))

from ocp import control_minimal_complexity_sweep


def main() -> None:
    report = control_minimal_complexity_sweep(
        horizons=(1, 2, 3, 4),
    )
    minima = {}
    for row in report['rows']:
        key = row['sensor_profile']
        if row['exact_recoverable'] and key not in minima:
            minima[key] = row['horizon']
    print(json.dumps({'minimal_exact_horizons': minima, 'rows': report['rows']}, indent=2))


if __name__ == '__main__':
    main()
