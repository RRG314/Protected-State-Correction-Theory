# Invariant Formal Audit

Status: `EXPLORATION / NON-PROMOTED`  
Date: 2026-04-18

This audit formalizes the current invariant stack with exact scope and explicit maturity labels.

## Core scopes used

- **S1 (Core linear):** finite linear recoverability with target map `L` and record map `O`.
- **S2 (Context-indexed linear):** finite set `{M_c}` with local vs shared decoder questions.
- **S3 (Descriptor-fiber catalogs):** finite witness catalogs where descriptors induce mixed fibers.
- **S4 (Stress/fragility):** family enlargement, mismatch, and perturbation stress suites.
- **S5 (Physics branch):** black-hole/cosmology and quantum extensions; non-canonical unless explicitly proved.

## Invariant-by-invariant audit

| Invariant | Formal object | Scope | Exact/quantitative | Status | Supports | Missing / correction |
|---|---|---|---|---|---|---|
| Fiber constancy / factorization | `tau = g ∘ M` iff exact recoverability | S1 | Exact | `PROVED` | exactness characterization | none on core statement |
| Row-space / kernel compatibility | `row(L) ⊆ row(O)` equiv `ker(O) ⊆ ker(L)` | S1 | Exact (+ residual quantitative form) | `PROVED` | exactness and no-go baselines | sharpen perturbation constants |
| Null-intersection dimension | `dim(ker(O) ∩ ker(L)^⊥)` proxy in current implementation | S1 | Exact obstruction indicator | `PROVED` | impossibility witness classification | unify notation with kernel-inclusion form |
| Collision gap / collapse modulus | maximal protected separation under record collisions | S1/S4 | Exact in low-null; proxy in high-null computational regime | `PROVED ON SUPPORTED FAMILY` + `VALIDATED / NUMERICAL ONLY` (proxy mode) | failure magnitude diagnostics | avoid using proxy rows for exact theorem claims |
| CID / context coherence defect | `CID = min_d max_c ||dM_c - L||` | S2 | Exact zero-test + quantitative defect | `PROVED ON SUPPORTED FAMILY` | local-vs-shared split, shared-feasibility testing | broader norm/conditioning theory |
| Context gap | `I(local exact) - I(shared exact)` | S2 | Exact indicator | `PROVED ON SUPPORTED FAMILY` | conditioned-vs-invariant theorem package | stronger structural characterization beyond indicator |
| `delta_free` | minimal unconstrained shared augmentation rows restoring shared exactness | S2 | Exact threshold (supported class) | `PROVED ON SUPPORTED FAMILY` | constructive repair law | closed-form bounds |
| `delta_C` | candidate-library defect in lifted rank geometry | S2/S3 | Exact constrained feasibility defect | `PROVED ON SUPPORTED FAMILY` | candidate-library no-go and gain-insufficiency | general necessary/sufficient theorem |
| DFMI | fraction of descriptor fibers that are mixed in exact/fail verdict | S3 | Quantitative anti-classifier invariant | `PROVED ON SUPPORTED FAMILY` | descriptor ambiguity diagnosis | confidence bounds under random generation |
| IDELB | irreducible descriptor error lower bound from fiber class counts | S3 | Quantitative lower bound | `PROVED ON SUPPORTED FAMILY` | no rank-only / no budget-only classifier claims | extension to weighted families |
| CL (compatibility lift) | `IDELB(phi)-IDELB(phi+)` | S3 | Quantitative lift-improvement invariant | `PROVED ON SUPPORTED FAMILY` | descriptor-lift theorem candidate | canonical normalization across branches |
| Enlargement fragility indicators | exactness flip under family enlargement | S4 | Quantitative fragility indicator | `PROVED ON SUPPORTED FAMILY` (existence), `VALIDATED` (rates) | false-positive no-go boundaries | scale laws vs enlargement geometry |
| Mismatch instability indicators | recovery error under off-family decoder deployment | S4 | Quantitative stress indicator | `VALIDATED / NUMERICAL ONLY` | model-mismatch boundary evidence | theorem-level bounds |
| Boundary/domain compatibility indicators (CFD/MHD) | branch-specific compatibility defects under domain/closure changes | S5 | Diagnostic / conditional | `CONDITIONAL` | branch-specific obstruction narratives | one unified formal invariant |
| Quantum alignment-style ratios | branch-limited alignment ratio in quantum estimation language | S5 | Restricted diagnostic | mostly `KNOWN / REFRAMED`; some `PROVED ON RESTRICTED CLASS` identities | quantum measurement design diagnostics | strong novelty-risk control |

## Formal audit conclusions

1. **No new universal core invariant displaced fiber/row-space exactness.**
2. **Most valuable additive stack is:** `CID + context gap + delta_free + delta_C + (DFMI, IDELB, CL)`.
3. **Collision/collapse quantities remain useful but must be explicitly mode-labeled** (exact vs proxy).
4. **Stress invariants are currently best treated as robustness diagnostics**, not promoted standalone theorems.
