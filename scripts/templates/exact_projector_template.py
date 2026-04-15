#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'src'))

from ocp import FiniteOCPSystem


def main() -> None:
    system = FiniteOCPSystem(
        protected_basis=np.array([[1.0], [0.0]], dtype=float),
        disturbance_basis=np.array([[0.0], [1.0]], dtype=float),
    )
    state = np.array([1.5, -0.75], dtype=float)
    protected, disturbance = system.decompose(state)
    recovered = system.exact_recover(state)
    print(
        json.dumps(
            {
                'state': state.tolist(),
                'protected_component': protected.tolist(),
                'disturbance_component': disturbance.tolist(),
                'recovered_state': recovered.tolist(),
                'recovery_error': float(np.linalg.norm(recovered - protected)),
            },
            indent=2,
        )
    )


if __name__ == '__main__':
    main()
