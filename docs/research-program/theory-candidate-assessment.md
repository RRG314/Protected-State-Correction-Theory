# Theory-Candidate Assessment

## Purpose

This note asks whether the branch results now support a serious theory candidate, or only a more careful reframing.

The current focused candidate is:

**Protected-Variable Recoverability Theory (PVRT)**

Core claim under test:
- recoverability depends on the interaction between the observation map, the protected variable, and the admissible family, not just on the amount of information.

## Candidate Theory Statements

### Candidate A: Broad Universal PVRT

Claim:
- one broad recoverability theory governs quantum, periodic-flow, control, and other constrained systems through a common threshold law.

Verdict:
- rejected

Why:
- the qubit, periodic, and diagonal-control thresholds arise from different mechanisms
- universal scalar-capacity language failed
- branch-level exactness still depends on genuinely different objects across the repo

### Candidate B: Restricted PVRT

Claim:
- recoverability is fiber-compatibility in general,
- and on restricted finite-dimensional linear families it becomes a real theorem program based on row-space inclusion, collision gaps, exact-regime upper envelopes, and minimal augmentation counts.

Verdict:
- strongest surviving candidate

Why it survives:
- exactness through fiber separation and `κ(0)` is clean
- `κ(η)/2` gives a real lower bound
- `κ(δ) ≤ ||K||_2 δ` now gives a real exact-regime upper bound in the restricted-linear branch
- same-rank counterexamples kill the “amount alone” shortcut cleanly
- periodic and diagonal family-level thresholds sit honestly as corollaries of the restricted-linear spine rather than as fake universal laws

### Candidate C: Branch-Specific Invariants Without A Named Theory

Claim:
- the repo should stop at branch-specific exactness, threshold, and no-go invariants without naming a theory candidate.

Verdict:
- still partly true
- now too weak as the whole story

Why it is no longer enough:
- the constrained-observation and design-engine branches now support a coherent restricted theorem-and-falsification spine
- the repo does have a central observation-layer candidate worth naming, as long as the scope stays honest

## Strongest Current Theory Statement

The strongest honest theory statement now is:

> Protected-variable recoverability is governed by the compatibility between observation fibers and protected-variable distinctions on the admissible family. In restricted finite-dimensional linear families this compatibility becomes a real theorem program: exactness is row-space inclusion, exact-regime ambiguity is linearly bounded above by an exact recovery operator, exact failure is quantified below by collision gaps, and minimal unrestricted augmentation is given by the row-space deficiency `δ(O, L; F)`.

This is narrower than a universal theory.
It is also stronger than “just a framework.”

## What The Current Theory Candidate Predicts

Restricted PVRT predicts:

1. same-rank records can still differ in exact recoverability
2. weaker protected variables can remain recoverable after stronger ones fail under the same record
3. exact restricted-linear recovery automatically yields a stable exact-regime upper envelope
4. branch-level thresholds depend on protected-variable structure, not only on record amount

## What Would Falsify It

Restricted PVRT would be materially weakened by any of the following:

1. a restricted-linear counterexample to row-space exactness
2. a restricted-linear counterexample to the same-rank insufficiency theorem
3. an exact restricted-linear case violating the `κ(δ) ≤ ||K||_2 δ` envelope
4. a robust cross-domain example showing that record amount alone determines recoverability once the admissible family is fixed

No such counterexample survived the current pass.

## What Remains Standard

Still standard or standard-adjacent:
- fiber separation
- `κ(0)=0`
- kernel/row-space exactness
- rank lower bounds
- many family-specific formulas once the right coordinates are chosen

The candidate theory only stays credible because it does **not** try to relabel those as novel by themselves.

## What May Be A Real Contribution

The strongest real contribution candidate is now:
- a restricted PVRT program built from
  - the collision-gap threshold law,
  - the exact-regime `κ` upper envelope,
  - the same-rank insufficiency theorem,
  - the minimal augmentation theorem,
  - and family-level corollaries on periodic and diagonal benchmark systems.

That is a **minor but real** theory-level contribution candidate.
It is not a broad new universal theory of observation.

## Best Next Upgrade Path

The strongest next path is:

1. a noisy / admissible-family-enlarged version of restricted PVRT
2. candidate-library or weighted-cost augmentation theorems
3. sharper no-go results showing when approximation survives but exactness cannot

## What To Reject

Reject as theory claims:
- universal PVRT across all current branches
- “information amount alone” language
- universal threshold language
- any statement that makes the current branch less restricted than the proofs justify
