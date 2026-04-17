# Integration Reference Audit (2026-04-16)

## Purpose

Audit citation completeness after integration/cleanup and classify each major lane as:
- standard literature fact,
- repo framing of known fact,
- repo-new theorem package,
- literature-unclear,
- plausibly literature-distinct.

## Coverage Summary

| Lane | Coverage status | Primary sources present | Audit verdict |
| --- | --- | --- | --- |
| Operator theory / perturbation | complete foundational anchors | Kato, Davis-Kahan, Björck-Golub | adequate for promoted operator language |
| Functional analysis / semigroups | complete foundational anchors | Pazy, Engel-Nagel | adequate for asymptotic branch claims |
| Projection / CFD / Helmholtz-Hodge | complete foundational anchors | Chorin, Brown-Cortez-Minion, Guermond-Minev-Shen | adequate for periodic/bounded projection framing |
| Topology / Hodge / bounded-domain obstruction | foundational anchors present | Arnold-Falk-Winther, Hatcher | adequate for current bounded-domain claims |
| QEC / sector anchors | foundational anchors present | Knill-Laflamme, Gottesman, Ahn-Doherty-Landahl | adequate for exact-sector and CQEC bridge language |
| Observability / identifiability / inverse lane | targeted anchors present | Villaverde et al., Alberti-Capdeboscq-Privat | adequate for restricted stability/mismatch framing |
| Information theory (secondary) | foundational anchors present | Shannon, Hamming | adequate; remains demoted for exact-branch core language |

## Branch-Level Literature Positioning

| Branch | Standard fact vs repo contribution |
| --- | --- |
| exact projector / sector / periodic Helmholtz | mostly standard facts + repo synthesis/packaging |
| bounded-domain/Hodge | standard Hodge/topology machinery + repo-specific obstruction/exactness packaging |
| asymptotic generator | standard semigroup/spectral machinery + repo branch-specific no-go and rate use |
| constrained-observation | standard linear/factorization core + repo-specific integrated theorem/no-go witness package |
| fiber limits | plausibly literature-distinct integrated anti-classifier/fragility package on restricted-linear classes |

## Citation Gaps Found

No major unsourced promoted external facts were found in the canonical integration docs.

Minor discipline note:
- branch-specific exploratory reports may still use broader vocabulary (including inverse-problem framing) more freely than canonical docs; this is acceptable as long as promoted claims in spines/maps remain citation-disciplined and scope-labeled.

## Actions Completed in This Pass

1. retained and cross-linked canonical reference anchors in:
   - `docs/references/core-references.md`
   - `docs/references/lens-integration-reference-map.md`
   - `docs/references/theory-candidate-literature-positioning.md`
2. validated that promoted theorem/no-go packages map to branch-level references and proof artifacts.
3. kept novelty language qualified and branch-scoped.

## Audit Verdict

Reference discipline is now strong enough for publication-facing branch claims, with novelty positioned conservatively and tied to theorem IDs/witness artifacts.
