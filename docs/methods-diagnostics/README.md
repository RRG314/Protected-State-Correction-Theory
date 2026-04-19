# Methods and Diagnostics

This lane contains instrumentation and diagnostic methodology.

Use this lane for:
- metric definitions and estimator assumptions,
- harness design and ablations,
- method comparisons against entropy/MI/Fisher/rank baselines,
- implementation-facing diagnostics.

Primary implementation anchors:
- `src/ocp/structural_information.py`
- `src/ocp/fiber_limits.py`
- `scripts/research/run_structural_information_harness.py`
- `data/generated/structural-information-theory/`
- `docs/methods-diagnostics/invariant-lane/`
- `docs/methods-diagnostics/positive_framework_buildout_options.md`

Methods are not theorem-core unless explicitly promoted in `docs/restricted-results/` with theorem status.
