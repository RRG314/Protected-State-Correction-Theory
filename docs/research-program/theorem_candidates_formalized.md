# Theorem Candidates Formalized

Status convention used in this file:
- `PROVED`
- `PROVED ON SUPPORTED FAMILY`
- `CONDITIONAL`
- `VALIDATED / EMPIRICAL ONLY`
- `OPEN`

Evidence sources include:
- `data/generated/context_sensitive_recoverability/*.csv`
- `data/generated/operator_discovery/*.csv`
- `docs/theorem-candidates/cfd-projection-results.md`
- `papers/mhd_paper_upgraded.md`
- `papers/descriptor-fiber-anti-classifier-branch.md`

## T1. Conditioned-vs-Invariant Split Existence

Statement:
There exist supported finite linear context families `(F,t)` such that conditioned exactness holds but context-invariant exactness fails.

Formal form:
`exists (F,t): [forall c, exists d_c: d_c M_c=t] and [not exists d_*: forall c, d_* M_c=t]`.

Scope:
- finite/synthetic linear context families with fixed context row width.

Evidence:
- Context-sensitive catalog: `506` local-exact/global-fail families (`1800` total).
- Operator catalog: `267` local-exact/global-fail families (`1000` total).

Proof sketch:
- Construct contexts with context-dependent target row perturbations `t + a_c u_c` and nuisance rows `u_c`.
- Each context separately spans `t`; shared decoder equations become mutually inconsistent.

Counterexample pressure:
- Shared-exact modes provide negatives where split disappears.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Novelty classification:
- `PLAUSIBLY DISTINCT` package; mechanics reduce to linear compatibility logic.

## T2. Descriptor-Only Insufficiency for Invariant Exactness

Statement:
No classifier depending only on `D_amt=(n,k,m,rank(M_stack),k*m)` is exact for context-invariant recoverability on supported witness classes.

Scope:
- same descriptor class and supported finite witness classes used in catalogs.

Evidence:
- context-sensitive anomalies: `23` same-descriptor opposite shared-verdict groups.
- operator anomalies: `23` opposite groups in base operator pass, `59` groups in agreement-operator continuation pass.

Proof sketch:
- Exhibit descriptor-matched groups with opposite exactness; any deterministic descriptor-only classifier must err.

Counterexample pressure:
- None found inside tested family class.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Novelty classification:
- `PLAUSIBLY DISTINCT` (finite-class no-go package), close to known insufficiency themes.

## T3. Positive Shared Augmentation Threshold Existence

Statement:
There exist local-exact/global-fail families with strictly positive shared augmentation threshold `r_*>0` under declared augmentation class.

Scope:
- augmentation class fixed to measurement-library rows (basis/context rows and combinations), no direct target-row injection.

Evidence:
- context-sensitive augmentation catalog (`506` rows): `r*=1` for `347`, `r*=2` for `159`.
- operator catalog (`486` augmented-found rows): thresholds `0/1/2` with nontrivial positive cases.

Proof sketch:
- For local-exact/global-fail families, search over admissible shared rows and verify first `r` where lifted feasibility residual vanishes.

Counterexample pressure:
- If augmentation class permits direct target-row insertion, thresholds collapse trivially; theorem must include admissibility constraint.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Novelty classification:
- `PLAUSIBLY DISTINCT` as scoped threshold package.

## T4. Family-Enlargement Fragility

Statement:
There exist families where context-invariant exactness flips under one-context enlargement while descriptor summary remains unchanged at amount-only level.

Scope:
- tested finite family-enlargement protocol.

Evidence:
- `94` enlargement flips in context-sensitive witness catalog.

Proof sketch:
- Append a context that preserves per-context amount descriptors but changes shared-decoder feasibility.

Counterexample pressure:
- Not universal; many families remain stable under enlargement.

Status:
- `VALIDATED / EMPIRICAL ONLY`.

Novelty classification:
- `CLOSE PRIOR ART / REPACKAGED` with strong branch utility.

