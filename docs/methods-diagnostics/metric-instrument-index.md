# Metric and Instrument Index

This index records the role and interpretation of active diagnostics.

## Compatibility and Augmentation Metrics

### `CID` (Context-Invariance Defect)

Definition (informal): distance from a shared decoder that is valid across declared contexts.

Role: detects global incompatibility hidden by context-local success.

Implementation anchor: context-sensitive lane artifacts and scripts.

### `delta_free`

Definition (informal): minimum number of unrestricted added measurements required for exact completion on the declared restricted class.

Role: converts qualitative insufficiency into a concrete augmentation requirement.

Implementation anchor: `src/ocp/fiber_limits.py`.

### `delta_C`

Definition (informal): residual incompatibility after augmentation is constrained to a declared candidate library.

Role: separates rank gain from exact completion when augmentation choices are constrained.

Implementation anchor: constrained augmentation routines and positive-framework artifacts.

## Descriptor-Fiber Diagnostics

### `DFMI`

Definition (informal): fraction of quantized descriptor fibers that contain mixed labels.

Role: measures failure of descriptor-only separation.

Implementation anchor: `src/ocp/structural_information.py`.

### `IDELB`

Definition (informal): lower-bound style mixedness score derived from minimum label counts inside descriptor fibers.

Role: quantifies ambiguity induced by descriptor compression on a tested catalog.

Implementation anchor: `src/ocp/structural_information.py`.

### `CL` (Compatibility Lift)

Definition (informal): improvement in ambiguity score after adding compatibility-aware features.

Role: measures separation gained beyond amount descriptors.

Implementation anchor: `compatibility_lift` in `src/ocp/structural_information.py`.

## Example

Consider two designs with equal observation rank. Amount-only descriptors tie the pair. If `DFMI` and `IDELB` remain high for one design but drop after compatibility-aware augmentation for the other, `CL` records that separation gain.

## Evidence Paths

- `docs/methods-diagnostics/invariant-lane/`
- `data/generated/structural-information-theory/`

Scope note: these metrics remain branch-limited diagnostics unless promoted to theorem status.
