# Nonlinear and Representational Regime Map

## Regime N1: Injective post-composition survival

Setting:
- finite/restricted family with record map `M` and target `p`, then nonlinear post-map `phi o M`.

Assumptions:
- `phi` injective on `M(A)`.

Claim:
- exactness class is preserved under post-composition.

Status:
- `PROVED` (`OCP-061`, positive side).

What survives:
- exactness under information-preserving nonlinear representation change.

What fails:
- no guarantee for non-injective `phi`.

Boundary:
- injectivity on realized record support is required.

Evidence / tests / artifacts:
- `postcomposition_exactness_report`
- `tests/math/test_structural_information.py` (injective `y -> y^3` witness)

Nonclaims:
- no unrestricted nonlinear invariance claim.

## Regime N2: Non-injective post-composition failure

Setting:
- same as N1, but with non-injective `phi`.

Assumptions:
- `phi` collapses distinct record values in support.

Claim:
- exactness can be destroyed by induced record collisions.

Status:
- `PROVED` (`OCP-061`, no-go side).

What survives:
- explicit fail boundary for representational collapse.

What fails:
- direct transfer of linear exactness theorems to arbitrary nonlinear maps.

Boundary:
- finite/restricted witness classes.

Evidence / tests / artifacts:
- `tests/math/test_structural_information.py` (non-injective `y -> y^2` witness)
- PN-5 boundary in `positive_no_go_boundaries.md`

Nonclaims:
- no claim that all nonlinear mappings are harmful.

## Regime N3: Reparameterization versus representation

Setting:
- coefficient-space reparameterization versus record-space nonlinear map.

Assumptions:
- reparameterization invertibility determines family-preserving transforms.

Claim:
- invertible coefficient reparameterization preserves exactness (`OCP-059`),
- non-injective record representation can destroy exactness (`OCP-061`).

Status:
- `PROVED` on declared classes.

What survives:
- separation between admissible coordinate change and destructive observation remap.

What fails:
- conflating representation changes with harmless reparameterizations.

Boundary:
- declared finite/restricted families.

Evidence / tests / artifacts:
- `primitive_object_reparameterization_certificate`
- `postcomposition_exactness_report`

Nonclaims:
- no universal nonlinear classification theorem.

## Nonlinear arena verdict

- Works: a sharp survive/fail split now exists on meaningful subclasses.
- Fails: broad nonlinear extension beyond class assumptions remains unsupported.
- Open: larger nonlinear subclasses with theorem-grade exactness criteria.
