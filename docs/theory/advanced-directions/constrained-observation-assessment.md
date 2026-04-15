# Constrained-Observation Branch Assessment

## Short Verdict

This branch deserves to stay in the repository.

It now supports a real **restricted Protected-Variable Recoverability Theory (PVRT) program**:
- exact fiber-compatibility,
- exact-regime lower and upper bounds,
- collision-gap thresholds,
- same-rank insufficiency,
- and minimal augmentation counts.

It still does **not** justify being sold as a broad universal theory of observation.

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
6. same-rank insufficiency in the restricted-linear branch

These are not deep on their own, but together they make the branch falsification-first in a productive way.

## 4. Strongest Clean Positive Results

The strongest clean positive outputs are now:

1. the operational lower bound

```text
worst-case protected-variable error ≥ κ_{M,p}(η)/2
```

2. the exact-regime upper envelope on the exact restricted-linear branch

```text
κ_{M,p}(δ) ≤ ||K||_2 δ
```

3. the nested restricted-linear collision-gap threshold law
4. the nested restricted-linear minimal-complexity criterion
5. the restricted-linear minimal augmentation theorem with exact count

```text
δ(O, L; F) = rank([O F; L F]) - rank(O F)
```

6. the periodic functional-support threshold law on the tested periodic modal families
7. the diagonal functional-interpolation threshold law on the tested scalar-output families
8. the full-versus-weaker protected-variable split in the qubit fixed-basis family
9. the same-rank insufficiency theorem, which kills the idea that record amount alone determines recoverability

These are the results worth pointing readers to first.

## 5. Minor Real Contribution Candidate

The most plausible minor contribution is now the following package:

> a restricted protected-variable recoverability theory program in which exactness is fiber-compatibility, exact restricted-linear recovery carries both lower and upper ambiguity bounds, record amount alone is falsified by same-rank counterexamples, and minimal-record / minimal-augmentation thresholds can be proved on conventional finite families.

That is not a major theorem claim, but it is stronger than the branch was before the current falsification pass.

## 6. Strongest Candidate For A Larger Contribution

The strongest current candidate is **restricted PVRT**, not `κ` alone.

The most plausible next upgrade would be one of the following:

- a useful theorem beyond `κ(0)=0`, `κ(η)/2`, and the exact-regime linear upper envelope,
- a robust threshold law under noisy or enlarged admissible families,
- or a sharp no-go theorem that is stronger than the current restricted-linear obstruction.

Right now, the honest surviving structure is:

- `κ(η)/2` is real and useful,
- `κ(δ) ≤ ||K||_2 δ` is real and useful in the exact restricted-linear branch,
- the stronger threshold laws still survive only through restricted-linear structure and family-level corollaries.

## 7. What Should Be Promoted

Promote this branch as:

- a formal observation-layer extension of Protected-State Correction Theory,
- a computationally useful recoverability lab,
- a place for strong no-go results,
- a branch with real minimal-record examples,
- and a branch with a real restricted-linear theory spine.

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
- a restricted theorem program,
- no inflated universal claim.
