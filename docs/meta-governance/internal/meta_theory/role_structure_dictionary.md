# Role-Structure Dictionary

Date: 2026-04-17

## Purpose

Create a common role vocabulary across branches and identify which roles are recurring, necessary, optional, or branch-specific.

## Universal Candidate Roles

| Role | Formal meaning |
| --- | --- |
| State (`x`) | Underlying system element in admissible family `A`. |
| Target (`T`) | Quantity to preserve/recover/close exactly. |
| Record (`M`) | Observation/representation map available to inference/correction. |
| Disturbance/Ambiguity (`D`) | Non-target variation that may contaminate or be indistinguishable under `M`. |
| Correction (`C`) | Operator/process used to remove/suppress disturbance relative to target. |
| Evolution (`E`) | Time-dependent dynamics (if present). |
| Constraint/Compatibility (`K`) | Condition linking roles that determines exactness vs failure. |
| Nuisance symmetry (`~`) | Equivalence that must be quotiented (phase/translation/gauge/etc.). |
| Distortion map | Map that collapses target-relevant distinctions (special case: `M` with target-distinguishing fibers). |
| Side information (`S_info`) | Added structure or measurements used to restore exactness. |

## Branch Mapping

| Branch | State | Target | Record/representation | Disturbance/ambiguity | Compatibility object | Correction/evolution | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OCP restricted recoverability | `x=Fz` | `LFz` | `OFz` | `ker(OF)` directions | `ker(OF) ⊆ ker(LF)` / fiber constancy | decoder `R` / augmentation | canonical theorem-grade lane |
| OCP projection/correction | field/state split | protected subspace/component | projector architecture | overlap/non-solenoidal component | orthogonality / domain-compatible Hodge structure | one-shot projector or damping generator | exact vs asymptotic split explicit |
| Soliton restricted lane | one-soliton manifold (mod sym) | quotient parameters | local/Fourier observation families | symmetry orbits + noninjective fibers | quotient injectivity conditions | optional reduction/projection operators | continuous promotion still conditional |
| MHD closure lane | Euler-potential ansatz state | exact closure (`R=0`) | chosen `(alpha,beta,eta,domain)` representation | closure remainder under resistive terms | ansatz/profile/domain compatibility ODEs | evolution-consistency condition | strong family dependence |
| SDS engineering layer | user-configured scenario | selected protected target | configured record architecture | diagnostic ambiguity classes | theorem-linked diagnostics | repair/augmentation suggestions | implementation layer, not theorem core |

## Recurrence and Necessity Assessment

### Recurring across all tested branches
- Target role
- At least one interacting structural role (record/operator/domain/symmetry/evolution)
- Compatibility criterion controlling verdict

### Often recurring (not always identical)
- Disturbance/ambiguity role
- Distortion/collapse mechanism
- Side-information augmentation role

### Branch-specific emphasis
- Symmetry quotient (`~`): strongest in soliton lane
- Boundary/topology/domain compatibility: strongest in CFD/MHD bounded settings
- Tool-layer workflow roles: strongest in SDS

## Necessary vs Optional (Current Evidence)

| Role | Necessary for nontrivial recoverability/correction? |
| --- | --- |
| Target | Yes |
| Interacting non-target structure | Yes (branch-limited evidence) |
| Explicit disturbance variable | Usually, but can be implicit in fibers/kernels |
| Side-information object | No (only for repair/enrichment) |
| Symmetry quotient | Optional; necessary only in symmetry-affected branches |
| Dynamic evolution role | Optional; needed for asymptotic/dynamical branches |

## Key Finding

The strongest recurring pattern is not “two physical substances.”

It is:
- a **target role**,
- an **interacting structural role**,
- and a **compatibility condition** that determines exactness/failure.

This supports a structural meta-theory candidate while avoiding metaphysical overreach.
