# Protected-State Correction Workbench Overview

## What It Is

The Protected-State Correction Workbench is a static scientific tool that makes the repository's strongest exact, asymptotic, and no-go results inspectable in the browser.

It is not a detached demo layer. Every module is linked to a theorem, a conditional branch, or an explicit rejected bridge in the repository.

## Modules
- Recoverability Lab
- Exact Projection Lab
- QEC Sector Lab
- MHD Projection Lab
- CFD Projection Lab
- Gauge Projection Lab
- Continuous Generator Lab
- No-Go Explorer

## What It Can Do
- inspect exact projector recovery and overlap failure
- explore recoverability under constrained observation across analytic, quantum, periodic-flow, and control-observer examples
- vary record complexity directly in the Recoverability Lab:
  - analytic degeneracy `ε`
  - qubit phase window
  - periodic Fourier cutoff and protected modal target
  - control observation horizon and control-family mode
- inspect exact, approximate, asymptotic, and impossible regimes without leaving the page
- compare exact periodic projection versus GLM asymptotic reduction
- inspect periodic incompressible velocity projection versus bounded-domain limits
- inspect a kept Maxwell / gauge projection extension
- inspect generator kernels, mixing, and finite-time exact-recovery failure
- inspect rejected bridges such as the bounded-domain projector transplant
- scrub time-history branches frame by frame in the MHD, gauge, and continuous-generator modules
- reset the current lab or the full workbench state without leaving the page
- save scenarios, reload them, export JSON, export figures, and share state links

## Recoverability Lab Highlights

The Recoverability Lab is the strongest recent branch-level addition.

It now supports four conventional system lanes:
- analytic benchmark
- fixed-basis qubit record
- finite periodic incompressible modal family
- functional-observability / control family

It exposes real branch outputs rather than placeholders:
- `κ(0)` and selected `κ(δ)`
- `κ(η)/2` lower bound in the analytic lane
- periodic modal cutoff thresholds tied to the chosen protected variable
- finite-history and asymptotic splits in the control lane
- diagonal minimal-history thresholds in the three-state control family

## What It Is For
- reviewer orientation
- theorem illustration
- teaching the exact-versus-asymptotic split
- showing minimal-record threshold behavior on tested families
- making time-dependent correction behavior visible instead of burying it in endpoint-only summaries
- making the physics extension legible without overclaiming it
- quick structural checks before reading the longer proofs
- checking whether a coarse record is good enough for exact recovery before trying to design a correction map

## What It Is Not For
- replacing the proofs
- claiming new physics theorems that are not in the repo
- hiding conditional status behind polished visuals
- turning analogy-only directions into promoted modules
- pretending that every branch has a meaningful time-history animation when the underlying result is static
