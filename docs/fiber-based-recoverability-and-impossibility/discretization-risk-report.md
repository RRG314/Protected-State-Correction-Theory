# Discretization Risk Report

## Goal

This note records the branch's current discretization-style false-positive witness.

## Periodic modal refinement witness

Stored in:
- [`periodic_refinement_false_positive.csv`](../../data/generated/unified-recoverability/periodic_refinement_false_positive.csv)

Current witness values:
- cutoff: `2`
- coarse mode count: `2`
- refined mode count: `4`
- coarse exact recoverable: `true`
- refined exact recoverable: `false`
- refined collision gap: `2.0`
- refined impossibility lower bound: `1.0`
- coarse decoder max error on refined family: `1.0`

## Interpretation

A coarse modal truncation can make an exact claim look stronger than it really is.
Here the cutoff record is exact on the coarse two-mode family, but fails as soon as the admissible family is refined to four modes while the target includes the newly admitted hidden support.

## Status

- `VALIDATED`
- theorem-linked through the restricted-linear family-enlargement logic
- still family-specific, not a universal discretization theorem
