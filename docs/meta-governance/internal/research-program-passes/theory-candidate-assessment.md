# Theory-Candidate Assessment

## Purpose

This note asks whether the branch results now support a serious theory candidate, or only a more careful reframing.

For the lens-integration and multi-candidate falsification pass, see:
- [theory-candidate-comparison.md](theory-candidate-comparison.md)
- [final-theory-formation-decision.md](final-theory-formation-decision.md)

The current focused candidate is:

**Protected-Variable Recoverability Theory (PVRT)**

Core claim under test:
- recoverability depends on the interaction between the observation map, the protected variable, and the admissible family, not just on the amount of information.

This file now also tracks a second, more falsification-heavy branch:

**Fiber-Based Recoverability and Impossibility**

Core claim under test:
- exact recoverability has a genuine universal factorization core,
- but stronger exact classifiers already fragment above that level.

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

The strongest new limit added on top of that statement is:
- exactness on a smaller admissible family does not certify exactness on an enlarged one once the enlarged family restores hidden target-changing directions inside the record kernel.

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

Structural Discovery should not be treated as a separate theory candidate.

Its honest status is:
- theorem-linked engineering layer
- practical synthesis of branch results
- useful subsystem because it turns proof status and failure analysis into concrete repair workflows
- not a new theorem program by itself

Discovery Mixer should be treated the same way.

Its honest status is:
- theorem-linked composition and diagnostics layer
- useful because it makes supported families composable and testable
- not a broad symbolic-math theory candidate
- only as strong as the underlying supported family reductions and validations

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

## Unified Branch Assessment

### Candidate D: Broad Unified Recoverability Theory

Claim:
- a serious universal theorem unifies observability, decodability, inverse recovery, QEC correction, PDE recovery, and detectability through one positive law stronger than fiber compatibility.

Verdict:
- rejected

Why:
- universal threshold language failed,
- universal detectability language failed,
- amount-only classifiers fail already inside the restricted-linear branch.

### Candidate E: Fiber-Based Recoverability / Impossibility Limits Branch

Claim:
- the universal exact core is factorization through the record map,
- the universal obstruction is fiber collision,
- stronger exactness laws above that level must be restricted and structural rather than amount-only.

Verdict:
- strongest surviving branch-wide formulation

Why it survives:
- it keeps the standard universal exactness criterion,
- it promotes the detectable-only/coarsening hierarchy honestly,
- and it now has the no-rank-only theorem, the fixed-library same-budget strengthening, the noisy weaker-versus-stronger separation theorem, the family-enlargement false-positive theorem, and the canonical model-mismatch instability theorem as sharp branch results.

Best honest summary:
- not a theory of everything,
- but a useful cross-field limits branch that says exactly where the common structure stops being universal.

### Candidate F: Descriptor-Fiber Anti-Classifier Branch

Claim:
- finite witness-class descriptor fibers can be used to compute irreducible amount-only classification error and compatibility lift above existing anti-classifier witnesses.

Verdict:
- keep as a real branch-limited quantitative extraction lane (`PROVED ON SUPPORTED FAMILY` + `VALIDATED`).

Why it survives:
- purity and lower-bound statements are exact on finite witness classes,
- generated invariants (`DFMI`, `IDELB`, `CL`) reproduce and sharpen existing rank/budget anti-classifier witnesses,
- the lane adds measurable diagnostic value without pretending to be a universal theorem layer.

Scope guard:
- keep this branch explicitly subordinate to restricted-linear/fiber theorem cores,
- do not promote finite witness-class extraction to unrestricted continuous theory claims.
