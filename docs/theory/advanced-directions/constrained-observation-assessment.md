# Constrained-Observation Branch Assessment

## Short Verdict

This branch deserves to stay in the repository.

It now has enough theorem-grade and computational substance to count as a real research lane.

It still does **not** justify being sold as a major standalone theorem program.

## 1. Definitely Standard

These are clean and useful, but they should be treated as standard or standard-adjacent:

- exact recoverability as a fiber-separation property
- the linear kernel criterion
- the row-space formulation of restricted exactness
- fixed-basis phase-loss logic in the qubit toy model
- the bare divergence-only no-go
- the basic observer / functional-observability structure
- the diagonal interpolation formulas as Vandermonde analysis

## 2. Useful Repackaging Only

These are worth keeping inside the repo, but they are not enough to claim novelty:

- the broad statement that recovery of a protected variable can be easier than recovery of the full state
- the broad exact / approximate / asymptotic / impossible vocabulary by itself
- the idea of organizing recoverability around admissible families instead of full ambient spaces

## 3. Useful Negative Results

The strongest kept negative outputs are:

1. divergence-only no-go on nontrivial constrained-flow families
2. fixed-basis phase-loss no-go for phase-sensitive protected variables
3. hidden-mode no-go in the diagonal scalar-output control family
4. same-record weaker-versus-stronger splits in the periodic and control families
5. one-step impossibility versus two-step recovery in the two-state control toy model

These are not deep on their own, but they make the branch falsification-first in a productive way.

## 4. Strongest Clean Positive Results

The strongest clean positive outputs are now:

1. the operational lower bound

```text
worst-case protected-variable error ≥ κ_{M,p}(η)/2
```

2. the nested restricted-linear collision-gap threshold law
3. the nested restricted-linear minimal-complexity criterion
4. the restricted-linear minimal augmentation theorem with exact count

```text
δ(O, L; F) = rank([O F; L F]) - rank(O F)
```

5. the periodic functional-support threshold law on the tested periodic modal families
6. the diagonal functional-interpolation threshold law on the tested scalar-output families
7. the full-versus-weaker protected-variable split in the qubit fixed-basis family

These are the results worth pointing readers to first.

## 5. Minor Real Contribution Candidate

The most plausible minor contribution is now the following package:

> a protected-variable recoverability framework in which the same constrained record can be exact for one protected quantity, approximate for another, asymptotic in an observer setting, and impossible for a stronger protected variable, together with an explicit restricted-linear collision-gap threshold law and finite-family threshold laws on conventional system classes.

That is not a major theorem claim, but it is stronger than the branch was before the current falsification pass.

## 6. Strongest Candidate For A Larger Contribution

The strongest candidate remains the collapse modulus `κ_{M,p}` **if** one of the following can still be shown:

- a useful theorem beyond `κ(0)=0` and `κ(η)/2`,
- a robust threshold law under noisy or enlarged admissible families,
- or a sharp no-go theorem that is stronger than family-specific linear-algebra obstruction.

Right now, the strongest surviving result in that direction is narrower:

- `κ(η)/2` is real and useful,
- but the stronger threshold laws currently survive only through restricted-linear structure.

## 7. What Should Be Promoted

Promote this branch as:

- a formal observation-layer extension of Protected-State Correction Theory,
- a computationally useful recoverability lab,
- a place for strong no-go results,
- a branch with real minimal-record examples,
- and a branch with two honest restricted-linear theorems:
  - the collision-gap threshold law,
  - and the minimal augmentation count theorem.

Do **not** promote it as:

- a major new universal theory of observation,
- a universal phase-transition theory,
- or a replacement for established observability, sufficiency, or inverse-stability literatures.

## 8. Current Recommendation

Keep the branch.

Promote the clean results and the tool.

Keep the claims narrow:
- real formal value,
- real negative results,
- real family-specific threshold laws,
- one useful restricted-linear theorem,
- no inflated theorem claim.
