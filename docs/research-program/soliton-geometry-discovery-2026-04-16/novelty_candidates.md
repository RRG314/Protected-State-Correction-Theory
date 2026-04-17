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
