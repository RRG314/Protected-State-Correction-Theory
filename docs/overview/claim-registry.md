# Claim Registry

| Claim ID | Short Name | Status | Evidence | Confidence | Key Files | Next Action |
| --- | --- | --- | --- | --- | --- | --- |
| OCP-001 | Formal OCP tuple | PROVED | repo-local definition and consistency checks | High | `docs/formalism/formal-theory.md` | Use as the primary formal language. |
| OCP-002 | Exact orthogonal projection theorem | PROVED | linear-algebra proof and tests | High | `docs/theorem-candidates/central-theorem.md; tests/math/test_core_projectors.py` | Promote as the clean finite-dimensional backbone. |
| OCP-003 | Indistinguishability no-go | PROVED | elementary contradiction proof | High | `docs/impossibility-results/no-go-results.md` | Promote as the strongest exact no-go statement. |
| OCP-004 | Continuous damping theorem | PROVED | closed-form solution and tests | High | `docs/theorem-candidates/backup-theorems.md; tests/math/test_core_projectors.py` | Use as the bridge from exact correction to asymptotic correction. |
| OCP-005 | QEC exact anchor | CONDITIONAL | standard QEC theorem plus repo-local rewrite | High | `docs/qec/qec-in-ocp.md; tests/math/test_qec_knill_laflamme.py` | Keep exact but conditional on KL-type assumptions. |
| OCP-006 | Helmholtz/Leray exact continuous anchor | PROVED | FFT operator construction and tests | High | `docs/mhd/divergence-cleaning-in-ocp.md; tests/math/test_mhd_projection.py` | Promote heavily as the best exact continuous example. |
| OCP-007 | GLM as asymptotic OCP | CONDITIONAL | implementation analysis and empirical reduction tests | Medium | `docs/mhd/glm-and-asymptotic-correction.md; tests/examples/test_glm_decay.py` | Present as a good asymptotic example, not exact correction. |
| OCP-008 | Control-theoretic instantiation | CONDITIONAL | structural control analysis | Medium | `docs/control/control-extension.md` | Keep conditional and design-oriented. |
| OCP-009 | Universal scalar correction capacity | OPEN | failed unification attempt | Low | `NOVELTY_AND_LIMITS.md; docs/impossibility-results/no-go-results.md` | Do not promote without a better category-specific definition. |
| OCP-010 | Topological Adam / ML extension | ANALOGY ONLY | local sibling-repo evidence is too weak | Low | `docs/disproven-or-weak/weak-extensions.md` | Keep secondary and unpromoted. |
| OCP-011 | Engineering design value | CONDITIONAL | operator examples and no-go criteria | Medium | `docs/applications/practical-use-cases.md` | Use as the main practical pitch, but keep the domain assumptions explicit. |
| OCP-012 | Exact-to-asymptotic bridge | CONDITIONAL | formalism + exact and asymptotic branches | Medium | `docs/formalism/exact-vs-asymptotic.md` | Promote after upgrading the bridge from framework language to a sharper theorem statement. |
| OCP-013 | Invariant-split generator theorem | PROVED | linear ODE proof and tests | High | `docs/theorem-candidates/generator-theorems.md; tests/math/test_continuous_generators.py` | Promote as the strongest next-step theorem beyond the projector case. |
| OCP-014 | Self-adjoint PSD corollary | PROVED | spectral proof and tests | High | `docs/theorem-candidates/generator-theorems.md; tests/math/test_continuous_generators.py` | Use as the cleanest grounded continuous-time strengthening. |
| OCP-015 | Mixing no-go for linear flows | PROVED | derivative-at-zero argument and tests | High | `docs/impossibility-results/no-go-results.md; tests/math/test_continuous_generators.py` | Promote as the strongest new linear-flow failure criterion in the repo. |
| OCP-016 | Exact correction rank lower bound | PROVED | linear-algebra proof and tests | High | `docs/theorem-candidates/capacity-theorems.md; tests/math/test_capacity.py` | Promote as the cleanest minimum-structure theorem in the repo. |
| OCP-017 | Sector distinguishability lower bound | CONDITIONAL | sector-based argument plus QEC example | Medium | `docs/theorem-candidates/capacity-theorems.md; tests/math/test_capacity.py` | Keep this branch-specific and avoid overstating it beyond the exact sector model. |
| OCP-018 | Category-specific capacity view | CONDITIONAL | definitions, lower bounds, and examples across branches | Medium | `docs/theorem-candidates/capacity-theorems.md; docs/open-questions/viable-next-directions.md` | Develop this further before treating it as a mature theory. |
