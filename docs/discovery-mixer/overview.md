# Discovery Mixer / Structural Composition Lab

## What It Is

The Discovery Mixer is an advanced theorem-linked workbench surface for composing supported mathematical system families and then asking a disciplined set of questions:

- is the composition structurally well-typed?
- is the requested protected target compatible with the chosen record and architecture?
- is the problem exact, approximate, asymptotic, impossible, or unsupported?
- what specific structure is missing?
- what is the smallest supported change that repairs the failure?
- what weaker target already works?
- what happens before versus after the proposed change?

It is not an arbitrary symbolic mathematics engine.
It is a typed composition and diagnostics layer built only over the families that this repository can actually analyze and validate.

## Why It Exists

The rest of the repository already contained theorem statements, no-go results, recoverability criteria, augmentation logic, and structural-discovery workflows.
The mixer turns those pieces into a composable laboratory.

Its purpose is to let a user build a system from supported parts instead of only replaying fixed demos.

## Operating Modes

### Structured mixer

Use built-in families, protected targets, record types, and correction architectures already tracked by the repository.

This is the safest mode.
It exposes the strongest theorem-backed and family-validated logic.

### Controlled custom input

Enter custom matrices, linear functionals, modal functionals, or diagonal/history targets, but only inside explicit supported structural classes.

If the input cannot be reduced to a supported class, the mixer refuses it explicitly and explains why.

### Random exploration

Run seeded exploration inside supported structural classes to discover:

- failures
- threshold crossings
- candidate augmentations
- weaker-versus-stronger target splits
- benchmark cases worth keeping

### Demo mode

Replay validated end-to-end cases that start from a failure and end with a tested repair.

## Supported Outcomes

The mixer returns one of these structural verdicts:

- `exact`
- `approximate`
- `asymptotic`
- `impossible`
- `unsupported`

Those verdicts are always paired with an evidence level:

- theorem-backed
- restricted exact theorem-backed
- family-specific validated result
- benchmark-guided empirical result
- heuristic suggestion
- unsupported

## What Makes It Trustworthy

The mixer is designed to avoid the usual failure mode of symbolic or AI-style sandboxes: pretending to support more than they really do.

In this repository, every promoted mixer result must trace back to one of:

- a proved restricted theorem
- a proved no-go statement
- a validated family-specific computational result
- a benchmarked engineering diagnostic

Unsupported inputs are rejected rather than silently approximated.

## Main Questions It Can Answer

- Does this record separate the target on the admissible family?
- Is the failure caused by hidden support, insufficient horizon, missing measurement rows, or boundary incompatibility?
- Does a weaker target survive under the same record?
- What exact row, mode, horizon, or architecture change is needed?
- Can the proposed fix be applied and shown to change the regime?

## Main Limits

The mixer does not claim:

- arbitrary nonlinear symbolic analysis
- universal theorem status across all families
- exact minimal redesign outside the supported theorem-backed branches
- automatic reduction of every PDE or physics system into the repo's theorem spine

Those limits are part of the design, not an afterthought.
