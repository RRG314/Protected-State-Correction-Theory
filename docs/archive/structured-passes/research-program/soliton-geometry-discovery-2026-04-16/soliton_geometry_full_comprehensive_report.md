# Soliton Waves and Geometry: Full Comprehensive Discovery Report

Date: 2026-04-16  
Program mode: discovery-first, falsification-first, novelty-seeking  
Scope: independent soliton-geometry research program (no forced retrofit to prior repos)

## Executive Summary

This report consolidates the full soliton+geometry discovery pass into one document. The landscape was mapped across integrable systems, topological solitons, geometric formulations, perturbative/dissipative regimes, and adjacent applied domains (optics, BEC, fluids, soft matter, plasma).

Main conclusions:

1. Geometry is genuinely central in several soliton lanes, but not through one universal framework.
2. The strongest mathematically real geometry lanes are:
   - integrable geometry (Lax/zero-curvature/Hamiltonian structure),
   - moving-frame and curvature/torsion formulations,
   - topological/homotopy classification,
   - structure-preserving geometric numerics.
3. Broad universalization attempts were falsified and rejected.
4. The strongest novelty candidate is a narrow theorem program on observation-limited recoverability of restricted soliton manifolds (modulo symmetry), with explicit counterexample pressure.
5. Cross-links to existing repos are possible only in narrow, explicit ways; forced merging is rejected.

Status summary:

- PROVED: no new theorem claimed in this discovery pass
- VALIDATED: orientation, lane classification, and falsification map
- CONDITIONAL: several candidate lanes (projection-preservation, defect thresholds)
- OPEN: top candidate theorem directions remain open and testable
- DISPROVED: broad one-framework geometry unification
- ANALOGY ONLY: geometry narratives without explicit invariants

## Master Contents

1. Orientation: what solitons are, key equations, and subfield map
2. Geometry-connection audit (kept vs rejected)
3. Adjacent-topic ecosystem and opportunity ranking
4. Novelty-candidate generation and triage
5. Falsification ledger (what failed, what survived)
6. Optional bridge to existing repos (only honest narrow links)
7. Start-here research plan (90-day execution)
8. Ranked reading list
9. Ranked theorem/simulation opportunity list
10. Beginner-to-advanced learning path

---

## 1) Orientation Report

# Soliton–Geometry Orientation (Discovery Pass)

Date: 2026-04-16  
Program mode: discovery-first, falsification-first, novelty-seeking

## 1) What a soliton is (and is not)

A **soliton** is a localized nonlinear wave that keeps coherent shape over long propagation and exhibits particle-like interaction behavior (e.g., phase shift after collision, but no generic dispersive destruction) in a governing regime where nonlinearity and dispersion balance.

A generic **traveling wave** is not automatically a soliton. Many traveling waves:
- disperse under perturbation,
- radiate strongly after collisions,
- or depend on non-robust parameter tuning.

A practical discriminator used in this program:
- **Soliton-like (strict)**: persistent localized profile + robust interaction signature in a mathematically defined equation class.
- **Localized wave (broad)**: persistent over finite time in numerics/experiments, but without full soliton structural guarantees.

## 2) Why solitons are stable

Stability mechanisms are regime-dependent:

1. **Integrable stability (exact/near-exact)**  
   Lax-pair / inverse-scattering structure gives infinitely many constraints and constrained scattering dynamics.

2. **Topological stability**  
   Homotopy class blocks continuous unwinding; defect charge is the obstruction.

3. **Energetic/metastable stability**  
   Localized state minimizes a constrained energy or survives due to dissipation/drive balance (dissipative solitons).

4. **Orbital/spectral stability**  
   Stability around a symmetry orbit (translation/phase) using linearized spectral structure and coercivity functionals.

## 3) Why geometry matters

Geometry is not decorative here. It enters through concrete objects:

- phase-space geometry (Hamiltonian, symplectic/Poisson structures),
- curve/surface invariants (curvature, torsion, immersion formulas),
- topology (homotopy degree, winding, skyrmion number, Hopf charge),
- manifold structure of coherent-state families (soliton manifolds/moduli).

## 4) Canonical equation backbone

| Equation | Canonical form (representative) | Soliton relevance | Geometry role |
|---|---|---|---|
| KdV | `u_t + 6uu_x + u_{xxx}=0` | Classical integrable solitons, IST archetype | Hamiltonian hierarchy, infinite conservation laws |
| NLS | `iψ_t + ψ_{xx} + 2|ψ|^2ψ=0` (focusing 1D) | Bright/dark solitons, breathers, MI route | Symplectic/Hamiltonian structure; phase-gauge orbit |
| sine-Gordon | `φ_{tt}-φ_{xx}+sinφ=0` | Kinks, antikinks, breathers | Pseudospherical-surface geometry link |
| mKdV | `u_t + 6u^2u_x + u_{xxx}=0` | Integrable pulses, Miura relations | Integrable hierarchy geometry |
| KP (KP-I/KP-II) | `(u_t+6uu_x+u_{xxx})_x + σu_{yy}=0` | 2D line-soliton dynamics/stability differences | Higher-dimensional integrable geometry |
| Gross–Pitaevskii | `iψ_t = (-Δ + V + g|ψ|^2)ψ` | Matter-wave solitons/vortices in BEC | Energy functional geometry + vortex topology |
| Complex Ginzburg–Landau (dissipative lane) | representative driven-damped NLS-type | Dissipative solitons (not integrable) | Attractor/phase-space geometry under gain-loss |

## 5) Major subfields map

| Lane | Typical questions | Dominant style | Maturity | Independent-path viability |
|---|---|---|---|---|
| Integrable systems | exact solvability, scattering data, asymptotics | theorem-heavy | very mature | medium (needs narrow scope) |
| Soliton geometry (curves/surfaces) | immersion formulas, frame equations, geometric PDE links | theorem + symbolic | mature but specialized | medium-high |
| Topological solitons | charge classification, defect dynamics, stability classes | theorem + simulation + experiment | mature/active | high if narrowly scoped |
| Nonlinear optics/fibers | MI, breathers, communication relevance | theory + experiment | very active | high for diagnostics/reduction questions |
| BEC/matter waves | trap effects, soliton/vortex dynamics, perturbations | theory + numerics + experiments | very active | high |
| Rogue-wave/modulation-instability | onset statistics, integrable turbulence, localization events | simulation + experiment + asymptotics | very active | medium-high |
| Structure-preserving numerics | long-time fidelity, conservation-compatible schemes | numerical analysis heavy | active | high |
| Plasma/MHD soliton-like structures | ion-acoustic/magnetosonic localized waves | asymptotic reductions + numerics | active but fragmented | medium |

