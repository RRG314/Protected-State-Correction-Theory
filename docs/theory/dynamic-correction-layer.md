# Dynamic Correction Layer

## Scope

This layer addresses time-dependent recovery/suppression: finite-time impossibility, asymptotic correction rates, and repeated-observation threshold behavior.

Primary sources:
- [`src/ocp/continuous.py`](../../src/ocp/continuous.py)
- [`src/ocp/next_phase.py`](../../src/ocp/next_phase.py)
- [`src/ocp/structural_information.py`](../../src/ocp/structural_information.py)
- [`data/generated/next-phase/dynamic_accumulation.csv`](../../data/generated/next-phase/dynamic_accumulation.csv)
- [`data/generated/next-phase/generator_dynamics.csv`](../../data/generated/next-phase/generator_dynamics.csv)
- [`data/generated/structural-information-theory/dynamic_garbling_law_checks.csv`](../../data/generated/structural-information-theory/dynamic_garbling_law_checks.csv)

## Promoted Dynamic Statements

### DYN-1: Finite-time exact recovery no-go for smooth linear generator flow
Status: `PROVED` (`OCP-020`).

No finite positive time can produce exact cancellation of generic disturbance components in the linear smooth-flow class.

### DYN-2: Asymptotic suppression with spectral margin
Status: `PROVED` (`OCP-013`, `OCP-014`).

For split-preserving generators with strictly stable disturbance block, disturbance norm decays exponentially at a spectral-margin-governed rate.

### DYN-3: Canonical repeated-observation threshold (finite history)
Status: `VALIDATED` (explicit branch witness).

In the canonical accumulation family, exact recoverability appears only after the 4th observation block. Before that, row-space residual remains positive.

Evidence:
- `exact_threshold_step = 4` in [`dynamic_accumulation.csv`](../../data/generated/next-phase/dynamic_accumulation.csv).

### DYN-4: Generator rate tracking bound
Status: `VALIDATED` (canonical branch witness).

For canonical flow witness:
- finite-time exact recovery remains false,
- bound is respected at all sampled times,
- disturbance-to-bound ratio decreases from `1.0` to about `0.708` over `t in [0,3]`.

Evidence:
- [`generator_dynamics.csv`](../../data/generated/next-phase/generator_dynamics.csv).

### DYN-5: Target-independent garbling semigroup monotonicity
Status: `PROVED` on finite binary-target, target-independent Markov garbling class (`OCP-055`).

Claim:
Given a finite experiment `Y_t` with binary target `T`, if

```text
P(T, Y_{t+1}) = P(T, Y_t) K
```

for a row-stochastic kernel `K` that does not depend on `T`, then the optimal squared-loss defect

```text
D_t = E[(T - E[T | Y_t])^2]
```

is nondecreasing in `t`.

Why this holds:
- each step is a Blackwell garbling of the previous experiment;
- MMSE is a Bayes risk, so information loss cannot reduce the optimal risk.

Local executable checks:
- `src/ocp/structural_information.py::garbling_mmse_flow_binary`
- `data/generated/structural-information-theory/dynamic_garbling_law_checks.csv`.

### DYN-6: Broad dynamic monotonicity no-go without garbling assumptions
Status: `PROVED` (counterexample, `OCP-056`).

If the transition law is allowed to depend on hidden target state, monotonicity can fail sharply.

Counterexample:
- start from uninformative single-label record (`D_0 = 0.25`);
- next-step record emits target directly (`D_1 = 0`).

This proves there is no unconditional dynamic monotonicity law across all transitions.

### DYN-7: Finite multivalued target garbling monotonicity
Status: `PROVED` on finite-valued targets under squared-loss MMSE and target-independent garbling (`OCP-057`).

Claim:
For finite target alphabet values `v_i in R`, if

```text
P(T, Y_{t+1}) = P(T, Y_t) K
```

with target-independent row-stochastic `K`, then

```text
D_t = E[(T - E[T | Y_t])^2]
```

is nondecreasing in `t`.

Local evidence:
- analytic multivalued witness flow in
  `data/generated/structural-information-theory/dynamic_garbling_law_checks.csv`
  (`law_case = target_independent_garbling_multivalued`).

### DYN-8: Binary symmetric garbling semigroup envelope
Status: `PROVED` on the declared analytic class (`OCP-058`).

Assumptions:
- binary target with prior `P(T=1)=0.5`,
- initial record equals target exactly,
- each step applies target-independent `BSC(epsilon)` with `epsilon in [0, 0.5]`.

Law:
- effective flip probability after `t` steps:

```text
epsilon_t = 0.5 * (1 - (1 - 2 epsilon)^t)
```

- MMSE flow:

```text
D_t = epsilon_t (1 - epsilon_t)
```

so `D_t` is monotone nondecreasing and converges to `0.25`.

Local evidence:
- `law_case = bsc_semigroup_closed_form` in
  `data/generated/structural-information-theory/dynamic_garbling_law_checks.csv`.

### DYN-9: BSC horizon threshold law
Status: `PROVED` on the declared binary BSC semigroup class (`OCP-063`).

Given any defect floor `d` with `0 <= d < 0.25`, the minimal horizon

```text
t*(d) = min { t : D_t >= d }
```

exists and is obtained by the first time the closed-form flow

```text
D_t = epsilon_t (1 - epsilon_t),   epsilon_t = 0.5*(1-(1-2epsilon)^t)
```

crosses `d`.

Local evidence:
- `data/generated/structural-information-theory/dynamic_horizon_thresholds.csv`.

## Disproved/Unresolved Dynamic Narratives

- "finite-time exactness can be recovered by smooth linear evolution" -> `DISPROVED` in branch class (`OCP-020`).
- "one universal history-length law across all branches" -> `OPEN`.
- "observation-with-time always improves to exactness in finite horizon" -> `DISPROVED` in general; depends on record architecture.
- "defect monotonicity holds for arbitrary transitions" -> `DISPROVED`; target-independent garbling assumptions are required.

## Domain Tie-In

This dynamic layer is intentionally connected to:
- asymptotic generator branch (operator-semigroup lane),
- repeated-record constrained-observation lane (history threshold lane),
- CFD/GLM asymptotic suppression interpretation (branch-scoped, not universalized).

## Literature Positioning

- likely literature-known foundations: semigroup and spectral theory ([Pazy 1983], [Engel-Nagel 2000]).
- repo framing: exact/no-go/rate separation with executable branch witnesses and theorem-ID-coupled diagnostics.

## Next Dynamic Targets

1. prove explicit horizon lower bounds for broader restricted-linear history families (`OPEN`),
2. quantify perturbation-to-rate sensitivity in generator branch (`OPEN`),
3. bridge dynamic thresholds to minimal augmentation laws (`OPEN`),
4. extend DYN-7 beyond squared-loss MMSE to additional loss classes (`OPEN`).
