# Positive Framework Equation Candidates

Status: theorem-first equation extraction for positive architecture lane.

## PE-1 Shared Decoder Lift Equation

Equation:
`A d = b`, where `A=[M_1^T;...;M_k^T]`, `b=[L;...;L]` (vectorized by target rows).

Interpretation:
- solvability equivalent to shared exact recoverability.

Status:
- `PROVED ON RESTRICTED CLASS`
- `KNOWN / REFRAMED`.

## PE-2 Agreement-Lift Inclusion Equation

Equation:
`row(L) subseteq row(G)`.

Interpretation:
- architecture criterion for positive exactness.

Status:
- `PROVED ON RESTRICTED CLASS`
- `KNOWN / REFRAMED`.

## PE-3 Free Completion Equation

Equation:
`r_free^* = rank([G;L]) - rank(G)`.

Interpretation:
- minimal free augmentation size.

Status:
- `PROVED ON RESTRICTED CLASS`
- `PLAUSIBLY DISTINCT` as branch-limited repair law packaging.

## PE-4 Constrained Completion Equation

Equation:
`delta_C = rank([G;C;L]) - rank([G;C])`.

Interpretation:
- `delta_C = 0` iff full-library constrained completion feasible.

Status:
- `PROVED ON RESTRICTED CLASS`
- `PLAUSIBLY DISTINCT` constrained-design certificate.

## PE-5 Descriptor-Lift Separation Equation (Finite Family)

Equation-style rule:
Two systems with same amount descriptor are separated by lift tuple if
`(CID_1, r_1, delta_{C,1}) != (CID_2, r_2, delta_{C,2})`.

Status:
- `PROVED ON SUPPORTED FAMILY` (finite generated families)
- `CONDITIONAL` as general theorem.

## Equation verdict

Best pushable equations:
1. `PE-3` free completion,
2. `PE-4` constrained completion defect,
3. `PE-1/PE-2` as canonical backbone equations.

No universal equation beyond restricted class should be claimed.