## 6) Integrable vs topological vs dissipative localized structures

- **Integrable solitons**: strongest exact mathematics; conservation-law rich; collision laws are sharp in specific equations.
- **Topological solitons**: robustness from global class constraints, not from IST.
- **Dissipative localized waves**: persistence from drive-loss balance; can be practically robust without integrability.

These are distinct mechanisms; conflating them is a common source of overclaim.

## 7) What is “structural stability” in this program

Working operational definition (for this discovery pass):

A localized wave family is structurally stable if persistence survives a specified perturbation class (equation coefficients, forcing/damping, observation/projection operations) with quantitatively controlled defect growth.

This yields testable outputs:
- persistence windows,
- defect scaling laws,
- projection-preservation/no-go statements.

## 8) Essential glossary (focused)

- **Soliton**: localized nonlinear wave with robust coherent propagation and interaction signature in a given model class.
- **Breather**: localized structure periodic/quasi-periodic in time (or space), often from integrable models.
- **Integrability**: existence of rich exact structure (e.g., Lax pair, IST, infinite conserved quantities).
- **Lax pair**: operator pair whose compatibility reproduces nonlinear PDE.
- **IST**: nonlinear analog of Fourier method for some integrable PDE initial-value problems.
- **Topological charge**: homotopy-derived invariant distinguishing defect classes.
- **Modulation instability (MI)**: sideband growth mechanism causing envelope breakup/localization.
- **Rogue wave**: rare, large-amplitude localized event; in integrable settings often tied to special rational/breather solutions.
- **Soliton manifold**: finite-dimensional family of coherent profiles modulo symmetries.
- **Structure-preserving scheme**: numerical method designed to conserve/approximate invariants or geometric structure over long times.

## 9) Orientation verdict

What is clearly true from baseline orientation:

- Soliton research is broad but internally segmented by distinct stability mechanisms.
- Geometry contributes real mathematics in multiple lanes (not one universal lens).
- The best novelty chances are in **narrow, rigorously scoped interfaces** (perturbed integrable structure, observation/reduction effects, or geometry-informed diagnostics), not in broad “new grand theory” claims.

## 10) Core references used for orientation

- Zabusky, N.J. & Kruskal, M.D. (1965). *Interaction of “Solitons” in a Collisionless Plasma*. Phys. Rev. Lett. 15, 240.  
  https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.15.240
- Gardner, C.S., Greene, J.M., Kruskal, M.D., Miura, R.M. (1967). *Method for Solving the KdV Equation*. Phys. Rev. Lett. 19, 1095.  
  https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.19.1095
- Lax, P.D. (1968). *Integrals of Nonlinear Equations of Evolution and Solitary Waves*.  
  https://www.osti.gov/biblio/4522657
- Zakharov, V.E. & Shabat, A.B. (1972). *Exact Theory of Two-dimensional Self-focusing and One-dimensional Self-modulation*. Sov. Phys. JETP 34, 62–69.  
  https://www.jetp.ras.ru/cgi-bin/dn/e_034_01_0062
- Kadomtsev, B.B. & Petviashvili, V.I. (1970). *On the stability of solitary waves in weakly dispersing media*.  
  https://www.mathnet.ru/eng/dan35447
- Hasimoto, H. (1972). *A soliton on a vortex filament*. J. Fluid Mech. 51(3), 477–485.  
  https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/abs/soliton-on-a-vortex-filament/1A2FF58DD1B8DE20509866A4713531F3
- Porter, M.A. (Scholarpedia entry). *Soliton* (2010).  
  https://www.scholarpedia.org/article/Soliton
- Kevrekidis, P.G. et al. (Scholarpedia entry). *Nonlinear Schrödinger systems: continuous and discrete*.  
  https://www.scholarpedia.org/article/Nonlinear_Schrodinger_systems%3A_continuous_and_discrete
- Manton, N. & Sutcliffe, P. (2004). *Topological Solitons*. Cambridge.  
  https://www.cambridge.org/core/books/topological-solitons/0A9670253EB1C8254BDACA4EE30C3AA3
- Benjamin, T.B. & Feir, J.E. (1967). *The disintegration of wave trains on deep water*. J. Fluid Mech. 27(3), 417–430.  
  https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/disintegration-of-wave-trains-on-deep-water-part-1-theory/246B0FC7833C7F9C18755482BD308CA8
- Peregrine, D.H. (1983). *Water waves, nonlinear Schrödinger equations and their solutions*. ANZIAM J. 25(1), 16–43.  
  https://www.cambridge.org/core/journals/anziam-journal/article/water-waves-nonlinear-schrodinger-equations-and-their-solutions/D87F5416C657F3B5C35AE96DF9F73DD0
- Gross, E.P. (1961). *Structure of a Quantized Vortex in Boson Systems*.  
  https://www.osti.gov/biblio/4028087
- Pitaevskii, L.P. (1965). *Vortices in an Imperfect Bose Gas* (Phys. Rev.).  
  https://journals.aps.org/pr/abstract/10.1103/PhysRev.138.A429
- Frantzeskakis, D.J. (2010). *Dark solitons in atomic BECs: from theory to experiments*.  
  https://arxiv.org/abs/1004.4071
- Nagaosa, N. & Tokura, Y. (2013). *Topological properties and dynamics of magnetic skyrmions*. Nat. Nanotech. 8, 899–911.  
  https://www.nature.com/articles/nnano.2013.243
- Bridges, T.J. (1997). *Multi-symplectic structures and wave propagation*.  
  https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/multisymplectic-structures-and-wave-propagation/C600E2AD2FB5A0A5AC31EB67F41E6CD7
- Hairer, E., Lubich, C., Wanner, G. (2006). *Geometric Numerical Integration*.  
  https://link.springer.com/book/10.1007/3-540-30666-8
- Akhmediev, N. & Ankiewicz, A. (eds.) (2005). *Dissipative Solitons*.  
  https://link.springer.com/book/10.1007/b11728
- Kivshar, Y.S. & Malomed, B.A. (1989). *Dynamics of solitons in nearly integrable systems*. Rev. Mod. Phys. 61(4).  
  https://journals.aps.org/rmp/issues/61/4
