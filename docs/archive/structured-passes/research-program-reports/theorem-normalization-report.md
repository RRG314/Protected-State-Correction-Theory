# Theorem Normalization Report (2026-04-16)

## Purpose

Normalize theorem and claim structure after lens integration so that:
- statement form,
- proof status,
- branch ownership,
- scope restrictions,
- and evidence level
are consistent across canonical docs.

Primary canonical sources:
- `docs/overview/proof-status-map.md`
- `docs/overview/claim-registry.md`
- `docs/finalization/theorem-spine-final.md`
- `docs/finalization/no-go-spine-final.md`

## Key Claim Normalization Checks

| Claim | Status check | Branch ownership check | Scope restriction check | Supersession/duplication check | Normalization verdict |
| --- | --- | --- | --- | --- | --- |
| `OCP-047` same-rank insufficiency | matches `PROVED` | constrained-observation restricted-linear | explicit restricted-linear scope retained | not superseded; remains core falsification result | normalized |
| `OCP-045` minimal augmentation theorem | matches `PROVED` | restricted-linear design layer | unrestricted added-measurement scope explicit | no silent stronger replacement | normalized |
| `OCP-043` collision-gap threshold law | matches `PROVED` | constrained-observation restricted-linear | bounded coefficient family scope explicit | consistent with `OCP-046` (complementary) | normalized |
| `OCP-046` exact-regime upper envelope | matches `PROVED` | constrained-observation restricted-linear | exact restricted-linear class explicit | not replacing `OCP-035`; complementary upper/lower structure | normalized |
| `OCP-048` target coarsening theorem | matches `PROVED` | fiber-based recoverability limits branch | forward-only implication scope explicit | converse failure remains documented | normalized |
| `OCP-049` no rank-only exact classifier | matches `PROVED` | fiber-based limits branch | restricted finite-dimensional linear class explicit | complements `OCP-047`, not duplicate | normalized |
| `OCP-050` no fixed-library budget-only exact classifier | matches `PROVED` | fiber-based limits branch | fixed-library unit-cost scope explicit | extends `OCP-049` in budget language | normalized |
| `OCP-052` family-enlargement false-positive theorem | matches `PROVED` | fiber-based limits branch | restricted-linear family-inclusion assumptions explicit | distinct from rank/budget anti-classifier theorems | normalized |
| `OCP-053` canonical model-mismatch instability | matches `PROVED` | fiber-based limits branch | canonical family and coefficient-box scope explicit | complementary to `OCP-052` mismatch lane | normalized |
| `OCP-044` bounded finite-mode Hodge theorem | matches `PROVED` | bounded-domain/Hodge/CFD branch | explicit finite-mode boundary-compatible family scope explicit | not overextended to full bounded theorem | normalized |
| `OCP-028` divergence-only bounded no-go | matches `PROVED` | bounded-domain/CFD no-go branch | nontrivial bounded protected class scope explicit | consistent with `OCP-044` positive restricted subcase | normalized |
| `OCP-020` finite-time exact recovery no-go | matches `PROVED` | asymptotic generator no-go branch | smooth linear flow scope explicit | remains canonical exact-vs-asymptotic separator | normalized |
| Asymptotic spectral-rate statements (`OCP-013`,`OCP-014`) | statuses remain `PROVED` under current assumptions | asymptotic generator branch | assumptions preserved; no over-generalization | no conflict with no-go layer | normalized |

## Terminology Normalization Applied

Canonical preference now enforced in normalization pass:
- alignment/kernel-row-space compatibility over rank-only shorthand,
- exact recoverability / exact correction language over entropy/inverse rephrasing on exact branches,
- bounded-domain obstruction language tied to boundary/Hodge compatibility,
- explicit evidence labels from terminology reference.

## Canonical Spine Coherence Fixes Applied

- Final theorem spine updated to include constrained-observation/fiber positive package and bounded-domain restricted exact theorem.
- Final no-go spine updated to include anti-classifier and false-positive/mismatch limits package.
- Final operator and architecture spines updated to include observation/fiber branch operator structure and branch boundaries.

## Residual Risks

1. Stability-vs-exactness lane remains partially open; avoid promoting universal stability theorem language.
2. Bounded-domain full exactness theorem beyond finite-mode family remains open.
3. Weighted-cost anti-classifier extension remains expansion lane, not promoted theorem spine.

## Normalization Outcome

Theorem/claim structure is now aligned across:
- claim registry,
- proof-status map,
- final theorem/no-go/operator/architecture spines,
- and lens-integration decision docs.
