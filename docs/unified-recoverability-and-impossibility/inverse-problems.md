# Inverse-Problem Mapping

## Status

`CONDITIONAL` mapping note with strong structural overlap.

## Native field language

Inverse problems ask whether causes or hidden states can be reconstructed from effects or measured data.
Classical anchors include:
- Hadamard's well-posedness language,
- later regularization theory such as Tikhonov-style stabilization.

## Branch translation

- `F`: admissible parameter/state family,
- `M`: forward map or data map,
- `p`: parameter or feature of interest,
- exact recoverability: uniqueness of the protected quantity from the data,
- approximate/stable recoverability: continuity modulus of protected recovery,
- impossibility: nonuniqueness or instability.

## Exact match

The fit is strongest here:
- fiber collisions are exactly nonuniqueness,
- the collapse modulus packages ambiguity under bounded data discrepancy,
- the adversarial lower bound is a clean worst-case instability statement.

## Strongest branch lesson

The branch forces a useful discipline that inverse-problem papers often need anyway:
- specify the admissible family,
- specify the exact target,
- and distinguish full-state inversion from protected-feature recovery.

## What is not claimed

The repo does not provide:
- general regularization theory,
- general PDE inverse stability,
- or broad uniqueness theorems outside the supported families.

Its contribution is narrower:
- a target-relative recoverability formalism,
- plus exact restricted theorems and explicit no-go witnesses.
