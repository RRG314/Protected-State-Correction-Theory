# Restricted Linear Recovery Template

Script:
- [`scripts/templates/restricted_linear_recovery_template.py`](../../scripts/templates/restricted_linear_recovery_template.py)

## Assumptions
- finite-dimensional linear admissible family
- linear observation map
- linear protected variable
- exact recovery judged on the restricted family

## Inputs
- observation matrix `O`
- protected matrix `L`
- optional candidate measurement rows
- optional family basis `F`

## Outputs
- exact / impossible verdict
- row-space residuals
- nullspace witness if recovery fails
- unrestricted minimal added-measurement count `δ(O, L; F)`
- minimal candidate augmentation if one exists

## Validation Checks
- compare row-space residuals to exact recoverability verdict
- verify nullspace witness changes the protected value while fixing the record
- if a candidate augmentation is suggested, rerun with the augmented matrix and confirm exact recovery

## Interpretation Guide
- zero residual means the protected row is already in the restricted record row space
- positive residual means the current record loses protected information
- the unrestricted minimal count is the theorem-backed best-case number of additional linear measurements needed if you are free to choose them
- minimal augmentation suggestions are the most actionable next-step result

## Limitations
- finite-dimensional linear only
- says nothing by itself about robustness outside the chosen family
