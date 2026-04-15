# Functional Observability Template

Script:
- [`scripts/templates/functional_observability_template.py`](../../scripts/templates/functional_observability_template.py)

## Assumptions
- linear time-invariant toy family
- scalar or low-dimensional protected functional
- finite observation horizon

## Inputs
- system parameters
- observation horizon set
- coupling / sensor strength values

## Outputs
- exact finite-history rows
- observer-side asymptotic reports where available
- recovery-error summaries

## Validation Checks
- compare exact finite-history verdicts against the restricted-linear criterion
- verify observer error decays when an asymptotic observer is reported

## Interpretation Guide
- exact finite-history recovery and asymptotic observer recovery are different outcomes
- if finite-history exactness fails but observer decay survives, switch architecture rather than forcing a static inverse

## Limitations
- toy LTI family only
- not a universal control theorem
