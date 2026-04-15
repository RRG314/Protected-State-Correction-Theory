# Structural Discovery Template Reference

Structural Discovery reuses and promotes the repo's existing creation templates.

Available templates in `scripts/templates/`:

- `restricted_linear_recovery_template.py`
- `functional_observability_template.py`
- `periodic_projection_template.py`
- `ambiguity_witness_template.py`
- `no_go_detection_template.py`
- `minimal_information_sweep_template.py`
- `asymptotic_observer_template.py`
- `exact_projector_template.py`

## How They Fit Structural Discovery

Restricted linear:

- best for candidate-library augmentation, weaker-target checks, and exact row-space diagnostics

Functional observability:

- best for finite-history threshold checks and observer-vs-exact design choices

Periodic projection:

- best for support threshold and coarse-record diagnostics on the finite modal family

Ambiguity witness / no-go:

- best for constructing counterexamples and proving that current records are structurally insufficient

Minimal-information sweep:

- best for record-complexity scans and threshold plots

## Template Output Expectations

Each template should produce:

- system definition
- protected target definition
- record definition
- validation checks
- failure or success interpretation
- explicit limits of the result

The Structural Discovery Studio is the fast interactive surface. The templates are the reproducible code-first surface.