## T5. Geometry-Sensitive Recoverability Split (CFD Branch)

Statement:
There exist bounded CFD sensor/layout families with identical count and rank descriptors but opposite exact recoverability verdicts due to geometry.

Scope:
- bounded finite-family CFD reconstruction branch.

Evidence:
- branch theorem/counterexample documentation in `docs/theorem-candidates/cfd-projection-results.md` and ranked system report.

Proof sketch:
- Build descriptor-matched measurement layouts and exhibit opposite reconstruction exactness.

Counterexample pressure:
- survives branch-level falsification; noisy extension still open.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Novelty classification:
- `PLAUSIBLY DISTINCT` in this finite CFD design package.

## T6. MHD Variable-Resistivity Obstruction + Restricted Survivors

Statement:
In declared cylindrical/annular Euler-potential classes, nonconstant variable resistivity induces closure obstruction with only restricted annular survivor families; axis-touching smooth nonconstant survivors are excluded in supported radial classes.

Scope:
- explicit families and domain classes in `papers/mhd_paper_upgraded.md`.

Evidence:
- Theorems 4.1–4.4 and 5.1–5.2 status-separated in paper.

Proof sketch:
- derive closure remainder `R`; exactness imposes ODE constraints; analyze domain regularity conditions.

Counterexample pressure:
- theorem scope does not include full toroidal/global class.

Status:
- `PROVED ON SUPPORTED FAMILY` (restricted classes).

Novelty classification:
- `PLAUSIBLY DISTINCT` in scoped MHD closure branch.

## T7. Descriptor-Fiber Purity and Irreducible Error Bounds

Statement:
On finite witness sets, perfect descriptor-only classification exists iff every descriptor fiber is pure; irreducible descriptor-only error lower bound is
`IDELB = (sum min(E_alpha,F_alpha))/|W|`.

Scope:
- finite witness classes only.

Evidence:
- `papers/descriptor-fiber-anti-classifier-branch.md` and generated invariant artifacts.

Proof sketch:
- fiber-wise necessity/sufficiency and majority-vote optimality per fiber.

Counterexample pressure:
- not an unrestricted continuous theorem.

Status:
- `PROVED ON SUPPORTED FAMILY`.

Novelty classification:
- `CLOSE PRIOR ART / REPACKAGED` with useful branch-limited extraction.

## T8. Candidate-Library Defect Feasibility Law (Agreement Continuation)

Statement:
Let `G` be the agreement-lift matrix for context family `{M_c}`, target `L`, and finite admissible shared-row library `C`.
Define
`delta_C = rank([G; C; L]) - rank([G; C])`.
Then full-library constrained exact shared recoverability is feasible iff `delta_C = 0`.

Scope:
- finite linear context families,
- augmentation restricted to rows from declared finite candidate library.

Evidence:
- agreement continuation catalog: `300` witness families,
- `14` explicit `delta_C > 0` impossibility cases,
- exact consistency between `delta_C = 0` and full-pool augmented exactness in tested families.

Proof sketch:
1. `delta_C = 0` iff `row(L) subseteq row([G; C])` by rank-inclusion equivalence.
2. If inclusion holds, a decoder exists over full augmented rows by linear solvability.
3. If inclusion fails (`delta_C > 0`), no subset of `C` can repair exactness since subset rowspace is contained in full-library rowspace.

Status:
- `PROVED ON RESTRICTED CLASS`.

Novelty classification:
- `PLAUSIBLY DISTINCT` as a constrained-design no-go/feasibility packaging,
- high overlap risk with known rank-feasibility principles in systems/design literature.

## Immediate theorem push priorities

1. T3 strengthening: necessary/sufficient criteria for `r*=1` and lower bounds for `r*>1` under fixed admissibility class (`OPEN`).
2. T1/T2 write-up into publication-grade narrow package.
3. T6 restricted-class extension before any broad MHD narrative expansion.
