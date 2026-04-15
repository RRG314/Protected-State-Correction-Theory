# Exact Projector Template

Script:
- [`scripts/templates/exact_projector_template.py`](../../scripts/templates/exact_projector_template.py)

## Assumptions
- protected and disturbance subspaces are orthogonal
- projection-compatible exact branch

## Inputs
- protected basis
- disturbance basis
- ambient state

## Outputs
- protected component
- disturbance component
- recovered state
- exact recovery error

## Validation Checks
- verify orthogonality before promoting the setup as an exact branch
- verify recovery equals the protected component up to numerical tolerance

## Interpretation Guide
- this is the cleanest exact branch in the repository
- use it to prototype exact correction logic before moving to a more domain-specific projector family

## Limitations
- not valid once the disturbance overlaps the protected object
