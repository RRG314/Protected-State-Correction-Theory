# Failure-Mode Taxonomy

Date: 2026-04-17
Pass: Meta-theory extraction

## Objective

Formalize cross-branch failure modes, identify reducibility to collision language, and determine whether this taxonomy yields theorem leverage.

## Minimal taxonomy

## Tier I — Distinction-loss failures (collision type)

### FM1. Fiber collision

`exists x1,x2 in A: M(x1)=M(x2), T(x1)!=T(x2)`.

- Verdict implication: exact recovery impossible on declared family.
- Reducibility: primitive collision mode.

### FM2. Symmetry blindness

Observation is invariant under nuisance symmetry but target is quotient-sensitive.

- Reducibility: yes, collision after quotienting (same observed record, different quotient target class).

### FM3. Operator-range insufficiency (restricted-linear)

`ker(OF) not subset of ker(LF)` (equiv. `row(LF) not subset row(OF)`).

- Reducibility: yes, induces target-distinguishing collisions in coefficient fibers.

## Tier II — Scope/architecture incompatibility failures

### FM4. Family enlargement failure

Exactness on `A_small` fails on `A_large` with `A_small subset A_large`.

- Reducibility: partly. Often appears as new collisions introduced by enlarged family, but key mechanism is scope mismatch.

### FM5. Model mismatch instability

Decoder exact on reference family but deployed on true family with mismatch.

- Reducibility: not purely collision; mismatch can induce error floor without immediate finite collision witness.

### FM6. Domain/topology mismatch

Architecture matches periodic or idealized constraints but fails bounded/domain-compatible protected class.

- Reducibility: generally no. Better viewed as compatibility-law failure (boundary/topology constraints missing).

## Tier III — Regime mismatch failures

### FM7. Exactness-vs-asymptotic split

Finite-horizon exactness fails while asymptotic observer recovery converges.

- Reducibility: no. Dynamic regime distinction, not static collision equivalence.

## Reduction table

| Mode | Collision-reducible? | Primary mechanism |
| --- | --- | --- |
| FM1 Fiber collision | Yes | target-mixed observation fibers |
| FM2 Symmetry blindness | Yes (quotient-collision form) | nuisance-invariant observation |
| FM3 Operator-range insufficiency | Yes | hidden target-changing kernel directions |
| FM4 Family enlargement | Partially | scope change introduces latent incompatible directions |
| FM5 Model mismatch | No (in general) | decoder-family incompatibility |
| FM6 Domain/topology mismatch | No (in general) | missing compatibility constraints |
| FM7 Exact-vs-asymptotic split | No | dynamic architecture regime mismatch |

## Theorem leverage from taxonomy

1. **Leverage L1 (collision core):** FM1-3 can inherit direct no-go logic from fiber collision theorems.
2. **Leverage L2 (scope fragility):** FM4 motivates explicit family-guard conditions in theorem statements.
3. **Leverage L3 (non-collision incompatibility):** FM5-7 prevent overcompression of all failures into one collision slogan.

## Status

- Taxonomy itself: `CLASSIFICATION PROGRAM (PROMOTE)`.
- Universal reduction of all failures to collision: `REJECTED`.
- Collision core as a strict sub-taxonomy: `PROVED USEFUL`.
