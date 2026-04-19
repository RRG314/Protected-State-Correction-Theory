# Protected-State Correction and Recoverability

[![Release](https://img.shields.io/github/v/release/RRG314/Protected-State-Correction-Theory?display_name=tag)](https://github.com/RRG314/Protected-State-Correction-Theory/releases)
[![License: MIT](https://img.shields.io/github/license/RRG314/Protected-State-Correction-Theory)](./LICENSE)
[![Workbench](https://img.shields.io/badge/Workbench-Live-0f8f82)](https://rrg314.github.io/Protected-State-Correction-Theory/docs/workbench/)
[![Program Scope](https://img.shields.io/badge/Scope-Branch--first%20%7C%20Theorem--first-1f6feb)](./branches/README.md)

Program identity: Protected-State Correction Theory (OCP).

This repository develops a theorem-first program in protected-state correction and constrained-observation recoverability. The central object is a declared triple `(A, M, T)`: admissible family, record map, and target map. Recovery claims are accepted only with explicit family scope, assumptions, and reproducible evidence.

## Scope

The repository studies exact and approximate target recovery under partial or constrained records. The same formal question appears in QEC-style sector recovery, partially observed control, CFD/MHD projection and closure limits, and restricted inverse settings.

## Adopted Backbone and Restricted Contributions

Adopted backbone:

- factorization and fiber-constancy logic,
- restricted linear row-space and kernel criteria,
- standard observability and identifiability framing.

Restricted contributions:

- branch-limited no-go theorems with executable witness families,
- anti-classifier results excluding amount-only exact classifiers on declared classes,
- minimal augmentation laws linked to generated artifacts,
- descriptor-fiber diagnostics that separate amount summaries from compatibility structure.

## Current Strong Result

The strongest publishable lane is the restricted fiber and anti-classifier package (`OCP-049` to `OCP-053`) with reproducible witness artifacts.

Canonical starting set:

- [Strongest paper lane](./docs/restricted-results/strongest-paper-lane.md)
- [Restricted linear fiber theory](./docs/fiber-based-recoverability-and-impossibility/restricted-linear-fiber-theory.md)
- [Descriptor-fiber anti-classifier branch paper](./papers/descriptor-fiber-anti-classifier-branch.md)

## Representative Witnesses

Same-rank opposite verdict:
Two observation designs can share rank and measurement count while only one exactly recovers the target. This is a direct witness against rank-only classification.

Boundary-sensitive projection failure:
A periodic projector can remove divergence in a bounded domain and still fail target recovery because boundary compatibility is violated.

## Repository Map

Canonical routing:

- [Start here](./docs/overview/start-here.md)
- [Repo authority map](./docs/overview/repo-authority-map.md)
- [Figure Index (image center)](docs/visuals/figure-index.html)
- [Visual Gallery](docs/visuals/visual-gallery.html)

Primary lanes:

- [Theorem core lane](./docs/theorem-core/README.md)
- [Restricted results lane](./docs/restricted-results/README.md)
- [Methods and diagnostics lane](./docs/methods-diagnostics/README.md)
- [Validation and evidence lane](./docs/validation-evidence/README.md)
- [Professional validation surface](./docs/app/professional-validation-report.md)
- [Physics translation lane](./docs/physics-translation/README.md)
- [Meta-governance lane](./docs/meta-governance/README.md)

## Branch Architecture

The repo is branch-first:

- [Core OCP backbone](./branches/00-core-ocp/README.md)
- [Exact projector and exact sector/QEC branch](./branches/01-exact-projector-and-sector/README.md)
- [Asymptotic generator branch](./branches/02-generator-and-asymptotic/README.md)
- [Constrained observation and recoverability branch](./branches/03-constrained-observation-and-pvrt/README.md)
- [Fiber-based recoverability and impossibility branch](./branches/04-fiber-recoverability-and-no-go/README.md)
- [Restricted linear augmentation/design branch](./branches/05-positive-recoverability-and-design/README.md)
- [Invariant and augmentation analysis branch](./branches/06-invariants-and-augmentation/README.md)
- [Periodic/Helmholtz and bounded-domain/Hodge CFD branch](./branches/07-cfd-bounded-domain/README.md)
- [MHD closure and obstruction branch](./branches/08-mhd-closure-and-obstruction/README.md)
- [Physics extension branch](./branches/09-physics-extension/README.md)
- [Workbench and discovery systems](./branches/10-workbench-and-discovery-systems/README.md)

## License

MIT - see [LICENSE](./LICENSE).
