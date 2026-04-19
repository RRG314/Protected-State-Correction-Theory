# Structural Information Theory Completion Report (Comprehensive)

Date: 2026-04-19  
Workspace: `/Users/stevenreid/Documents/New project`  
Primary artifacts: `/Users/stevenreid/Documents/New project/data/generated/theory_completion/*`

## 0) Scope, Method, Nonclaims

This report is theorem-first and falsification-first. It is built from executable audit and validation artifacts, not from narrative synthesis alone.

Nonclaims enforced:
- No claim that gravity is made of information.
- No new force/interaction claim.
- No universal scalar invariant claim.
- No toy-only promotion (toy families used only as sanity checks).

Status labels used exactly:
- PROVED
- VALIDATED
- CONDITIONAL
- OPEN
- DISPROVED
- ANALOGY ONLY

## 1) Evidence Base Used

Audit/validation was computed by:
- `/Users/stevenreid/Documents/New project/scripts/experiments/run_structural_theory_completion.py`

Generated outputs used in this report:
- `/Users/stevenreid/Documents/New project/data/generated/theory_completion/audit_claims.csv`
- `/Users/stevenreid/Documents/New project/data/generated/theory_completion/dependency_edges.csv`
- `/Users/stevenreid/Documents/New project/data/generated/theory_completion/missing_pieces_map.csv`
- `/Users/stevenreid/Documents/New project/data/generated/theory_completion/structural_metric_ablation.csv`
- `/Users/stevenreid/Documents/New project/data/generated/theory_completion/witness_catalog.csv`
- `/Users/stevenreid/Documents/New project/data/generated/theory_completion/object_candidate_comparison.csv`
- `/Users/stevenreid/Documents/New project/data/generated/theory_completion/theorem_status_map.csv`
- `/Users/stevenreid/Documents/New project/data/generated/theory_completion/failure_catalog.csv`
- `/Users/stevenreid/Documents/New project/data/generated/theory_completion/physics_translation_map.csv`
- `/Users/stevenreid/Documents/New project/data/generated/theory_completion/theory_completion_summary.json`

Upstream branch artifacts consumed by the audit:
- OCP claim registry and unified-recoverability witnesses
- MHD theorem proof-status map
- gravity recoverability theorem checks/killer pass
- information-research high-pressure summary (including SPARC hidden-inference lane)
- internal cross-program theorem boundary memos

## 2) Direct Answers to the Main Questions

### Q1. What exact positive-theory pieces were already present but scattered?

Already present and mathematically active:
- `fiber_factorization` exactness core (PROVED): factorization/fiber-constancy criterion.
- `operator_alignment` restricted-linear bridge (PROVED): row-space/kernel compatibility form.
- `target_hierarchy` split (PROVED): same record can recover coarser target while failing finer target.
- `augmentation` law (PROVED): compatibility-aligned augmentation can repair recoverability.
- `family_fragility` (PROVED): enlargement can create false positives.
- `model_mismatch` instability (PROVED): decoder transfer can fail despite similar descriptor budgets.
- `amount_no_go` package (PROVED): rank/budget/amount-only exact classifiers fail on declared witness classes.
- `closure_obstruction` package (PROVED/VALIDATED): boundary/domain/closure compatibility governs exactness.

Cross-source claim inventory (83 total):
- PROVED: 55
- VALIDATED: 6
- CONDITIONAL: 13
- OPEN: 1
- DISPROVED: 4
- ANALOGY ONLY: 4

### Q2. What exact pieces are still missing?

Missing-core table (all explicit in `missing_pieces_map.csv`):
- MP-1 Primitive structural object (explicit axioms): definitional gap.
- MP-2 Stability layer beyond exactness: theorem-grade gap.
- MP-3 Dynamic irreversibility/coarse-graining law: theorem-grade gap.
- MP-4 Quantification layer axioms (vector-valued): quantitative gap.
- MP-5 Physics translation theorem boundary: theorem+empirical gap.
- MP-6 Unified cross-domain reduction harness: empirical harness gap.
- MP-7 SDS formal boundary discipline: scope-control gap.

### Q3. Is “information as structure preserved under transformation” only reformulation?

