# Central Theorem Candidate

## Plain-Language Summary

The strongest exact theorem in the current repository is intentionally modest: it is the theorem that turns the OCP slogan into a real mathematical correction statement.

It is not yet a deep new cross-domain theorem. But it is the exact backbone everything else relies on.

## Theorem OCP-T1: Exact Protected-Subspace Recovery

Let `H` be a finite-dimensional inner-product space or Hilbert space. Let `S` and `D` be closed subspaces such that

```text
H = S ⊕ D,   S ⟂ D.
```

Let `P_S` denote the orthogonal projector onto `S`.

Then for every `x in H` written uniquely as `x = s + d` with `s in S` and `d in D`,

```text
P_S x = s.
```

Equivalently, `P_S` fixes the protected subspace and annihilates the disturbance space:

```text
P_S|_S = I_S,   P_S|_D = 0.
```

Therefore `P_S` is an exact OCP recovery operator on `(S,D)`.

## Proof

Since `H = S ⊕ D`, every `x in H` has a unique decomposition `x = s + d`.

Because `P_S` is the orthogonal projector onto `S`, it acts as the identity on `S` and as zero on `S^⊥`. Since `D ⊂ S^⊥` by orthogonality, we have

```text
P_S x = P_S(s+d) = P_S s + P_S d = s + 0 = s.
```

That proves exact recovery.

## Corollary OCP-C1: Uniqueness Among Linear Recoveries

Under the same assumptions, any linear operator `R` satisfying

```text
R|_S = I_S,   R|_D = 0
```

must agree with `P_S` on `H = S ⊕ D`.

So, in the orthogonal exact branch, the exact recovery operator is uniquely determined by the protected/disturbance split.

## Why This Theorem Matters

This theorem does three things for the repository:
- it gives a precise exact notion of protected-state correction,
- it makes the no-go results meaningful,
- and it provides the finite-dimensional template from which the continuous projection example is understood.

## Status

- Status: `THEOREM`
- Strength: exact, simple, foundational
- Limitation: mathematically elementary; strongest as a backbone rather than as a novelty claim
