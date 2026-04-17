# Soliton Branch Literature Audit

Date: 2026-04-17

## Purpose

Audit each OCP-integrated soliton claim against outside literature to avoid novelty inflation and identify where this branch is likely standard, repackaged, or plausibly distinct.

## Audit Outcomes by Claim Type

| Branch result | Literature overlap assessment | Classification |
| --- | --- | --- |
| Symmetry non-identifiability under invariant observations | Core identifiability principle is standard across inverse problems and phase retrieval contexts. | Standard background |
| Quotient recoverability formulation on restricted one-soliton manifolds | Formulation is standard in spirit (identifiability modulo group actions), but this repo packages it as an explicit OCP-style recoverability branch object. | Standard fact in repo-specific packaging |
| Same-count opposite verdict on selected observation families | Aligns with broader identifiability literature where measurement structure beats count, but explicit nonlinear one-soliton witness packaging is less commonly presented in this exact format. | Plausible restricted extension |
| Magnitude-only noninjectivity/noise floor behavior | Closely related to known phase-loss/phase-retrieval nonuniqueness phenomena. | Likely known mechanism, branch-specific witness package |
| Projection-preservation split across operators on same class | Structure-preserving integrator and reduction behavior is well studied; explicit one-soliton manifold preservation/failure catalog in this branch is likely a benchmark packaging contribution rather than a foundational theorem. | Mostly known direction with branch-specific validation |
| Universal bridge to linear augmentation laws | Not supported by literature or by internal tests in current form. | Rejected claim |

## Primary Literature Anchors Used

1. N. J. Zabusky and M. D. Kruskal (1965), “Interaction of ‘Solitons’ in a Collisionless Plasma and the Recurrence of Initial States,” *Phys. Rev. Lett.* 15, 240–243.  
   DOI: `10.1103/PhysRevLett.15.240`
2. C. S. Gardner, J. M. Greene, M. D. Kruskal, R. M. Miura (1967), “Method for Solving the Korteweg-de Vries Equation,” *Phys. Rev. Lett.* 19, 1095–1097.  
   DOI: `10.1103/PhysRevLett.19.1095`
3. P. D. Lax (1968), “Integrals of Nonlinear Equations of Evolution and Solitary Waves,” *Comm. Pure Appl. Math.* 21, 467–490.
4. V. E. Zakharov and A. B. Shabat (1972), “Exact Theory of Two-Dimensional Self-Focusing and One-Dimensional Self-Modulation of Waves in Nonlinear Media,” *Sov. Phys. JETP* 34(1), 62–69.
5. M. J. Ablowitz and H. Segur (1981), *Solitons and the Inverse Scattering Transform*, SIAM.
6. H. Hasimoto (1972), “A Soliton on a Vortex Filament,” *J. Fluid Mech.* 51(3), 477–485.
7. E. Hairer, C. Lubich, G. Wanner (2006), *Geometric Numerical Integration*, Springer.
8. T. R. Taha and M. J. Ablowitz (1984), “Analytical and Numerical Aspects of Certain Nonlinear Evolution Equations. II. Numerical, Nonlinear Schrödinger Equation,” *J. Comput. Phys.* 55(2), 203–230.
9. R. Balan, P. Casazza, D. Edidin (2006), “On Signal Reconstruction Without Phase,” *Appl. Comput. Harmon. Anal.* 20(3), 345–356.
10. N. Manton and P. Sutcliffe (2004), *Topological Solitons*, Cambridge University Press.

## Literature Risk Notes

- High risk of “already known” classification if claims are stated broadly as generic identifiability or generic numerical preservation results.
- Lower risk and stronger positioning if statements stay at: **restricted family + explicit observation/reduction classes + explicit witness sets + explicit status labels**.

## Audit Verdict

The integrated branch is literature-compatible as a **narrow theorem/benchmark candidate layer**. It is not supportable as a broad new theory claim at this stage.
