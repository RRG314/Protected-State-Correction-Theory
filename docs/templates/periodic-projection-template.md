# Periodic Projection Template

Script:
- [`scripts/templates/periodic_projection_template.py`](../../scripts/templates/periodic_projection_template.py)

## Assumptions
- periodic domain
- projection-compatible incompressible or divergence-controlled family
- protected variable expressed in retained modal support or protected coefficients

## Inputs
- modal family
- cutoff family
- protected functional coefficients

## Outputs
- minimal exact cutoff by functional
- mean / worst recovery error by cutoff
- collapse curves for the tested family

## Validation Checks
- confirm the predicted exact cutoff matches the first exact row in the sweep
- compare exact and truncated error curves under more than one norm if the setup is modified

## Interpretation Guide
- this template is strongest when the protected variable has clear spectral support
- if the protected support exceeds the retained cutoff, exact recovery is blocked by design

## Limitations
- periodic only
- do not transplant the result directly to bounded domains
