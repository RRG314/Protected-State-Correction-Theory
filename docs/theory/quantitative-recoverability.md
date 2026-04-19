# Quantitative Recoverability Layer

## Scope

This layer extends binary exact/impossible outputs with computable quantities for restricted-linear and validated finite families. It is operator-first and branch-scoped.

Primary implementation and artifacts:
- [`src/ocp/next_phase.py`](../../src/ocp/next_phase.py)
- [`data/generated/next-phase/next_phase_summary.json`](../../data/generated/next-phase/next_phase_summary.json)
- [`data/generated/next-phase/quantitative_profiles.csv`](../../data/generated/next-phase/quantitative_profiles.csv)

## Candidate Quantities

Let `O` be observation map, `L` protected target map, and `F` admissible family basis.

- `r_row(O,L;F)`: row-space residual (`restricted_linear_rowspace_residual`).
- `r_norm(O,L;F)`: normalized row-space defect (`normalized_rowspace_defect`).
- `theta_def(O,L;F)`: principal-angle defect (`principal_angle_defect`), equal to `sin(theta_max)`.
- `gamma(O,L;F)`: collision gap (`restricted_linear_collision_gap`) on bounded coefficient boxes.
- `delta(O,L;F)`: unrestricted minimal augmentation count (`linear_recoverability_design_report`).
- `||D||_2`: decoder operator norm upper bound when exact decoder exists.

## Candidate Assessment

| Candidate | Intended meaning | Status | Survived use |
| --- | --- | --- | --- |
| `r_row` | direct inclusion defect `row(LF) ⊆ row(OF)` | `PROVED` (restricted-linear) | strongest exactness defect quantity |
| `theta_def` | geometric alignment defect | `PROVED` (restricted-linear) | equivalent exactness criterion; useful for angle-style diagnostics |
| `r_norm` | scale-normalized defect | `PROVED` (restricted-linear) | comparable across families with different target scale |
| `gamma` | protected collision severity at equal records | `PROVED` (validated finite/restricted families) | lower-bound and anti-classifier witness quantity |
| `delta` | minimal repair amount | `PROVED` (restricted-linear) | constructive design law (`OCP-045`) |
| single universal scalar `q` across all branches | one-number global theory | `DISPROVED` | fails under rank-only/budget-only/family-enlargement counterexamples (`OCP-049`, `OCP-050`, `OCP-052`) |

## Surviving Theorem-Grade Statements

### QR-1: Exactness equivalence via row-space or principal-angle defect
Status: `PROVED` (restricted-linear family).

For fixed `F`, exact recoverability is equivalent to `r_row(O,L;F)=0`. In the same class this is equivalent to `theta_def(O,L;F)=0`.

Notes:
- this is a repo framing of standard row-space/subspace-angle facts ([Kato 1995], [Bjork-Golub 1973], [Davis-Kahan 1970]);
- repo contribution is executable branch-coupled criterion packaging.

### QR-2: Same-rank insufficiency survives quantitative strengthening
Status: `PROVED` (`OCP-047`, `OCP-049`).

Same observation rank can yield opposite exactness verdicts; quantitative defects (`r_row`, `theta_def`, `gamma`, `delta`) separate them.

### QR-3: Exact-but-fragile vs robust-exact split
Status: `VALIDATED` with canonical witness family.

Exact cases with full coefficient rank (`rank(OF)=dim(F)`) remain robust under tested perturbations; exact rank-deficient aligned cases can fail at arbitrarily small perturbations.

## Falsification Results Kept

- No universal scalar `q` promoted.
- Rank-only and budget-only classifier programs remain rejected.
- Collision-gap-only ranking is not a full substitute for row-space defect and augmentation deficiency.

## Benchmarked Witness Table

Canonical quantitative profiles from [`quantitative_profiles.csv`](../../data/generated/next-phase/quantitative_profiles.csv):

| Case | Exact | `r_row` | `theta_def` | `gamma` | `delta` | Class |
| --- | --- | --- | --- | --- | --- | --- |
| robust-full-information | yes | `0` | `0` | `0` | `0` | robust exact |
| exact-but-fragile | yes | `0` | `0` | `0` | `0` | aligned exact but fragile |
| augmentation-repairable | no | `0.7071` | `0.7071` | `2` | `1` | repairable misaligned |
| collision-dominated witness | no | `1` | `1` | `2` | `1` | repairable misaligned |

## Novelty Triage

- likely literature-known: row-space inclusion criterion, principal-angle perturbation background.
- repo framing of known facts: executable quantitative profile package combining `r_row`, `theta_def`, `gamma`, `delta`.
- plausibly literature-distinct: integrated anti-classifier + augmentation + mismatch benchmarking bundle attached to one theorem/no-go registry.

## References

- [core-references.md](../references/core-references.md)
- [protected-state-correction.bib](../references/protected-state-correction.bib)
