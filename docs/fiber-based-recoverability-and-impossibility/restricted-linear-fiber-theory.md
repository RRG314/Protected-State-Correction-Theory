# Restricted Linear Fiber Theory

## Status and scope

This file is theorem-grade on declared restricted linear families.

Known backbone in this file:
- factorization and fiber constancy logic,
- kernel and row-space exactness criteria.

Repo-specific contribution in this file:
- executable witness packages (`OCP-049`, `OCP-050`, `OCP-052`, `OCP-053`),
- branch-limited diagnostics tied to generated artifacts.

## Setup

We work on a restricted linear family:

```text
x = Fz,
y = OFz,
p(x) = LFz.
```

In coefficient space, equal-record fibers are affine slices of the form `z + ker(OF)`.

## Exactness criterion

Exact target recovery is possible exactly when the target is constant on each record fiber.
In the restricted linear class this is equivalent to:

```text
ker(OF) ⊆ ker(LF)
```

and equivalently:

```text
row(LF) ⊆ row(OF).
```

This criterion is adopted backbone, not a new universal claim.

## Why fiber language helps here

The fiber view makes failure mode geometry visible.
Two systems can share observation rank but have different target behavior inside `ker(OF)`. That is the core mechanism behind opposite exactness verdicts.

## How key theorems fit this view

`OCP-045` (minimal augmentation): add rows until target variation inside the record kernel is removed.

`OCP-047`, `OCP-049`, `OCP-050`: amount-only descriptors can match while target behavior on fibers differs.

`OCP-051`: a weaker target can be stable under noise while a stronger target remains impossible on the same record map.

`OCP-052`: exactness on a narrow family can disappear after admissible-family enlargement.

`OCP-053`: exactness on the true family does not guarantee robustness to model mismatch.

## Concrete example

Take two observation operators with the same rank. If the first one hides only target-neutral directions, exact recovery can hold. If the second hides a direction that changes the target, exact recovery fails. Rank did not change, but fiber alignment did.

## Artifact-backed evidence

Implementation and generated artifacts:
- [`src/ocp/fiber_limits.py`](../../src/ocp/fiber_limits.py)
- [`restricted_linear_fiber_geometry.csv`](../../data/generated/unified-recoverability/restricted_linear_fiber_geometry.csv)
- [`family_enlargement_false_positive.csv`](../../data/generated/unified-recoverability/family_enlargement_false_positive.csv)
- [`model_mismatch_stress.csv`](../../data/generated/unified-recoverability/model_mismatch_stress.csv)

These artifacts are branch-limited. They support declared families only.

## Citation anchors for overlap-critical statements

- Factorization/sufficiency backbone:
  - Doob-Dynkin style factorization overview: <https://arxiv.org/abs/1801.00974>
  - Blackwell comparison context: <https://digicoll.lib.berkeley.edu/record/112749/files/math_s2_article-08.pdf>
  - Coarse-graining and Blackwell order: <https://arxiv.org/abs/1701.07602>
- Identifiability/observability overlap:
  - Structural identifiability: <https://www.sciencedirect.com/science/article/abs/pii/002555647090132X>
  - Nonlinear observability: <https://doi.org/10.1109/TAC.1977.1101601>
  - Kalman filtering baseline: <https://www.cs.unc.edu/~welch/kalman/media/pdf/Kalman1960.pdf>
