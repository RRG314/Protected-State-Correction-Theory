# Static and Algebraic Regime Map

## Regime A1: Exactness by fiber and kernel compatibility

Setting:
- finite and restricted-linear families with declared `(A, M, p)`.

Assumptions:
- deterministic records and targets on declared family.

Claim:
- exact recoverability is equivalent to fiber constancy and, in restricted-linear form, to `ker(O F) subset ker(L F)`.

Status:
- `PROVED` (`OCP-030`, `OCP-031`, `OCP-054`).

What survives:
- exact/no-go classification on declared families.

What fails:
- no amount-only descriptor can replace compatibility interaction in general.

Boundary:
- finite/restricted-linear families only.

Evidence / tests / artifacts:
- `tests/math/test_recoverability.py`
- `tests/math/test_structural_information.py`
- `docs/theory/advanced-directions/constrained-observation-formalism.md`

Nonclaims:
- no universal theorem for unrestricted nonlinear inverse classes.

## Regime A2: Reparameterization invariance

Setting:
- restricted-linear family `x = F z` under coefficient reparameterization `x = F Q u`.

Assumptions:
- `Q` invertible.

Claim:
- exactness verdict is invariant under invertible reparameterization.

Status:
- `PROVED` (`OCP-059`).

What survives:
- coordinate changes that preserve family geometry.

What fails:
- non-invertible mappings are not covered.

Boundary:
- invertible reparameterization only.

Evidence / tests / artifacts:
- `primitive_object_reparameterization_certificate`
- `tests/math/test_structural_information.py`

Nonclaims:
- no invariance claim for rank-deficient reparameterizations.

## Regime A3: Amount-code deterministic classifier boundary

Setting:
- finite datasets with quantized amount-code classes.

Assumptions:
- deterministic classifier depends only on amount-code tuple.

Claim:
- exact deterministic classification is possible iff each amount-code class has one label; mixed-code collisions are decisive no-go witnesses.

Status:
- `PROVED` (`OCP-062`).

What survives:
- exact classifier feasibility test on declared finite coded datasets.

What fails:
- amount-only deterministic exact classification in presence of mixed-code collisions.

Boundary:
- deterministic amount-code class only.

Evidence / tests / artifacts:
- `amount_scalar_exact_classifier_possible`
- `amount_scalar_nonreducibility_certificate`
- `data/generated/structural-information-theory/amount_scalar_nonreducibility.csv`

Nonclaims:
- does not classify stochastic or model-based scalar learners outside declared code map.

## Static arena verdict

- Works: exactness and no-go boundaries are sharp and test-backed on declared classes.
- Fails: amount-only reduction remains impossible on supported witness and external lanes.
- Open: universal scalar reduction and unrestricted nonlinear algebraic closure.
