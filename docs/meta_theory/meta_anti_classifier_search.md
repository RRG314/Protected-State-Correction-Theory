# Meta Anti-Classifier Search

Date: 2026-04-17
Pass: Meta-theory extraction

## Objective

Extract the weakest abstract conditions under which amount-only classifiers must fail, then test those conditions against major branches.

## Candidate theorem MAC-1: Descriptor-Fiber Purity Criterion

### Strongest form

For any branch class `C`, amount-only descriptors cannot exactly classify recoverability.

### Weaker form (proved)

Let `C` be a class with exactness verdict `v: C -> {0,1}` and descriptor `a: C -> A`.
A perfect classifier `h: A -> {0,1}` exists **iff** every descriptor fiber `a^{-1}(alpha)` is verdict-pure.

### Proof

- If `h` exists, all systems with same `alpha` share verdict `h(alpha)`, so fibers are pure.
- If all fibers are pure, define `h(alpha)` as the common verdict on that fiber.

### Status

`PROVED` (set-theoretic, branch-agnostic theorem).

---

## Candidate theorem MAC-2: Irreducible Amount-Only Error Bound

### Strongest form

Any amount-only classifier has a nonzero error floor whenever compatibility varies.

### Weaker form (proved on finite witness classes)

For finite witness class `W` and descriptor `a`, any deterministic classifier `h(a)` has

`Err_W(h) >= IDELB(a;W) = (sum_alpha min(E_alpha,F_alpha))/|W|`.

### Status

`PROVED ON SUPPORTED FAMILY` (finite witness classes).

---

## Candidate theorem MAC-3: Compatibility-Separated Same-Amount Opposite Verdict

### Strongest form

Across all branches, if two systems share amount descriptor but have different compatibility invariant, their exactness verdicts must differ.

### Weaker form

Existence theorem: if there exist two systems with same amount descriptor and opposite verdict, amount-only exact classification fails on that class (immediate corollary of MAC-1).

### Counterexample pressure

The strong form is false in general: compatibility differences need not always flip verdicts unless compatibility metric is complete and calibrated.

### Status

- strongest form: `REJECTED`
- weaker existence corollary: `PROVED`

## Branch tests

| Branch | Same-amount opposite-verdict evidence | MAC-1 applicability | MAC-2 applicability | Notes |
| --- | --- | --- | --- | --- |
| Restricted-linear OCP | theorem-backed (`OCP-047`, `OCP-049`, `OCP-050`) | strong | strong | canonical support branch |
| Bounded-domain / architecture mismatch | yes for architecture-transplant style witnesses, but amount descriptor not canonical | conditional | conditional | requires careful descriptor definition |
| Restricted soliton quotient | validated same-count opposite-verdict witness sets | restricted | restricted | continuous promotion remains open |
| MHD supported families | amount descriptor is not natural primary object | weak | weak | better treated as compatibility-classification, not amount classification |

## Extracted theorem package

Promote:
1. `MAC-1` descriptor-fiber purity criterion (`PROVED`),
2. `MAC-2` irreducible descriptor-only error bound (`PROVED ON SUPPORTED FAMILY`),
3. witness-corollary anti-classifier no-go (`PROVED` once witness exists).

Do not promote:
- universal same-amount opposite-verdict theorem across all branch types.
