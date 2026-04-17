# Branch Audit

## Purpose

This note audits the repository as a branch-based research program rather than as a finished framework. Every branch is treated honestly: strongest result, strongest failure, strongest limitation, and whether it is worth pushing harder.

## Current Geometry Pass

Repo-native consolidated geometry findings for this program:
- [GEOMETRY_FINDINGS_FOR_REPO_2026-04-16.md](GEOMETRY_FINDINGS_FOR_REPO_2026-04-16.md)

## Current Lens Integration Pass

Lens integration and theory-formation outputs for this program:
- [LENS_INTEGRATION_COMPLETE_REPORT_2026-04-16.md](LENS_INTEGRATION_COMPLETE_REPORT_2026-04-16.md)
- [lens-integration-map.md](lens-integration-map.md)
- [lens-promotion-decisions.md](lens-promotion-decisions.md)
- [theory-candidate-comparison.md](theory-candidate-comparison.md)
- [final-theory-formation-decision.md](final-theory-formation-decision.md)
- [../validation/lens-integration-validation-plan.md](../validation/lens-integration-validation-plan.md)
- [../validation/lens-integration-validation-results.md](../validation/lens-integration-validation-results.md)
- [../references/lens-integration-reference-map.md](../references/lens-integration-reference-map.md)
- [../references/theory-candidate-literature-positioning.md](../references/theory-candidate-literature-positioning.md)

## Current Next-Phase Deepening Pass

Quantitative/stability/dynamic/minimal-structure and deep-dive outputs:
- [next-phase-audit.md](next-phase-audit.md)
- [next-phase-paper-lanes.md](next-phase-paper-lanes.md)
- [next-phase-final-report.md](next-phase-final-report.md)
- [../theory/quantitative-recoverability.md](../theory/quantitative-recoverability.md)
- [../theory/stability-and-fragility.md](../theory/stability-and-fragility.md)
- [../theory/dynamic-correction-layer.md](../theory/dynamic-correction-layer.md)
- [../theory/minimal-structure-classification.md](../theory/minimal-structure-classification.md)
- [../cfd/next-phase-deep-dive.md](../cfd/next-phase-deep-dive.md)
- [../fiber-based-recoverability-and-impossibility/next-phase-deep-dive.md](../fiber-based-recoverability-and-impossibility/next-phase-deep-dive.md)
- [../app/next-phase-tool-integration.md](../app/next-phase-tool-integration.md)

## Current Soliton Branch Admission Pass

Soliton-to-OCP admission and stress-test outputs:
- [../soliton-branch/branch_admission_report.md](../soliton-branch/branch_admission_report.md)
- [../soliton-branch/internal_ocp_alignment_report.md](../soliton-branch/internal_ocp_alignment_report.md)
- [../soliton-branch/status_normalization.md](../soliton-branch/status_normalization.md)
- [../soliton-branch/claim_registry.md](../soliton-branch/claim_registry.md)
- [../soliton-branch/literature_audit.md](../soliton-branch/literature_audit.md)
- [../soliton-branch/novelty_positioning.md](../soliton-branch/novelty_positioning.md)
- [../soliton-branch/stress_test_report.md](../soliton-branch/stress_test_report.md)
- [../soliton-branch/validation_scope_note.md](../soliton-branch/validation_scope_note.md)
- [../soliton-branch/final_branch_decision.md](../soliton-branch/final_branch_decision.md)

Canonical scope-sync overlays for this pass:
- [../integration/cross_repo_audit.md](../integration/cross_repo_audit.md)
- [../integration/repo_scope_statement.md](../integration/repo_scope_statement.md)
- [../soliton_branch/overview.md](../soliton_branch/overview.md)
- [../soliton_branch/status_registry.md](../soliton_branch/status_registry.md)

## Branch Matrix

