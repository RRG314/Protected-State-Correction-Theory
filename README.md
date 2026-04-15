# Protected-State Correction Theory

[![Release](https://img.shields.io/github/v/release/RRG314/Protected-State-Correction-Theory?display_name=tag)](https://github.com/RRG314/Protected-State-Correction-Theory/releases)
[![Workbench](https://img.shields.io/badge/Workbench-Live-0f8f82)](https://rrg314.github.io/Protected-State-Correction-Theory/docs/workbench/)
[![Scope](https://img.shields.io/badge/Scope-Exact%20%7C%20Asymptotic%20%7C%20No--Go-1f6feb)](https://github.com/RRG314/Protected-State-Correction-Theory/blob/main/docs/finalization/architecture-final.md)
[![Physics Extension](https://img.shields.io/badge/Physics-QEC%20%7C%20Projection%20%7C%20Damping-5c6ac4)](https://github.com/RRG314/Protected-State-Correction-Theory/blob/main/docs/physics/physics-system-matrix.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-2f855a.svg)](LICENSE)

Core principle: **Orthogonal Correction Principle (OCP)**.

This repository exists to answer a focused question that appears in several technical settings:

> when can a system remove the part that should not be there without damaging the part that must be preserved?

The repository develops that question into a theorem-first research program. It treats protected-state correction as a formal framework with exact recovery results, asymptotic correction results, explicit impossibility statements, operator constructions, and a physics extension that is kept only where the operator structure survives honest testing.

In plain language, the project does four things:
- identify what part of a system must be preserved,
- identify what part counts as disturbance, contamination, or nonphysical content,
- build or characterize correction operators that act on the disturbance without corrupting the protected object,
- and prove when exact recovery, asymptotic suppression, or impossibility actually occurs.

In formal language, the project works with a state space `H`, a protected subspace or protected sector, a disturbance family, and a correction architecture. It studies projector recovery, sector recovery, generator-based damping, detectability, correction image, and failure of correction when those structures are not rich enough.

## Initial Public Release

The current public release is [v1.0.0](docs/releases/v1.0.0.md).

This is the first release intended to stand on its own as a public research repository rather than an internal build log. It brings the theorem spine, the no-go layer, the workbench, the physics bridge testing, and the reviewer-facing documents into one coherent public path.

## Why This Repository Exists

The project is not trying to force one grand law across quantum error correction, fluid projection, constraint damping, and control.

Its more grounded goal is to build a usable framework for situations where:
- there is a meaningful protected object,
- there is a meaningful disturbance family,
- and there is a nontrivial question about whether correction can act on one without damaging the other.

That narrower question is still worth pursuing. It produces theorem statements, concrete operators, counterexamples, and design criteria that are easier to test and easier to reuse.

## What This Repository Now Supports

This repository does **not** claim a universal theorem covering QEC, control, PDE correction, and optimization under one scalar law.

It now supports a narrower and stronger statement:
- protected-state correction is a finished theorem-first framework,
- with an exact projector branch,
- an exact sector branch,
- an exact periodic continuous projection anchor,
- an asymptotic generator branch,
- a theorem-grade no-go layer,
- and a physics extension that is real but not universal.

## Strongest Current Results

### Exact branch
- **OCP-T1** exact orthogonal protected-subspace recovery.
- **OCP-T5** exact sector recovery for pairwise orthogonal coordinate-compatible sector embeddings.
- **OCP-T4** exact correction rank lower bound.

### Continuous / asymptotic branch
- **OCP-T2** continuous damping theorem for `x_dot = -k P_D x`.
- **OCP-T3** invariant-split generator theorem.
- **OCP-C2** self-adjoint PSD corollary with explicit spectral-gap decay bound.

### No-go layer
- **OCP-N1** overlap / indistinguishability no-go.
- **OCP-N5** mixing no-go for linear flows.
- **OCP-N7** no finite-time exact recovery in the smooth linear flow branch.
- **OCP-N8** sector-overlap detection no-go.

### Strongest anchor systems
- QEC as the exact sector anchor under standard assumptions.
- Periodic Helmholtz/Leray projection as the exact continuous anchor.
- Periodic incompressible velocity projection as a kept CFD corollary of the exact continuous branch.
- GLM cleaning as an asymptotic continuous architecture, explicitly not exact.

## What Is Inside

The repository is organized so readers can enter from different angles:

- theory and proofs for readers who want the formal spine first,
- a workbench for readers who want to test the structure interactively,
- physics bridge documents for readers who care about concrete systems,
- executable code and validation for readers who want reproducibility.

## Start Here

1. [Start Here](docs/overview/start-here.md)
2. [Usefulness Roadmap](docs/overview/usefulness-roadmap.md)
3. [User Entry Paths](docs/overview/user-entry-paths.md)
4. [Initial Public Release Notes](docs/releases/v1.0.0.md)
5. [Final Architecture](docs/finalization/architecture-final.md)
6. [Final Theorem Spine](docs/finalization/theorem-spine-final.md)
7. [Final No-Go Spine](docs/finalization/no-go-spine-final.md)
8. [How To Read This Repo](docs/peer_review/how-to-read-this-repo.md)
9. [Protected-State Correction Workbench](docs/workbench/index.html)
10. [Recoverability / Correction Studio](docs/app/recoverability-correction-studio.md)
11. [Template Index](docs/templates/README.md)
12. [Constrained-Observation Recoverability Branch](docs/theory/advanced-directions/constrained-observation-recoverability.md)
13. [Physics System Matrix](docs/physics/physics-system-matrix.md)
14. [CFD System Matrix](docs/cfd/cfd-system-matrix.md)
15. [Research-Program Branch Audit](docs/research-program/branch-audit.md)
16. [Ranked Contribution Roadmap](docs/research-program/ranked-roadmap.md)
17. [Open-Problem Program](docs/research-program/open-problem-program.md)
18. [Citable Expansion Directions](docs/references/citable-expansion-directions.md)

## What You Can Do With This Repository

Use it as a theory repository:
- read the theorem spine, no-go spine, and proof-status map to see exactly what has been proved and where the boundaries are.

Use it as a scientific workbench:
- run the static workbench to explore exact projection, sector recovery, generator-based damping, and explicit no-go examples.
- use the Recoverability / Correction Studio to decide what record is sufficient, what weaker target is still recoverable, and what to add next.

Use it as a design system:
- start from the reusable templates to build restricted linear recovery checks, observability checks, projection threshold sweeps, ambiguity witnesses, and no-go diagnostics on your own problem.

Use it as a physics comparison layer:
- trace which physics systems are kept, which are conditional, and which were rejected after operator-level testing.

Use it as a research starting point:
- follow the citable reference map and the open-problem catalog to connect the current framework to stronger outside literatures without blurring the limits of the present repo.

## How To Cite This Work

If you are citing the repository as a whole, use the repository citation metadata and include the release or access context when possible.

Citation files:
- [CITATION.cff](CITATION.cff)
- [How to Cite This Work](docs/references/how-to-cite-this-work.md)
- [Reference Library (BibTeX)](docs/references/protected-state-correction.bib)

If you are citing a specific result, it is best to:
- cite the repository itself,
- name the exact theorem, no-go result, or application document you are using,
- and cite the outside anchor paper that supports the surrounding standard literature.

Author metadata:
- Steven Reid
- ORCID: [0009-0003-9132-3410](https://orcid.org/0009-0003-9132-3410)

## Contributing

This repository is open to contribution, but it is curated around proof status, falsification, and scope control.

The best contributions usually do one of these well:
- sharpen a theorem, proof, lemma, or no-go statement
- improve a kept physics or application lane without forcing it broader
- improve the workbench so it reflects the math more faithfully
- strengthen validation, reproducibility, or reviewer-facing documentation

Start here if you want to help:

1. [CONTRIBUTING.md](CONTRIBUTING.md)
2. [Contributing Paths](docs/overview/contributing-paths.md)
3. [Start Here](docs/overview/start-here.md)

Community files:
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](SECURITY.md)
- [Support](SUPPORT.md)
- [MIT License](LICENSE)

## Protected-State Correction Workbench

The repository now includes a static GitHub-Pages-compatible workbench in:

- `docs/workbench/`

Modules:
- Recoverability / Correction Studio
- Exact Projection Lab
- QEC Sector Lab
- MHD Projection Lab
- CFD Projection Lab
- Gauge Projection Lab
- Continuous Generator Lab
- No-Go Explorer

The workbench is tied directly to the theorem and no-go documents. It is not a detached demo layer.

## Constrained-Observation Branch

The repository now also includes a research branch on **Constrained-Observation Recoverability**.

This branch asks when a coarse record preserves enough information to recover a protected variable exactly, approximately, asymptotically, or not at all. It is grounded in conventional systems rather than only in repo-native language:

- fixed-basis qubit records,
- periodic incompressible-flow reconstruction,
- and a small functional-observability control model.

The strongest current clean results in that branch are:
- the adversarial lower bound `worst-case protected-variable error ≥ κ(η)/2`,
- a closed-form qubit phase-window collision law,
- a restricted-linear minimal-complexity criterion,
- a restricted-linear design layer with ambiguity witnesses and minimal augmentation suggestions,
- family-level periodic functional-support thresholds,
- and a diagonal functional-interpolation threshold law on a scalar-output control family.

Start here:

1. [Branch overview](docs/theory/advanced-directions/constrained-observation-recoverability.md)
2. [Formalism](docs/theory/advanced-directions/constrained-observation-formalism.md)
3. [Derivations](docs/theory/advanced-directions/constrained-observation-derivations.md)
4. [Clean results](docs/theory/advanced-directions/constrained-observation-clean-results.md)
5. [Failures and dead ends](docs/theory/advanced-directions/constrained-observation-failures.md)
6. [Results report](docs/theory/advanced-directions/constrained-observation-results-report.md)
7. [Branch assessment](docs/theory/advanced-directions/constrained-observation-assessment.md)
8. [Recoverability / Correction Studio](docs/app/recoverability-correction-studio.md)
9. [Template Index](docs/templates/README.md)

## Physics Extension

The strongest kept physics lanes are:
- QEC as the exact sector anchor,
- periodic Helmholtz/Leray projection as the exact continuous anchor,
- periodic incompressible projection as a kept CFD extension of the same exact projector branch,
- Maxwell / Coulomb-gauge projection as a kept exact extension of the projector branch,
- GLM divergence cleaning as an asymptotic comparator,
- numerical-relativity constraint damping as a conditional asymptotic extension,
- continuous quantum error correction as a conditional future bridge.

The repo also preserves explicit rejections, including the failure of naive periodic-projector transplantation to bounded-domain problems.

## Repository Map

- `docs/finalization/` - final theorem, no-go, operator, and architecture spine
- `docs/peer_review/` - reviewer-facing framing, novelty, proof status, and paper map
- `docs/formalism/` - core framework and exact-vs-asymptotic split
- `docs/qec/` - QEC foundation and OCP sector framing
- `docs/mhd/` - exact periodic projection and asymptotic GLM branch
- `docs/cfd/` - incompressible projection, bounded-domain scope control, and kept versus rejected CFD bridges
- `docs/physics/` - kept and rejected physics bridges, including the citable extension matrix
- `docs/control/` - conditional control extension and worked linear example
- `docs/theorem-candidates/` - theorem-level results including generator, capacity, and sector branches
- `docs/impossibility-results/` - core and advanced no-go structure
- `docs/open-questions/` - disciplined open-problem catalog and dead-end curation
- `docs/research-program/` - branch audit, ranked roadmap, open-problem program, theory assessment, and usefulness-by-branch notes
- `docs/workbench/` - static Pages-ready scientific workbench
- `docs/templates/` - reusable build templates for exact, asymptotic, and no-go design problems
- `docs/applications/` - practical integration notes, including app / engine-facing recoverability design
- `src/ocp/` - executable operator and validation code
- `scripts/templates/` - script entry points for reusable recoverability and correction setups
- `tests/` - theorem, operator, workbench, and regression checks

## Validation

```bash
cd '/Users/stevenreid/Documents/New project/repos/ocp-research-program'
./scripts/validate/run_all.sh
```

This now runs:
- discovery and claim regeneration
- operator example generation
- static workbench example generation
- markdown link checks
- static workbench asset check
- Python theorem tests
- Node workbench tests

## Release Materials

- [Release Notes Index](docs/releases/README.md)
- [v1.0.0 Release Notes](docs/releases/v1.0.0.md)
- [Changelog](CHANGELOG.md)
- [Final Report](FINAL_REPORT.md)
- [System Report](SYSTEM_REPORT.md)
- [Citation Metadata](CITATION.cff)

## Current Honest Rating

The repository currently earns an **EXCELLENT** rating as a finished repository-scale research program.

Why this rating is justified:
- the repo now has a polished theorem spine,
- materially stronger new theorem/no-go content beyond the earlier baseline,
- a finished negative-results layer,
- reviewer-facing documentation,
- and a real usable static workbench.

Important limit on that rating:
- this does **not** mean OCP is now a universal correction theory,
- and it does **not** erase the fact that the strongest mathematics is still operator-theoretic and that the boundary-sensitive continuous branch remains open.

The current public-facing title is theory-first on purpose:
- main title: **Protected-State Correction Theory**
- core internal principle: **Orthogonal Correction Principle (OCP)**
- physics lane: **Physics Extension of Protected-State Correction Theory**