- Washimi, H. & Taniuti, T. (1966). *Propagation of Ion-Acoustic Solitary Waves of Small Amplitude*. Phys. Rev. Lett. 17, 996.  
  https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.17.996

---

## 2) Geometry Connection Audit

# Geometry–Soliton Connection Audit

Date: 2026-04-16  
Method: mode-by-mode audit, literature check, falsification-first filtering

## Executive summary

Geometry is genuinely central in several soliton lanes, but not in one universal way.  
Strongest mathematically real connections in this pass:

1. Integrable geometry (Lax/zero-curvature/symplectic structure)
2. Curve and moving-frame geometry (Hasimoto lane)
3. Topological classification (homotopy/charge-protected defects)
4. Geometric structure-preserving numerics (multisymplectic/symplectic)

Most overhyped failures come from treating “geometry” as metaphor rather than explicit invariant machinery.

---

## Mode 1: Curve/surface geometry

**Core objects**
- space curves, curvature `κ`, torsion `τ`
- immersed surfaces (e.g., pseudospherical surfaces)

**Standard**
- Hasimoto transform: vortex filament geometry ↔ NLS-type structure.

**Active**
- soliton surfaces and geometric reconstructions in integrable PDE families.

**Likely overhyped**
- generic claims that every localized wave has a useful immersion geometry.

**Verdict**: **KEPT (strong)**  
Because explicit geometric invariants and transforms are available.

---

## Mode 2: Moving frames / curvature / torsion formulations

**Core objects**
- Frenet–Serret frames, frame-compatible PDE reductions

**Standard**
- frame reductions for vortex-filament and related geometric flows.

**Active**
- perturbative extensions, non-ideal corrections.

**Likely overhyped**
- applying moving-frame formalisms where no closed reduced dynamics survives.

**Verdict**: **KEPT (strong in restricted classes)**

---

## Mode 3: Integrable-systems geometry

**Core objects**
- Lax pairs, zero-curvature equations, hierarchies, Hamiltonian/symplectic structures

**Standard**
- KdV/NLS/sine-Gordon/KP integrability structure.

**Active**
- perturbative integrability breaking, asymptotic integrability, finite-gap and modulation.

**Likely overhyped**
- pretending weakly perturbed systems remain effectively integrable globally.

**Verdict**: **KEPT (very strong)**

---

## Mode 4: Contact/symplectic/Poisson geometry

**Core objects**
- phase-space forms, Poisson brackets, multisymplectic PDE structure

**Standard**
- Hamiltonian formulations and conservation-law geometry.

**Active**
- structure-preserving numerics and long-time fidelity.

**Likely overhyped**
- generic use of symplectic language with no quantitative gain.

**Verdict**: **KEPT (strong, especially for numerics and perturbation analysis)**

---

## Mode 5: Topological solitons and homotopy classes

**Core objects**
- topological charge, homotopy classes, skyrmion/Hopf-type invariants

**Standard**
- topological stability as obstruction to unwinding.

**Active**
- condensed-matter/topological-texture realizations and controlled experiments.

**Likely overhyped**
- conflating topological protection with full dynamical robustness under all perturbations.

**Verdict**: **KEPT (very strong, mechanism-distinct from integrability)**

---

## Mode 6: Geometric flows and soliton-like solutions

**Core objects**
- curvature-driven evolution equations, self-similar/soliton solutions in flow equations

**Standard**
- broad geometric-flow machinery in PDE geometry.

**Active**
- flow-specific soliton-like structures and singularity analysis.

**Likely overhyped**
- importing geometric-flow intuition into dispersive-wave models without compatibility checks.

**Verdict**: **PARTIAL KEEP (conditional)**

---

## Mode 7: Differential-geometric interpretations of nonlinear PDEs

**Core objects**
- geometric reformulation of compatibility conditions (e.g., sine-Gordon and curvature)

**Standard**
- classical geometry links for selected equations.

**Active**
- specialized geometrization programs for selected integrable/nonintegrable classes.

**Likely overhyped**
- “all nonlinear PDE are geometry in disguise” claims with no theorem payload.

**Verdict**: **KEPT ONLY WHEN INVARIANTS/OBSTRUCTIONS ARE EXPLICIT**

---

## Mode 8: Soliton surfaces and immersion formulas

**Core objects**
- Sym–Tafel / Fokas–Gel’fand style immersion constructions

**Standard**
- established in integrable-geometry literature for selected systems.

**Active**
- ongoing work in specialized integrable classes.

**Likely overhyped**
- purely visual surface construction with no downstream theorem or stability use.

**Verdict**: **PARTIAL KEEP (niche but real)**

---

## Kept vs rejected summary

### Kept (strong lanes)
1. Integrable geometry (Lax/zero-curvature/Hamiltonian hierarchy)
2. Moving-frame and curvature-torsion formulations in supported classes
3. Topological-soliton homotopy classification
4. Geometric structure-preserving numerical analysis

### Kept (restricted/niche)
1. Soliton-surface immersion formulas (if tied to explicit invariants)
2. Geometric-flow analogies (if equation-class match is explicit)

### Rejected (for this program)
1. Decorative differential-geometry language without computable objects
2. Broad “everything is geometry” synthesis claims
3. Coordinate-only rewrites without new theorem, obstruction, or diagnostic value

## Strongest mathematically real geometry lanes for a new program

1. **Perturbed-integrable geometry**: quantify loss of integrable structure using explicit defect functionals.
2. **Topology-vs-integrability stability comparison** in narrow classes (not universal).
3. **Geometry-preserving reduction/integration criteria**: when a projection/discretization preserves soliton-class invariants vs destroys them.

## Status labels (this audit)

- PROVED: none new in this pass (audit only)
- VALIDATED: literature-backed classification map
- CONDITIONAL: several candidate geometric lanes require restricted assumptions
- OPEN: theorem development for perturbation and projection-preservation criteria
- DISPROVED: universal geometry-unification framing
- ANALOGY ONLY: unspecific geometric metaphors without invariants

## References used in this audit

- Hasimoto (1972), JFM: vortex-filament soliton geometry  
  https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/abs/soliton-on-a-vortex-filament/1A2FF58DD1B8DE20509866A4713531F3
