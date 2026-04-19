# Protected-State Correction and Recoverability

[![Release](https://img.shields.io/github/v/release/RRG314/Protected-State-Correction-Theory?display_name=tag)](https://github.com/RRG314/Protected-State-Correction-Theory/releases)
[![License: MIT](https://img.shields.io/github/license/RRG314/Protected-State-Correction-Theory)](./LICENSE)
[![Workbench](https://img.shields.io/badge/Workbench-Live-0f8f82)](https://rrg314.github.io/Protected-State-Correction-Theory/docs/workbench/)
[![Program Scope](https://img.shields.io/badge/Scope-Branch--first%20%7C%20Theorem--first-1f6feb)](./branches/README.md)

Program identity: Protected-State Correction Theory (OCP).

This repository studies one technical question:

**When can you recover the target you care about from the measurements you actually have?**

That question appears in several places: quantum error correction, partially observed control, CFD/MHD projection and closure, and restricted inverse problems.

## What this repo does

The repo gives explicit success and failure criteria for recoverability on declared families. It treats recoverability as a compatibility problem between:
- the observation map,
- the target map,
- and the admissible family.

When exact recovery is impossible, the repo gives either a proof of impossibility or a minimal augmentation requirement.

## Known backbone vs repo contribution

Known backbone in the literature:
- factorization and fiber constancy logic,
- restricted linear kernel and row-space criteria,
- standard identifiability and observability framing.

What this repo contributes:
- branch-limited no-go theorems with executable witness families,
- anti-classifier results that rule out amount-only exact classifiers on declared classes,
- minimal augmentation laws tied to concrete artifacts and tests,
- reproducible diagnostics that separate descriptor amount from compatibility structure.

## Strongest result right now

The strongest publishable lane is the restricted fiber and anti-classifier package (`OCP-049` to `OCP-053`) with reproducible witness artifacts.

Start here:
- [Strongest paper lane](./docs/restricted-results/strongest-paper-lane.md)
- [Restricted linear fiber theory](./docs/fiber-based-recoverability-and-impossibility/restricted-linear-fiber-theory.md)
- [Descriptor-fiber anti-classifier branch paper](./papers/descriptor-fiber-anti-classifier-branch.md)

## Two concrete examples

1. Same rank, opposite recoverability
Two observation designs can have the same rank and the same measurement count, but one exactly recovers the target and the other does not. This is a direct witness against rank-only classification.

2. Boundary-sensitive projection failure
A periodic projector can remove divergence in a bounded domain but still fail target recovery because boundary compatibility is violated. The amount of observation did not change, but structural compatibility did.

## What this does in practice

If you design a sensing or correction architecture, this repo helps you answer:
- is exact recovery possible on my declared family,
- if not, what exact obstruction causes failure,
- what is the smallest augmentation that can fix it,
- which diagnostics are useful and which are only amount summaries.

## Where to go next

If you want a fast orientation:
- [Start here](./docs/overview/start-here.md)
- [Repo authority map](./docs/overview/repo-authority-map.md)

If you want theorem anchors:
- [Theorem core lane](./docs/theorem-core/README.md)

If you want branch-limited contribution results:
- [Restricted results lane](./docs/restricted-results/README.md)

If you want diagnostics and implementation details:
- [Methods and diagnostics lane](./docs/methods-diagnostics/README.md)

If you want validation and evidence:
- [Validation and evidence lane](./docs/validation-evidence/README.md)

If you want physics-facing interpretation with strict boundaries:
- [Physics translation lane](./docs/physics-translation/README.md)

If you want audits, overlap positioning, and claim policy:
- [Meta-governance lane](./docs/meta-governance/README.md)

## Branch map

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
