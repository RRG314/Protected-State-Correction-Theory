# Minimal-Information Sweep Template

Script:
- [`scripts/templates/minimal_information_sweep_template.py`](../../scripts/templates/minimal_information_sweep_template.py)

## Assumptions
- there is a tunable record-complexity parameter such as horizon, cutoff, or retained rows
- exact recovery is meaningful on the tested family

## Inputs
- complexity levels
- protected variable choice
- admissible family

## Outputs
- first exact complexity level
- error and collision summaries below and above the threshold

## Validation Checks
- rerun with a finer complexity grid if possible
- cross-check exactness with the linear criterion or explicit reconstruction operator

## Interpretation Guide
- the first exact level is often the most actionable design output in the repo
- below that level, the tool should tell you whether to add information or weaken the target

## Limitations
- family-specific unless a proof says otherwise