- Bridges (1997), multisymplectic PDE structure  
  https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/multisymplectic-structures-and-wave-propagation/C600E2AD2FB5A0A5AC31EB67F41E6CD7
- Manton & Sutcliffe (2004), topological solitons  
  https://www.cambridge.org/core/books/topological-solitons/0A9670253EB1C8254BDACA4EE30C3AA3
- Nagaosa & Tokura (2013), magnetic skyrmions  
  https://www.nature.com/articles/nnano.2013.243
- Hairer–Lubich–Wanner (2006), geometric numerical integration  
  https://link.springer.com/book/10.1007/3-540-30666-8
- Zakharov–Shabat (1972), NLS integrable core  
  https://www.jetp.ras.ru/cgi-bin/dn/e_034_01_0062

---

## 3) Adjacent Topics Map

# Adjacent Topics Commonly Studied With Solitons

Date: 2026-04-16  
Scope: adjacent lanes with relevance to soliton+geometry research planning

## 1) Topic map (what, why, style, difficulty)

| Topic | Why studied | Main questions | Dominant style | Difficulty | Independent path fit |
|---|---|---|---|---|---|
| Inverse scattering (IST) | exact solvability backbone | which PDE admit IST; data ↔ solution map | theorem-heavy | high | medium (narrow projects only) |
| Modulation instability (MI) | mechanism for localization/breakup | thresholds, sideband growth, transition to localized states | theory + numerics + experiments | medium | high |
| Rogue waves / integrable turbulence | extreme-event statistics | when rare peaks emerge; role of integrability/randomness | simulation + experiment + asymptotics | medium-high | medium-high |
| Breathers | coherent nonstationary localized structures | stability windows, perturbation response | theorem + simulation | medium | high |
| Vortices / vortex filaments | geometry-rich coherent structures | topology, filament dynamics, reconnections | geometry + PDE + computation | high | medium-high |
| Topological defects/textures | robustness via charge classes | charge conservation, annihilation channels, dynamics | theorem + simulation + experiment | high | high (if restricted) |
| Integrability breaking | realism beyond ideal PDE | persistence under damping/forcing/inhomogeneity | perturbation theory + numerics | high | very high |
| Nonlinear optics / fibers | strongest application maturity | pulse shaping, MI control, communication constraints | mixed theorem/experiment | medium | high |
| BEC / matter-wave solitons | clean lab realization of nonlinear waves | trap effects, dark/bright/vortex interactions | mixed theorem/simulation/experiment | medium-high | high |
| Soft matter / liquid crystals | accessible topological soliton experiments | defect-soliton taxonomy, controllability | experiment + modeling | medium-high | medium |
| Plasma / MHD soliton-like waves | physically important nonlinear waves | reductive asymptotics validity, stability, defects | asymptotic theory + numerics | high | medium |
| Structure-preserving numerics | reproducible long-time dynamics | what discretizations keep invariants/geometry | numerical analysis heavy | medium-high | very high |

## 2) Why each is studied (plain language)

- **IST/integrable systems**: gives rare exact nonlinear solvability and deep structural control.
- **MI/rogue waves**: explains how smooth wavetrains can suddenly localize into extreme events.
- **Breathers**: model recurrent localization, useful between strict solitons and chaotic waves.
- **Topological defects/solitons**: stability from global structure, often robust in realistic materials.
- **Integrability breaking**: reality check; exact models are idealized, perturbations are unavoidable.
- **Optics/BEC**: experimental platforms where nonlinear wave theory can be tested precisely.
- **Structure-preserving numerics**: without geometric preservation, long-time simulation conclusions can be misleading.

## 3) Ranked opportunity list (this pass)

Ranking criterion: theorem potential + falsifiability + feasible independent execution.

1. **Integrability-breaking with quantitative defect laws**  
   Why high: mature background but still strong room for narrow theorem/no-go statements.
2. **Projection/reduction preservation of soliton manifolds**  
   Why high: clean theorem + numerical benchmark pairing; strong design relevance.
3. **Observation-limited identifiability of soliton parameters**  
   Why high: explicit inverse/identifiability question with constructive counterexamples possible.
4. **Topological-vs-integrable stability comparison in one explicit paired model**  
   Why medium-high: interesting, but model selection and fairness constraints are hard.
5. **Multisymplectic vs non-structure-preserving simulation diagnostics for soliton collisions**  
   Why medium-high: actionable and reproducible, though novelty must be carefully scoped.
6. **MI threshold refinement in variable-coefficient NLS classes**  
   Why medium: active and competitive area; novelty requires sharp restriction.
7. **Soft-matter topological soliton transfer insights**  
   Why medium: rich experimentally, but theorem lane can be diffuse.
8. **Broad plasma/MHD “soliton unification” claims**  
   Why low: too broad; high risk of weak or already-known statements.

## 4) Theorem-heavy vs simulation-heavy vs experiment-heavy split

- Mostly theorem-heavy: IST, integrable geometry, topological classification foundations.
- Balanced theorem/simulation: perturbation of integrable systems, structure-preserving numerics, observation-limited recovery.
- Mostly experiment-driven with theoretical support: optics implementation, BEC/soft-matter realization lanes.

## 5) Fit for independent-research path

Best independent pathway is **hybrid theorem + reproducible numerics**:
- avoid full-field experimental dependence,
- avoid claiming broad universal physics,
- target one explicit equation class + one perturbation family + one measurable defect functional.

## 6) References used for adjacent-lane map

- Akhmediev & Ankiewicz (eds.), *Dissipative Solitons*  
  https://link.springer.com/book/10.1007/b11728
- Kivshar & Malomed (1989), dynamics in nearly integrable systems  
  https://journals.aps.org/rmp/issues/61/4
- Benjamin & Feir (1967), MI foundational lane  
  https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/disintegration-of-wave-trains-on-deep-water-part-1-theory/246B0FC7833C7F9C18755482BD308CA8
- Peregrine (1983), NLS/water-wave link for localized events  
  https://www.cambridge.org/core/journals/anziam-journal/article/water-waves-nonlinear-schrodinger-equations-and-their-solutions/D87F5416C657F3B5C35AE96DF9F73DD0
- Frantzeskakis (2010), BEC soliton review  
  https://arxiv.org/abs/1004.4071
- Washimi & Taniuti (1966), ion-acoustic solitary-wave classic  
  https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.17.996
- Bridges (1997), multisymplectic PDE lane  
  https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/multisymplectic-structures-and-wave-propagation/C600E2AD2FB5A0A5AC31EB67F41E6CD7

