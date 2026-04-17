# Final Report

## Integration + Validation Update (2026-04-16)

This report now includes the full integration/validation/theory-status pass requested after the lens investigation.

Primary outcome:
- operator theory remains the strongest overall foundation,
- functional analysis remains the strongest continuous/PDE foundation,
- geometry remains a theorem-support layer (not the foundation),
- rank/count/budget-only exact classifiers remain falsified on supported classes,
- bounded-domain obstruction plus restricted exact bounded family survives,
- final theory status is `B` (partial branch-limited candidate), not a repo-wide universal theory promotion,
- and soliton overlap is admitted only as a conditional candidate branch with explicit scope limits.

Canonical pass outputs:
- `docs/research-program/integration-audit.md`
- `docs/research-program/integration-gap-list.md`
- `docs/research-program/theorem-normalization-report.md`
- `docs/validation/full-integration-validation-plan.md`
- `docs/validation/full-integration-validation-results.md`
- `docs/research-program/further-expansion-results.md`
- `docs/references/integration-reference-audit.md`
- `docs/references/branch-literature-map.md`
- `docs/app/repo-workbench-consistency-report.md`
- `docs/research-program/final-theory-status-decision.md`

Soliton branch-admission addendum (2026-04-17):
- `docs/soliton-branch/branch_admission_report.md`
- `docs/soliton-branch/internal_ocp_alignment_report.md`
- `docs/soliton-branch/status_normalization.md`
- `docs/soliton-branch/literature_audit.md`
- `docs/soliton-branch/stress_test_report.md`
- `docs/soliton-branch/final_branch_decision.md`

Cross-repo integration sync addendum (2026-04-17):
- `docs/integration/cross_repo_audit.md`
- `docs/integration/repo_scope_statement.md`
- `docs/integration/public_vs_internal_map.md`
- `docs/soliton_branch/overview.md`
- `docs/soliton_branch/status_registry.md`
- `docs/soliton_branch/final_branch_decision.md`

## 1. What Was Found In Local Files

The local search again confirmed that the strongest usable OCP material was spread across:
- the existing OCP theorem and no-go spine,
- MHD divergence-control work,
- QEC bridge notes,
- and cross-structure/no-go material from nearby programs.

The new pass did not uncover a hidden finished physics-unification draft.
It uncovered enough projector, constraint-cleaning, and correction-language material to justify a disciplined **physics extension**, a branch-based open-problem program, and two real partial solutions to previously high-priority open problems, but not a theory rename around physics alone.

## 2. What Was Added In This Pass

This pass added major upgrades across the repo:

1. a real physics-extension layer in `docs/physics/`
2. a citable outside-literature map in `docs/references/citable-expansion-directions.md`
3. a stronger physics-side counterexample for bounded-domain projector transplantation
4. a redesigned static workbench with clearer card-based hierarchy, improved naming, and a kept Maxwell/gauge module
5. a full constrained-observation recoverability branch with formal notes, no-go structure, computational experiments, generated artifacts, and a new Structural Discovery Studio
6. a practical design layer with reusable templates, user-entry paths, and app-facing recoverability guidance
7. a visible research-program layer with branch audit, ranked roadmap, open-problem program, theory-candidate assessment, and usefulness-by-branch notes
8. a restricted bounded-domain exact theorem on the boundary-compatible finite-mode Hodge family
9. a restricted-linear minimal augmentation theorem that turns design advice into an exact count
10. a Discovery Mixer / Structural Composition Lab that turns those theorem-backed and family-backed branches into a typed composition, diagnostics, and repair surface
11. a fiber-based recoverability / impossibility branch that keeps the universal exact core, formalizes detectable-only target hierarchies, proves no-rank-only and no-budget-only exact classifier theorems on the restricted-linear class, and now includes exact family-enlargement and canonical model-mismatch false-positive theorems

The current extension pass also added:

- a narrow CFD lane centered on incompressible projection methods, bounded-domain projection limits, and a new divergence-only bounded no-go
- and an observation-layer branch centered on recoverability of protected variables under coarse records

The current cross-repo positioning is also clearer:
- CFD now deserves a standalone CFD-first repo for projection, reconstruction, and bounded-domain structure
- MHD now deserves a standalone closure-first repo for Euler-potential exactness and variable-resistivity obstruction theory
- this repository keeps the restricted recoverability and design-engine role

## 3. Strongest Current Theory After The Physics Audit

The promoted theorem spine remains:
- exact projector recovery
- exact sector recovery
- invariant-split generator correction
- PSD spectral-gap asymptotic corollary
- rank/image lower-bound structure

The promoted no-go spine remains:
- overlap / indistinguishability failure
- mixing failure for linear flows
- sector-overlap failure
- finite-time exact-recovery failure for smooth linear flows

