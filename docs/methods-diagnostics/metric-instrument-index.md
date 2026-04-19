# Metric and Instrument Index

This page explains what each diagnostic is trying to detect.

## Compatibility and augmentation metrics

### `CID` (Context-Invariance Defect)

Plain meaning:
How far a setup is from having one shared decoder that works across contexts.

Why it exists:
Local context success can hide global incompatibility.

Implementation anchor:
- context-sensitive lane artifacts and scripts.

### `delta_free`

Plain meaning:
Minimum number of unrestricted added measurements needed for exact completion on the declared restricted class.

Why it exists:
It turns “needs more information” into a concrete number.

Implementation anchor:
- `src/ocp/fiber_limits.py`

### `delta_C`

Plain meaning:
Residual incompatibility after you restrict augmentation to a declared candidate library.

Why it exists:
A library can increase rank but still fail exact completion.

Implementation anchor:
- constrained augmentation routines and positive-framework artifacts.

## Descriptor-fiber diagnostics

### `DFMI`

Plain meaning:
Fraction of quantized descriptor fibers that contain mixed labels (exact and fail together).

Why it exists:
If many fibers are mixed, descriptors are not separating verdicts well.

Implementation anchor:
- `src/ocp/structural_information.py`

### `IDELB`

Plain meaning:
A lower-bound style mixedness score built from minimum label counts inside descriptor fibers.

Why it exists:
It quantifies unavoidable ambiguity induced by descriptor compression on the tested catalog.

Implementation anchor:
- `src/ocp/structural_information.py`

### `CL` (Compatibility Lift)

Plain meaning:
Improvement in ambiguity score after adding compatibility-aware features.

Why it exists:
It checks whether compatibility information adds practical separation beyond amount descriptors.

Implementation anchor:
- `compatibility_lift` in `src/ocp/structural_information.py`

## One simple example

Suppose two designs have the same observation rank. Amount-only descriptors tie them. If `DFMI` and `IDELB` stay high for one design and drop after compatibility-aware augmentation for the other, `CL` captures that lift. This tells you why one design is recoverable and the other is not, even though rank matched.

## Evidence paths

- `docs/methods-diagnostics/invariant-lane/`
- `data/generated/structural-information-theory/`

Scope note:
These metrics are branch-limited diagnostics unless explicitly promoted to theorem status.