---

## 4) Novelty Candidate Report

# Novelty Candidate Report: Solitons + Geometry

Date: 2026-04-16  
Method: narrow candidates only; each candidate stress-tested for novelty risk and failure modes

## Candidate 1 — Observation-limited recoverability of soliton parameters (symmetry-quotiented)

**Idea**  
For a restricted one-soliton manifold in NLS/KdV-like settings, characterize when partial observations uniquely determine parameters **modulo translation/phase symmetries**.

**Why it might be novel**  
Many results recover full fields or use complete scattering data; fewer provide explicit minimal-observation identifiability criteria on restricted, symmetry-quotiented families with constructive non-uniqueness witnesses.

**Closest literature**
- IST and inverse problems for integrable equations (classical)
- BEC/optics parameter-estimation practice (mostly applied)

**What could kill it**
- already-known identifiability theorem in equivalent form
- criterion collapses to trivial rank/regularity condition
- dependence on unrealistic noise-free assumptions

**Rating**: **STRONG**  
**Current status**: **OPEN (high-priority start lane)**

---

## Candidate 2 — Projection/reduction preservation theorem/no-go for soliton manifolds

**Idea**  
Given a projection/reduction operator `P` (spectral truncation, Galerkin, or structure-preserving variant), derive criteria for whether `P` preserves a target soliton manifold invariantly (exactly, asymptotically, or not at all).

**Why it might be novel**  
There is broad numerical literature, but a clean theorem/no-go pair for an explicit soliton manifold plus explicit projection class is still plausible and publication-relevant.

**Closest literature**
- geometric numerical integration
- split-step and symplectic/multisymplectic solvers

**What could kill it**
- result is known under different terminology
- only reproduces standard consistency/stability conditions without soliton-specific content

**Rating**: **STRONG**  
**Current status**: **OPEN**

---

## Candidate 3 — Integrability-defect threshold law under structured perturbations

**Idea**  
Define a computable defect functional (conservation-law drift / scattering-data mismatch proxy) and prove a threshold separating long-lived coherent behavior from rapid dispersive deformation in a restricted perturbation family.

**Why it might be novel**  
Perturbative near-integrable analysis exists, but a practical theorem-plus-benchmark threshold law in one explicit class could still be distinct.

**Closest literature**
- near-integrable soliton dynamics (Kivshar–Malomed and successors)
- modulation and asymptotic stability analyses

**What could kill it**
- threshold reduces to numerically tuned heuristic only
- defect functional not invariant enough to be meaningful

**Rating**: **MEDIUM–STRONG**  
**Current status**: **OPEN**

---

## Candidate 4 — Topological-vs-integrable stability comparison in a paired model class

**Idea**  
Construct a fair paired comparison: one integrable-coherence mechanism vs one topological-protection mechanism under matched perturbation classes.

**Why it might be novel**  
Comparative statements are often qualitative; a restricted quantitative comparison could be useful.

**Closest literature**
- topological soliton monographs and skyrmion/defect dynamics
- integrable perturbation theory

**What could kill it**
- comparison is apples-to-oranges due to incompatible state spaces
- no common perturbation metric yields meaningful theorem

**Rating**: **MEDIUM**  
**Current status**: **OPEN (high falsification risk)**

---

## Candidate 5 — Geometry-aware sensing diagnostics for MI-to-localization transitions

**Idea**  
Use low-dimensional geometric diagnostics (phase-space loop area, local curvature-like proxies, conserved-density drift) to classify early transition from stable wavetrain to localization events.

**Why it might be novel**  
Potentially useful for interpretable diagnostics, but crowded area.

**Closest literature**
- MI and rogue-wave diagnostics
- integrable turbulence statistics

**What could kill it**
- only a repackaged ML feature set with no theorem content
- diagnostics are non-robust across equation variants

**Rating**: **MEDIUM**  
**Current status**: **OPEN / VALIDATION-HEAVY**

---

## Candidate 6 — Soliton-surface invariants as predictive quantities

**Idea**  
Use immersion-geometry invariants (for equations admitting soliton-surface representation) to predict stability windows or defect growth.

**Why it might be novel**  
Could connect geometry to predictive outputs if invariants are computable and non-redundant.

**Closest literature**
- Sym–Tafel/Fokas–Gel’fand surface constructions

**What could kill it**
- invariants are computationally expensive but not predictive
- equivalent to existing conserved quantities with no gain

**Rating**: **WEAK–MEDIUM**  
**Current status**: **OPEN (likely niche)**

---

## Candidate 7 — Universal geometry-unification claim across all soliton classes

**Idea**  
Single theory explaining integrable, topological, and dissipative solitons under one geometry.

**Why it might be novel**  
Broad framing only.

**What could kill it**
- immediately fails mechanism mismatch (integrability vs topology vs dissipation)

**Rating**: **TOO BROAD / UNSAFE**  
**Current status**: **DISPROVED as a near-term research target**

## Strongest three candidates

1. Observation-limited recoverability on restricted soliton manifolds (Candidate 1)
2. Projection/reduction preservation theorem/no-go (Candidate 2)
3. Integrability-defect threshold law (Candidate 3)

## Strongest single “start here now” direction

### Start-here direction: Candidate 1

**Working problem statement**  
For a one-soliton family of a selected equation (start with focusing 1D NLS), determine necessary and sufficient conditions on a restricted observation operator class for unique recovery of soliton parameters modulo symmetry group action.

**Reason this is first**
- narrow and theorem-accessible,
- falsifiable with explicit counterexamples,
- directly supports later extensions to noisy/perturbed settings,
- can be developed without forcing connection to existing repo frameworks.

## Novelty discipline note

No candidate above is claimed novel yet.  
Each is a **plausible lane** requiring theorem search + counterexample pressure + literature cross-check before novelty claims.

## References grounding novelty context

- Integrable foundations: Zabusky–Kruskal (1965), GGKM (1967), Lax (1968), Zakharov–Shabat (1972)
- Near-integrable dynamics: Kivshar–Malomed (Rev. Mod. Phys. 1989)
- Geometry and moving frames: Hasimoto (1972)
- Topological solitons: Manton–Sutcliffe (2004)
- MI/rogue-wave foundations: Benjamin–Feir (1967), Peregrine (1983)

---

## 5) Falsification Results

