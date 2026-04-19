# Quantum Alignment Repo Fit

Status: placement decision for corrected quantum-alignment lane.

## Candidate placements evaluated

## Option 1: `docs/physics/` narrow quantum extension

Fit:
- strong (keeps scope constrained and theorem-language explicit).

Risk:
- low narrative risk if labeled branch-limited.

## Option 2: constrained-observation/recoverability core lane

Fit:
- medium.

Risk:
- can blur theorem-spine boundaries if overpromoted.

## Option 3: TSIT/target-specific design application note

Fit:
- medium-high for design interpretation.

Risk:
- can hide quantum-specific assumptions if merged too aggressively.

## Option 4: benchmark-only note, no theorem lane

Fit:
- too conservative for current evidence (restricted proofs do survive).

## Option 5: reject integration except archive

Fit:
- too strict given corrected restricted proofs and clean boundary results.

## Placement decision

Selected placement:
- **Keep as quantum measurement-design sub-branch under `docs/physics/` with branch-limited theorem status.**

Why:
1. Restricted theorem content survives after correction.
2. Literature overlap is high, so front-door promotion is not justified.
3. The lane is still valuable as a measurement-design and falsification discipline branch.

## Integration level and constraints

Integrate at:
- narrow branch documentation + references + branch-audit mapping.

Do not integrate as:
- canonical theorem-spine replacement,
- repo-wide narrative reset,
- universal quantum claim.

## Safe public-facing claim

“On a restricted qubit class, the lane provides a corrected and falsification-tested measurement-alignment identity in trace form, plus explicit failure boundaries outside that class.”

## Unsafe public-facing claim

“Alpha conservation is a universal quantum law” or “the lane yields a new quantum foundation.”

