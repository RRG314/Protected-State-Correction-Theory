# Branch Literature Map (2026-04-16)

## Purpose

Single branch-indexed map from repo branches to canonical literature anchors and novelty status.

## Map

| Branch | Core objects | Canonical references | Repo contribution status |
| --- | --- | --- | --- |
| Exact finite-dimensional orthogonal projection | subspace split, orthogonal projector | Kato (operator framework) | standard fact in repo theorem packaging (`OCP-002`, `OCP-003`, `OCP-016`) |
| Exact sector / QEC | orthogonal syndrome sectors, sector recovery maps | Knill-Laflamme, Gottesman, Ahn-Doherty-Landahl | mostly standard anchor with repo branch integration (`OCP-005`, `OCP-019`, `OCP-021`) |
| Exact periodic Helmholtz/Leray | divergence-free/gradient decomposition on periodic domain | Chorin; Brown-Cortez-Minion; Guermond-Minev-Shen | standard projection result in OCP framing (`OCP-006`, `OCP-027`) |
| Bounded-domain / Hodge / CFD | boundary-compatible decomposition, harmonic/topological obstruction | Arnold-Falk-Winther; Hatcher; Guermond-Minev-Shen | mixed: standard background + repo theorem/no-go packaging (`OCP-023`, `OCP-028`, `OCP-029`, `OCP-044`) |
| Maxwell / gauge projection | transverse/longitudinal split, gauge orbit interpretation | Calabrese; Berchenko-Kogan/Stern | standard physics operator facts mapped into branch (`OCP-022`) |
| Asymptotic generator | invariant split, spectral abscissa/gap, semigroup decay | Pazy; Engel-Nagel; Davis-Kahan | standard functional-analytic machinery with repo branch-level theorem/no-go integration (`OCP-013`, `OCP-014`, `OCP-015`, `OCP-020`) |
| Constrained-observation / recoverability | record map, target map, fiber constancy, row-space/kernel alignment | Björck-Golub; Davis-Kahan; Donoho; Candès-Romberg-Tao | mixture: known core + repo integrated theorem package (`OCP-030`–`OCP-047`) |
| Fiber/unified limits | target hierarchy, anti-classifier, family-enlargement and mismatch fragility | Shannon; Hamming; Villaverde et al.; Alberti-Capdeboscq-Privat | strongest plausibly literature-distinct integrated package on restricted-linear classes (`OCP-048`–`OCP-053`) |

## Discipline Rules Used

1. promote only branch claims with explicit proof/witness artifacts,
2. keep standard facts labeled as standard,
3. label repo novelty as theorem package/organization unless literature-distinct status is justified,
4. avoid universal claims not supported across branches.

## Reusable Cross-Links

- bibliography: `docs/references/protected-state-correction.bib`
- core references: `docs/references/core-references.md`
- lens integration map: `docs/references/lens-integration-reference-map.md`
- theory positioning: `docs/references/theory-candidate-literature-positioning.md`
