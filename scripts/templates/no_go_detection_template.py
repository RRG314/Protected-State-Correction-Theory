#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'src'))

from ocp.design import linear_recoverability_design_report


def main() -> None:
    observation = np.array([[1.0, 0.0, 0.0]], dtype=float)
    protected = np.array([[0.0, 0.0, 1.0]], dtype=float)
    report = linear_recoverability_design_report(observation, protected)
    payload = {
        'exact_recoverable': report.exact_recoverable,
        'reason': 'restricted-linear row-space insufficiency' if not report.exact_recoverable else 'none',
        'row_space_residuals': list(report.row_space_residuals),
        'nullspace_protected_gap': report.nullspace_protected_gap,
    }
    print(json.dumps(payload, indent=2))


if __name__ == '__main__':
    main()
