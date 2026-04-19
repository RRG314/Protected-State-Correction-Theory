# Final Universal Core

Date: 2026-04-17

## Core Decision

A full universal theory across OCP, soliton, MHD, and SDS does **not** survive.
A branch-limited unifying framework does survive with a small abstract core plus branch-specific strengthening.

## Universal Core (promoted)

### UC-1: Factorization/Fiber Exactness Core
For a declared admissible family `A`, target `T`, and record `M`:
- exact recoverability holds iff `T` factors through `M` on `A`,
- equivalently iff `T` is constant on fibers of `M`.

Status: `PROVED` (abstract recoverability core).

### UC-2: Collision/Indistinguishability No-Go Core
If there exist `x,x' in A` with `M(x)=M(x')` but `T(x) != T(x')`, exact recovery fails on `A`.

Status: `PROVED` (universal no-go corollary).

## Branch-Limited Core (promoted as restricted)

### BC-1: Compatibility over amount
Amount/rank/budget alone do not classify exactness on supported restricted families.

Status: `PROVED` in OCP restricted-linear branch; `PROVED ON SUPPORTED FAMILY` or `CONDITIONAL` in soliton lanes.

### BC-2: Family-enlargement fragility
Exactness on a smaller admissible family can fail on an enlarged family.

Status: `PROVED` in OCP restricted-linear lane; partial/conditional parallels elsewhere.

### BC-3: Model-mismatch instability
Exactness under true family does not guarantee robustness of mismatched decoder/architecture.

Status: `PROVED` in canonical OCP lane; branch-dependent conditional/validated analogues elsewhere.

### BC-4: Domain/topology/boundary obstruction
Exactness can be blocked by architecture-domain incompatibility even when scalar constraints appear corrected.

Status: `PROVED` in bounded-domain OCP lane and supported MHD radial/annular classes.

## Not in Universal Core

- Universal projection-preservation law: `REJECTED`.
- Universal amount-only classifier: `REJECTED`.
- Universal emergence/recoverability equivalence: `REJECTED`.
- Two-reservoir SDS engineering motif as theorem core: `ANALOGY ONLY`.

## Final Formulation

The surviving unifying theory is:

**Structure-Dependent Recoverability and Obstruction Framework (branch-limited):**
- universal abstract core: factorization + collision no-go,
- branch-limited strengthening: compatibility, fragility, mismatch, domain obstruction,
- explicit separation of theorem-core from engineering/discovery analogies.
