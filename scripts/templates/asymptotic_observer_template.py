#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'src'))

from ocp import functional_observability_sweep


def main() -> None:
    report = functional_observability_sweep(epsilon_values=(0.2,), horizons=(1, 2))
    observer = report['observer_reports'][0]
    payload = {
        'epsilon': observer['epsilon'],
        'gain': observer['gain'],
        'spectral_radius': observer['spectral_radius'],
        'protected_error_history': observer['protected_error_history'],
    }
    print(json.dumps(payload, indent=2))


if __name__ == '__main__':
    main()
