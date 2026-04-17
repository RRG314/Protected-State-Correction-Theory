# Model-Mismatch Stress Report

## Goal

This report tests a quieter but important false-positive class:
- the true family may remain exactly identifiable,
- while the inverse map trained on a nearby family still drifts.

## Canonical theorem result

### `OCP-053`
On the canonical family

```text
F_beta = span{e1, e2 + beta e3},
M(x) = (x1, x2),
p(x) = x3,
```

each fixed `beta` yields exact target identifiability.
But the decoder exact on `beta0` incurs worst-case exact-data target error

```text
|beta - beta0| / sqrt(1 + beta^2)
```

on the true family `F_beta` over the unit coefficient box.

Artifact:
- [`canonical_model_mismatch.csv`](../../data/generated/unified-recoverability/canonical_model_mismatch.csv)

Current canonical rows for `beta0 = 1`:
- `beta = 0.5`: formula and brute-force max error both about `0.4472`
- `beta = 1.0`: formula and brute-force max error both `0`
- `beta = 2.0`: formula and brute-force max error both about `0.4472`

## Broader validated stress suite

Artifact:
- [`model_mismatch_stress.csv`](../../data/generated/unified-recoverability/model_mismatch_stress.csv)

Current suite shows:
- exact recovery can remain true on the true family,
- while the reference-family decoder still drifts under nearby structural mismatch.

## What this means

The branch can now state a clean outside-facing lesson:
- exact identifiability of the true model does not imply robustness of a decoder built on the wrong model class.
