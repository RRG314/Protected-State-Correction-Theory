# Asymptotic Observer Template

Script:
- [`scripts/templates/asymptotic_observer_template.py`](../../scripts/templates/asymptotic_observer_template.py)

## Assumptions
- dynamic record stream
- exact one-shot recovery may fail
- observer-style asymptotic recovery is plausible

## Inputs
- system parameters
- observer gain or gain construction rule
- protected variable

## Outputs
- observer gain
- spectral radius or equivalent decay diagnostic
- protected-error history

## Validation Checks
- verify decay numerically over multiple steps
- compare to the finite-history exactness verdict so the architecture switch is justified

## Interpretation Guide
- use this when the right answer is not “collect more data then invert once,” but “estimate online from a continuing record”

## Limitations
- asymptotic convergence is not exact one-shot recovery
