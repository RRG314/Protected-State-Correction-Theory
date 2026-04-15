# Open-Problem Program

## Purpose

This file turns each major branch into an explicit research program. Each branch gets:
- one serious open question
- one theorem target
- one no-go or counterexample target
- one computational attack path
- one validation path

## 1. Exact Branch

- Serious open question:
  can the exact projector branch be extended from orthogonal direct sums to meaningful non-orthogonal correction settings without collapsing into coordinate artifacts?
- Theorem target:
  a clean exact theorem for a restricted non-orthogonal but complemented class, or a proof that orthogonality is the only honest exact class under the repo's preservation requirements.
- No-go target:
  show that naive oblique correction generically corrupts the protected component unless extra compatibility conditions hold.
- Computational attack plan:
  randomized finite-dimensional complemented-subspace sweeps with explicit corruption metrics.
- Validation path:
  exact recovery residuals, idempotence checks, and protected-drift checks across random families.

## 2. Exact Sector / QEC Branch

- Serious open question:
  is there one additional exact sector anchor that sharpens the operator language rather than merely duplicating the three-qubit bit-flip story?
- Theorem target:
  one more exact sector theorem on a nontrivial stabilizer or classical coding family with genuinely sharper sector maps.
- No-go target:
  prove that sector overlap or non-coordinate embeddings force detection ambiguity in the chosen anchor.
- Computational attack plan:
  exact sector recovery matrices and overlap sweeps on one carefully chosen second anchor.
- Validation path:
  exact recovery errors, overlap matrices, and syndrome/label distinguishability checks.

## 3. Exact Continuous Projection / CFD Branch

- Serious open question:
  how far can exact bounded-domain correction be pushed beyond the now-solved finite-mode boundary-compatible Hodge family?
- Theorem target:
  a broader bounded-domain exactness theorem for domain-compatible Hodge projectors with explicit admissible boundary data.
- No-go target:
  sharper bounded-domain impossibility when the operator preserves divergence but fails the protected boundary class.
- Computational attack plan:
  multi-family bounded-domain mode tests, projector-vs-transplant comparisons, and boundary-trace diagnostics.
- Validation path:
  divergence, boundary-normal trace, idempotence, orthogonality, and independent projector-construction agreement.

## 4. Asymptotic Generator Branch

- Serious open question:
  can the invariant-split generator theorem be extended to a broader robust class without losing exact protection of the protected coordinates?
- Theorem target:
  a theorem with explicit robustness bounds under controlled off-diagonal perturbations or semigroup assumptions.
- No-go target:
  show that certain non-normal or weakly mixed generators still force protected drift despite spectral decay on the disturbance block.
- Computational attack plan:
  randomized block-perturbed generator sweeps, comparison to exact exponential formulas, and decay-margin diagnostics.
- Validation path:
  protected-preservation residuals, disturbance decay rates, finite-time exactness residuals, and independent matrix-exponential checks.

## 5. GLM / Constraint-Damping Branch

- Serious open question:
  can asymptotic damping architectures be classified cleanly enough to give branch-specific design rules rather than only examples?
- Theorem target:
  a branch-specific sufficient criterion for asymptotic correction with explicit stable/neutral/unstable mode separation.
- No-go target:
  show when damping-only schemes reduce a scalar residual while leaving the protected class structurally underdetermined.
- Computational attack plan:
  parameter sweeps over damping strengths, auxiliary-field couplings, and residual decay profiles.
- Validation path:
  monitored residual decay, protected-variable drift, and comparison against exact projector references where available.

## 6. Continuous-QEC Bridge

- Serious open question:
  can one real operator statement be extracted from the continuous-QEC bridge without turning the branch into analogy language?
- Theorem target:
  a restricted continuous-measurement/reset statement with explicit code-sector preservation assumptions.
- No-go target:
  show that smooth-flow-only constructions cannot produce exact finite-time sector recovery on nontrivial error families.
- Computational attack plan:
  small monitored-channel toy models with exact vs asymptotic recovery comparisons.
- Validation path:
  sector distinguishability checks, logical-state error tracking, and consistency with the smooth-flow no-go.

## 7. Constrained-Observation Recoverability Branch

- Serious open question:
  can the current restricted-linear threshold spine be extended to a genuinely robust noisy theorem beyond `κ(0)=0` and `κ(η)/2`?
- Theorem target:
  a noise-aware or family-enlargement extension of the nested restricted-linear collision-gap theorem.
- No-go target:
  explicit coarse-record lower bounds that block exact recovery even when weaker protected variables remain recoverable.
- Computational attack plan:
  broader nested-family sweeps, perturbation/noise stress tests, and exact nullspace-on-a-box calculations.
- Validation path:
  collision-gap monotonicity, exact/no-go boundary checks, generated-artifact consistency, and independent brute-force checks on small cases.

## 8. Restricted-Linear / Design-Engine Layer

- Serious open question:
  which parts of the new minimal-augmentation theorem survive when measurements are restricted to a finite candidate library, noisy records, or structured sensor costs?
- Theorem target:
  a candidate-library or weighted-cost augmentation theorem that extends `δ(O, L; F)` into a real design invariant.
- No-go target:
  prove that below-deficiency or below-cost augmentations cannot yield exact recovery even when they look plausible heuristically.
- Computational attack plan:
  candidate-library search, random restricted-family stress tests, and weighted augmentation experiments.
- Validation path:
  exact row-space checks, augmentation-count equality, and agreement between closed-form deficiency and brute-force candidate search on small families.

## 9. Practical Workbench / Studio Layer

- Serious open question:
  can the studio become a real branch-to-tool surface without drifting away from the validated math?
- Theorem target:
  not a new theorem; the target is faithful theorem-surfacing and diagnosis logic.
- No-go target:
  catch any workbench conclusion that cannot be reproduced by the offline scripts.
- Computational attack plan:
  browser smoke, static test coverage, script-to-workbench output comparisons, and stale-artifact checks.
- Validation path:
  workbench example generation, Node tests, browser interaction checks, and generated-artifact consistency tests.