| Branch | What it is about | Strongest clean result | Strongest negative result | Strongest limitation | Status | Worth pushing harder? |
| --- | --- | --- | --- | --- | --- | --- |
| Exact branch | finite-dimensional protected/disturbance decomposition and exact projector recovery | OCP-T1 exact protected-subspace recovery | OCP-N1 overlap kills exact recovery | mostly standard linear algebra once the setup is fixed | narrow anchor | yes, but mainly as backbone rather than novelty target |
| Exact sector / QEC branch | exact recovery from pairwise orthogonal disturbance sectors | OCP-T5 exact sector recovery | OCP-N8 sector overlap destroys unique exact detection | novelty risk is high because the best exact anchor is still close to standard QEC/operator language | strong exact anchor | yes, but only if one more anchor sharpens the formalism |
| Exact continuous periodic branch | exact projector correction for divergence-free periodic fields | OCP-006 periodic Helmholtz/Leray exact anchor | naive bounded transplant is rejected | broad generalization to realistic bounded domains is still delicate | strong exact continuous anchor | yes |
| CFD lane | incompressible projection methods and bounded-domain limits | periodic incompressible projection exact fit; bounded finite-mode Hodge exact subcase | divergence-only bounded no-go; naive periodic transplant rejection | beyond the finite-mode bounded theorem, general exactness depends on the actual domain-compatible Hodge operator | narrow but real application branch | yes |
| Maxwell / gauge projection branch | projector-compatible transverse/longitudinal splitting in physics | transverse gauge projection fit | none stronger than the inherited projector no-go structure | mostly reinterpretive; limited theorem headroom inside this repo | narrow physics extension | keep, but do not overinvest |
| Asymptotic generator branch | continuous asymptotic correction under invariant splits | OCP-T3 invariant-split generator theorem and OCP-C2 PSD corollary | OCP-N5 mixing no-go; OCP-N7 finite-time exact recovery no-go | strongest current results are linear and split-preserving | strong theorem branch | yes |
| GLM / constraint-damping branch | asymptotic cleaning and damping instead of exact projection | asymptotic classification survives | cannot be promoted to exact correction | practical but harder to sharpen into strong theorems without more PDE structure | comparator branch | keep, but targeted investment only |
| Continuous-QEC bridge | bridge between exact sector correction and continuous monitored correction | citable conditional bridge | smooth-flow finite-time exactness no-go blocks naive overclaiming | still conditional and bridge-like rather than theorem-complete | conditional bridge | keep, but do not oversell |
| Constrained-observation recoverability branch | exact/approximate/asymptotic/impossible recovery under coarse records | OCP-043 plus the exact-regime upper envelope and same-rank insufficiency theorem | same-record weaker-versus-stronger split; phase-loss and hidden-mode no-gos | broad universal PVRT failed; strongest surviving form is restricted-linear | strongest current theory-program branch in repo | yes, heavily |
| Fiber-based recoverability / impossibility branch | common formal limits on recoverability, detectability, distinguishability, irrecoverability, and false-positive exactness claims across fields | universal fiber-factorization exactness plus OCP-049/OCP-050 anti-universal classifier theorems, OCP-051 noisy weaker-vs-stronger separation, OCP-052 family-enlargement false-positive theorem, and OCP-053 canonical model-mismatch instability theorem | one universal threshold law, one amount-only classifier, one family-blind exactness slogan, and one family-blind inverse-map robustness slogan all fail | strongest positive laws above the fiber level remain restricted by field or family | serious synthesis / limits branch | yes, but keep falsification-first |
| Soliton nonlinear-wave candidate branch | quotient recoverability and projection-preservation/no-go on restricted one-soliton NLS families | symmetry non-identifiability no-go plus validated same-count opposite-verdict witnesses on tested families | direct linear minimal-augmentation transfer and broad universal bridge claims fail | strongest positive claims remain finite-grid validated/conditional rather than closed continuous theorems | conditional candidate branch (`B`) | yes, but only as a tightly bounded bridge lane |
| Restricted-linear / design-engine layer | measurement sufficiency, minimal augmentation, and design diagnostics on restricted families | OCP-T6 restricted-linear minimal augmentation theorem | below-deficiency augmentation impossibility | limited to restricted finite-dimensional linear families | strongest practical theorem-to-tool branch | yes, heavily |
| Structural Discovery subsystem | failure diagnosis, missing-structure detection, supported repair suggestions, and before/after validation | validated end-to-end diagnosis-and-repair demos across periodic, control, qubit, and restricted-linear families | no in-studio fix is promoted unless a theorem-backed or validated family-backed path exists | novelty is mostly engineering and theorem-surfacing rather than standalone mathematics | high-value subsystem | yes, as a practical research-system layer |
| Discovery Mixer / Structural Composition Lab | typed composition, compatibility analysis, custom-input reduction, constrained random search, and augmentation discovery across supported families | validated typed composition plus before/after repair on user-built restricted-linear, periodic, control, and bounded-domain cases | unsupported symbolic or mixed-family inputs are rejected explicitly rather than silently approximated | theorem headroom is still limited by the supported family reductions; it is not a universal symbolic engine | high-value advanced lab | yes, as a serious engineering and theorem-surfacing subsystem |
| Practical workbench / studio layer | turning the theory into decisions, diagnosis, and next-step guidance | real recoverability / correction studio with artifact-backed outputs | fake or weak interactivity gets caught by browser and static tests | usefulness depends on keeping it wired to the actual math | tool layer | yes, but only when coupled to clean branch results |
| Rejected / demoted directions | optimizer, generic constrained-Hamiltonian automatic fit, universal scalar capacity | none | broad claims fail repeatedly | not worth renewed effort without new operators or theorems | frozen | no |

## Strongest Current Backbone

The repo's current backbone is:
- exact branch as the finite-dimensional anchor,
- exact sector/QEC branch as the clean sector-conditioned anchor,
- exact periodic projection as the clean continuous anchor,
- asymptotic generator branch as the strongest finished continuous theorem branch,
- constrained-observation and restricted-linear design layers as the strongest current open theorem/program branches,
- fiber-based recoverability / impossibility as the cleanest statement of what part of recoverability theory is universal and what part fails to unify,
- no-go layer as the main scope-control mechanism.

## Strongest Current Contribution Candidates

1. constrained-observation / restricted-linear threshold and augmentation theorems
2. bounded-domain exact correction under explicit boundary-compatible Hodge assumptions
3. asymptotic generator completion beyond invariant splits, if a sharper theorem survives
4. structural discovery as the main theorem-to-tool bridge, provided it stays rigorously tied to the validated branch results
5. discovery mixer as the advanced composition and counterexample-generation surface, provided it stays inside supported typed families

## Weakest Parts To Demote Or Freeze

1. universal scalar capacity language
2. broad cross-domain phase-transition language without explicit family hypotheses
3. generic constrained-Hamiltonian automatic-fit claims
4. optimizer / ML reintegration without explicit operators and falsification discipline

## Honest Bottom Line

The repo is no longer just a framework. It now has:
- strong mature anchors,
- one serious theorem-and-tool branch around constrained observation and restricted-linear design,
- one partially solved bounded-domain exactness problem,
- and a clear set of branches that should stay frozen unless something materially stronger appears.
