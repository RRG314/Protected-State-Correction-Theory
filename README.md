# Protected-State Correction Theory

[![Release](https://img.shields.io/github/v/release/RRG314/Protected-State-Correction-Theory?display_name=tag)](https://github.com/RRG314/Protected-State-Correction-Theory/releases)
[![Workbench](https://img.shields.io/badge/Workbench-Live-0f8f82)](https://rrg314.github.io/Protected-State-Correction-Theory/docs/workbench/)
[![Scope](https://img.shields.io/badge/Scope-Exact%20%7C%20Asymptotic%20%7C%20No--Go-1f6feb)](https://github.com/RRG314/Protected-State-Correction-Theory/blob/main/docs/finalization/architecture-final.md)
[![Physics Extension](https://img.shields.io/badge/Physics-QEC%20%7C%20Projection%20%7C%20Damping-5c6ac4)](https://github.com/RRG314/Protected-State-Correction-Theory/blob/main/docs/physics/physics-system-matrix.md)

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
- GLM cleaning as an asymptotic continuous architecture, explicitly not exact.

## What Is Inside

The repository is organized so readers can enter from different angles:

- theory and proofs for readers who want the formal spine first,
- a workbench for readers who want to test the structure interactively,
- physics bridge documents for readers who care about concrete systems,
- executable code and validation for readers who want reproducibility.

## Start Here

1. [Start Here](docs/overview/start-here.md)
2. [Initial Public Release Notes](docs/releases/v1.0.0.md)
3. [Final Architecture](docs/finalization/architecture-final.md)
4. [Final Theorem Spine](docs/finalization/theorem-spine-final.md)
5. [Final No-Go Spine](docs/finalization/no-go-spine-final.md)
6. [How To Read This Repo](docs/peer_review/how-to-read-this-repo.md)
7. [Protected-State Correction Workbench](docs/workbench/index.html)
8. [Physics System Matrix](docs/physics/physics-system-matrix.md)
9. [Citable Expansion Directions](docs/references/citable-expansion-directions.md)

## What You Can Do With This Repository

Use it as a theory repository:
- read the theorem spine, no-go spine, and proof-status map to see exactly what has been proved and where the boundaries are.

Use it as a scientific workbench:
- run the static workbench to explore exact projection, sector recovery, generator-based damping, and explicit no-go examples.

Use it as a physics comparison layer:
- trace which physics systems are kept, which are conditional, and which were rejected after operator-level testing.

Use it as a research starting point:
- follow the citable reference map and the open-problem catalog to connect the current framework to stronger outside literatures without blurring the limits of the present repo.

## Protected-State Correction Workbench

The repository now includes a static GitHub-Pages-compatible workbench in:

- `docs/workbench/`

Modules:
- Exact Projection Lab
- QEC Sector Lab
- MHD Projection Lab
- Gauge Projection Lab
- Continuous Generator Lab
- No-Go Explorer

The workbench is tied directly to the theorem and no-go documents. It is not a detached demo layer.

## Physics Extension

The strongest kept physics lanes are:
- QEC as the exact sector anchor,
- periodic Helmholtz/Leray projection as the exact continuous anchor,
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
- `docs/physics/` - kept and rejected physics bridges, including the citable extension matrix
- `docs/control/` - conditional control extension and worked linear example
- `docs/theorem-candidates/` - theorem-level results including generator, capacity, and sector branches
- `docs/impossibility-results/` - core and advanced no-go structure
- `docs/open-questions/` - disciplined open-problem catalog and dead-end curation
- `docs/workbench/` - static Pages-ready scientific workbench
- `src/ocp/` - executable operator and validation code
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
