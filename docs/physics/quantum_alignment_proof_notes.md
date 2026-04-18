# Quantum Alignment Proof Notes

Status: proof notes for restricted-class quantum-alignment statements.

## 1) Restricted projective qubit identity (QA-T2)

Assumptions:
- Pure qubit family with Bloch vector `n(theta_1, theta_2)`.
- Tangent derivatives `d_k n = partial n / partial theta_k` are linearly independent.
- At the evaluation point, coordinates are chosen so `F_Q` is diagonal:
  - `F_Q,kk = ||d_k n||^2`,
  - `d_1 n orthogonal d_2 n`.
- Single projective measurement with axis `m` (`||m||=1`).

For a two-outcome projective measurement:
- `p_pm = (1 +/- n·m)/2`.
- `partial_k p_pm = +/- (d_k n · m)/2`.
- Therefore
  - `F_M,kk = (d_k n · m)^2 / (1 - (n·m)^2)`.

Hence
- `alpha_k^2 = F_M,kk/F_Q,kk = ((d_k n · m)^2)/(||d_k n||^2 (1-(n·m)^2))`.

Let
- `e_1 = d_1 n / ||d_1 n||`,
- `e_2 = d_2 n / ||d_2 n||`.

Then `{e_1, e_2, n}` is orthonormal. Decompose
- `m = m_1 e_1 + m_2 e_2 + m_3 n`, with `m_1^2 + m_2^2 + m_3^2 = 1`.

Now
- `alpha_1^2 = m_1^2 / (1-m_3^2)`,
- `alpha_2^2 = m_2^2 / (1-m_3^2)`.

So
- `alpha_1^2 + alpha_2^2 = (m_1^2 + m_2^2)/(1-m_3^2) = 1`.

QED on the declared class.

## 2) Coordinate-invariant trace form (QA-T3)

With parameter vector `theta` and `2x2` matrices:
- `F_Q,ij = d_i n · d_j n`,
- `F_M,ij = (d_i n·m)(d_j n·m)/(1-(n·m)^2)`.

Define tangent projection of `m`:
- `m_T = m - (n·m) n`.

Then `F_M` is the pullback of rank-1 tensor `(m_T m_T^T)/(1-(n·m)^2)` to parameter coordinates. Since `||m_T||^2 = 1-(n·m)^2`, the induced trace on the two-dimensional tangent metric equals `1`:
- `trace(F_Q^{-1} F_M) = 1`.

This expression is coordinate-invariant.

## 3) Rank-1 qubit POVM extension (QA-T4)

Rank-1 qubit POVM form:
- `E_a = (w_a/2)(I + v_a·sigma)`, with `||v_a||=1`, `w_a > 0`,
- completeness gives `sum_a w_a = 2` and `sum_a w_a v_a = 0`.

For pure qubit state Bloch vector `n`:
- `p_a = Tr(rho E_a) = (w_a/2)(1+n·v_a)`.
- `partial_i p_a = (w_a/2)(d_i n · v_a)`.

So
- `F_M,ij = sum_a [w_a (d_i n·v_a)(d_j n·v_a)]/[2(1+n·v_a)]`.

Define operator
- `G = sum_a [w_a/(2(1+n·v_a))] v_a v_a^T`.

Then `F_M` is tangent pullback of `G`. Therefore
- `trace(F_Q^{-1}F_M) = trace(P_T G)`, where `P_T = I - nn^T`.

Compute:
- `trace(P_T G)`
- `= sum_a [w_a/(2(1+n·v_a))] (1-(n·v_a)^2)`
- `= sum_a [w_a(1-n·v_a)]/2`
- `= (1/2)(sum_a w_a - n·sum_a w_a v_a)`
- `= (1/2)(2-0) = 1`.

QED on the rank-1 qubit POVM class.

## 4) Balanced corollary (QA-C1)

From `alpha_1^2 + alpha_2^2 = 1`, maximize `min(alpha_1, alpha_2)`.
The optimum is at `alpha_1 = alpha_2`, giving
- `alpha_1 = alpha_2 = 1/sqrt(2)`.

This is attained by choosing `m` with equal tangent components and zero normal component.

## 5) Notes on limits and singular points

At points where `p_a=0` and `partial p_a=0`, direct ratio formulas show `0/0`. The statements above use the analytic limit value; they do not treat that as information loss.

