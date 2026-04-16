# Field Conventions Report

## Scope
This note synthesizes conventions from representative outlets and papers in three lanes:
- applied math/control/inverse-problem-adjacent (for the OCP core paper),
- MHD/plasma/applied PDE (for the MHD paper),
- CFD/projection/Helmholtz-Hodge structure (for the bridge paper).

The goal is not to imitate one journal template verbatim; it is to produce reviewer-familiar structure and emphasis.

## Sources Consulted

### Control / inverse / observability lane
1. SIAM Journal on Control and Optimization (SICON) scope page
   - https://www.siam.org/publications/siam-journals/siam-journal-on-control-and-optimization/
2. SIAM style manual (top matter, key words, theorem/proof style)
   - https://www.siam.org/media/hmbhpgm1/stylemanual-1.pdf
3. Inverse Problems (IOP) article requirements
   - https://publishingsupport.iopscience.iop.org/journals/inverse-problems/about-inverse-problems/
4. Functional observability + sensor placement theorem-heavy sample
   - https://arxiv.org/abs/2307.08923
5. Efficient constrained sensor placement theorem-heavy sample
   - https://arxiv.org/abs/1711.08264

### MHD / plasma lane
1. Journal of Plasma Physics author instructions (notation discipline)
   - https://www.cambridge.org/core/journals/journal-of-plasma-physics/information/author-instructions/preparing-your-materials
2. AIP author instructions (physics-writing constraints, concise manuscript expectations)
   - https://publishing.aip.org/resources/researchers/author-instructions/
3. Euler-potentials-in-resistive-context comparative sample
   - https://academic.oup.com/mnras/article/401/1/347/1006503

### CFD / projection lane
1. Journal of Fluid Mechanics author instructions (insight-first requirement)
   - https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/information/author-instructions
2. Journal of Fluid Mechanics preparation details (abstract/keywords conventions)
   - https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/information/author-instructions/preparing-your-materials
3. Projection-method computational paper sample (algorithm + numerical validation balance)
   - https://arxiv.org/abs/2304.14690
4. Helmholtz-Hodge decomposition theorem/computation sample
   - https://arxiv.org/abs/2603.27714

## Extracted Conventions By Field

## 1) OCP core paper (control / inverse / observability)

### Title style
- Precise claim-first titles are standard.
- Overly broad “unified theory” titles are disfavored unless scope is genuinely broad.

### Abstract style
- Compact theorem-and-consequence abstract (typically one paragraph).
- Include: setup, main theorem/no-go, and practical implication.
- Avoid long philosophy framing.

### Body structure
- Introduction with explicit problem class and contribution bullets.
- Formal setup + assumptions before theorem statements.
- Main theorem section with lemma/theorem/proposition numbering.
- Counterexample section is normal and often expected for impossibility claims.
- Discussion/limitations are explicit when scope is restricted.

### Proof placement
- Core proof ideas in main text; technical expansions in appendix.

### Numerical expectation
- For linear-theorem papers, small explicit constructions and stress checks are sufficient.
- Numerical experiments should validate claims; they do not replace proofs.

### Related work norms
- Dedicated related-work section or compact review paragraph in introduction is common.

## 2) MHD paper (plasma / applied PDE)

### Title style
- Problem-and-regime specific titles are common (e.g., exactness/obstruction under stated coefficient/domain assumptions).

### Abstract style
- Physics-facing but mathematically precise.
- State PDE/model assumptions, what is proved, and what is only validated numerically/symbolically.

### Body structure
- Governing equation and notation first.
- Derivation sections separated from interpretation sections.
- Domain/boundary assumptions must be explicit.
- If symbolic tooling is used, keep it in verification or appendix role.

### Proof/derivation placement
- Closed-form derivations in main body when central.
- Algebraic detail can move to appendices.

### Numerical expectation
- Validation tables/plots are normal even for theory-heavy plasma papers.
- Must separate theorem statements from computational confirmation.

### Related work norms
- Usually integrated into introduction plus focused discussion where model choice matters.

## 3) Bridge paper (CFD projection / Helmholtz-Hodge)

### Title style
- Mechanism-forward titles are typical: method + failure/success condition.

### Abstract style
- Short and concrete: method class, success/failure contrast, mechanism, scope.

### Body structure
- Problem framing around projection architecture.
- Exact success case and failure case should be side-by-side.
- Mechanism section explaining why divergence reduction may fail for bounded classes.
- Comparison table is highly useful and reviewer-friendly.

### Proof vs computation
- Mathematical statements plus benchmark evidence are both expected.
- “Validated” should be used where theorem-level proof is unavailable.

### Limitations handling
- Explicit scope controls are expected in CFD journals; avoid universal claims.

## Cross-paper style decisions adopted in this pass
1. Single consistent author block and metadata style across all three papers.
2. Explicit status tags: `PROVED`, `VALIDATED`, `CONDITIONAL`, `OPEN`, `INTERPRETATION`.
3. One theorem-numbering convention per paper (`Theorem`, `Proposition`, `Corollary`, `Example`).
4. Explicit limitations section in each paper.
5. No hidden migration of validated-only claims into proved language.
