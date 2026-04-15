# CFD System Matrix

This file records the incompressible-CFD directions tested against Protected-State Correction Theory.

| CFD system | Protected object | Disturbance family | Correction architecture | Exact or asymptotic | Fit verdict | Keep? |
| --- | --- | --- | --- | --- | --- | --- |
| Periodic incompressible velocity projection | divergence-free velocity field | additive gradient contamination / non-solenoidal intermediate velocity | Helmholtz / Hodge projector `P_df` or exact pressure projection | exact | EXACT FIT | yes |
| Periodic projection methods inside fractional-step solvers | divergence-free velocity after the projection step | divergence error created by the predictor step | pressure Poisson correction followed by projection | exact at the correction step | EXACT FIT for the correction operator, not for the whole solver | yes |
| Bounded-domain projection with domain-compatible Hodge projector and matching boundary data | divergence-free velocity class with boundary constraints | contamination that preserves the admissible decomposition class | domain-compatible Hodge projector | exact on the implemented finite-mode Hodge family; conditional more broadly | CONDITIONAL FIT WITH A PROVED RESTRICTED EXACT SUBCASE | yes |
| Boundary-insensitive reuse of the periodic projector on bounded domains | bounded-domain incompressible protected class | gradient contamination plus boundary-sensitive modes | unchanged periodic FFT projector | neither exact nor honest asymptotic correction for the bounded protected class | REJECTED | no |
| Divergence-only correction on bounded incompressible classes | bounded divergence-free class with multiple distinct states sharing the same divergence data | any disturbance family requiring recovery of the full protected velocity rather than only a scalar constraint | any map factoring only through `div u` | impossible as an exact recovery architecture on a nontrivial protected class | REJECTED / NO-GO | no |
| GLM-style divergence damping interpreted as a CFD correction architecture | approximately divergence-controlled velocity or magnetic field | divergence error | damped auxiliary-field evolution | asymptotic | ASYMPTOTIC FIT | yes, but as comparator only |

## Reading Guide

- The strongest CFD fit is the periodic incompressible projection branch.
- The weakest and most important rejection is the idea that fixing divergence alone is enough for exact bounded-domain recovery.
- The bounded-domain branch now has one proved positive subcase: the implemented boundary-compatible finite-mode Hodge family. Beyond that, the branch remains conditional: the exact operator must be the domain-compatible Hodge projector for the protected class, not a boundary-oblivious transplant.
- GLM-style damping is still useful, but it belongs on the asymptotic side of the repo, not the exact CFD side.
