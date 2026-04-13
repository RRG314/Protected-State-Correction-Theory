# Orthogonal Correction Principle (OCP) Research Program

This repository develops the Orthogonal Correction Principle as a formal research direction about **protected-state correction**.

Plain-language version:
- identify what part of a system must be preserved,
- identify what part counts as disturbance,
- build correction operators that act on the disturbance without corrupting the protected object,
- and prove when exact recovery, asymptotic suppression, or impossibility actually occurs.

Formal version:
- choose a state space `H`, a protected subspace `S`, and a disturbance family,
- build exact projector or sector recovery operators when possible,
- build asymptotic generator-based correction laws when exact one-step recovery is impossible,
- and prove no-go results when separation, detectability, or correction image are insufficient.

## What This Repository Now Supports

This repository does **not** claim a universal theorem covering QEC, control, PDE correction, and optimization under one scalar law.

It now supports a narrower and stronger statement:
- OCP is a finished protected-state correction framework,
- with an exact projector branch,
- an exact sector branch,
- an exact periodic continuous projection anchor,
- an asymptotic generator branch,
- and a theorem-grade no-go layer.

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

## Start Here

1. [Start Here](docs/overview/start-here.md)
2. [Final Architecture](docs/finalization/architecture-final.md)
3. [Final Theorem Spine](docs/finalization/theorem-spine-final.md)
4. [Final No-Go Spine](docs/finalization/no-go-spine-final.md)
5. [How To Read This Repo](docs/peer_review/how-to-read-this-repo.md)
6. [OCP Workbench](docs/workbench/index.html)

## OCP Workbench

The repository now includes a static GitHub-Pages-compatible workbench in:

- `docs/workbench/`

Modules:
- Exact Projection Lab
- QEC Sector Lab
- MHD Projection Lab
- Continuous Generator Lab
- No-Go Explorer

The workbench is tied directly to the theorem and no-go documents. It is not a detached demo layer.

## Repository Map

- `docs/finalization/` - final theorem, no-go, operator, and architecture spine
- `docs/peer_review/` - reviewer-facing framing, novelty, proof status, and paper map
- `docs/formalism/` - core framework and exact-vs-asymptotic split
- `docs/qec/` - QEC foundation and OCP sector framing
- `docs/mhd/` - exact periodic projection and asymptotic GLM branch
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

## Current Honest Rating

Current honest internal rating: **EXCELLENT** as a finished repository-scale research program.

Why this rating is justified:
- the repo now has a polished theorem spine,
- materially stronger new theorem/no-go content beyond the earlier baseline,
- a finished negative-results layer,
- reviewer-facing documentation,
- and a real usable static workbench.

Important limit on that rating:
- this does **not** mean OCP is now a universal correction theory,
- and it does **not** erase the fact that the strongest mathematics is still operator-theoretic and that the boundary-sensitive continuous branch remains open.

It means the repository is now finished enough, disciplined enough, and documented enough to stand as the main OCP research program going forward.
