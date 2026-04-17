# Open Problem Program

This branch now targets open problem classes that are clearly recognized outside the repo: inverse problems, identifiability, observability, sensor design, coarse observation, model mismatch, and PDE-side reconstruction.

## Near-term theorem candidates

### 1. Weighted-cost anti-classifier theorem
Plain language:
- can equal total sensing cost still hide opposite exactness verdicts?

Formal target:
- extend `OCP-050` from unit-cost candidate libraries to genuinely weighted libraries.

Outside relevance:
- sensor placement and measurement design almost never treat sensors as equal-cost in practice.

Current branch base:
- `OCP-050`, `OCP-052`.

Blocker:
- need a clean weighted family construction that does not collapse back to the unit-cost case.

### 2. Sensor-geometry theorem beyond coordinate witnesses
Plain language:
- geometry may beat amount, but can we state exactly how on a broader supported class?

Formal target:
- derive an exact classifier on a richer but still honest restricted sensor family using support/row-space geometry rather than raw count.

Outside relevance:
- observability and sensor design.

### 3. Stronger family-enlargement theorem on PDE-style benchmark families
Plain language:
- can the family-enlargement false-positive theorem be lifted from abstract restricted-linear families to a clearer PDE-side exact/no-go statement?

Formal target:
- an exact enlargement theorem on one supported modal or bounded-domain class.

## Medium-term branch-defining problems

### 4. Restricted nonlinear fiber-compatibility theorem or theorem-failure
Plain language:
- does any narrow nonlinear class keep a usable analog of the restricted-linear exactness criterion?

Outside relevance:
- inverse problems and identifiability beyond linear models.

Progress criterion:
- either one real theorem on a narrow nonlinear class,
- or a sharp theorem-failure showing why the current linear factorization machinery breaks.

### 5. Bounded-domain recoverability boundary theorem
Plain language:
- where exactly does bounded-domain recoverability survive, and where does projector mismatch inevitably kill it?

Outside relevance:
- PDE observation, inverse problems, and architecture-sensitive reconstruction.

### 6. Exact versus asymptotic observer/coarsening equivalence on one restricted class
Plain language:
- can exact recovery, coarsened detectability, and asymptotic observer convergence be related by one theorem on a nontrivial class?

## Long-shot but academically real problems

### 7. Partial-boundary data fiber hierarchies for PDE inverse problems
Plain language:
- characterize target-constant versus target-mixed fibers under partial boundary measurements.

Why it matters outside the repo:
- boundary control, PDE inverse problems, and partial data uniqueness.

### 8. Stability and false-positive certification under discretization refinement
Plain language:
- when does discretization refinement preserve exact claims, and when does it expose hidden collisions?

Current branch base:
- periodic refinement false-positive witness.

### 9. Model-class dependence and robust exactness
Plain language:
- which exact recoverability claims survive nearby family misspecification, and which are structurally brittle?

Current branch base:
- restricted-linear model-mismatch stress report.