The strongest new physics-side addition is:
- the explicit rejection of naive periodic-projector transplantation to bounded-domain protected classes

That result materially sharpened the scope of the exact continuous branch.

The strongest new positive bounded-domain addition is:
- the boundary-compatible finite-mode Hodge theorem, which proves exact bounded-domain correction on an explicit restricted family instead of leaving the bounded branch purely negative

The strongest new observation-layer addition is:
- the constrained-observation recoverability framework centered on the collapse modulus `κ_{M,p}` and on exact / approximate / asymptotic / impossible classification across quantum, periodic flow, and control examples

The strongest new limits-branch addition is:
- the fiber-based recoverability / impossibility framework, whose main surviving theorem-grade output is negative:
  above the universal fiber/factorization level, exact recoverability cannot be classified by record amount alone, exactness on a smaller restricted family can fail immediately under honest family enlargement even on the supported finite-dimensional linear class, and exact identifiability of the true family does not imply robustness of a decoder built for the wrong restricted family

The strongest current constrained-observation branch results now added on top of that are:
- the adversarial lower bound `worst-case protected-variable error ≥ κ(η)/2`,
- the restricted-linear exact-regime upper envelope `κ(δ) ≤ ||K||_2 δ`,
- the same-rank insufficiency theorem showing that record amount alone does not determine exact recoverability,
- a nested restricted-linear collision-gap threshold law on bounded admissible coefficient families,
- a restricted-linear minimal-complexity criterion based on row-space inclusion,
- a restricted-linear minimal augmentation theorem with exact count

```text
δ(O, L; F) = rank([O F; L F]) - rank(O F),
```

- a same-record weaker-versus-stronger recovery split,
- a closed-form qubit phase-window collision law,
- a family-level periodic cutoff threshold on the tested two-mode incompressible family,
- a stronger periodic functional-support threshold law that survives repeated-cutoff stress tests,
- a diagonal functional-interpolation threshold law that survives larger polynomial stress tests,
- and a corrected exact-versus-asymptotic control-history split after replacing a misleading sampled collision estimate with an exact nullspace calculation.

That branch now supports a real restricted **Protected-Variable Recoverability Theory (PVRT)** program:
- broad universal PVRT failed,
- restricted finite-dimensional linear PVRT survived,
- and the branch now has several theorem-grade restricted-linear core results.

It still remains a useful formal and computational extension rather than a major standalone theorem program.

The new fiber-based branch pushes that lesson one step further:
- universal exactness survives cleanly as fiber compatibility,
- detectable-only survives cleanly through target coarsening,
- but stronger amount-only or rank-only universal classifiers fail,
- that failure survives even inside a fixed unit-cost candidate library,
- weaker noisy recovery can remain quantitatively separated from stronger-target impossibility on the same restricted-linear record,
- exactness can fail under honest family enlargement,
- and exact-data model mismatch can incur a closed-form target error even when every fixed true family remains exactly identifiable.

## 4. Strongest New Physics Results And Decisions

### Kept exact physics extension
- Maxwell / Coulomb-gauge transverse projection
- status: `KEPT PHYSICS EXTENSION`
- reason: this is a real projector-compatible exact fit, not just analogy

### Kept conditional asymptotic physics extension
- numerical-relativity constraint damping
- status: `CONDITIONAL`
- reason: it fits the generator/damping branch when the protected/constraint-violation split is made explicit

### Kept conditional bridge
- continuous quantum error correction / feedback
- status: `CONDITIONAL`
- reason: it is a real citable bridge between exact sector recovery and continuous correction, but not yet a promoted theorem branch here

### Rejected bridge
- naive periodic-projector reuse on bounded-domain problems
- status: `DISPROVED`
- reason: explicit counterexample shows divergence can be removed while the bounded protected class still fails because boundary-normal structure is not preserved

### Kept narrow CFD extension
- periodic incompressible velocity projection
- status: `PROVED`
- reason: it is the same exact projector class as the periodic Helmholtz/Leray branch, now written explicitly in incompressible CFD language

### New restricted bounded-domain exact result
- boundary-compatible finite-mode Hodge projection
- status: `PROVED`
- reason: exact bounded-domain correction now survives on an explicit boundary-compatible finite-mode family even though the naive periodic transplant remains rejected

### New CFD-facing no-go
- divergence-only bounded recovery
- status: `PROVED`
- reason: distinct bounded incompressible protected states can share the same divergence data, so divergence alone cannot determine an exact recovery map on the protected class

### Rejected for now
- generic constrained Hamiltonian systems as an automatic OCP branch
- status: `ANALOGY ONLY`
- reason: the repo still lacks a canonical projector, recovery operator, or stable correction law in that level of generality

