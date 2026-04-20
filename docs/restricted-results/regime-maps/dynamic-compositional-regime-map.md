# Dynamic and Compositional Regime Map

## Regime D1: Target-independent garbling monotonicity

Setting:
- finite target and finite record process under repeated target-independent Markov garbling.

Assumptions:
- update `P(T, Y_{t+1}) = P(T, Y_t) K` with row-stochastic `K` independent of `T`.

Claim:
- squared-loss MMSE defect is nondecreasing in time.

Status:
- `PROVED` (`OCP-055` for binary, `OCP-057` finite multivalued).

What survives:
- monotonic defect degradation under declared garbling class.

What fails:
- no statement for target-dependent transition laws.

Boundary:
- target-independent garbling class only.

Evidence / tests / artifacts:
- `garbling_mmse_flow_binary`
- `garbling_mmse_flow_discrete`
- `data/generated/structural-information-theory/dynamic_garbling_law_checks.csv`

Nonclaims:
- no branch-agnostic monotonicity claim.

## Regime D2: Binary symmetric semigroup envelope

Setting:
- binary target with prior `0.5`, perfect initial record, repeated `BSC(epsilon)`.

Assumptions:
- `epsilon in [0, 0.5]`, target-independent composition.

Claim:
- closed-form defect flow with monotone approach to `0.25` and explicit horizon threshold crossings.

Status:
- `PROVED` (`OCP-058`, `OCP-063`).

What survives:
- semigroup envelope and horizon map on declared analytic class.

What fails:
- this closed form does not transfer to arbitrary channels.

Boundary:
- declared BSC semigroup class only.

Evidence / tests / artifacts:
- `bsc_mmse_flow_from_perfect_observation`
- `bsc_horizon_threshold`
- `data/generated/structural-information-theory/dynamic_horizon_thresholds.csv`

Nonclaims:
- no universal horizon law across all dynamic channels.

## Regime D3: Broad monotonicity failure

Setting:
- transitions allowed to depend on hidden target.

Assumptions:
- target-conditioned transition kernels are permitted.

Claim:
- dynamic defect monotonicity can fail sharply.

Status:
- `PROVED` no-go (`OCP-056`).

What survives:
- explicit no-go boundary preventing overreach.

What fails:
- branch-agnostic monotonicity claim.

Boundary:
- unrestricted target-dependent transitions.

Evidence / tests / artifacts:
- `target_dependent_transition_no_go_example`
- dynamic counterexample row in `dynamic_garbling_law_checks.csv`

Nonclaims:
- none beyond declared no-go boundary.

## Dynamic arena verdict

- Works: monotonic degradation and threshold laws on declared garbling/semigroup classes.
- Fails: monotonicity collapses once target dependence is allowed.
- Open: broad dynamic law beyond declared transform classes.
