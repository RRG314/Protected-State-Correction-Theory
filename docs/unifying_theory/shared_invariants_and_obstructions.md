# Shared Invariants and Obstructions

Date: 2026-04-17

Goal: identify the smallest non-decorative set that organizes the surviving branch mathematics.

## I1. Fiber-Collision / Exactness Invariant

Define

`kappa_0(A,T,M) = sup{ d_Z(T(x),T(x')) : x,x' in A, M(x)=M(x') }`.

- `kappa_0 = 0` iff exact recoverability holds.
- `kappa_0 > 0` gives impossibility by collision.

Appearance:
- OCP recoverability/fiber branch (direct theorem).
- Soliton observation-collision logic on quotient lanes.
- MHD analogue only when closure equation is represented as map-collision logic.

Decision: **KEEP (core invariant)**.

## I2. Alignment / Compatibility Defect (Restricted Linear)

For `A={Fz}`, define compatibility defect

`rho_align(O,L;F) = dist(row(LF), row(OF))`.

Equivalent exactness condition: `rho_align = 0`.

Appearance:
- OCP restricted-linear exactness.
- Soliton finite-family analogues via observation-family collision separation.

Decision: **KEEP (branch-limited, stronger-than-rank)**.

## I3. Side-Information Deficiency / Minimal Augmentation

`delta(O,L;F) = rank([OF;LF]) - rank(OF)`.

Interpretation: minimum unrestricted added linear measurements required for exactness on supported restricted-linear families.

Decision: **KEEP (constructive branch invariant)**.

## I4. Anti-Classifier Obstruction

An anti-classifier witness is a pair of systems with equal amount summary (`rank`, `count`, or fixed-library budget) and opposite exactness verdict.

Appearance:
- OCP `same-rank`, `no-rank-only`, `no-budget-only` theorem package.
- Soliton same-count opposite-verdict witness package on supported families.

Decision: **KEEP (branch-limited obstruction type)**.

## I5. Family-Enlargement Fragility Indicator

`phi_FE = 1` if exact on `A_s` but non-exact on enlarged `A_l` (`A_s ⊂ A_l`), else `0`.

Appearance:
- OCP theorem `OCP-052`.
- Soliton finite-family conditional parallels.
- MHD ansatz-enlargement failures (supporting pattern, not identical theorem form).

Decision: **KEEP (branch-limited fragility invariant)**.

## I6. Model-Mismatch Instability Floor

For mismatch decoder `R_hat` and true family `A_true`, define

`E_mm = sup_{x in A_true} d_Z(T(x), R_hat(M(x)))`.

Appearance:
- OCP canonical theorem `OCP-053` (closed-form floor in declared family).
- Soliton conditional mismatch growth analogues.

Decision: **KEEP (branch-limited instability invariant)**.

## I7. Boundary/Topology Compatibility Obstruction

Define compatibility residual class as a tuple, e.g.

`B_comp = (constraint_residual, boundary_mismatch, topology_mismatch)`.

Exactness requires all components in the declared branch to vanish/fit.

Appearance:
- OCP bounded-domain transplant no-go and restricted Hodge exactness.
- MHD annular survivor vs smooth-axis obstruction.

Decision: **KEEP (domain-structured obstruction type)**.

## I8. Symmetry-Quotient Obstruction

For nuisance group action `G`, define quotient-collision set

`Q_coll = {(x,x') : M(x)=M(x'), [x] != [x'] in A/G}`.

If `Q_coll` contains target-distinguishing pairs, non-identifiability persists modulo symmetry.

Appearance:
- Soliton theorem lane central.
- OCP bridge lane restricted analogue.

Decision: **KEEP (restricted but important)**.

## I9. Emergence/Self-Organization Scores

Metrics like localization growth, peak counts, coherence retention, and attractor diagnostics are valuable discovery metrics but not currently theorem-level unifying invariants for recoverability/correction core.

Decision: **DEMOTE to discovery metrics (not core invariant)**.

## Minimal Shared Set

The smallest high-value organizing set is:
1. `kappa_0` (fiber collision/exactness),
2. `rho_align` (compatibility defect),
3. `delta` (augmentation deficiency),
4. anti-classifier witness type,
5. `phi_FE` (family enlargement fragility),
6. `E_mm` (model-mismatch instability),
7. boundary/topology compatibility obstruction,
8. symmetry-quotient obstruction.

Anything beyond this set is currently decorative or branch-specific instrumentation.
