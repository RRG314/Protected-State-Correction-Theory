# Ambiguity Witness Template

Script:
- [`scripts/templates/ambiguity_witness_template.py`](../../scripts/templates/ambiguity_witness_template.py)

## Assumptions
- finite-dimensional linear or linearized restricted family
- exact failure caused by hidden directions or record collisions

## Inputs
- observation matrix
- protected matrix
- optional admissible-family basis

## Outputs
- explicit witness in the observation nullspace
- protected-gap size for that witness

## Validation Checks
- verify the witness leaves the record unchanged
- verify the witness changes the protected variable

## Interpretation Guide
- an ambiguity witness is stronger than a vague statement that the map is noninvertible
- it shows how the current record fails on the protected task you actually care about

## Limitations
- witness quality depends on the chosen family restriction
