# Missing-Work Integration Map (Phase 1)

Date: 2026-04-19  
Scope: local-only integration into `/Users/stevenreid/Documents/New project/repos/ocp-research-program`.

## Integration Rules Used

1. Keep only items that close an identified missing piece (MP-1..MP-7), strengthen falsification, or improve citation/scope honesty.
2. Do not import broad exploratory material that does not map to current theorem boundaries.
3. Preserve provenance for every imported artifact.
4. Use four-way decision labels: `INTEGRATE`, `REFERENCE`, `ARCHIVE-SUPPORT`, `REJECT-DRIFT`.

## Imported or Referenced Items

| External source item | Decision | Local destination | Why this decision | Provenance |
| --- | --- | --- | --- | --- |
| `docs/research-program/structural_information_theory_comprehensive_report.md` | INTEGRATE | `docs/research-program/structural-information-theory/external-imports/structural_information_theory_comprehensive_report.md` | Authoritative MP-1..MP-7 gap specification and status labels | Local workspace root report |
| `docs/research-program/adversarial_originality_overlap_usefulness_audit.md` | INTEGRATE | `docs/research-program/structural-information-theory/external-imports/adversarial_originality_overlap_usefulness_audit.md` | Required overlap-risk baseline for later re-audit | Local workspace root report |
| `data/generated/theory_completion/*` | INTEGRATE | `data/imported/structural-information-theory/` | Canonical generated evidence for completion report and dependency map | Local generated artifacts (2026-04-19) |
| `data/generated/information_research/real_system_metrics.csv` | INTEGRATE | `data/imported/structural-information-theory/real_system_metrics.csv` | Real-system witness lane needed for out-of-family checks | Information-research lane artifacts |
| `data/generated/information_research/high_pressure_summary.json` | INTEGRATE | `data/imported/structural-information-theory/high_pressure_summary.json` | Compact anti-classifier summary across battlefields | Information-research lane artifacts |
| `data/generated/gravity_recoverability/gravity_recoverability_metrics.csv` | INTEGRATE | `data/imported/structural-information-theory/gravity_recoverability_metrics.csv` | Required for gravitational hidden-state and degradation checks | Gravity recoverability lane artifacts |
| `data/generated/gravity_recoverability/gravity_theorem_checks.json` | INTEGRATE | `data/imported/structural-information-theory/gravity_theorem_checks.json` | Existing theorem candidate statuses and contradictions | Gravity recoverability lane artifacts |
| `data/generated/gravity_recoverability/gravity_killer_pass.json` | INTEGRATE | `data/imported/structural-information-theory/gravity_killer_pass.json` | Existing collapse/survival tags for killer pass continuity | Gravity recoverability lane artifacts |
| `src/information_research/instruments/*.py` | REFERENCE | referenced in harness notes and this integration map | Used as external implementation reference while OCP-local functions were rewritten under `src/ocp/structural_information.py` | Information-research instrument code |
| `mhd-toolkit/docs/theorems/proof_status.md` | REFERENCE | referenced in closure/physics translation docs | MHD theorem statuses are relevant but toolkit remains independent repo | Companion MHD toolkit |
| `repos/cfd-research-program/docs/*` (broad set) | REFERENCE | referenced only in cross-domain harness notes | Useful for boundary/closure positioning; no direct import needed for theorem closure here | Companion CFD repo |
| `repos/rdt-project-showcase/docs/*` (broad set) | REFERENCE | referenced only where symmetry/partition context is required | Contextual only; no direct closure of MP gaps | Companion RDT repo |

## Rejected as Drift (Not Imported)

| Candidate | Decision | Reason |
| --- | --- | --- |
| Broad geometry discovery passes (`docs/research-program/geometry-pass-2026-04-16/*`) | REJECT-DRIFT | Valuable exploratory context but not directly needed for MP-1..MP-7 closure in this pass |
| Soliton adjacent-topic reading-lists and orientation docs | REJECT-DRIFT | Literature orientation material, no immediate theorem/harness closure impact |
| Generic “theory of everything” or universalization drafts in archived internal notes | REJECT-DRIFT | Conflicts with scope discipline and adversarial audit recommendations |
| Non-recoverability engineering docs unrelated to theorem/no-go/invariant boundaries | REJECT-DRIFT | Would bloat repo and dilute claim boundaries |

## Phase 1 Output Summary

- Imported authoritative completion and overlap audits into OCP-local path.
- Imported generated evidence needed for closure and re-audit.
- Preserved external instrument code as support material without promoting it as theorem-core.
- Deferred companion-repo content to references unless directly required by proof/harness outputs.
