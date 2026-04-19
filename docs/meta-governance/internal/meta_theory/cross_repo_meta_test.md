# Cross-Repo Meta-Theory Test

Date: 2026-04-17

## Test Protocol

For each branch we evaluate:
1. Is there a protected/target role?
2. Is there a second interacting role?
3. Is the second role necessary?
4. Is exactness/failure controlled by compatibility between them?
5. Does one-object or amount-only description fail?
6. Does representation/observation collapse essential distinctions?
7. Does this support, weakly resemble, or refute the candidate meta-theories?

## A. OCP / Recoverability Branches

### Evidence tested
- Fiber/factorization exactness (`OCP-030`, UCT-1)
- Collision no-go (UCT-2)
- No rank-only classifier (`OCP-049`)
- No fixed-budget-only classifier (`OCP-050`)
- Same-rank insufficiency (`OCP-047`)
- Family-enlargement false-positive theorem (`OCP-052`)
- Model-mismatch instability (`OCP-053`)
- Bounded-domain obstruction (`OCP-023`, `OCP-028`)

### Evaluation
| Question | Result |
| --- | --- |
| 1 | Yes: target `T` is explicit. |
| 2 | Yes: record/operator/domain structures (`M`, `C`, boundary compatibility). |
| 3 | Yes: changing record/operator/domain flips verdicts. |
| 4 | Yes: exactness via compatibility (`T = R ∘ M`, `ker(OF) ⊆ ker(LF)`, bounded-domain compatibility). |
| 5 | Yes: amount-only fails (rank/count/budget anti-classifier theorems). |
| 6 | Yes: target-distinguishing collisions and hidden-kernel directions create impossibility. |
| 7 | Strong support for Candidates B and C; support for Candidate A. |

Verdict: **Strong support**.

## B. Soliton Restricted Branch (OCP-integrated layer)

### Evidence tested
- Symmetry non-identifiability no-go (`SOL-OCP-001`, PROVED)
- Same-count opposite verdict (`SOL-OCP-005`, VALIDATED + CONDITIONAL)
- Projection-preservation/no-go split (`SOL-OCP-007`, VALIDATED + CONDITIONAL)

### Evaluation
| Question | Result |
| --- | --- |
| 1 | Yes: quotient target (modulo nuisance symmetry). |
| 2 | Yes: observation class + symmetry group + reduction operator. |
| 3 | Yes on supported families: observation family choice changes identifiability. |
| 4 | Yes: compatibility depends on quotient-aware injectivity. |
| 5 | Likely yes: same-count opposite verdict supports amount-only failure, but continuous theorem still conditional. |
| 6 | Yes: symmetry-invariant observation collapses target-relevant distinctions. |
| 7 | Supports A/C strongly on supported families; supports B at restricted-validated level. |

Verdict: **Moderate-to-strong restricted support** (continuous global promotion not justified).

## C. MHD Closure/Obstruction Branch

### Evidence tested
- Constant-resistivity exact families (Theorems 3.1–3.4 in `mhd_paper_upgraded.md`)
- Variable-resistivity obstruction (Theorems 4.1–4.3)
- Annular vs axis-touching split (Corollary 4.4)
- Mixed/tokamak-adjacent restricted branches (Theorems 5.1–5.2, Proposition 5.3)

### Evaluation
| Question | Result |
| --- | --- |
| 1 | Yes: target is exact closure (`R=0`) in declared ansatz classes. |
| 2 | Yes: interacting role includes resistivity profile `eta(r)`, domain class, and ansatz geometry. |
| 3 | Yes on supported families: changing `eta` profile or domain class changes exactness. |
| 4 | Yes: exactness controlled by compatibility ODE/factorization conditions. |
| 5 | Yes (restricted sense): scalar amount indicators do not classify; profile/domain structure matters. |
| 6 | Partly: failure is more operator/domain mismatch than pure observation collapse; still a structural compatibility failure. |
| 7 | Strong support for A and B (branch-limited); partial support for C (via compatibility mismatch rather than pure measurement collapse). |

Verdict: **Strong branch-limited support**.

## D. SDS / Workbench Engineering Layer

### Evidence tested
- Distinction between theorem core and engineering layer (`theorem_hierarchy_final.md`, levels E vs U/B)
- Structural Discovery Studio and Discovery Mixer as theorem-linked tooling (`branch-audit.md`, app docs)
- Two-reservoir motif not promoted as theorem core (analogy-only in framework docs)

### Evaluation
| Question | Result |
| --- | --- |
| 1 | Yes, in tool workflows: explicit protected target selection. |
| 2 | Yes: record design, compatibility diagnostics, augmentation operations. |
| 3 | Yes operationally: wrong architecture yields failing regimes; fixes depend on compatibility structure. |
| 4 | Yes at tooling level, but this is implementation of branch theorems, not independent theorem evidence. |
| 5 | Yes in practice: amount-only heuristics are insufficient in tool diagnostics. |
| 6 | Yes in diagnostics language, but mostly inherited from theorem branches. |
| 7 | Supports A/B/C as engineering corroboration; does not independently prove meta-theory. |

Verdict: **Supporting but non-foundational evidence**.

## Cross-Repo Summary by Candidate

| Candidate | OCP | Soliton | MHD | SDS | Combined verdict |
| --- | --- | --- | --- | --- | --- |
| A Interaction requirement | Strong | Moderate-strong (restricted) | Strong (restricted) | Supporting | Survives as branch-limited meta-pattern |
| B Unification-limit (amount-only failure) | Strong theorem support | Restricted validated support | Restricted support | Supporting | Survives strongly in restricted branches; cross-branch generalization conditional |
| C Representation-distortion limits | Strong (fiber collisions) | Strong (symmetry blindness) | Partial (compatibility mismatch dominates) | Supporting | Survives with broadened wording: “distinction-loss/compatibility-loss” rather than measurement-only |
| D Strong universal multi-role claim | Not implied | Not implied | Not implied | Not implied | Not supported as universal theorem statement |

## Immediate Conclusion

The evidence does **not** support a universal “everything needs two parts” law.

The evidence **does** support a branch-limited framework:
- exactness/failure depends on compatibility between target role and interacting structural roles,
- amount-only compression is provably insufficient on key supported classes,
- distinction collapse (via collisions/symmetry/mismatch) is a recurring no-go mechanism.
