# Theorem Hierarchy Final

Date: 2026-04-17

Canonical hierarchy used in this pass:
- `LEVEL U`: universal core
- `LEVEL B1`: branch-limited theorem package
- `LEVEL B2`: branch-limited validated package
- `LEVEL E`: engineering/tool consequences
- `LEVEL A`: analogy-only
- `LEVEL R`: rejected

## Normalized Stack

| ID | Level | Result | Status | One-sentence statement | Why this level |
|---|---|---|---|---|---|
| H-U1 | U | Fiber/factorization exactness (`OCP-030`) | `PROVED` | Exact recoverability holds iff target is constant on record fibers (equiv. factors through record). | Survives unchanged across recoverability branches as abstract core. |
| H-U2 | U | Collision no-go corollary | `PROVED` | If equal records carry different target values, exact recovery is impossible. | Universal impossibility form of H-U1. |
| H-U3 | U | Quotient/factorization admissible-family form | `PROVED` | Exactness is always relative to declared admissible family and nuisance equivalence. | Needed to prevent hidden universalization across families/symmetries. |
| H-B1-1 | B1 | Restricted-linear compatibility (`OCP-031`) | `PROVED` | Exactness iff `ker(OF) ⊆ ker(LF)` (equiv. row-space inclusion). | Exact theorem beyond U core but class-restricted. |
| H-B1-2 | B1 | Minimal augmentation (`OCP-045`) | `PROVED` | Minimum unrestricted added measurements is `δ(O,L;F)=rank([OF;LF])-rank(OF)`. | Constructive theorem only in restricted-linear branch. |
| H-B1-3 | B1 | No rank-only classifier (`OCP-049`) | `PROVED` | Rank tuple alone cannot classify exactness on supported restricted-linear class. | Strong anti-classifier theorem, explicitly class-scoped. |
| H-B1-4 | B1 | No fixed-library budget-only classifier (`OCP-050`) | `PROVED` | Equal fixed-library budget can yield opposite exactness verdicts. | Strong anti-classifier theorem, design-catalog scoped. |
| H-B1-5 | B1 | Family-enlargement fragility (`OCP-052`) | `PROVED` | Exactness on smaller family can fail on enlarged family with explicit witnesses. | Theorem-grade fragility law in supported class. |
| H-B1-6 | B1 | Canonical model-mismatch instability (`OCP-053`) | `PROVED` | Decoder exact on model family can incur explicit error floor on true family. | Theorem-grade mismatch law in canonical class. |
| H-B1-7 | B1 | Bounded-domain transplant no-go + divergence-only no-go (`OCP-023`,`OCP-028`) | `PROVED` | Scalar constraint removal alone does not certify bounded-domain exact protected recovery. | Domain-compatibility theorem/no-go pair. |
| H-B1-8 | B1 | Bounded finite-mode Hodge exactness (`OCP-044`) | `PROVED ON SUPPORTED FAMILY` | Exactness survives on explicit boundary-compatible finite-mode family. | Positive bounded-domain theorem but restricted-family only. |
| H-B1-9 | B1 | Soliton symmetry non-identifiability | `PROVED` | Symmetry-invariant observations can block unique recovery modulo quotient classes. | Exact theorem on declared restricted soliton classes. |
| H-B1-10 | B1 | Soliton same-count opposite-verdict package | `PROVED ON SUPPORTED FAMILY` + `CONDITIONAL` continuous | Equal observation count can yield opposite identifiability verdicts. | Strong restricted analogue; continuous generalization still open. |
| H-B1-11 | B1 | MHD variable-`η` obstruction + annular survivor split | `PROVED ON SUPPORTED FAMILY` | Nonconstant smooth axis-touching survivors fail in supported radial classes; annular survivors remain. | Domain/regularity obstruction theorem package in declared MHD class. |
| H-B2-1 | B2 | Soliton projection preservation/no-go split | `VALIDATED` + `CONDITIONAL` theorem | Some projection classes are near-preserving while others are explicit no-go in tested lane. | Reproducible but not promoted universal theorem. |
| H-B2-2 | B2 | MHD sheet-thinning defect scaling | `VALIDATED` | Defect trend `max|R| ~ ε/δ` appears in declared benchmark family. | Empirical branch support, not theorem. |
| H-B2-3 | B2 | Rank-fragility quantitative split (OCP discovery lane) | `VALIDATED` | Small perturbation sensitivity differs strongly by structural class in tested setups. | Reproducible quantitative indicator, theorem upgrade pending. |
| H-E1 | E | Structural Discovery Studio | `VALIDATED` | Theorem-linked diagnostics/repair workflow reliably maps failures to supported fixes. | Engineering consequence layer that operationalizes B1/B2. |
| H-E2 | E | Discovery Mixer / composition lab | `VALIDATED` | Typed composition and status-tagged outputs enforce scope-aware branch usage. | Tool layer, not theorem source. |
| H-E3 | E | SDS two-reservoir optimizer branch | `VALIDATED` + `OPEN` superiority | Two-reservoir gating is stable and competitive on tested benchmarks, but not dominant. | Engineering-adjacent lane; no theorem-core promotion. |
| H-A1 | A | Universal self-organization = correction equivalence | `ANALOGY ONLY` | Dynamic emergence and operator correction share motifs but not theorem identity. | Conceptual parallel without theorem transfer. |
| H-A2 | A | Two-reservoir SDS motif as general structural principle | `ANALOGY ONLY` | Cross-branch intuition exists but no theorem-grade shared map. | No admissible formal transfer proved. |
| H-R1 | R | Universal amount-only law | `REJECTED` | Rank/count/budget alone do not universally classify exactness. | Contradicted by theorem-level anti-classifier package. |
| H-R2 | R | Universal projection-preservation law | `REJECTED` | Projection success/failure is operator/domain/family dependent. | Counterexamples in OCP bounded-domain and soliton lanes. |
| H-R3 | R | Universal recoverability-preservation-emergence theorem | `REJECTED` | One theorem cannot currently capture these distinct process classes without distortion. | Over-broad and not evidence-supported. |

## Normalization Decision

Promote only `U` and `B1` into theorem-core narrative. Keep `B2` and `E` explicit but non-theorem-core. Preserve `A` and `R` sections in every framework-facing writeup.
