# Beginner-to-Advanced Learning Path: Soliton Waves and Geometry

Date: 2026-04-16  
Audience: independent researcher who wants theorem-quality understanding, not just simulations

## Stage 0 — Prerequisites (1–2 weeks)

Target skills:
- PDE basics (well-posedness language)
- Fourier/spectral methods
- ODE phase portraits
- differential geometry basics (curves/surfaces, curvature)
- Hamiltonian mechanics basics

Exit check:
- can derive linear dispersion relation and explain dispersion-vs-nonlinearity tradeoff.

## Stage 1 — Core soliton foundations (2–3 weeks)

Read:
- Zabusky–Kruskal (1965)
- GGKM (1967)
- Lax (1968)
- Drazin–Johnson chapters on KdV/NLS/sine-Gordon

Do:
- derive one-soliton KdV profile by traveling-wave reduction
- numerically simulate one-soliton propagation and two-soliton collision (basic fidelity)

Exit check:
- can state what separates a soliton from a generic solitary pulse.

## Stage 2 — Integrable structure and geometry (2–4 weeks)

Read:
- Zakharov–Shabat (1972)
- Ablowitz–Clarkson (selected chapters)
- Hasimoto (1972)

Do:
- map one geometric relation (curve/torsion lane) to NLS-form dynamics in a toy setup
- list conserved quantities for one integrable model and test numerically

Exit check:
- can explain Lax/IST conceptually and identify where geometric structure is explicit.

## Stage 3 — Beyond exact integrability (2–4 weeks)

Read:
- Kivshar–Malomed (near-integrable dynamics)
- Akhmediev–Ankiewicz (dissipative solitons)
- Benjamin–Feir and Peregrine references

Do:
- run perturbation sweeps (coefficient inhomogeneity / damping)
- quantify coherent-structure defect growth

Exit check:
- can distinguish exact, near-integrable, and dissipative persistence mechanisms.

## Stage 4 — Topological solitons and robust geometry (2–4 weeks)

Read:
- Manton–Sutcliffe
- Nagaosa–Tokura (skyrmion review)

Do:
- compute one topological charge in a toy field configuration
- compare charge-protected vs integrability-protected robustness under matched perturbation design

Exit check:
- can explain why topological and integrable stability are different and non-interchangeable.

## Stage 5 — Reproducible computation and structure-preserving numerics (2–4 weeks)

Read:
- Hairer–Lubich–Wanner
- Bridges (multisymplectic)

Do:
- compare structure-preserving vs non-preserving integrators on long-time soliton diagnostics
- produce reproducible benchmark notebook/scripts

Exit check:
- can justify a numerical method choice using geometric/invariant criteria.

## Stage 6 — Research launch (ongoing)

Start with one narrow problem:
- observation-limited recoverability of one-soliton manifold (mod symmetry), or
- projection-preservation/no-go for one equation + projection class.

Deliverable standard:
- theorem candidate,
- disproof attempt,
- reproducible benchmark,
- explicit status labels (PROVED/CONDITIONAL/OPEN/etc.).

## Common failure modes to avoid

1. Trying to unify integrable/topological/dissipative solitons too early.
2. Confusing “looks localized in simulation” with “soliton”.
3. Using geometry terminology without explicit invariants.
4. Skipping falsification and going straight to narrative.

## Minimal weekly cadence (recommended)

- 2 days reading + derivation
- 2 days computational checks
- 1 day falsification write-up
- 1 day synthesis note with status labels

This cadence keeps the program theorem-oriented and honest.
