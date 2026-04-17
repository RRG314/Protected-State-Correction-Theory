# No-Go and Counterexample Report

## Purpose

This branch is falsification-first.
The point is not to make universal claims sound plausible.
The point is to kill the ones that fail and keep the failure as part of the result.

## 1. Universal fiber collision

Claim killed:
- exact recovery can hold despite indistinguishable protected values on a record fiber.

Counterexample logic:
- if `M(x)=M(x')` but `p(x)≠p(x')`, a single recovery value would have to equal two different targets.

Verdict:
- impossible
- foundational no-go
- standard

## 2. Finite detectable-only witness

Saved branch artifact:
- `data/generated/unified-recoverability/unified_recoverability_summary.json`

Witness:
- same record value `1` occurs for two admissible states,
- stronger target takes values `1` and `2`, so exact recovery fails,
- weaker coarsened target takes value `1` on both, so it remains exact.

Lesson:
- the same record can support detection/coarsened recovery while blocking the stronger target.

## 3. Restricted-linear weaker-versus-stronger witness

Saved branch artifact:
- `data/generated/unified-recoverability/unified_recoverability_summary.json`

Witness:
- record rows: `e_1^T` and `(e_2+e_3)^T`
- weaker target: `(e_2+e_3)^T`
- stronger target: `e_3^T`

Result:
- weaker target exact,
- stronger target impossible.

Lesson:
- same record,
- same ambient family,
- different target,
- different verdict.

## 4. No-rank-only classifier witness family

Saved branch artifact:
- `data/generated/unified-recoverability/rank_only_classifier_witnesses.csv`

For every tested `n > r ≥ 1` and `r ≤ k < n`, the branch now stores same-rank opposite-verdict witnesses.

This kills the claim that:
- record amount,
- observation rank,
- or target rank plus observation rank
alone determine exact recoverability.

## 5. Fixed-library same-budget witness family

Saved branch artifacts:
- `data/generated/unified-recoverability/candidate_library_budget_witnesses.csv`
- `data/generated/unified-recoverability/coordinate_rank_enumeration.csv`

Witness structure:
- one shared coordinate candidate library,
- unit sensor costs,
- same selection size,
- same total budget,
- opposite exactness verdicts.

Lesson:
- even after the admissible measurement family is fixed,
- and even after budget/count are held fixed,
- exactness still depends on which structural directions are actually measured.

## 6. Noisy weaker-versus-stronger separation witness

Saved branch artifacts:
- `data/generated/unified-recoverability/unified_recoverability_summary.json`
- `data/generated/unified-recoverability/noisy_restricted_linear_hierarchy.csv`

Witness:
- weaker target remains exactly recoverable with a linear decoder,
- stronger target has positive collision gap on the same bounded family,
- the stronger impossibility floor survives every bounded noise radius,
- while the weak target retains a quantitative upper bound `||K||_2 η`.

Lesson:
- noise does not automatically blur the stronger/weak hierarchy away,
- and stable weak recovery can remain meaningfully separated from stronger-target impossibility.

## 7. Exact-versus-asymptotic split witness

Saved branch artifact:
- `data/generated/unified-recoverability/control_exact_vs_asymptotic_split.csv`
- `data/generated/unified-recoverability/control_regime_hierarchy.csv`

On the control toy family:
- one-step exact recovery fails,
- two-step finite-history recovery succeeds,
- and observer-based asymptotic recovery converges.

Lesson:
- exact, asymptotic, and detectable-only are not cosmetic labels.
- they are genuinely different regimes.

## 8. Failed universal slogans

Killed or demoted in this branch:
- one universal threshold law
- one universal scalar recoverability capacity
- one universal detectability notion across all fields
- amount-only exactness language

## 9. Best negative result

The best negative result is not “noninvertible maps are noninvertible.”
It is:
- fiber exactness is universal,
- but amount-only exactness classifiers fail already in the restricted-linear theorem class,
- even inside a fixed candidate library with fixed budget.