Answer: not only reformulation, but also not universal closure yet.
- Core exactness statement is KNOWN/REFORMULATION-level in spirit, but here integrated with executable no-go/fragility/mismatch/closure packages.
- The strengthened package is branch-limited and empirically/theorem-supported in multiple lanes.
- Universal extension claims collapse under killer pass.

### Q4. Correct mathematical object in this framework?

Best current object: **Fiber-Quotient Structural Object (FQSO)**.

From candidate comparison:
- FQSO selection rank: `0.8444`
- coverage ratio: `0.8889`
- proved-axis hit ratio: `0.7778`
- tautology risk: low

Other candidates (partition-only, category-like, etc.) are weaker in proved-axis coverage.

### Q5. Cleanest positive definition surviving pressure

Let:
- admissible family `A`,
- hidden state `x in A`,
- record map `M: A -> Y`,
- target map `T: A -> Z`.

Define:
- record fibers `Pi_M = { M^{-1}(y) }`,
- target fibers `Pi_T = { T^{-1}(z) }`.

**Information for target T through record M on A** is the target-relevant distinction structure induced by the refinement relation between `Pi_M` and `Pi_T`, plus obstruction data where refinement fails.

Exact recoverability condition (core):
- `T` recoverable from `M` on `A` iff `Pi_M` refines `Pi_T` iff `T = R o M` for some decoder `R`.

Loss condition:
- loss exists iff there exist `x1, x2 in A` with `M(x1)=M(x2)` but `T(x1)!=T(x2)` (target-varying collisions).

### Q6. Strongest quantification layer compatible with no-go results

Do not use one scalar. Use structural profile vectors.

Promoted profile coordinates (branch-dependent):
- `IDELB`, `DFMI` (descriptor-fiber obstruction scale)
- `TFCD` (target-fiber impurity defect)
- `CD = 1 - I(T;Y)/I(X;Y)` (compatibility defect surrogate)
- `LID`/ambiguity volume proxies (hidden-state ambiguity)
- closure defect (`CDF`) and recoverability flow defects where applicable

### Q7. Dead ends to drop now

Drop/demote now:
- Universal scalar correction/information capacity claim: DISPROVED.
- Universal cross-domain version of gravity candidate: DISPROVED.
- Strict target-coarsening threshold ordering in tested Hawking surrogate: DISPROVED.
- SDS as theorem core: ANALOGY ONLY (keep as engineering layer).

### Q8. Restricted invariants worth continuing

Promising and currently surviving:
- Descriptor-fiber irreducible error bound (`IDELB`) as a no-go witness.
- Compatibility lift (`CL_abs`, `CL_rel`) for measuring improvement beyond amount-only descriptors.
- Compatibility-defect/recoverability-defect degradation trends in declared surrogate channels.

Scope: restricted classes only, not universal.

### Q9. What new definitions/theorems/experiments are needed next?

Highest-priority build steps:
- Formalize one typed primitive object with explicit axioms (MP-1).
- Prove stability theorem under perturbations (MP-2).
- Prove branch-limited semigroup-style monotonicity/threshold law for degradation (MP-3).
- Build explicit vector-axiom quantification layer (MP-4).
- Convert physics mappings from interpretation to theorem templates with assumptions/nonclaims (MP-5).

## 3) Dependency Map (What Depends on What)

From `dependency_edges.csv`:
- `fiber_factorization -> amount_no_go` (collision/indistinguishability yields impossibility).
- `fiber_factorization -> operator_alignment` (restricted-linear bridge).
- `operator_alignment -> augmentation` (deficiency drives minimal augmentation).
- `operator_alignment -> target_hierarchy` (same record, weaker/stronger split).
- `amount_no_go -> capacity_quantification` (IDELB/DFMI-style irreducible error quantification).
- `target_hierarchy -> family_fragility -> model_mismatch`.
- `closure_obstruction -> physics_translation`.
- `engineering_layer -> physics_translation` with explicit non-core boundary.

This is a coherent dependency DAG for a branch-limited positive theory.

## 4) Candidate Positive Theory (Formal Draft)

### 4.1 Primitive Object (proposed)

