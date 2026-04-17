# Unified Recoverability and Impossibility

> Legacy branch-facing overview kept for compatibility.
> Canonical local presentation now lives in [../fiber-based-recoverability-and-impossibility/overview.md](../fiber-based-recoverability-and-impossibility/overview.md).

## Status

Serious theory branch inside the repository.

This branch is **not** a claim of a theory of everything.
It is a falsification-first attempt to isolate:
- the part of recoverability/impossibility that is genuinely universal,
- the part that survives only on restricted classes,
- and the point where cross-field unification breaks.

## Branch question

Across information theory, coding, inverse problems, control, QEC, CFD, and selected MHD lanes:

1. what is the common mathematical obstruction to exact recovery?
2. what is the cleanest shared language for recoverability, detectability, and impossibility?
3. what stronger universal claims fail, even before leaving the repo's restricted theorem classes?

## Strongest surviving result

The branch's strongest surviving result is a **negative theorem**:

> above the universal fiber/factorization level, exact recoverability cannot be classified by record amount alone, even on restricted finite-dimensional linear families.

In executable form, the repo now proves and stress-tests:
- a universal exactness criterion through fibers,
- a coarsening-based detectable-only principle,
- a restricted-linear **no rank-only exact classifier theorem**,
- a fixed-library same-budget strengthening of that negative theorem,
- and a quantitative noisy weaker-versus-stronger separation theorem.

That is the branch's main contribution.
It is stronger than a slogan and more honest than a fake universal law.

## Strongest honest summary

What survives universally:
- exact recoverability is factorization of the target through the record map,
- impossibility is fiber collision,
- weaker targets are easier than stronger targets because coarsenings collapse distinctions.

What does **not** survive universally:
- one scalar recoverability capacity,
- one cross-field threshold law,
- rank/count/bandwidth/history/sensor number alone as a complete exactness classifier.

What survives only on restricted classes:
- row-space exactness,
- collision-gap thresholds,
- minimal augmentation counts,
- fixed-library same-budget anti-classifiers,
- noisy weaker-versus-stronger separation bounds,
- periodic support thresholds,
- diagonal/history interpolation thresholds.

## Reading order

For a newcomer:
1. [usefulness-guide.md](usefulness-guide.md)
2. [core-formalism.md](core-formalism.md)
3. [field-dictionary-overview.md](field-dictionary-overview.md)
4. [literature-anchors.md](literature-anchors.md)
5. [theorem-candidates.md](theorem-candidates.md)
6. [proof-sketches.md](proof-sketches.md)
7. [no-go-counterexamples.md](no-go-counterexamples.md)
8. [final-report.md](final-report.md)

For a technical reader:
1. [core-formalism.md](core-formalism.md)
2. [literature-anchors.md](literature-anchors.md)
3. [theorem-candidates.md](theorem-candidates.md)
4. [proof-sketches.md](proof-sketches.md)
5. [no-go-counterexamples.md](no-go-counterexamples.md)
6. field dictionaries of interest
7. [validation-summary.md](validation-summary.md)
8. [novelty-assessment.md](novelty-assessment.md)

## Evidence status legend

- `PROVED`: exact derivation or contradiction proof survives.
- `VALIDATED`: computational or artifact-backed result survives independent checks.
- `CONDITIONAL`: branch claim depends on field assumptions not proved here.
- `DISPROVED`: the broader claim failed.
- `ANALOGY ONLY`: suggestive translation, not a theorem.
- `OPEN`: worth pursuing, not yet established.

## Workbench relation

This branch does **not** add a fake universal symbolic tool.
Its workbench relation is narrower and honest:
- the existing Structural Discovery Studio,
- Recoverability / Observation Studio,
- Benchmark / Validation Console,
- and Discovery Mixer
already instantiate restricted parts of this branch on supported families.

The right current UI lesson is not “the app solves the unified theory.”
It is:
- the app can exhibit the branch's restricted exact/no-go structure,
- and the branch explains why unsupported universal claims must be rejected.
