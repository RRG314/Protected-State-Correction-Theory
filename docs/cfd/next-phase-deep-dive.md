# CFD Bounded-Domain Deep Dive (Next Phase)

## Lane Definition

- Protected object: divergence-compatible velocity component under boundary conditions.
- Disturbance family: irrotational/boundary-incompatible components contaminating velocity reconstruction.
- Observation/correction architecture: periodic projection transplant vs bounded-domain Hodge-compatible correction.

Core sources:
- [`src/ocp/cfd.py`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/src/ocp/cfd.py)
- [`src/ocp/next_phase.py`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/src/ocp/next_phase.py)
- [`data/generated/next-phase/cfd_deep_dive.csv`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/data/generated/next-phase/cfd_deep_dive.csv)

## Starting Anchors

- positive anchor: bounded finite-mode boundary-compatible Hodge theorem (`OCP-044`).
- no-go anchors: transplant failure (`OCP-023`) and divergence-only bounded no-go (`OCP-028`).

## Next-Phase Quantitative Findings

From the generated sweep over `grid_size in {17,25,33}` and contamination `{0.1,0.2,0.3}`:

- periodic divergence suppression remains extremely large (`min ~ 9.13e10`), with near-zero periodic recovery error in periodic class,
- bounded transplant keeps large boundary-normal residual,
- bounded Hodge-compatible correction keeps boundary-normal residual near machine floor,
- bounded-Hodge vs transplant boundary-normal ratio is massive (`min ~ 2.99e8`),
- bounded Hodge recovery error remains near machine floor (`max ~ 1.02e-14`).

## Promoted Statements

### CFD-NP-1: Boundary compatibility is a quantitative separator, not just a qualitative warning
Status: `VALIDATED` (supported explicit families).

### CFD-NP-2: Periodic transplant and bounded Hodge classes are sharply separated by boundary-normal residual ratio
Status: `VALIDATED` (explicit families).

### CFD-NP-3: Universal bounded-domain exactness classifier beyond explicit compatible families
Status: `OPEN`.

## Falsification Notes

Rejected in this pass:
- "periodic exactness quality implies bounded exactness under naive transplant".
- "divergence suppression alone certifies bounded exact recovery".

Both remain inconsistent with branch theorems and generated witnesses.

## Literature Positioning

- likely literature-known: projection methods, Hodge compatibility, boundary-condition sensitivity (Chorin 1968; Brown-Cortez-Minion 2001; Guermond-Minev-Shen 2006; Arnold-Falk-Winther 2006).
- repo framing and value: theorem/no-go packaging with executable domain-family witnesses and branch-scoped design diagnostics.

## Next Theorem Targets

1. sharpen boundary-obstruction theorem into computable boundary-compatibility index,
2. extend finite-mode compatibility theorem to broader explicit bounded families,
3. derive perturbation margins for boundary-condition mismatch.
