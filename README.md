# Orthogonal Correction Principle (OCP) Research Program

This repository develops the Orthogonal Correction Principle as a formal research direction about **protected-state correction**.

Plain-language version:
- some part of a system is the part we want to preserve,
- some part of a system is disturbance or error,
- correction works only when the disturbance can be separated from what must be preserved,
- and the correction machinery is strong enough to remove or suppress the disturbance without damaging the protected part.

Formal version:
- choose a state space `H`, a protected subspace `S`, and a disturbance space `D`,
- construct correction operators that act on `D` while fixing `S`,
- prove exact recovery when possible,
- prove asymptotic suppression when exact recovery is impossible or too expensive,
- and prove no-go results when the decomposition or distinguishability assumptions fail.

## What This Repository Actually Achieves

This repository does **not** claim a grand universal theorem covering quantum error correction, control theory, divergence cleaning, and machine learning in one stroke.

It does produce a narrower and more credible outcome:
- a usable formal language for protected-state correction,
- exact finite-dimensional theorems for orthogonal projector recovery,
- exact continuous operator constructions using Helmholtz/Leray projection,
- asymptotic correction theorems for continuous damping and invariant-split generators,
- a clean QEC rewrite in OCP language using code space, syndrome sectors, and recovery maps,
- and explicit impossibility results showing when correction cannot be defined nontrivially.

That makes the current program best described as:
- **a protected-state correction framework with real operator constructions and no-go results**,
- plus a serious bridge between exact correction and asymptotic correction.

## Strongest Current Results

### Exact results
- **Exact projection recovery theorem:** if `H = S ⊕ D` with `S ⟂ D`, orthogonal projection onto `S` exactly recovers the protected component.
- **Indistinguishability no-go theorem:** if `S ∩ D != {0}`, exact recovery from `x = s + d` is impossible by any single-valued recovery map.
- **Continuous damping theorem:** the flow `xdot = -k P_D x` leaves `S` fixed and exponentially damps `D`.
- **Invariant-split generator theorem:** a much wider class of linear generators `K` preserves `S` and suppresses `D` when `K|_S=0`, `K(D)\subseteq D`, and the restriction on `D` is exponentially stable.
- **Self-adjoint PSD corollary:** if `K` is positive semidefinite with `ker(K)=S`, the spectral gap on `S^\perp` gives an explicit decay bound.
- **Helmholtz/Leray projection example:** periodic divergence cleaning gives an exact continuous-domain OCP operator.
- **Linear-flow mixing no-go:** if `P_S K P_D \neq 0`, disturbance leaks into protected coordinates and the flow is not an OCP correction flow.

### Conditional or system-dependent results
- **QEC fits OCP exactly** when the relevant Knill-Laflamme / syndrome-separation assumptions hold.
- **GLM cleaning fits OCP asymptotically**, not as an exact projector.
- **Control theory fits conditionally** when the protected/disturbance split is invariant and feedback acts only on correctable modes.

### Not promoted
- optimizer / ML bridges,
- broad universal-capacity claims,
- vague cross-domain unification language without operator content.

## Start Here

1. [start-here.md](docs/overview/start-here.md)
2. [formal-theory.md](docs/formalism/formal-theory.md)
3. [qec-foundations.md](docs/qec/qec-foundations.md)
4. [divergence-cleaning-in-ocp.md](docs/mhd/divergence-cleaning-in-ocp.md)
5. [generator-theorems.md](docs/theorem-candidates/generator-theorems.md)
6. [no-go-results.md](docs/impossibility-results/no-go-results.md)

## Repository Map

- `docs/overview/` - entry points, discovery inventory, claim registry, proof status
- `docs/formalism/` - core definitions and exact vs asymptotic split
- `docs/qec/` - exact QEC anchor and OCP rewrite
- `docs/control/` - cautious control-theoretic extension
- `docs/mhd/` - exact projection cleaning and asymptotic GLM cleaning
- `docs/operators/` - actual projector and recovery constructions
- `docs/theorem-candidates/` - central theorem, continuous generator theorems, and theorem program
- `docs/impossibility-results/` - exact no-go results and failed/unfinished unification attempts
- `src/ocp/` - executable operator and validation code
- `tests/` - finite-dimensional, QEC, MHD, and continuous-generator validation checks
- `archive/raw-imports/` - preserved local source material used to build this program

## How To Validate

```bash
cd '/Users/stevenreid/Documents/New project/repos/ocp-research-program'
./scripts/validate/run_all.sh
```

This rebuilds the discovery inventory and claim registry, runs operator examples, and executes the test suite.

## Current Status

The honest current rating is **GOOD**.

Why not `EXCELLENT` yet:
- the strongest exact theorems are still linear-algebraic or operator-theoretic rather than deep new cross-domain theorems,
- the QEC and Helmholtz anchors are real but largely reinterpret known structures,
- the control extension is conditional rather than theorem-complete,
- and the framework still needs either a sharper category-specific capacity theorem or a stronger boundary-sensitive continuous theorem to reach a clearly higher level.

Why this is still meaningful:
- the repo now has a real theorem spine,
- a real operator spine,
- a clear exact/asymptotic split,
- and a falsification-first boundary around what OCP can and cannot honestly claim.

## Deep Report

- [SYSTEM_REPORT.md](SYSTEM_REPORT.md)
