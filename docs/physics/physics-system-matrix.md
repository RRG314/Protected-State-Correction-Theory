# Physics System Matrix

This file records the physics systems tested against the protected-state correction framework.

| System | Protected object | Disturbance family | Correction architecture | Exact or asymptotic | OCP fit verdict | Keep? |
| --- | --- | --- | --- | --- | --- | --- |
| QEC sector systems | code space / logical state | correctable syndrome sectors | sector projectors and recovery family | exact | exact fit under standard Knill-Laflamme assumptions | yes |
| Periodic Helmholtz/Leray projection | divergence-free field component | gradient contamination | orthogonal projection onto the divergence-free subspace | exact | exact fit | yes |
| GLM divergence cleaning | physical field content | divergence / constraint violation | damped auxiliary-field evolution | asymptotic | asymptotic fit only | yes |
| Maxwell / Coulomb-gauge projection | transverse field or vector-potential component | longitudinal / pure-gradient component | transverse projector / gauge projection | exact on projection-compatible domains | exact fit as a corollary of the projector branch | yes |
| Numerical-relativity constraint damping | constraint-satisfying solution sector | constraint-violating modes | constraint-damping evolution terms | asymptotic | conditional asymptotic fit | yes |
| Continuous quantum error correction / feedback | code sector / logical information | monitored error channels and syndrome drift | continuous measurement plus feedback or engineered dissipation | asymptotic or measurement-conditioned exact | conditional fit | yes, but conditional |
| Naive periodic-projector transplant to bounded domains | bounded-domain divergence-free class with boundary data | gradient contamination plus boundary-sensitive modes | periodic FFT projector reused unchanged | neither, for the bounded problem | rejected by explicit counterexample | no |
| Generic constrained Hamiltonian systems | reduced physical phase space | gauge / constraint directions | no canonical projector or recovery map in current repo scope | unclear | analogy only unless extra reduction data is supplied | no |

## Reading Guide

- The first three rows are the strongest current anchors and remain central.
- The Maxwell row survives because it is genuinely the same operator class as the exact projection branch.
- Numerical relativity and continuous QEC are worth keeping because they expose real asymptotic or feedback-correction architectures, but they are not promoted as new theorem branches yet.
- The bounded-domain transplant and generic constrained-Hamiltonian rows are valuable precisely because they mark where the theory stops.