## 5. Strongest New Counterexample

The new bounded-domain projector counterexample gives:
- pre-projection divergence RMS: `7.1889`
- post-periodic-projection divergence RMS: `5.45e-15`
- physical boundary-normal RMS: `2.30e-32`
- projected boundary-normal RMS: `3.11e-2`

This is exactly the kind of result the framework needed.
It shows that removing one residual is not enough if the protected class includes boundary data.

## 6. Workbench Status

The workbench was redesigned and renamed to:
- [Protected-State Correction Workbench](docs/workbench/index.html)

Current validation-facing workbench reports:
- [docs/app/tool-qualification-report.md](docs/app/tool-qualification-report.md)
- [docs/app/professional-validation-report.md](docs/app/professional-validation-report.md)
- [docs/app/workbench-architecture.md](docs/app/workbench-architecture.md)
- [docs/app/workbench-data-flow.md](docs/app/workbench-data-flow.md)
- [docs/app/workbench-refactor-report.md](docs/app/workbench-refactor-report.md)

Current modules:
- Structural Discovery Studio
- Discovery Mixer / Structural Composition Lab
- Benchmark / Validation Console
- Exact Projection Lab
- QEC Sector Lab
- MHD Projection Lab
- CFD Projection Lab
- Gauge Projection Lab
- Continuous Generator Lab
- No-Go Explorer

Usability changes:
- removed the problematic sticky translucent header
- rebuilt the entry area around a clearer hero + module-card layout
- added a task-first quickstart layer so users can start from failure mode, recoverability question, or benchmark need instead of browsing theory modules blindly
- separated configuration, results, theory links, and outside literature
- reduced repeated cramped text
- added a kept physics-extension module instead of leaving the physics lane buried in docs only
- added decision-oriented guidance that says what to add next when a record is insufficient
- added reusable templates and user-facing paths so the repo can be used to build and diagnose systems, not only read about them
- added exportable share-link, JSON, CSV, report, and figure outputs for workbench scenarios
- added a Benchmark / Validation Console that turns built-in demos and module health into an in-workbench trust surface
- added a dedicated tool-qualification and known-results verification report so the workbench is tested as a tool, not only as a codebase
- added a typed Discovery Mixer so users can build supported compositions directly, enter controlled custom matrices or symbolic-linear functionals, run constrained random exploration, and test supported fixes without leaving the workbench
- refactored the static workbench into explicit domain, engine, data, app, and UI helper layers so state, charts, catalog metadata, and analysis dispatch no longer live in one page file

## 7. Outside Literature Layer

The repo now has a cleaner citable literature path in:
- [docs/references/citable-expansion-directions.md](docs/references/citable-expansion-directions.md)
- [docs/references/core-references.md](docs/references/core-references.md)

Most useful current outside anchors:
- Knill and Laflamme for exact QEC
- Ahn, Doherty, and Landahl for continuous QEC
- Chorin for projection methods
- Brown, Cortez, and Minion for projection-method accuracy and boundary behavior
- Guermond, Minev, and Shen for projection-method scope and formulation
- Dedner et al. for GLM/hyperbolic cleaning
- Calabrese / Berchenko-Kogan and Stern / Abalos for Maxwell and constraint-preserving systems
- Gundlach et al. and Weyhausen et al. for numerical-relativity constraint damping

## 8. Validation And Test Results

Validation entry point:
- [scripts/validate/run_all.sh](scripts/validate/run_all.sh)

Professional validation reports:
- [docs/app/tool-qualification-report.md](docs/app/tool-qualification-report.md)
- [docs/app/professional-validation-report.md](docs/app/professional-validation-report.md)

Current validation status:
- generated inventories: passed
- generated claim registry: passed
- generated operator examples: passed
- generated recoverability examples: passed
- generated design examples: passed
- generated workbench examples: passed
- generated discovery-mixer examples: passed
- markdown link check: passed
- naming consistency check: passed
- static workbench asset check: passed
- expanded randomized and multi-grid falsification checks: passed
- real browser smoke of the Structural Discovery Studio: passed
- real browser smoke of the Discovery Mixer: passed
- real browser smoke of the Benchmark / Validation Console and boundary repair flow: passed
- tool qualification surface: `11` qualified modules and `21/21` known-answer matches on the qualified matrix
- professional validation audit: `25/25` known-answer cases, `7/7` adversarial cases, and `10/10` live workflows
- Node workbench test suite: `29 passed`
- Python theorem/operator/example test suite: `148 passed`

