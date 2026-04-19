# Equation Candidates

Status: equation-form discovery with reduction/falsification tags.

## E1. Context-Lifted Shared Decoder Equation (CLE)

Equation:
`A d = b`, with
`A=[M_1^T;...;M_k^T]`, `b=[t;...;t]`.

Claim tested:
- solvability of CLE is equivalent to context-invariant exactness.

Result:
- equivalence holds in supported linear class.

Status:
- `PROVED` (equivalence in declared class).
- novelty: `REDUCES TO EXISTING OCP LOGIC`.

## E2. Defect Equation (Minimax Form)

Equation:
`CID(F,t)=min_d max_c ||d M_c - t||_2`.

Claim tested:
- `CID=0` iff CLE solvable.

Result:
- holds by construction in linear class.

Status:
- `PROVED` equivalence.
- novelty: `REDUCES TO EXISTING OCP LOGIC`.

## E3. Augmentation Feasibility Equation

Equation family:
Find minimal `r` and `U` in admissible class `A` such that
`exists d: d [M_c;U] = t` for all `c`.

Claim tested:
- positive minimal threshold appears on local-exact/global-fail families.

Result:
- `PROVED ON SUPPORTED FAMILY` (threshold existence) in declared augmentation search class.

Limits:
- exact closed-form law for `r_*` still `OPEN`.

Novelty:
- `PLAUSIBLY DISTINCT` scoped threshold equation package.

## E4. Domain-Geometry Split Equation (CFD-facing)

Equation idea:
Descriptor-matched measurement equations can remain solvable/unsolvable depending on geometry/domain-tagged observation operators.

Result:
- supported by branch witness results, but this pass does not derive one new closed universal equation.

Status:
- `PROVED ON SUPPORTED FAMILY` as branch theorem class,
- `OPEN` for broader equation law.

## E5. Variable-Resistivity Closure Equation (MHD)

Equation idea:
Exactness in supported MHD classes imposed by closure remainder equations/ODE constraints (e.g., annular survivors).

Result:
- branch equations already proved in restricted classes (`papers/mhd_paper_upgraded.md`).

Status:
- `PROVED ON SUPPORTED FAMILY`.
- novelty: `PLAUSIBLY DISTINCT` in branch scope.

## E6. Candidate-Library Defect Equation (Constrained Augmentation)

Equation:
`delta_C = rank([G; C; L]) - rank([G; C])`, where `G` is agreement-lifted observation.

Claim tested:
- `delta_C = 0` iff full-library constrained exact shared recovery is feasible.

Result:
- holds in supported finite linear class.

Status:
- `PROVED ON RESTRICTED CLASS`.

Limits:
- scoped to finite linear families and declared candidate libraries.
- not a universal novelty claim beyond rank-inclusion logic.

## Equation Discovery Verdict

- Best equation-level contribution is still scoped formalization, now including constrained-library defect feasibility (`delta_C`) in addition to CLE and augmentation equations.
- New universal equation did not survive.
