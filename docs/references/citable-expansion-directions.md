# Citable Expansion Directions

This file lists outside research that can be cited directly when expanding the repository.

For reusable BibTeX entries, use:

- [protected-state-correction.bib](./protected-state-correction.bib)

For the repository citation itself, use:

- [how-to-cite-this-work.md](./how-to-cite-this-work.md)

## 1. Exact QEC Anchor

- Knill, E. and Laflamme, R. (1997). *Theory of Quantum Error-Correcting Codes*. *Physical Review A* 55(2), 900--911. DOI: [10.1103/PhysRevA.55.900](https://doi.org/10.1103/PhysRevA.55.900)
- Why it matters here: this is the cleanest exact anchor for the sector-recovery branch.

## 2. Stabilizer and Code-Structure Background

- Gottesman, D. (1997). *Stabilizer Codes and Quantum Error Correction*. PhD thesis, California Institute of Technology. arXiv: [quant-ph/9705052](https://arxiv.org/abs/quant-ph/9705052)
- Why it matters here: this is a good standard reference when the discussion needs stabilizer-side structure rather than only the Knill-Laflamme condition.

## 3. Continuous Quantum Error Correction

- Ahn, C., Doherty, A. C., and Landahl, A. J. (2002). *Continuous Quantum Error Correction via Quantum Feedback Control*. *Physical Review A* 65, 042301. DOI: [10.1103/PhysRevA.65.042301](https://doi.org/10.1103/PhysRevA.65.042301)
- Why it matters here: this is the best citable bridge from exact sector recovery into continuous-time or feedback-driven correction.

## 4. Projection Methods and Constraint Projection

- Chorin, A. J. (1968). *Numerical Solution of the Navier--Stokes Equations*. *Mathematics of Computation* 22(104), 745--762. DOI: [10.1090/S0025-5718-1968-0242392-2](https://doi.org/10.1090/S0025-5718-1968-0242392-2)
- Brown, D. L., Cortez, R., and Minion, M. L. (2001). *Accurate Projection Methods for the Incompressible Navier--Stokes Equations*. *Journal of Computational Physics* 168(2), 464--499. DOI: [10.1006/jcph.2001.6715](https://doi.org/10.1006/jcph.2001.6715)
- Guermond, J.-L., Minev, P., and Shen, J. (2006). *An Overview of Projection Methods for Incompressible Flows*. *Computer Methods in Applied Mechanics and Engineering* 195(44--47), 6011--6045. DOI: [10.1016/j.cma.2005.10.010](https://doi.org/10.1016/j.cma.2005.10.010)
- Why it matters here: this is the classical projection-method lane for exact constrained recovery in PDE settings.

## 5. MHD Divergence Cleaning

- Dedner, A., Kemm, F., Kr{"o}ner, D., Munz, C.-D., Schnitzer, T., and Wesenberg, M. (2002). *Hyperbolic Divergence Cleaning for the MHD Equations*. *Journal of Computational Physics* 175(2), 645--673. DOI: [10.1006/jcph.2001.6961](https://doi.org/10.1006/jcph.2001.6961)
- Evans, C. R. and Hawley, J. F. (1988). *Simulation of Magnetohydrodynamic Flows: A Constrained Transport Method*. *The Astrophysical Journal* 332, 659--677.
- Why they matter here: these separate exact constraint-preserving or projection-style ideas from asymptotic cleaning architectures.

## 6. Maxwell Constraint Preservation

- Calabrese, G. (2004). *A Remedy for Constraint Growth in Numerical Relativity: The Maxwell Case*. arXiv: [gr-qc/0404036](https://arxiv.org/abs/gr-qc/0404036)
- Berchenko-Kogan, Y. and Stern, A. (2020). *Constraint-Preserving Hybrid Finite Element Methods for Maxwell's Equations*. *Journal of Computational Physics* 401, 109340. DOI: [10.1016/j.jcp.2019.109340](https://doi.org/10.1016/j.jcp.2019.109340)
- Why they matter here: these give operator-level and constraint-preserving literature directly adjacent to the projector branch.

## 7. Numerical-Relativity Constraint Damping

- Gundlach, C., Martin-Garcia, J. M., Calabrese, G., and Hinder, I. (2005). *Constraint Damping in the Z4 Formulation and Harmonic Gauge*. *Classical and Quantum Gravity* 22(17), 3767--3774. DOI: [10.1088/0264-9381/22/17/025](https://doi.org/10.1088/0264-9381/22/17/025)
- Weyhausen, A., Bernuzzi, S., and Hilditch, D. (2012). *Constraint Damping for the Z4c Formulation of General Relativity*. *Physical Review D* 85, 024038. DOI: [10.1103/PhysRevD.85.024038](https://doi.org/10.1103/PhysRevD.85.024038)
- Abalos, J. F. (2021). *On Constraint Preservation and Strong Hyperbolicity*. arXiv: [2111.06295](https://arxiv.org/abs/2111.06295)
- Why they matter here: these provide the strongest citable asymptotic-PDE correction lane beyond the existing MHD anchor.

## Use Pattern

The cleanest way to use these citations is:

- cite the repository for the framework itself,
- cite the specific theorem or application document you are using,
- cite Knill-Laflamme when discussing exact sector recovery,
- cite Chorin, Brown-Cortez-Minion, or Guermond-Minev-Shen when discussing exact continuous or incompressible projection,
- cite Dedner, Gundlach, Weyhausen, or Abalos when discussing asymptotic correction and constraint damping,
- and cite Ahn-Doherty-Landahl when discussing a future continuous-QEC bridge.
