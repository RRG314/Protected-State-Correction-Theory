#!/usr/bin/env python3
from __future__ import annotations

"""Compatibility entrypoint for the former unified recoverability runner.

The canonical script for the local fiber-based branch now lives in
`scripts/compare/run_fiber_recoverability_examples.py`.
"""

from run_fiber_recoverability_examples import main


if __name__ == '__main__':
    main()
