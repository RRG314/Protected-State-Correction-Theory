# Descriptor-Fiber Anti-Classifier Bounds and Compatibility Lift on Supported Witness Classes

Steven Reid  
Independent Researcher  
ORCID: 0009-0003-9132-3410  
sreid1118@gmail.com  
April 2026

## Abstract

This paper formalizes a branch-limited quantitative layer for the OCP anti-classifier program. On finite witness classes with binary exactness verdicts, we define descriptor fibers and prove two finite-class results: a purity criterion for perfect descriptor-only classification and an irreducible descriptor-only error lower bound. We then define computable invariants: descriptor-fiber mixedness (`DFMI`), irreducible descriptor error lower bound (`IDELB`), and compatibility lift (`CL`). On current OCP witness artifacts, amount-only descriptors are mixed (`DFMI=1`) with nonzero irreducible error, while adding compatibility information collapses the lower bound to zero on the tested rank witness class. Scope is intentionally restricted to supported finite witness families.

**Keywords:** anti-classifier, descriptor fibers, recoverability, incompatibility, finite witness classes, branch-limited invariants

## 1. Scope and Placement

This branch is a quantitative extraction layer under the restricted-linear and fiber no-go program. It is not a universal theory and is not a replacement for core projector/recoverability branches.

## 2. Setup

Let `W` be a finite witness set with exactness verdict `v: W -> {0,1}` and descriptor map `a: W -> A`.
For each descriptor value `alpha in im(a)`, define:

- `E_alpha = |{w in W : a(w)=alpha, v(w)=1}|`
- `F_alpha = |{w in W : a(w)=alpha, v(w)=0}|`

The preimage `a^{-1}(alpha)` is a descriptor fiber.

## 3. Theorem 1 (Descriptor-Fiber Purity)

A perfect deterministic descriptor-only classifier `h: A -> {0,1}` satisfying `h(a(w))=v(w)` for all `w in W` exists iff every descriptor fiber is verdict-pure:

- for each `alpha`, either `E_alpha=0` or `F_alpha=0`.

### Proof sketch

Necessity: if `h` is exact, all witnesses with same descriptor must share a label.  
Sufficiency: if every fiber is pure, assign the unique fiber label to `h(alpha)`.

## 4. Theorem 2 (Irreducible Descriptor-Only Error)

Define:

- `IDELB(a;W) = (sum_alpha min(E_alpha,F_alpha))/|W|`

For any deterministic descriptor-only classifier `h: A -> {0,1}`:

- `Err_W(h) >= IDELB(a;W)`.

Majority vote on each fiber attains this bound.

### Corollary

If any descriptor fiber is mixed (`E_alpha>0` and `F_alpha>0`), perfect descriptor-only classification is impossible on `W`.

## 5. Quantitative Invariants

Define:

- `DFMI(a;W) = |{alpha : E_alpha>0 and F_alpha>0}| / |im(a)|`
- `CL(b|a;W) = IDELB(a;W) - IDELB((a,b);W)`

`CL` measures reduction in irreducible descriptor-only error after adding compatibility descriptor `b`.

## 6. Supported Witness Results

Computed from:
- `data/generated/unified-recoverability/rank_only_classifier_witnesses.csv`
- `data/generated/unified-recoverability/candidate_library_budget_witnesses.csv`

Summaries:
- `data/generated/descriptor-fiber-anti-classifier/meta_classifier_invariants.csv`
- `data/generated/descriptor-fiber-anti-classifier/meta_classifier_invariants.json`

Observed on current witness suites:
1. Rank tuple descriptor: `DFMI=1.0`, `IDELB=0.5`.
2. Budget tuple descriptor: `DFMI=1.0`, `IDELB≈0.2857`.
3. Rank + row-space proxy: `IDELB=0` on tested rank witness class, giving positive `CL`.

## 7. Status

- Mathematical status: `PROVED ON SUPPORTED FAMILY` (finite witness classes).
- Computational status: `VALIDATED` on generated artifacts.
- Promotion status: branch-limited quantitative layer, not universal branch core.

## 8. Limits

1. Finite witness classes only.
2. No unrestricted continuous theorem is claimed here.
3. No universal branch transfer law is claimed.
4. The layer quantifies known anti-classifier structure; it does not replace branch-level exactness theorems.

## 9. Relation to the OCP Spine

This paper strengthens anti-classifier diagnostics in a scoped way:
- consistent with `OCP-049`, `OCP-050`, `OCP-052`, `OCP-053`;
- useful for classifying descriptor insufficiency and compatibility gain;
- kept branch-limited by design.
