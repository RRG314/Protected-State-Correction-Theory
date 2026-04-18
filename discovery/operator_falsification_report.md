# Operator Falsification Report

Status: direct counterattack against candidate operators/projections/equations.
Data:
- `data/generated/operator_discovery/operator_witness_catalog.csv` (1000 rows)
- `data/generated/operator_discovery/operator_anomaly_catalog.csv` (26 rows)

## Attack 1

Claim attacked:
- candidate operators collapse to row-space/kernel compatibility logic.

Result:
- `SURVIVES`.

Reason:
- SDCO, CID/CCD, and CLE are mathematically equivalent reformulations of shared decoder feasibility in the linear class.
- CLDO (`delta_C`) remains a constrained-library feasibility certificate, not a broad new operator family.

## Attack 2

Claim attacked:
- candidate equations are just factorization/fiber constancy rewrites.

Result:
- `PARTIALLY SURVIVES`.

Reason:
- CLE/CID collapse to existing compatibility logic.
- augmentation feasibility and `delta_C` equations remain useful scoped extensions due explicit shared-augmentation admissibility constraints.

## Attack 3

Claim attacked:
- candidate projection methods only work due hand-built families.

Result:
- `PARTIALLY SURVIVES`.

Reason:
- projection diagnostics are broad but not theorem-distinct.
- insufficiency result (projection success with invariant failure) appears at scale (`491` cases), not isolated handcraft.

## Attack 4

Claim attacked:
- candidate metrics add no theorem power beyond existing OCP quantities.

Result:
- `SURVIVES` for most candidates.

Reason:
- most operators are diagnostics/reparameterizations.
- strongest additive signal is augmentation-threshold structure plus candidate-library defect no-go certificates.

## Attack 5

Claim attacked:
- candidate “new law” fails outside tiny synthetic family.

Result:
- `PARTIALLY SURVIVES`.

Reason:
- split/no-go patterns are robust across large generated sets.
- full closed-form augmentation law and broad branch transfer remain open.

## Attack 6

Claim attacked:
- candidate objects are computationally useful but not mathematically distinct.

Result:
- `SURVIVES` for SDCO/CID/CLE/projection gains.
- `PARTIALLY SURVIVES` for augmentation operator family.

## Falsification Outcome

What survived as serious math now:
- theorem package around conditioned-vs-invariant split,
- descriptor-only insufficiency,
- positive augmentation threshold existence on supported families,
- constrained candidate-library feasibility/impossibility equation (`delta_C`).

What did not survive as new operator math:
- claims of genuinely new operator/projection/equation classes independent of existing OCP compatibility logic.

Working conclusion:
- operator discovery produced useful computational diagnostics,
- but theorem novelty remains primarily in scoped no-go/threshold packaging rather than new algebraic objects.
