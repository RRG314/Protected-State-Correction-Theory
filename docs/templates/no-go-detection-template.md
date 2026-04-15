# No-Go Detection Template

Script:
- [`scripts/templates/no_go_detection_template.py`](../../scripts/templates/no_go_detection_template.py)

## Assumptions
- the target problem can be written as a restricted recovery problem
- the record and protected variable are explicit

## Inputs
- observation map
- protected variable map
- admissible family restriction if needed

## Outputs
- exact / impossible verdict
- residual-based diagnosis
- nullspace-protected gap when failure is structural

## Validation Checks
- rerun after adding the proposed missing record row or horizon
- confirm that the no-go disappears only when the record changes in the predicted way

## Interpretation Guide
- use this template when you want to stop chasing a naive recovery idea quickly and honestly

## Limitations
- a no-go in one restricted family does not automatically prove a no-go for all models of the same application
