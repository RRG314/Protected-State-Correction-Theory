# Divergence Cleaning in OCP Language

Projection-based divergence cleaning gives the cleanest continuous exact example in this repository.

On compatible domains, write `B = B_df + ∇φ` with `div(B_df)=0`. The correction map

$$
R(B)=P_{df}B=B-\nabla\Delta^{-1}(\operatorname{div}B)
$$

recovers the protected divergence-free component exactly. In branch terms, `B_df` is protected structure and `∇φ` is removable disturbance.

The value of this example is that all objects are explicit: protected class, disturbance class, decomposition, and correction operator. That makes it a genuine exact anchor, not a loose analogy.

Repository tests verify divergence reduction and recovery consistency on declared families.