Generated artifacts of note:
- [data/generated/validations/operator_examples.json](data/generated/validations/operator_examples.json)
- [data/generated/validations/workbench_examples.json](data/generated/validations/workbench_examples.json)
- [data/generated/validations/claim_registry.csv](data/generated/validations/claim_registry.csv)
- [data/generated/validations/system_summary.json](data/generated/validations/system_summary.json)
- [data/generated/recoverability/recoverability_summary.json](data/generated/recoverability/recoverability_summary.json)
- [data/generated/design/design_template_examples.json](data/generated/design/design_template_examples.json)
- [data/generated/structural_discovery/structural_discovery_summary.json](data/generated/structural_discovery/structural_discovery_summary.json)
- [data/generated/structural_discovery/structural_discovery_demo_table.csv](data/generated/structural_discovery/structural_discovery_demo_table.csv)
- [data/generated/discovery_mixer/discovery_mixer_summary.json](data/generated/discovery_mixer/discovery_mixer_summary.json)
- [data/generated/discovery_mixer/discovery_mixer_demo_table.csv](data/generated/discovery_mixer/discovery_mixer_demo_table.csv)

## 9. Final Naming Decision

Strongest honest public identity:
- main theory: **Protected-State Correction Theory**
- core internal principle: **Orthogonal Correction Principle (OCP)**
- physics lane: **Physics Extension of Protected-State Correction Theory**
- app: **Protected-State Correction Workbench**

This decision is documented in:
- [docs/finalization/naming-and-terminology.md](docs/finalization/naming-and-terminology.md)

## 10. Final Assessment

Current honest rating: **EXCELLENT**.

That rating is justified under the current stricter bar because the repository now has:
- a polished theorem spine
- a strong no-go layer
- disciplined open-problem handling
- reviewer-facing scope control
- a real static workbench
- and a stronger justified physics connection than the earlier baseline

Important limit on that rating:
- this is not a physics-dominant universal theory repo
- and it is not a claim that the whole program is now broadly proved across physics domains

It is **excellent as a theorem-first research repository with a real but carefully delimited physics extension and a visible branch-based open-problem program**.

The new CFD lane does not change that overall rating upward. It strengthens the repository by making one more application slice more real and by adding a sharper negative result at the same time.

## 11. Strongest Next Directions

The best next directions are now clearer and more grounded:

1. a broader bounded-domain exactness theorem beyond the solved finite-mode Hodge subcase
2. a robust noisy extension of the restricted-linear PVRT spine, especially the collision-gap, exact-regime upper-envelope, and minimal-augmentation theorems
3. sharper asymptotic theorems for constraint-damping architectures in real PDE settings
4. a more formal continuous-QEC bridge only if it yields real operator statements instead of analogy

## 12. Directions To Leave Alone For Now

Do not promote or spend major time on:
- universal scalar-capacity revival
- generic constrained Hamiltonian claims without explicit recovery operators
- broad optimizer/ML reintegration
- any renaming that makes physics sound more dominant than the proofs justify
- any claim that broad universal PVRT has been proved
- any claim that the constrained-observation branch is already a major new theory rather than a promising formal/computational lane with a real restricted PVRT spine and several narrow threshold results

## 13. Lens Integration And Theory-Formation Decision (2026-04-16)

The completed lens investigation was integrated as a selective promotion pass, not a rebrand.

Primary outcomes:
- promoted operator-theory and functional-analysis payloads where they sharpen exactness/no-go/rate claims,
- kept geometry as a theorem-support layer where it is computable and branch-valid,
- explicitly demoted inverse-problem, information-theory, and dynamical framing where they weaken exact branch language,
- kept theorem IDs and branch boundaries unchanged.

Required lens-integration outputs are now tracked in:
- [docs/research-program/lens-integration-map.md](docs/research-program/lens-integration-map.md)
- [docs/research-program/lens-promotion-decisions.md](docs/research-program/lens-promotion-decisions.md)
- [docs/research-program/theory-candidate-comparison.md](docs/research-program/theory-candidate-comparison.md)
- [docs/validation/lens-integration-validation-plan.md](docs/validation/lens-integration-validation-plan.md)
- [docs/validation/lens-integration-validation-results.md](docs/validation/lens-integration-validation-results.md)
- [docs/references/lens-integration-reference-map.md](docs/references/lens-integration-reference-map.md)
- [docs/references/theory-candidate-literature-positioning.md](docs/references/theory-candidate-literature-positioning.md)
- [docs/research-program/final-theory-formation-decision.md](docs/research-program/final-theory-formation-decision.md)

Validation used claim-type-matched testing and passed:
- full validation run: passed,
- Node consistency suite: `29 passed`,
- Python theorem/operator/example suite: `148 passed`,
- focused recheck (recoverability/unified/cfd/generator): `66 passed`,
- focused workbench static recheck: `21 passed`.

Final theory-formation verdict for this pass:
- `B` (one partial theory candidate survives, still branch-limited),
- no repo-identity rename is justified from this pass alone.