Proposed typed object:
- `I = (A, M, T, Pi_M, Pi_T, C_{M,T})`

Where:
- `Pi_M` and `Pi_T` are record/target fiber structures.
- `C_{M,T}` is a compatibility-obstruction component (exactly zero for exact recoverability, positive when collisions are target-varying).

Status: CONDITIONAL (definition draft; full axiom package not yet finalized).

### 4.2 Core Definitions

Recoverability (exact):
- `Rec_A(M,T)=1` iff `exists R: T = R o M` on `A`.
- Status: PROVED in declared theorem package.

Loss:
- `Loss_A(M,T)=1` iff `exists x1,x2 in A` with same record and different target.
- Status: PROVED as collision criterion on declared families.

Compatibility:
- structural compatibility is the degree to which record-fibers avoid target variation.
- Measured by defect objects (`IDELB`, `TFCD`, `CD`, etc.) in finite/restricted forms.
- Status: VALIDATED (restricted classes), not universal theorem yet.

Amount descriptors relation:
- Entropy/MI/Fisher/rank summarize amount/geometry classes of observations.
- They are insufficient for exact target recoverability classification in general.
- Status: PROVED on restricted witness families; not disproving their utility for other tasks.

## 5) Quantification Layer Results (Non-Scalar)

### 5.1 Instrument Definitions Used

From `/Users/stevenreid/Documents/New project/src/information_research/instruments/`:
- Recoverability defect: `D(T|Y)=E||T-E[T|Y]||^2`.
- TFCD: conditional target impurity averaged over observation fibers.
- Compatibility defect surrogate: `CD = 1 - I(T;Y)/I(X;Y)` (clipped ratio form).
- Closure defect: normalized residual after best resolved linear closure fit.
- Hidden-state ambiguity: rank/logdet-based local ambiguity proxies.
- Descriptor-fiber metrics: `DFMI`, `IDELB`; plus compatibility lift `CL`.

### 5.2 Cross-domain ablation summary

From `structural_metric_ablation.csv`:
- Positive `CL_rel` in 6/8 datasets.
- Highest lifts:
  - `ocp_rank_witness`: `CL_rel=1.0000`, `IDELB 0.5000 -> 0.0000`
  - `info_hidden_inference` (real SPARC lane): `CL_rel=0.8214`, `IDELB 0.2000 -> 0.0357`
  - `gravity_quantum`: `CL_rel=0.7500`
  - `gravity_hidden_mass` (real hidden-mass lane): `CL_rel=0.5714`
  - `gravity_blackhole` surrogate: `CL_rel=0.4000`

Important falsification note:
- Simple threshold balanced-accuracy is not uniformly improved; some lanes degrade.
- Interpretation: reduced irreducible descriptor-fiber obstruction does not guarantee every downstream classifier/scorer improves.
- Therefore no universal performance claim is promoted.

### 5.3 Strong contradiction witnesses

From `witness_catalog.csv` (same descriptor fiber, opposite recoverability verdict):
- `info_hidden_inference`: defect gap `36.54` on real SPARC contexts.
- `gravity_hidden_mass`: defect gap `0.482`.
- `gravity_blackhole` surrogate: defect gap `0.4232`.
- `ocp_rank_witness`: exact-vs-fail pairs at same rank descriptors (gap `1.0`).

These are direct contradiction witnesses against amount-only sufficiency.

## 6) Physics Translation Layer (What Is Actually Theorem-Powered)

From `physics_translation_map.csv`:
- Measurement mapping (`M`, fibers): PROVED.
- Coarse-graining split (recover coarse/fail fine): PROVED.
- Irreversibility trend under degradation/lossy transforms: VALIDATED (branch-limited/surrogate).
- Landauer bridge: CONDITIONAL (interpretive without new theorem yet).
- Symmetry-orbit loss mapping: PROVED in restricted symmetry classes.
- Boundary/domain compatibility and closure obstruction mapping: PROVED/VALIDATED in MHD/CFD-linked lanes.
- SDS translation: ANALOGY ONLY.

Conclusion:
- Physics link is theorem-grade in specific map classes (measurement, boundary compatibility, closure obstruction).
- It remains conditional/interpretive for broad erasure thermodynamic claims.