# Falsification Results: Soliton–Geometry Discovery Pass

Date: 2026-04-16  
Objective: kill weak directions early; retain only theorem-grade or benchmark-grade lanes

## Falsification protocol used

For each candidate direction we asked:
1. Is this already a standard theorem in disguise?
2. Does it rely on vague geometry language without computable structure?
3. Does it collapse outside a coordinate artifact or idealized setting?
4. Can failure be exhibited with explicit perturbations/counterexamples?

---

## Candidate-by-candidate falsification outcomes

### C1. Observation-limited recoverability on restricted soliton manifolds

- **Attempted kill**: “This is just ordinary inverse scattering.”
- **Finding**: not automatically. IST assumes richer/global scattering data than many constrained observation settings.
- **Attempted kill**: “It collapses to trivial linear algebra.”
- **Finding**: symmetry quotients (translation/phase) and nonlinear profile parameterization prevent trivial reduction in general.
- **Outcome**: **SURVIVES** with strict scope restrictions.
- **Status**: **OPEN**

### C2. Projection/reduction preservation theorem/no-go

- **Attempted kill**: “Numerical-analysis literature already settles this fully.”
- **Finding**: broad preservation theory exists, but soliton-manifold-specific exact/no-go criteria under explicit projection classes remain plausibly open in narrow settings.
- **Attempted kill**: “Only consistency-order restatement.”
- **Finding**: can avoid this by tying to manifold invariance or symmetry-respecting defects.
- **Outcome**: **SURVIVES (conditional)**
- **Status**: **OPEN / CONDITIONAL**

### C3. Integrability-defect threshold law

- **Attempted kill**: “Thresholds are purely empirical.”
- **Finding**: risk is real; many published thresholds are heuristic.
- **Counterbalance**: in restricted perturbation families, defect-growth bounds may be derivable and benchmarkable.
- **Outcome**: **PARTIAL SURVIVAL**
- **Status**: **CONDITIONAL**

### C4. Topological-vs-integrable stability comparison

- **Attempted kill**: “Incommensurate mechanisms make theorem comparison meaningless.”
- **Finding**: strong risk confirmed. Comparable perturbation metrics and matched state spaces are hard.
- **Outcome**: **WEAK SURVIVAL only as carefully constrained comparative study**
- **Status**: **OPEN (high risk)**

### C5. Geometry-aware MI localization diagnostics

- **Attempted kill**: “Just feature engineering without theorem content.”
- **Finding**: this failure mode is common; novelty risk is high.
- **Outcome**: **SURVIVES only if tied to provable diagnostic bounds or reproducible benchmark superiority**
- **Status**: **VALIDATION-HEAVY / CONDITIONAL**

### C6. Soliton-surface invariants for prediction

- **Attempted kill**: “Surface reconstructions are explanatory only.”
- **Finding**: often true; predictive gain not automatic.
- **Outcome**: **MOSTLY FAILS as a primary lane**
- **Status**: **ANALOGY ONLY unless a concrete predictive invariant is shown**

### C7. Universal geometry unification

- **Attempted kill**: mechanism mismatch test.
- **Finding**: fails immediately (integrable vs topological vs dissipative stability are structurally different).
- **Outcome**: **REJECTED**
- **Status**: **DISPROVED (as near-term research program)**

---

## Rejected directions (explicit)

1. “One-geometry-to-rule-all-solitons” framing  
   Reason: structural mechanism mismatch; no falsifiable core invariant.

2. Pure immersion-visualization program without predictive theorem target  
   Reason: explanatory but weak theorem leverage.

3. Broad cross-domain plasma/MHD unification claims from soliton analogies alone  
   Reason: high overreach risk and weak falsifiability.

## Surviving directions after falsification

1. **Restricted observation recoverability for soliton manifolds** (best)
2. **Projection-preservation/no-go on explicit manifold class**
3. **Perturbative integrability-defect thresholds in narrow coefficient families**

## Falsification verdict

- The broad/hype lanes were mostly eliminated.
- The most defensible program is narrow, explicit, and theorem-driven with reproducible numerics.
- The surviving program is strong enough to justify immediate scoped work, but not broad novelty claims yet.

## Status summary (required labels)

- PROVED: none new in this discovery pass
- CONDITIONAL: C2, C3, C5
- VALIDATED: literature-backed falsification outcomes and lane filtering
- OPEN: C1, C2, C3, C4
- DISPROVED: C7
- ANALOGY ONLY: C6 unless predictive theorem support appears

---

## 6) Optional Existing-Repo Bridge

# Optional Existing-Repo Bridge (Only If Honest)

Date: 2026-04-16  
Policy: do not force mergers; keep soliton program independent unless a concrete theorem/benchmark link survives.

## Bridge test criteria

A cross-link is kept only if it can support at least one of:
- exact criterion,
- sharp no-go,
- computable invariant,
- reproducible benchmark family.

## Candidate cross-links tested

### Link A — Recoverability of soliton parameters under coarse observation

**Bridge target**: constrained-observation/recoverability logic (existing OCP-style lane)  
**Soliton-side object**: restricted one-soliton manifold with symmetry quotient.

**Assessment**
- This can be made precise without importing broader OCP branding.
- Cleanly phrased as an independent identifiability/recoverability theorem problem.

**Verdict**: **KEPT (narrow bridge)**  
**Status**: **OPEN (worth a dedicated small branch or companion note)**

---

### Link B — Projection/reduction preserving coherent structures

**Bridge target**: projection-success/failure logic from bridge/PDE ideas  
**Soliton-side object**: whether a projection preserves soliton manifold or produces defect drift.

**Assessment**
- Mathematical bridge is plausible and non-forced.
- Must stay equation-class-specific (e.g., one NLS/KdV lane + one projection class).

**Verdict**: **KEPT (restricted)**  
**Status**: **CONDITIONAL**

---

### Link C — Minimal-augmentation logic transferred directly to nonlinear soliton dynamics

**Assessment**
- Direct transfer is not justified at current stage.
- Nonlinear symmetry and manifold structure make naive translation risky.

**Verdict**: **REJECTED for now**  
**Status**: **DISPROVED as immediate transfer**

---

### Link D — MHD-soliton unification lane

**Assessment**
- Soliton-like plasma waves exist, but direct theorem-sharing with current Euler-potential closure program is weak right now.
- Risk of analogy inflation is high.

