# Full Claim Audit

Date: 2026-04-17
Method: claim-registry extraction + branch mapping + explicit tool/meta additions.

| Claim ID | Short Statement | Branch | Current Status | Claim Type | Evidence Type | Test Method | Risk | Final Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OCP-001 | Formal OCP tuple | A | PROVED | theorem | repo-local definition and consistency checks | exact linear algebra + projector witness search | Medium | PROVED |
| OCP-002 | Exact orthogonal projection theorem | A | PROVED | theorem | linear-algebra proof and tests | exact linear algebra + projector witness search | Medium | PROVED |
| OCP-003 | Indistinguishability no-go | A | PROVED | theorem | elementary contradiction proof | exact linear algebra + projector witness search | Medium | PROVED |
| OCP-004 | Continuous damping theorem | E | PROVED | theorem | closed-form solution and tests | spectral decomposition + non-normal generator stress tests | Medium | PROVED |
| OCP-005 | QEC exact anchor | B | CONDITIONAL | theorem | standard QEC theorem plus repo-local rewrite | sector overlap witness + basis-invariant checks | Medium | CONDITIONAL |
| OCP-006 | Helmholtz/Leray exact continuous anchor | C | PROVED | theorem | FFT operator construction and tests | FFT/Helmholtz recomputation + idempotence tests | Medium | PROVED |
| OCP-007 | GLM as asymptotic OCP | J | CONDITIONAL | theorem | implementation analysis and empirical reduction tests | bridge-scope check + theorem-vs-analogy separation | High | CONDITIONAL |
| OCP-008 | Control-theoretic instantiation | J | CONDITIONAL | theorem | structural control analysis | bridge-scope check + theorem-vs-analogy separation | High | CONDITIONAL |
| OCP-009 | Universal scalar correction capacity | K | OPEN | theorem | failed unification attempt | meta-layer overlap and invariant reproducibility checks | High | OPEN |
| OCP-010 | Topological Adam / ML extension | K | ANALOGY ONLY | bridge | local sibling-repo evidence is too weak | meta-layer overlap and invariant reproducibility checks | High | ANALOGY ONLY |
| OCP-011 | Engineering design value | I | CONDITIONAL | tool | operator examples and no-go criteria | workbench consistency tests + export/label checks | Medium | CONDITIONAL |
| OCP-012 | Exact-to-asymptotic bridge | I | CONDITIONAL | bridge | formalism + exact and asymptotic branches | workbench consistency tests + export/label checks | High | CONDITIONAL |
| OCP-013 | Invariant-split generator theorem | E | PROVED | theorem | linear ODE proof and tests | spectral decomposition + non-normal generator stress tests | Medium | PROVED |
| OCP-014 | Self-adjoint PSD corollary | E | PROVED | theorem | spectral proof and tests | spectral decomposition + non-normal generator stress tests | Medium | PROVED |
| OCP-015 | Mixing no-go for linear flows | E | PROVED | theorem | derivative-at-zero argument and tests | spectral decomposition + non-normal generator stress tests | Medium | PROVED |
| OCP-016 | Exact correction rank lower bound | A | PROVED | theorem | linear-algebra proof and tests | exact linear algebra + projector witness search | Medium | PROVED |
| OCP-017 | Sector distinguishability lower bound | B | CONDITIONAL | theorem | sector-based argument plus QEC example | sector overlap witness + basis-invariant checks | Medium | CONDITIONAL |
| OCP-018 | Category-specific capacity view | K | CONDITIONAL | theorem | definitions, lower bounds, and examples across branches | meta-layer overlap and invariant reproducibility checks | High | CONDITIONAL |
| OCP-019 | Exact sector recovery theorem | B | PROVED | theorem | operator construction, proof sketch, and tests | sector overlap witness + basis-invariant checks | Medium | PROVED |
| OCP-020 | Finite-time exact recovery no-go for smooth linear flows | E | PROVED | theorem | invertibility argument plus workbench and test examples | spectral decomposition + non-normal generator stress tests | Medium | PROVED |
| OCP-021 | Sector-overlap detection no-go | B | PROVED | theorem | subspace contradiction proof and overlapping-sector test case | sector overlap witness + basis-invariant checks | Medium | PROVED |
| OCP-022 | Transverse gauge projection fit | J | PROVED ON SUPPORTED FAMILY | bridge | direct corollary of the projection branch plus physics reinterpretation | bridge-scope check + theorem-vs-analogy separation | High | PROVED ON SUPPORTED FAMILY |
| OCP-023 | Periodic projector transplant to bounded domains | D | DISPROVED | theorem | explicit boundary counterexample and tests | bounded-domain counterexample generation + boundary diagnostics | Low | DISPROVED |
| OCP-024 | Constraint damping in additional physics systems | J | CONDITIONAL | theorem | cross-system operator comparison | bridge-scope check + theorem-vs-analogy separation | High | CONDITIONAL |
| OCP-025 | Continuous quantum error correction bridge | J | CONDITIONAL | bridge | QEC/control literature comparison plus branch mapping | bridge-scope check + theorem-vs-analogy separation | High | CONDITIONAL |
| OCP-026 | Generic constrained Hamiltonian fit | J | ANALOGY ONLY | bridge | current repo lacks a canonical projector/recovery construction in that generality | bridge-scope check + theorem-vs-analogy separation | High | ANALOGY ONLY |
| OCP-027 | Periodic incompressible projection fit | C | PROVED ON SUPPORTED FAMILY | bridge | operator corollary plus executable periodic CFD tests | FFT/Helmholtz recomputation + idempotence tests | High | PROVED ON SUPPORTED FAMILY |
| OCP-028 | Divergence-only bounded recovery no-go | D | PROVED | theorem | elementary distinguishability argument plus bounded-state witness | bounded-domain counterexample generation + boundary diagnostics | Medium | PROVED |
| OCP-029 | Bounded-domain projection classification | D | CONDITIONAL | theorem | classification statement tied to the bounded counterexample and Hodge-projector criterion | bounded-domain counterexample generation + boundary diagnostics | Medium | CONDITIONAL |
| OCP-030 | Observation fiber exactness | F | PROVED | theorem | formal derivation plus branch tests | fiber/collision brute-force + threshold recomputation | Medium | PROVED |
| OCP-031 | Restricted linear protected-variable recovery | F | PROVED | theorem | linear-algebra derivation and tests | fiber/collision brute-force + threshold recomputation | Medium | PROVED |
| OCP-032 | Fixed-basis phase-loss no-go | F | PROVED | theorem | toy-model derivation and computational sweep | fiber/collision brute-force + threshold recomputation | Medium | PROVED |
| OCP-033 | Periodic record classification | F | CONDITIONAL | theorem | conventional computational benchmark with generated artifacts | fiber/collision brute-force + threshold recomputation | Medium | CONDITIONAL |
| OCP-034 | Finite-history versus asymptotic recovery split | F | PROVED | theorem | model-specific derivation, explicit formula, and computational sweep | fiber/collision brute-force + threshold recomputation | Medium | PROVED |
| OCP-035 | Collapse-modulus noise lower bound | F | PROVED | theorem | metric derivation plus analytic benchmark and tests | fiber/collision brute-force + threshold recomputation | Medium | PROVED |
| OCP-036 | Restricted observation rank lower bound | F | PROVED | theorem | rank-nullity derivation and tests | fiber/collision brute-force + threshold recomputation | Medium | PROVED |
| OCP-037 | Qubit phase-window collision law | F | PROVED | theorem | closed-form derivation and numerical sweep | fiber/collision brute-force + threshold recomputation | Medium | PROVED |
| OCP-038 | Periodic cutoff threshold on the two-mode family | F | PROVED | theorem | family-level rank argument plus recovery-error sweep | fiber/collision brute-force + threshold recomputation | Medium | PROVED |
| OCP-039 | Periodic functional-support threshold | F | PROVED | theorem | kernel-based derivation, row-space residual checks, discretization checks, and recovery sweeps | fiber/collision brute-force + threshold recomputation | Medium | PROVED |
| OCP-040 | Nested linear minimal observation complexity | F | PROVED | theorem | restricted-linear derivation plus independent periodic/control threshold checks | fiber/collision brute-force + threshold recomputation | Medium | PROVED |
| OCP-043 | Nested restricted-linear collision-gap threshold law | F | PROVED | theorem | restricted-linear derivation, independent nullspace-on-a-box checks, stress sweeps, and generated-artifact consistency tests | fiber/collision brute-force + threshold recomputation | Medium | PROVED |
| OCP-041 | Same-record weaker-versus-stronger split | F | PROVED | theorem | row-space argument plus periodic/control counterexample families | fiber/collision brute-force + threshold recomputation | Medium | PROVED |
| OCP-042 | Diagonal functional interpolation threshold | F | PROVED | theorem | Vandermonde/interpolation derivation plus independent linear-recovery, nullspace, and sweep tests | fiber/collision brute-force + threshold recomputation | Medium | PROVED |
| OCP-044 | Boundary-compatible finite-mode Hodge projection | D | PROVED ON SUPPORTED FAMILY | theorem | integration-by-parts derivation plus independent discrete projector-construction checks and tests | bounded-domain counterexample generation + boundary diagnostics | Medium | PROVED ON SUPPORTED FAMILY |
| OCP-045 | Restricted-linear minimal augmentation theorem | G | PROVED | theorem | row-space derivation, random stress tests, and design-artifact consistency checks | row-space/kernel automation + anti-classifier witness regeneration | Medium | PROVED |
| OCP-046 | Restricted-linear exact-regime upper envelope | G | PROVED | theorem | direct linear derivation plus exact-case computational checks and generated recoverability artifacts | row-space/kernel automation + anti-classifier witness regeneration | Medium | PROVED |
| OCP-047 | Same-rank observation insufficiency | G | PROVED | theorem | explicit construction plus dimension-stress tests | row-space/kernel automation + anti-classifier witness regeneration | Medium | PROVED |
| OCP-048 | Detectable-only through target coarsening | H | PROVED | theorem | factorization argument plus finite and restricted-linear witnesses | logical dependency audit + family-enlargement/mismatch stress | Medium | PROVED |
| OCP-049 | No rank-only exact classifier theorem | H | PROVED | theorem | explicit witness construction, exhaustive small-dimension coordinate enumeration, and generated artifacts | logical dependency audit + family-enlargement/mismatch stress | Medium | PROVED |
| OCP-050 | No fixed-library budget-only exact classifier theorem | H | PROVED | theorem | explicit fixed-library construction, exhaustive subset enumeration, and generated artifacts | logical dependency audit + family-enlargement/mismatch stress | Medium | PROVED |
| OCP-051 | Noisy weaker-versus-stronger separation theorem | H | PROVED | theorem | restricted-linear derivation plus brute-force noise-grid cross-checks and generated artifacts | logical dependency audit + family-enlargement/mismatch stress | Medium | PROVED |
| OCP-052 | Restricted-linear family-enlargement false-positive theorem | H | PROVED | theorem | fiber-factorization argument plus collision-gap lower bound, explicit witness construction, generated artifacts, and branch tests | logical dependency audit + family-enlargement/mismatch stress | Medium | PROVED |
| OCP-053 | Canonical model-mismatch instability theorem | H | PROVED | theorem | closed-form derivation plus brute-force equality checks and generated artifacts | logical dependency audit + family-enlargement/mismatch stress | Medium | PROVED |
| WB-001 | Benchmark console module-health rows match validated workbench surfaces. | I | VALIDATED | tool | node consistency tests + generated validation snapshot | workbench consistency tests + export/label checks | High | VALIDATED |
| META-001 | Descriptor-fiber invariants (DFMI/IDELB/CL) quantify finite-class anti-classifier limits. | K | PROVED ON SUPPORTED FAMILY | theorem | finite-class theorem + regenerated witness statistics | meta-layer overlap and invariant reproducibility checks | Medium | PROVED ON SUPPORTED FAMILY |
