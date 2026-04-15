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
    observation = np.array(
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 1.0],
        ],
        dtype=float,
    )
    protected = np.array([[0.0, 0.0, 1.0]], dtype=float)
    candidate_rows = [
        np.array([0.0, 1.0, 0.0], dtype=float),
        np.array([0.0, 0.0, 1.0], dtype=float),
        np.array([1.0, 1.0, 0.0], dtype=float),
    ]
    report = linear_recoverability_design_report(
        observation,
        protected,
        candidate_rows=candidate_rows,
    )
    payload = {
        'observation_matrix': observation.tolist(),
        'protected_matrix': protected.tolist(),
        'candidate_rows': [row.tolist() for row in candidate_rows],
        'exact_recoverable': report.exact_recoverable,
        'row_space_residuals': list(report.row_space_residuals),
        'minimal_added_measurements': report.minimal_added_measurements,
        'candidate_exact_sets': [list(combo) for combo in report.candidate_exact_sets],
        'nullspace_witness': None if report.nullspace_witness is None else report.nullspace_witness.tolist(),
        'nullspace_protected_gap': report.nullspace_protected_gap,
    }
    print(json.dumps(payload, indent=2))


if __name__ == '__main__':
    main()
