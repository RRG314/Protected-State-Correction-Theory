#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'src'))

from ocp.design import nullspace_witness_for_protected_loss


def main() -> None:
    observation = np.array(
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 1.0],
        ],
        dtype=float,
    )
    protected = np.array([[0.0, 0.0, 1.0]], dtype=float)
    witness, gap = nullspace_witness_for_protected_loss(observation, protected)
    print(json.dumps({'witness': None if witness is None else witness.tolist(), 'protected_gap': gap}, indent=2))


if __name__ == '__main__':
    main()
