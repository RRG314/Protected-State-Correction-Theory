# No-Go Candidates Formalized

Status labels:
- `PROVED`
- `PROVED ON SUPPORTED FAMILY`
- `VALIDATED / EMPIRICAL ONLY`
- `CONDITIONAL`
- `OPEN`

## N1. Fiber-Collision Impossibility (Core)

Statement:
If two admissible states have identical records but different target values, exact recovery of that target is impossible.

Form:
`M(x)=M(x') and tau(x)!=tau(x') => no exact decoder on family`.

Status:
- `PROVED` (logical obstruction).

Novelty:
- `ALREADY KNOWN IN SUBSTANCE`.

## N2. Conditioned Exactness Does Not Imply Invariant Exactness

Statement:
There exist supported context families where each context is exactly recoverable but no shared decoder exists.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- context-sensitive and operator catalogs (`506` and `267` local-exact/global-fail cases respectively).

Novelty:
- `PLAUSIBLY DISTINCT` as scoped no-go package.

## N3. No Rank-Only / Budget-Only Exact Classifier

Statement:
Amount-only descriptors fail to classify invariant exactness: descriptor-matched families can have opposite exactness verdicts.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- `23` groups in base catalogs and `59` groups in agreement-operator continuation catalog.

Novelty:
- `PLAUSIBLY DISTINCT` finite-class no-go corpus.

## N4. Stack Projection Sufficiency Fails for Shared Decoder Feasibility

Statement:
`tau` may lie in rowspace of `M_stack` while shared decoder feasibility still fails.

Evidence:
- operator anomaly type `projection_succeeds_but_shared_decoder_fails` with `491` cases.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Novelty:
- `REDUCES TO EXISTING OCP LOGIC` (clarifies distinction, not new algebraic law).

## N5. Divergence-Only Bounded Recovery Insufficiency (CFD)

Statement:
In nontrivial bounded protected classes, divergence-only records are insufficient for exact bounded recovery.

Status:
- `PROVED` in branch scope.

Evidence:
- `docs/theorem-candidates/cfd-projection-results.md` (No-Go OCP-CFD-N1).

Novelty:
- `CLOSE PRIOR ART / REPACKAGED`, branch-useful and retained.

## N6. Variable-Resistivity Closure Obstruction (MHD)

Statement:
For supported Euler-potential radial classes with nonconstant `eta(r)`, nontrivial exact survivors are restricted (annular), and broad smooth-axis exactness fails.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Evidence:
- `papers/mhd_paper_upgraded.md` Theorems 4.1–4.4.

Novelty:
- `PLAUSIBLY DISTINCT` scoped obstruction package.

## N7. Family-Enlargement Fragility No-Go (Conditional)

Statement:
Exactness can fail under one-context family enlargement even when base descriptor summaries stay unchanged.

Status:
- `VALIDATED / EMPIRICAL ONLY`.

Evidence:
- `94` enlargement flips in context-sensitive catalog.

Novelty:
- `CLOSE PRIOR ART / REPACKAGED` and currently conditional as theorem.

## N8. Broad Universal-Classifier and Universal-Theory Claims

Statement:
A single scalar/descriptor classifier for cross-branch exactness and broad universal unification claims are not supported by the current corpus.

Status:
- `DISPROVED / COLLAPSED` at broad scope.

Evidence:
- full-system falsification outputs and theorem ranking decisions.

## N9. Positive Candidate-Library Defect Implies Repair Impossibility

Statement:
For agreement-lift matrix `G`, target `L`, and candidate library `C`, if
`delta_C = rank([G; C; L]) - rank([G; C]) > 0`,
then no augmentation using rows from `C` can restore invariant exactness.

Status:
- `PROVED ON RESTRICTED CLASS`.

Evidence:
- agreement continuation catalog: `14` explicit impossibility cases with `delta_C > 0`.

## N10. Library Rank Gain Is Not Sufficient

Statement:
`rank([G; C]) - rank(G) >= r_free^*` is not sufficient for candidate-library feasibility.

Status:
- `PROVED ON RESTRICTED CLASS`.

Evidence:
- deterministic unit-test counterexample plus `14` catalog cases where gain bound holds but `delta_C > 0`.

## No-go package to push now

Primary no-go package:
1. N2 conditioned-vs-invariant split,
2. N3 no amount-only exact classifier,
3. N4 projection-sufficiency failure for shared decoder feasibility,
4. N9/N10 candidate-library impossibility and gain-insufficiency laws.

Secondary branch no-go package:
- N5 (CFD bounded divergence-only insufficiency),
- N6 (MHD variable-eta obstruction in restricted classes).
