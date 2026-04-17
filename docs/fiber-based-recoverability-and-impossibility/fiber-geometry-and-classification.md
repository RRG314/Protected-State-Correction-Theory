# Fiber Geometry And Classification

## Purpose

The branch now treats fibers as the real structural object, but it only classifies them where the repo has honest support.
This note records what is currently supportable and what remains open.

## Supported fiber classes in this repo

### Singleton fibers

A singleton fiber means the record already separates every admissible state in the supported family.
That is stronger than this branch usually needs.
Exact recovery only needs the target to be constant on fibers, not the state to be unique.

### Finite ambiguous fibers

Supported directly in finite witnesses:
- the coarsened-detectable examples
- the qubit phase-loss family on discrete reductions
- explicit same-record stronger-versus-weaker examples

These are the cleanest examples of:
- exact weaker-target recovery
- stronger-target impossibility
- finite collision witnesses

### Affine / linear fibers

This is the strongest current classified class.
On a restricted linear family

```text
x = F z,
y = O F z,
p(x) = L F z,
```

the coefficient-space fibers are affine slices

```text
z + ker(O F).
```

That gives a clean classified geometry:
- coefficient dimension: `dim(z)`
- observation rank: `rank(O F)`
- fiber dimension: `dim ker(O F)`
- target-constant fibers iff `ker(O F) ⊆ ker(L F)`

The new canonical executable report is:
- [`src/ocp/fiber_limits.py`](../../src/ocp/fiber_limits.py)

Generated artifact:
- [`restricted_linear_fiber_geometry.csv`](../../data/generated/unified-recoverability/restricted_linear_fiber_geometry.csv)

### Nested fibers under richer records

Supported directly in:
- periodic cutoff families
- diagonal/history families
- restricted-linear augmentation theorems

Adding measurements or longer histories refines fibers.
The branch keeps this as a theorem-backed or family-backed statement only on supported nested families.

## What the branch can currently classify honestly

### Target-constant versus target-mixed fibers

This is the main honest dichotomy.
The branch can say whether the target is constant on current fibers in:
- the finite witnesses
- restricted-linear families
- periodic threshold families
- diagonal/history benchmark families
- selected control observer examples

### Fiber dimension versus recoverability

The branch can classify one important negative fact:
- fiber dimension or observation rank alone does not determine exact recoverability.

That is the content behind:
- `OCP-047`
- `OCP-049`
- `OCP-050`

Equal fiber dimension can still hide different target alignment.
That is why amount-only language fails.

## What is not promoted here

Not claimed in this branch:
- a full smooth geometric classification of nonlinear fibers
- a universal curvature theory of fibers
- a general dimension-only recoverability theorem
- a cross-field metric geometry of fibers beyond the supported restricted classes

## Best current classification summary

The strongest honest classification program is:
1. finite ambiguous fibers for explicit counterexamples,
2. affine fibers for the restricted-linear theorem class,
3. nested refinement families for periodic, control, and augmentation thresholds,
4. target-constant versus target-mixed as the universal branch distinction.
