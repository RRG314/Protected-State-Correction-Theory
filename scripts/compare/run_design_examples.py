#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import sys

import numpy as np

ROOT = Path('/Users/stevenreid/Documents/New project/repos/ocp-research-program')
sys.path.insert(0, str(ROOT / 'src'))

from ocp.design import linear_recoverability_design_report

OUT = ROOT / 'data/generated/design/design_template_examples.json'


CANDIDATE_LABELS = ['measure x2', 'measure x3', 'measure x1+x2']


def normalize(report) -> dict[str, object]:
    return {
        'exact_recoverable': bool(report.exact_recoverable),
        'rank_observation': int(report.rank_observation),
        'rank_protected': int(report.rank_protected),
        'recoverable_row_indices': list(report.recoverable_row_indices),
        'unrecoverable_row_indices': list(report.unrecoverable_row_indices),
        'row_space_residuals': [float(value) for value in report.row_space_residuals],
        'nullspace_witness': None if report.nullspace_witness is None else [float(value) for value in report.nullspace_witness],
        'nullspace_protected_gap': float(report.nullspace_protected_gap),
        'unrestricted_minimal_added_measurements': int(report.unrestricted_minimal_added_measurements),
        'minimal_added_measurements': report.minimal_added_measurements,
        'candidate_exact_sets': [list(combo) for combo in report.candidate_exact_sets],
        'candidate_exact_labels': [[CANDIDATE_LABELS[index] for index in combo] for combo in report.candidate_exact_sets],
    }


observation = np.array(
    [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 1.0],
    ]
)
candidates = [
    np.array([0.0, 1.0, 0.0]),
    np.array([0.0, 0.0, 1.0]),
    np.array([1.0, 1.0, 0.0]),
]

examples = {
    'linear_tail_pair': {
        'measurement_labels': ['measure x1', 'measure x2+x3'],
        'candidate_labels': CANDIDATE_LABELS,
        'protected_labels': ['recover x2', 'recover x3'],
        'report': normalize(
            linear_recoverability_design_report(
                observation,
                np.array(
                    [
                        [0.0, 1.0, 0.0],
                        [0.0, 0.0, 1.0],
                    ]
                ),
                candidate_rows=candidates,
            )
        ),
    },
    'linear_x3_only': {
        'measurement_labels': ['measure x1', 'measure x2+x3'],
        'candidate_labels': CANDIDATE_LABELS,
        'protected_labels': ['recover x3'],
        'report': normalize(
            linear_recoverability_design_report(
                observation,
                np.array([[0.0, 0.0, 1.0]]),
                candidate_rows=candidates,
            )
        ),
    },
    'linear_weaker_sum': {
        'measurement_labels': ['measure x1', 'measure x2+x3'],
        'candidate_labels': CANDIDATE_LABELS,
        'protected_labels': ['recover x2+x3'],
        'report': normalize(
            linear_recoverability_design_report(
                observation,
                np.array([[0.0, 1.0, 1.0]]),
                candidate_rows=candidates,
            )
        ),
    },
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(examples, indent=2))
print(f'wrote {OUT}')