## 7) Falsification and Killer Pass Outcomes

Survivors:
- Restricted no-go package for amount-only exactness (PROVED).
- Family-enlargement fragility (PROVED).
- Model-mismatch instability lower bound (PROVED).
- Compatibility-threshold candidate under declared degradation classes (VALIDATED).

Collapsed/demoted:
- Strict universal coarsening ordering law in tested Hawking surrogate (DISPROVED).
- Universal scalar invariant (DISPROVED).
- Universal cross-domain promotion of restricted gravity candidate (DISPROVED).
- SDS-as-core theorem claim (ANALOGY ONLY).

## 8) Theorem Candidate Package (Current Best Status)

From `theorem_status_map.csv`:
- ST-1 Exact recoverability iff factorization/fiber-constancy: PROVED.
- ST-2 No amount-only exact classifier on restricted finite witness classes: PROVED.
- ST-3 Compatibility augmentation lowers irreducible descriptor-only error bound: VALIDATED.
- ST-4 Family-enlargement false-positive fragility: PROVED.
- ST-5 Model-mismatch instability lower bound: PROVED.
- ST-6 Compatibility threshold under observation degradation: VALIDATED.
- ST-7 Continuity-aware stability above factorization core: OPEN.
- ST-8 Physics irreversibility translation theorem: CONDITIONAL.

## 9) One Primary Result to Promote Now

### Selected primary result category
**Strong negative result with computable restricted invariant package**.

### Exact promoted statement (restricted)

For declared finite witness classes in gravitational hidden-state inference and cross-domain recoverability sets, any amount-only descriptor family (entropy/MI/Fisher/rank surrogates) admits a strictly positive irreducible deterministic classification lower bound (`IDELB > 0`) for exact target recoverability; adding target-record compatibility descriptors yields strictly lower obstruction (`CL_abs > 0`), often substantial.

Status:
- No-go core: PROVED (restricted witness classes).
- Improvement law: VALIDATED (multiple real/surrogate lanes).

Strongest real-system witness:
- SPARC hidden-inference lane: `IDELB 0.2000 -> 0.0357`, `CL_rel=0.8214` (`n=140`).

## 10) What Should Be Dropped Immediately

- Universal scalar “information capacity” claims.
- Universalized gravity-information versions of restricted results.
- Any claim that SDS is theorem-core without explicit theorem-node mapping.
- Any strict coarsening-order law not robust under tested degradations.

## 11) What Is Needed for a Serious Paper

Required to move from strong internal result to publishable theorem package:
- Finalize MP-1 axioms for the primitive object `I`.
- Prove MP-2 stability theorem with explicit perturbation norms.
- Prove MP-3 branch-limited monotonicity/threshold theorem for declared semigroup degradation classes.
- Strengthen MP-4 vector-axiom quantification and prove non-reducibility theorem to amount-only coordinates under explicit assumptions.
- Expand MP-6 unified attack harness to continuous-family and estimator-robustness tests.
- Add independent out-of-sample real-data validation in hidden-state lanes.

## 12) Recommended Next Architecture (Not in OCP Repo)

Keep next-stage development in this workspace under a dedicated lane:
- `src/information_research/theory_core/`
- `src/information_research/validation/`
- `tests/theory_core/`
- `docs/research-program/structural_information_theory/`
- `data/generated/theory_completion/` as the canonical artifact sink

Rationale:
- Preserves OCP theorem package integrity.
- Allows cross-repo mining without forcing all claims into OCP scope.
- Keeps branch-limited claims and theorem-core boundaries explicit.

## 13) Final Verdict

**VERDICT: NEW RESTRICTED INVARIANT PACKAGE + PUBLISHABLE NEGATIVE RESULT (branch-limited).**

What is genuinely new enough to promote now:
- Cross-domain restricted no-go framing with executable descriptor-fiber obstruction diagnostics and compatibility-lift quantification, validated on real hidden-inference lanes and additional physics surrogates.

What is reframed:
- The exact recoverability/fiber-factorization core (known structure, now integrated and operationalized across branches).

What remains incomplete:
- A fully axiomatized primitive object, stability theorem, and fully theorem-grade irreversibility translation law.
