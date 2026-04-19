# Soliton Branch Stress Test Report

Date: 2026-04-17

## Stress Test Scope

Two stress axes were applied:
- internal OCP stress (does the branch genuinely match OCP structure?),
- external literature stress (does the branch collapse into known facts without added value?).

## A. Internal OCP Stress

### A1. Symmetry handling stress

Question: does the branch look nontrivial only because symmetry quotienting is mishandled?

Result: survives. Raw collisions split cleanly into symmetry-orbit collisions vs true non-identifiability. The branch would be misleading without quotienting, but with quotienting the retained failures remain real.

### A2. Same-count failure stress

Question: does same-count opposite verdict disappear under explicit witness extraction?

Result: survives on tested family. For Family B with `obs_dim=4`, `local_complex_2` has zero true non-identifiable pairs while `local_magnitude_4` has `145152`.

### A3. Projection-preservation analogy stress

Question: is projection lane merely numerical noise?

Result: restricted survival. On single-soliton states, `lowpass_k18pct` is near-exact while `subsample_interp_x8` fails strongly; both fail on collision-state relative to one-soliton manifold, which is expected and correctly labeled.

### Internal stress conclusion

Internal OCP parallels survive only as restricted analogues. Broad transfer claims fail.

## B. External Literature Stress

### B1. “Just inverse scattering” stress

Result: partial collapse avoided only because branch target is constrained finite observation families rather than full scattering data.

### B2. “Just Jacobian rank” stress

Result: branch adds global collision witness sets and same-count opposite-verdict examples, not just local rank diagnostics.

### B3. Grid dependence stress

Result: major limitation remains. Most positive identifiability claims are finite-grid exhaustive and not yet continuous theorems.

### B4. “Already covered by known projection numerics” stress

Result: mostly known direction; branch value is scoped benchmark curation and explicit no-go split, not foundational numerical novelty.

### External stress conclusion

Branch survives as a **restricted integration candidate** but not as a novel standalone theorem package yet.

## Stress-Test Final Verdict

- Admit as conditional OCP candidate branch.
- Keep heavy status labeling.
- Require theorem upgrades before any promotion beyond candidate status.
