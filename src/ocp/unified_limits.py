from __future__ import annotations

"""Compatibility wrapper for the former unified-limits module.

The canonical implementation for this local branch now lives in
`ocp.fiber_limits`. This wrapper is intentionally thin so existing imports,
artifacts, and unpushed branch history continue to work during the migration.
"""

from .fiber_limits import *  # noqa: F401,F403
from .fiber_limits import __all__  # noqa: F401
