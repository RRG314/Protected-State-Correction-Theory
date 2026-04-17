# Final Branch Report

## What the branch is now

This branch is now best presented as a **fiber-based recoverability, impossibility, and false-positive detection program**.

Core structure:
- exact recovery is target constancy on record fibers,
- impossibility is target variation inside those fibers,
- weaker-target survival is target coarsening on those fibers,
- measurement redesign is fiber refinement,
- false positives arise when exactness is exported outside the family, target, discretization, or architecture that actually made the theorem true.

## What was preserved

Preserved fully:
- theorem IDs,
- generated examples,
- validations,
- workbench-facing integrations,
- compatibility shims for the older unified branch name.

## What new results survived in this pass

### `OCP-052` — restricted-linear family-enlargement false-positive theorem
Survived as `PROVED`.

Current canonical witness:
- small family exact: `true`
- enlarged family exact: `false`
- enlarged-family collision gap: `2.0`
- enlarged-family impossibility lower bound: `1.0`
- small-family exact decoder max error on enlarged family: `1.0`

Why it matters:
- it links the branch directly to outside identifiability and inverse-problem classes,
- it says exactly how a true exact result can become a false positive when the family is enlarged.

### `OCP-053` — canonical model-mismatch instability theorem
Survived as `PROVED`.

Current canonical witness:
- reference family parameter `beta_0 = 1.0`
- true-family parameters checked: `0.5`, `1.0`, `2.0`
- exact true-family identifiability: `true` for each fixed `beta`
- closed-form worst-case mismatch error on the unit coefficient box:
  `|beta - beta_0| / sqrt(1 + beta^2)`
- generated rows agree with brute-force evaluation to numerical precision

Why it matters:
- it gives the branch a clean inverse-problem theorem about exact-data failure under decoder mismatch,
- it shows that exact identifiability of the true family does not imply robustness of an inverse map trained on the wrong admissible family.

### New validated stress layers
- model mismatch can produce decoder drift even when the true family remains exactly recoverable,
- periodic modal refinement can destroy an apparent coarse exactness claim.

## What broke under falsification

What did **not** survive as a stronger universal claim:
- universal sensor-count laws,
- universal budget laws,
- universal family-robust exactness,
- universal discretization-robust exactness,
- universal PDE-side observability equivalence.

That failure is now explicit and useful rather than hidden.

## What survived from the stopping / switch / augment check

The stopping idea survived only in a modest form:
- as a theorem-linked decision layer,
- not as a new theorem branch,
- and not as a new repo identity.

What survives cleanly:
- stop exact pursuit when the target is fiber-mixed,
- switch to a weaker target when the coarsened target is exact on the same record,
- augment the record when a finite exact repair is known,
- change architecture when exact pursuit fails but a supported bounded-domain or asymptotic architecture survives,
- stop promoting a positive result when family enlargement or model mismatch breaks robustness.

## What known open-problem classes the branch now touches

The branch now honestly touches:
- partial-observation identifiability,
- sensor design and observability geometry,
- ill-posed inverse problems and nonuniqueness,
- control/PDE exact-versus-asymptotic reconstruction boundaries,
- model-mismatch and discretization false-positive risk.

## Strongest plausible publication unit now

Strongest current publication unit:
- a restricted theorem/falsification paper on recoverability limits under fiber geometry,
- centered on `OCP-049` through `OCP-053`,
- with family-enlargement, model-mismatch, and refinement false-positive layers.

## Strongest realistic next theorem target

Best next theorem target:
- weighted-cost or geometry-constrained anti-classifier theorems extending `OCP-050` without leaving the honest restricted-linear lane.

## Where the branch is still weak

Still too weak or too family-restricted:
- nonlinear extension,
- broad PDE inverse problems,
- universal model-mismatch robustness,
- universal discretization stability,
- field-equivalence beyond dictionary-level correspondence.
