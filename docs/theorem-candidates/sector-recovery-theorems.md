# Sector Recovery Theorems

## Plain-Language Summary

The exact sector branch is the strongest way to move beyond the simple projector theorem without drifting into vague analogy.

This file formalizes what the QEC anchor has been showing operationally: if a protected space is embedded into pairwise orthogonal disturbance sectors, then a single sector-conditioned recovery architecture can map every such disturbed sector back to the protected space exactly.

It also records the sharp failure mode: once sector overlap appears, unique exact sector detection collapses.

## Theorem OCP-T5: Exact Recovery For Pairwise Orthogonal Sector Embeddings

Let `H` be a finite-dimensional real or complex inner-product space and let `S ⊂ H` be a protected `k`-dimensional subspace with ordered basis matrix

```text
B_S ∈ H^{n×k}
```

of full column rank.

Let `D_1, ..., D_m ⊂ H` be `k`-dimensional pairwise orthogonal sector subspaces with full-rank ordered basis matrices

```text
B_i ∈ H^{n×k},   i = 1, ..., m.
```

Assume the basis matrices are coordinate-compatible with `B_S`, meaning that a coefficient vector `c ∈ F^k` represents the protected state `B_S c` and the disturbed sector state `B_i c` in sector `D_i`.

Let `Q_i` denote the orthogonal projector onto `D_i`, and define the sector-conditioned recovery operator

```text
R = Σ_i B_S B_i^{+} Q_i,
```

where `B_i^{+}` is the Moore-Penrose pseudoinverse.

Then for every `i` and every `c ∈ F^k` one has

```text
R(B_i c) = B_S c.
```

So the sector family admits an exact OCP recovery architecture.

### Proof Sketch

Because `B_i` has full column rank,

```text
B_i^{+} B_i = I_k.
```

Because the sector subspaces are pairwise orthogonal,

```text
Q_j(B_i c) = 0   for j ≠ i,
Q_i(B_i c) = B_i c.
```

Therefore

```text
R(B_i c)
= Σ_j B_S B_j^{+} Q_j(B_i c)
= B_S B_i^{+} B_i c
= B_S c.
```

That is exact recovery on each sector.

## Corollary OCP-C4: QEC Sector Recovery Fits The Exact Sector Branch

For the 3-qubit bit-flip code with correctable sector family

```text
C, X_1 C, X_2 C, X_3 C,
```

the repository's sector-recovery operator is an instance of OCP-T5.

This corollary is not a new QEC theorem. Its value is that it gives the OCP program a finished exact sector branch with an explicit operator formula rather than only a verbal bridge.

## Proposition OCP-P5: Exact Sector Recovery Needs Coordinate-Compatible Embeddings

The theorem above is not basis-free in a naive sense. Exact recovery requires that each sector carry the protected coefficients in a compatible way.

This is why the sector branch is naturally phrased either through:
- isometric embeddings `U_i : S -> D_i`, or
- ordered basis matrices with aligned protected coordinates.

Without that structure, one cannot even state what it means to recover the same protected state from different sectors.

## Why This Matters

This theorem materially strengthens the repository because it does three things at once:
- it upgrades the QEC bridge from analogy to a genuine exact OCP theorem branch,
- it supplies an explicit operator construction that other researchers can reuse,
- and it clarifies that exact sector recovery is a real alternative to the single-projector exact branch.

## Executable Support

- `src/ocp/sectors.py`
- `tests/math/test_sector_recovery.py`
- `src/ocp/qec.py`
