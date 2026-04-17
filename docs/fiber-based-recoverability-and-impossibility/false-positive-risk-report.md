# False-Positive Risk Report

## Main result of this pass

The strongest new surviving branch result is:
- `OCP-052`: restricted-linear family-enlargement false-positive theorem.

Clean content:
- exact recovery on a smaller admissible family does not justify exact recovery on a larger one,
- and the larger family's collision gap immediately becomes a worst-case error lower bound for every decoder on that larger family.

## Canonical witness

Stored in:
- [`family_enlargement_false_positive.csv`](../../data/generated/unified-recoverability/family_enlargement_false_positive.csv)

Current witness values:
- small family dimension: `2`
- large family dimension: `3`
- small-family exactness: `true`
- large-family exactness: `false`
- large-family collision gap: `2.0`
- larger-family impossibility lower bound: `1.0`
- reference decoder max error on large family: `1.0`

## What this means

The branch can now say something stricter than “family restriction matters.”
It can certify that:
- a restricted exact decoder is not safe to trust outside its certified family,
- and the failure can be lower-bounded before any heuristic reconstruction is run.

## Honest novelty status

- theorem form: `repo-new`
- spirit: likely literature-known / standard-adjacent
- branch value: high, because it turns a vague warning into a theorem-linked false-positive certificate.
