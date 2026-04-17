# Legacy Exploratory Note (Superseded by Descriptor-Fiber Anti-Classifier Branch Paper)

Canonical active version:
- `papers/descriptor-fiber-anti-classifier-branch.md`

---

# Descriptor-Fiber Anti-Classifier Bounds: A Quantitative Extraction from Structure-Dependent Recoverability

Steven Reid  
Independent Researcher  
ORCID: 0009-0003-9132-3410  
sreid1118@gmail.com  
April 2026

## Abstract

This note extracts a concrete mathematical addition from the recent meta-theory layer. The broad statement “compatibility matters more than amount” is mostly interpretive unless converted into explicit objects. We do that by introducing descriptor-fiber quantities for finite witness classes: (i) a purity criterion that characterizes when descriptor-only exact classification is possible, and (ii) an irreducible descriptor-only error lower bound. These yield computable invariants: descriptor-fiber mixedness (`DFMI`), irreducible descriptor error lower bound (`IDELB`), and compatibility lift (`CL`). We evaluate them on existing OCP witness datasets. Rank-only descriptors attain `DFMI=1` and `IDELB=0.5`, budget-only descriptors attain `DFMI=1` and `IDELB≈0.2857`, while adding a row-space compatibility proxy yields `IDELB=0` on the same rank witness class (`CL=0.5`). The result is branch-limited and finite-class in proof scope; no universal cross-physics claim is made.

**Keywords:** anti-classifier, recoverability, descriptor fibers, incompatibility, lower bound, branch-limited invariants

## 1. Setup

Let `W` be a finite witness set of systems with exactness verdict
`v: W -> {0,1}`.

Let `a: W -> A` be a descriptor map (e.g., rank tuple, count/budget tuple).
For `alpha in im(a)`, define:

- `E_alpha = |{w in W : a(w)=alpha, v(w)=1}|`,
- `F_alpha = |{w in W : a(w)=alpha, v(w)=0}|`.

Call `a^{-1}(alpha)` a descriptor fiber.

## 2. Main Theorem (Descriptor-Fiber Purity)

### Theorem 2.1

A perfect deterministic classifier `h: A -> {0,1}` with
`h(a(w)) = v(w)` for all `w in W` exists **iff** every descriptor fiber is verdict-pure, i.e. for each `alpha`, either `E_alpha=0` or `F_alpha=0`.

### Proof

- (`=>`) If perfect `h` exists, all `w` with same descriptor value `alpha` share verdict `h(alpha)`, so no fiber can contain both labels.
- (`<=`) If each fiber is pure, define `h(alpha)` as that fiber’s unique verdict; then `h(a(w))=v(w)` for all `w`.

QED.

### Corollary 2.2 (Anti-classifier witness rule)

If one descriptor fiber is mixed (`E_alpha>0` and `F_alpha>0`), no perfect descriptor-only classifier exists on `W`.

## 3. Quantitative Lower Bound

Define

`IDELB(a;W) = (sum_{alpha} min(E_alpha,F_alpha)) / |W|`.

Define

`DFMI(a;W) = |{alpha: E_alpha>0 and F_alpha>0}| / |im(a)|`.

### Theorem 3.1 (Irreducible descriptor-only error)

For any deterministic descriptor-only classifier `h: A -> {0,1}`,

`Err_W(h) >= IDELB(a;W)`.

The bound is attained by majority vote on each descriptor fiber.

### Proof

Within each fiber `a^{-1}(alpha)`, any constant label misclassifies at least the minority `min(E_alpha,F_alpha)`. Summing over fibers yields the lower bound. Majority vote achieves exactly that minority count per fiber.

QED.

## 4. Compatibility Lift

Given a refinement descriptor `b` (compatibility information), define

`CL(b|a;W)=IDELB(a;W)-IDELB((a,b);W)`.

Positive `CL` quantifies how much compatibility structure reduces unavoidable amount-only error.

## 5. Computed Examples (existing repo witness sets)

Source files:
- `data/generated/unified-recoverability/rank_only_classifier_witnesses.csv`
- `data/generated/unified-recoverability/candidate_library_budget_witnesses.csv`

Computed summary:
- `data/generated/meta-theory/meta_classifier_invariants.csv`
- `data/generated/meta-theory/meta_classifier_invariants.json`

### Example A: Rank tuple descriptor `a=(n,r,k)`

- `DFMI = 1.0`
- `IDELB = 0.5`
- best possible rank-only accuracy `<= 0.5`

Interpretation: in this witness class, every rank descriptor fiber is mixed exact/fail.

### Example B: Budget tuple descriptor `a=(n,r,selection,cost)`

- `DFMI = 1.0`
- `IDELB = 0.285714...`
- best possible descriptor-only accuracy `<= 0.714285...`

Interpretation: budget-only descriptors are also structurally mixed on this witness set.

### Example C: Add compatibility proxy `b = rowspace_residual_bin`

On the same rank witness class:
- `IDELB((a,b);W) = 0`
- `CL(b|a;W) = 0.5`

Interpretation: compatibility information removes the ambiguity present in amount-only descriptors for this witness set.

## 6. What This Adds Beyond Existing Branch Results

Existing theorems already prove specific anti-classifier failures (rank-only, budget-only) in supported classes. This note adds:

1. a descriptor-agnostic finite-class criterion (`Theorem 2.1`),
2. a quantitative irreducible error lower bound (`Theorem 3.1`),
3. cross-witness comparable invariants (`DFMI`, `IDELB`, `CL`).

This is a genuine extraction layer, not a new universal theorem of recoverability.

## 7. Limits

1. Theorems here are finite-class descriptor-classification statements; they do not replace branch PDE/continuous proofs.
2. `IDELB` is dataset/class dependent, not a universal physical constant.
3. This does not imply all branches share one descriptor set or one universal anti-classifier law.
4. No claim is made about universal GR/QM unification impossibility.

## 8. Relation to Current Repo Core

- Compatible with fiber/factorization exactness core.
- Compatible with no rank-only/no budget-only theorems.
- Provides a quantitative extraction layer for counterexample families already in the repo.
- Keeps branch-limited status discipline intact.

## 9. Conclusion

A mathematically real meta-level addition survives: descriptor-fiber anti-classifier bounds and invariants. The broad meta-theory language remains interpretive unless tied to these explicit objects. The extracted package is small, exact, and useful for classification pressure without universal overclaiming.