**Verdict**: **REJECTED (for now)**  
**Status**: **ANALOGY ONLY currently**

---

### Link E — Bounded-vs-periodic structural mismatch analogy

**Assessment**
- Conceptual analogy exists (boundary/domain effects can alter coherent-wave persistence).
- No immediate theorem bridge established in this discovery pass.

**Verdict**: **MAYBE (investigation-only)**  
**Status**: **OPEN, not promoted**

## Kept vs rejected summary

### Kept
1. Soliton-parameter recoverability under constrained observation (narrow, explicit)
2. Projection/reduction preservation/no-go for coherent-state manifolds

### Rejected or not promoted
1. Direct minimal-augmentation transfer to nonlinear full setting
2. Broad MHD-soliton unification
3. Broad bounded-vs-periodic analogies without explicit equation-class theorem

## Recommendation

Keep the soliton program as a separate identity.  
If any bridge is pursued, start with **Link A** in a narrow standalone note that can later map to existing repo language only after results survive.

---

## 7) Start-Here Research Plan

# Start-Here Research Plan (Soliton + Geometry)

Date: 2026-04-16  
Program identity: independent soliton-geometry program, discovery-first and falsification-first

## Chosen first direction

**Direction S1**: Observation-limited recoverability of restricted soliton manifolds (modulo symmetry).

Why first:
- narrow and theorem-accessible,
- strong falsifiability via explicit counterexamples,
- bridges naturally to numerics without forcing broad framework transfer.

## 0) Core working problem

For a selected equation class (start with focusing 1D NLS one-soliton family), define:
- parameter manifold `P` (amplitude, velocity, center, phase),
- symmetry quotient (translation/phase equivalence),
- observation operators `M` from a controlled family.

Goal:
- characterize when `M` uniquely identifies equivalence classes in `P`.

## 1) First 90-day execution plan

### Weeks 1–2: setup + precise model

Deliverables:
- formal problem statement
- admissible observation class
- exact identifiability target (mod symmetry)
- known-results boundary note (to avoid rediscovery)

Kill conditions:
- if problem reduces to immediate standard theorem with no extension value, pivot to S2.

### Weeks 3–5: theorem/no-go attempt

Deliverables:
- necessary condition theorem candidate
- sufficient condition theorem candidate (restricted)
- same-observation non-uniqueness counterexample family

Kill conditions:
- if necessary and sufficient conditions collapse into tautology with no computable criterion.

### Weeks 6–8: perturbation robustness layer

Deliverables:
- conditional robustness bound under small model perturbations/noise
- failure examples where identifiability collapses abruptly

Kill conditions:
- if robustness claims cannot be quantified beyond numerics.

### Weeks 9–12: reproducible benchmark package

Deliverables:
- script set generating witness/counterexample families
- table of exact / approximate / impossible regimes in this restricted setting
- final note: proved vs conditional vs open

## 2) Parallel backup direction (activate only if S1 stalls)

**Direction S2**: Projection/reduction preservation/no-go for soliton manifolds.

Trigger to activate:
- S1 novelty collapses quickly or theorem payload is too weak.

Minimum viable result:
- one exact preservation criterion + one explicit no-go counterexample for a projection class.

## 3) Research hygiene rules

1. No universal claims across all soliton types.
2. Every promotion must be theorem/counterexample/benchmark backed.
3. Distinguish clearly: PROVED, CONDITIONAL, VALIDATED, OPEN, DISPROVED, ANALOGY ONLY.
4. Keep geometry only where it yields explicit invariants/obstructions.

## 4) Deliverables in this discovery package

- `soliton_geometry_orientation.md`
- `geometry_connection_audit.md`
- `adjacent_topics_map.md`
- `novelty_candidates.md`
- `falsification_results.md`
- `optional_existing_repo_bridge.md`
- `start_here_research_plan.md`
- `ranked_reading_list.md`
- `ranked_theorem_simulation_opportunities.md`
- `learning_path_beginner_to_advanced.md`

## 5) Decision gates (go/no-go)

### Gate A (end of week 5)
- Keep S1 only if at least one nontrivial theorem/no-go statement survives.

### Gate B (end of week 8)
- Keep S1 as main lane only if robustness layer yields quantitative content, not only numerics.

### Gate C (end of week 12)
- Promote to paper-lane only if package contains:
  - at least one theorem-grade statement,
  - at least one counterexample family,
  - reproducible scripts and regime table.

## 6) Immediate next actions (this week)

1. Fix exact one-soliton parametrization and equivalence relation.
2. Choose two explicit observation families (one likely sufficient, one likely deficient).
3. Prove first non-uniqueness lemma for deficient observation family.
4. Build first numeric witness scripts to cross-check formulas.

## 7) Final status of this plan

- Program-level status: **VALIDATED as a viable discovery program**
- Main lane status: **OPEN (high promise)**
- Broad unification status: **DISPROVED / rejected**

---

## 8) Ranked Reading List

# Ranked Reading List (Soliton + Geometry)

Date: 2026-04-16  
Use: staged reading for this exact research program

## Tier 1 — Must-read core (start here)

1. Zabusky & Kruskal (1965), PRL: historical and conceptual soliton anchor.  
   https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.15.240
2. Gardner, Greene, Kruskal, Miura (1967), PRL: IST breakthrough for KdV.  
   https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.19.1095
3. Lax (1968): integrability and conserved structure viewpoint.  
   https://www.osti.gov/biblio/4522657
4. Zakharov & Shabat (1972): NLS integrable core and scattering framework.  
   https://www.jetp.ras.ru/cgi-bin/dn/e_034_01_0062
5. Drazin & Johnson, *Solitons: An Introduction* (Cambridge, 1989).  
   https://www.cambridge.org/core/books/solitons/3992154606336D7459B839EB29BF9C38
6. Ablowitz & Clarkson, *Solitons, Nonlinear Evolution Equations and Inverse Scattering* (1991).  
   https://www.cambridge.org/core/books/solitons-nonlinear-evolution-equations-and-inverse-scattering/5DBED94706868291C74AB13ACC750A79

## Tier 2 — Geometry and topology core

7. Hasimoto (1972), vortex-filament geometry link.  
   https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/abs/soliton-on-a-vortex-filament/1A2FF58DD1B8DE20509866A4713531F3
8. Manton & Sutcliffe, *Topological Solitons* (2004).  
   https://www.cambridge.org/core/books/topological-solitons/0A9670253EB1C8254BDACA4EE30C3AA3
