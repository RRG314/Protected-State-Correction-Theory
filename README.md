# Protected-State Correction and Recoverability

[![Release](https://img.shields.io/github/v/release/RRG314/Protected-State-Correction-Theory?display_name=tag)](https://github.com/RRG314/Protected-State-Correction-Theory/releases)
[![License: MIT](https://img.shields.io/github/license/RRG314/Protected-State-Correction-Theory)](./LICENSE)
[![Workbench](https://img.shields.io/badge/Workbench-Live-0f8f82)](https://rrg314.github.io/Protected-State-Correction-Theory/docs/workbench/)
[![Program Scope](https://img.shields.io/badge/Scope-Branch--first%20%7C%20Theorem--first-1f6feb)](./branches/README.md)

_Program identity: Protected-State Correction Theory (OCP)._ 

This repository studies one recurring technical question across several fields:

**when can a system remove unwanted components without disturbing what must be preserved?**

That question appears in quantum error correction, control and observability, projection methods in CFD and MHD, and reconstruction from constrained measurements. The project isolates the shared structure behind those settings and states exact success and failure conditions with explicit scope.

## Overview

The program is theorem-first. For each branch, it defines a protected target, describes the disturbance or ambiguity class, and asks whether recovery from the available record is exact, impossible, or repairable by minimal augmentation. Whenever exact theorems are not available, results are labeled as restricted-family, validated, conditional, or open.

## Core Structure

Most branches use four objects: a state space, a target map, a record map, and a correction or decoder map. The central question is whether the target factors through the record. In fiber language, exact recoverability holds exactly when the target is constant on observation fibers.

In the restricted linear setting with `x = Fz`, `y = OFz`, and target `LFz`, exact linear recovery exists if and only if

$$
\ker(OF) \subseteq \ker(LF)
\quad\text{equivalently}\quad
\operatorname{row}(LF) \subseteq \operatorname{row}(OF).
$$

When this fails, minimal free augmentation is

$$
\delta(O,L;F)=\operatorname{rank}\!\begin{bmatrix}OF\\LF\end{bmatrix}-\operatorname{rank}(OF).
$$

## Main Results

The repository combines positive and negative results. On supported classes, exact recoverability and minimal-repair laws are explicit. The no-go side is equally central: same rank or same measurement count does not guarantee recoverability, and no rank-only or fixed-budget exact classifier survives. This is why the program emphasizes compatibility structure over amount-only summaries.

The current quantitative layer adds context-sensitive and descriptor-fiber diagnostics (`CID`, `delta_free`, `delta_C`, `DFMI`, `IDELB`, `CL`) where they improve classification on declared families.

## Branches

The repo is organized as a branch-first research program:

- [Core OCP backbone](./branches/00-core-ocp/README.md)
- [Exact projector and exact sector/QEC branch](./branches/01-exact-projector-and-sector/README.md)
- [Asymptotic generator branch](./branches/02-generator-and-asymptotic/README.md)
- [Constrained-observation and recoverability branch](./branches/03-constrained-observation-and-pvrt/README.md)
- [Fiber-based recoverability and impossibility branch](./branches/04-fiber-recoverability-and-no-go/README.md)
- [Restricted-linear augmentation/design branch](./branches/05-positive-recoverability-and-design/README.md)
- [Invariant and augmentation analysis branch](./branches/06-invariants-and-augmentation/README.md)
- [Periodic/Helmholtz and bounded-domain/Hodge CFD branch](./branches/07-cfd-bounded-domain/README.md)
- [MHD closure and obstruction branch](./branches/08-mhd-closure-and-obstruction/README.md)
- [Physics extension branch](./branches/09-physics-extension/README.md)
- [Workbench and discovery systems](./branches/10-workbench-and-discovery-systems/README.md)

## Canonical Documentation Routing

- [Single authority map](./docs/overview/repo-authority-map.md)
- [Theorem core lane](./docs/theorem-core/README.md)
- [Restricted results lane](./docs/restricted-results/README.md)
- [Methods and diagnostics lane](./docs/methods-diagnostics/README.md)
- [Validation and evidence lane](./docs/validation-evidence/README.md)
- [Physics translation lane](./docs/physics-translation/README.md)
- [Meta-governance lane](./docs/meta-governance/README.md)

## Workbench

The workbench is an interface for testing recoverability conditions, diagnosing structural failure, and applying supported repair operations. It is tied to the theorem layer and benchmark catalogs; it is not treated as an independent source of mathematical claims.

## Scope

Theorems are branch-limited by design. Exact results are proved on explicitly defined classes, broader claims are promoted only when they survive counterexample pressure, and exploratory physics extensions are kept separate from the core spine. The repository does not claim a universal recoverability law across all systems.

## Use Cases

Typical uses include recoverability diagnosis for a fixed measurement design, minimal augmentation planning, anti-classifier counterexample construction, bounded-domain projection failure analysis, and branch-limited physics interpretation where theorem status is explicit.

## Papers and Contributions

- [Main contributions](./docs/overview/main-contributions.md)
- [Papers index](./papers/README.md)
- Descriptor-fiber anti-classifier branch paper: [papers/descriptor-fiber-anti-classifier-branch.md](./papers/descriptor-fiber-anti-classifier-branch.md)

## License

MIT — see [LICENSE](./LICENSE).