9. Nagaosa & Tokura (2013), magnetic skyrmion review.  
   https://www.nature.com/articles/nnano.2013.243
10. Bridges (1997), multisymplectic PDE geometry.  
    https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/multisymplectic-structures-and-wave-propagation/C600E2AD2FB5A0A5AC31EB67F41E6CD7
11. Hairer, Lubich, Wanner, *Geometric Numerical Integration* (2006).  
    https://link.springer.com/book/10.1007/3-540-30666-8

## Tier 3 — Stability, perturbation, and beyond-integrable lanes

12. Kivshar & Malomed (1989), near-integrable soliton dynamics (RMP).  
    https://journals.aps.org/rmp/issues/61/4
13. Akhmediev & Ankiewicz (eds.), *Dissipative Solitons* (2005).  
    https://link.springer.com/book/10.1007/b11728
14. Benjamin & Feir (1967), MI foundation.  
    https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/disintegration-of-wave-trains-on-deep-water-part-1-theory/246B0FC7833C7F9C18755482BD308CA8
15. Peregrine (1983), NLS and localized extreme events.  
    https://www.cambridge.org/core/journals/anziam-journal/article/water-waves-nonlinear-schrodinger-equations-and-their-solutions/D87F5416C657F3B5C35AE96DF9F73DD0
16. Ablowitz, Biondini, Wang (2016), KP Whitham modulation (entry to dispersive hydrodynamics).  
    https://arxiv.org/abs/1610.03478

## Tier 4 — Application-adjacent lanes

17. Gross (1961), quantized vortex structure in boson systems.  
    https://www.osti.gov/biblio/4028087
18. Pitaevskii (Phys. Rev.), vortex lines in imperfect Bose gas.  
    https://journals.aps.org/pr/abstract/10.1103/PhysRev.138.A429
19. Frantzeskakis (2010), dark solitons in BEC review.  
    https://arxiv.org/abs/1004.4071
20. Washimi & Taniuti (1966), ion-acoustic solitary waves (plasma classic).  
    https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.17.996
21. Agrawal, *Nonlinear Fiber Optics* (standard optics reference).  
    https://www.sciencedirect.com/book/9780128170427/nonlinear-fiber-optics

## Tier 5 — Orientation aids (good quick refresh)

22. Scholarpedia: Soliton (Porter).  
    https://www.scholarpedia.org/article/Soliton
23. Scholarpedia: Nonlinear Schrödinger systems.  
    https://www.scholarpedia.org/article/Nonlinear_Schrodinger_systems%3A_continuous_and_discrete
24. Kadomtsev–Petviashvili original citation page (MathNet).  
    https://www.mathnet.ru/eng/dan35447

## Reading order recommendation

- Week 1: Tier 1 + items 7 and 12
- Week 2: items 10, 11, 14, 15
- Week 3: items 8, 9, 17–20
- Week 4 onward: target-lane deepening based on chosen theorem direction

## Notes on usage

- Use Tier 1/2 to avoid rediscovering known structure.
- Use Tier 3 to prevent overclaiming stability beyond integrable assumptions.
- Use Tier 4 to keep physical relevance honest without drifting into pure phenomenology.

---

## 9) Ranked Theorem/Simulation Opportunities

# Ranked Theorem / Simulation Opportunity List

Date: 2026-04-16  
Ranking logic: theorem potential + falsifiability + reproducibility + novelty safety

## Tier A (highest priority)

### A1. Identifiability theorem for restricted one-soliton manifold under partial observation

- Type: theorem + counterexample
- Core output: necessary/sufficient conditions modulo symmetry orbit
- Falsifier: explicit non-unique parameter pairs under same observation
- Difficulty: medium-high
- Novelty risk: medium (manageable with strict scope)
- Status: OPEN

### A2. Projection-preservation criterion + no-go for soliton manifold invariance

- Type: theorem + reproducible numerics
- Core output: exact criterion for one projection class and one no-go class
- Falsifier: construct projection with same approximation order but opposite preservation verdict
- Difficulty: high
- Novelty risk: medium
- Status: OPEN/CONDITIONAL

### A3. Integrability-defect threshold law for structured perturbations

- Type: conditional theorem + benchmark law
- Core output: explicit defect measure and persistence/failure threshold map
- Falsifier: perturbation family violating proposed threshold monotonicity
- Difficulty: high
- Novelty risk: medium-high
- Status: CONDITIONAL

## Tier B (strong but riskier)

### B1. Topological vs integrable stability comparison under matched perturbations

- Type: comparative theorem/simulation package
- Core output: fair, restricted comparison theorem (or explicit no-go to fair comparison)
- Falsifier: no common metric supports meaningful side-by-side claim
- Difficulty: high
- Novelty risk: high
- Status: OPEN

### B2. Structure-preserving numerical diagnostics for long-time collision fidelity

- Type: numerical analysis + benchmark protocol
- Core output: reproducible fidelity metric distinguishing geometry-preserving from non-preserving schemes
- Falsifier: metric fails to generalize across two canonical equations
- Difficulty: medium-high
- Novelty risk: medium
- Status: OPEN

### B3. Observation-threshold map under noise for soliton parameter recovery

- Type: theorem-lite bounds + simulation
- Core output: exact/approximate/impossible regions in noise-observation plane
- Falsifier: no stable phase transition under realistic noise models
- Difficulty: medium-high
- Novelty risk: medium-high
- Status: OPEN

## Tier C (defer unless Tier A stalls)

### C1. Soliton-surface invariant predictors

- Type: geometry-heavy exploratory
- Core output: predictive invariant tied to stability/defect growth
- Main risk: becomes interpretation-only geometry
- Status: WEAK / OPEN

### C2. Broad plasma/MHD generalized soliton-obstruction map

- Type: broad synthesis
- Main risk: overreach and low theorem density
- Status: TOO BROAD / REJECTED for now

## Best immediate theorem candidate

**A1** is the most actionable first theorem lane.

## Best immediate simulation candidate

**B2** is the strongest reproducible simulation lane with high practical value and low hype risk.

## Suggested package for first publishable unit

1. A1 theorem/no-go core  
2. small B3 noise threshold appendix  
3. B2 reproducibility benchmark section

This bundle stays narrow, defensible, and literature-aware.

---

## 10) Learning Path (Beginner to Advanced)

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

