# Lens Integration Map (2026-04-16)

## Scope

This map integrates the completed lens investigation into the active OCP / Protected-State Correction repository using a falsification-first filter.

Promotion classes:
- `A` integrate now into theorem spine
- `B` integrate now into branch docs and diagnostics only
- `C` keep as investigation result (not promoted)
- `D` reject or archive as secondary/misleading
- `E` open-problem / future theorem candidate

## Integration Table

| Lens-derived result | Promotion class | Primary branch target | What it strengthens | Required repo change type | Literature status | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| OT-4 alignment/kernel invariant `alpha(tau,T)=||P_{ker(T*)^perp}v||/||v||` | `A` | constrained-observation + fiber/restricted-linear limits | invariant stronger than raw rank/count; same-rank opposite verdict explanation | theorem-spine interpretation update, diagnostics language, workbench evidence labels | likely literature-known in operator form, repo framing and anti-classifier packaging plausibly distinct | Promote as core replacement invariant above rank-only language |
| OT-4 row-space form `v in row(T)` for exact recoverability | `A` | constrained-observation (`OCP-031`, `OCP-047`, `OCP-049`) | exactness criterion wording; anti-classifier explanation | theorem-spine interpretation update (no ID changes) | literature-known linear algebra fact; repo use is branch-specific | Promote as canonical exactness test language in restricted-linear classes |
| OT-3 spectral-abscissa / spectral-gap rate sharpening | `A` | asymptotic generator, GLM comparator | asymptotic rate statements and branch boundaries (exact vs asymptotic) | branch-doc theorem sharpening and validation labeling | literature-known semigroup/operator fact; repo application likely framing-new | Promote where split-preserving generator assumptions hold |
| OT-2 factorization parameterization `C=(I-P_S)A` | `B` | exact projector + design layer | constructive design interpretation (not new theorem) | branch docs and design guidance text | literature-known projector algebra | Keep as design interpretation, not novelty theorem |
| FA-3 bounded-domain Hodge/topological obstruction (`b1(Omega)` lane) | `A` | bounded-domain/Hodge/CFD + bounded-domain no-go spine | obstruction theory sharpening for `OCP-023/OCP-028/OCP-029/OCP-044` | no-go/exactness classification wording and open-problem targeting | likely literature-known Hodge theorem; repo obstruction packaging likely distinct | Promote as primary bounded-domain theorem/no-go organizing axis |
| FA-1 Poincare/eigenvalue efficiency framing | `B` | bounded-domain + asymptotic PDE lane | rate/efficiency interpretation, not exactness criterion | branch docs and benchmark interpretation | literature-known | Keep as secondary quantitative lens |
| Geometry G-3 principal-angle/alignment restatement of OT-4 | `B` | constrained-observation and anti-classifier explanation surfaces | geometric interpretation of row-space/kernel tests | diagnostics/workbench explanation only | likely literature-known; repo packaging new-ish | Keep as supporting geometry, not primary foundation |
| Principal-angle perturbation fragility (stability envelope style) | `E` | constrained-observation + restricted-linear robustness open lane | stability-vs-exactness theorem candidate | open-problem + validation program only | literature-unclear for this exact packaging | Keep as forward theorem candidate (not yet proved repo-wide) |
| Domain/boundary geometry as strict obstruction in bounded settings | `A` | bounded-domain/Hodge/CFD | stronger no-go explanations for periodic transplant failure | no-go docs and branch audit emphasis | mixed: core facts known, repo bounded OCP packaging plausibly distinct | Promote as mandatory bounded-domain gate |
| Gauge/orbit quotient interpretation | `B` | Maxwell/gauge projection branch | conceptual cleanup for invisible directions/orbits | branch docs only | likely literature-known | Keep narrow and projection-compatible |
| IP-1 target-specific stability (`factorization + continuity`) | `E` | constrained-observation/fiber branch | open failure mode (exact but unstable) and target hierarchy refinement | open-problem and validation plan only | literature-unclear in repo phrasing | Keep as open problem candidate, no theorem promotion yet |
| Inverse-problem language on exact projector/QEC anchors | `D` | exact projector + sector/QEC | none; often worsens clarity | archive/demotion decision only | N/A | Reject for exact branches; keep inverse-problem language narrow |
| IT fractional recoverability `FR=I/H` | `C` | constrained-observation quantification lane | continuous score/ranking interpretation | optional branch-doc appendix only | literature-known | Keep as secondary metric, not theorem spine |
| Entropy wording for exact branches (`H=0` restatements) | `D` | exact projector/QEC/Helmholtz | none (decorative) | archive/demotion decision only | N/A | Reject as exact-branch language inflation |
| DS-1 asymptotic-to-exact parameter transition framing | `C` | GLM/asymptotic comparator branch | interpretation-only for control parameter sweeps | optional branch-doc commentary | literature-unclear but low theorem value | Keep as exploratory interpretation only |
| DS language on one-shot exact branches | `D` | exact projector/QEC/Helmholtz | none; misleading | archive/demotion decision only | N/A | Reject |

## Promotion Summary

- `A`: OT-4 kernel/alignment invariant; OT-3 spectral rate sharpening; FA-3 bounded-domain topological obstruction; domain/boundary geometry gate.
- `B`: OT-2 constructive factorization interpretation; geometry as support (not foundation); gauge/orbit branch cleanup; FA-1 efficiency interpretation.
- `C`: IT fractional recoverability and DS-1 transition framing as secondary investigation outputs.
- `D`: entropy inflation on exact branches; inverse-problem overreach on exact branches; dynamical-language overreach on one-shot branches.
- `E`: target-specific stability criterion and perturbation-robustness envelopes as explicit theorem candidates.

## Branch Mapping Snapshot

| Branch | Primary promoted lens payload |
| --- | --- |
| Exact finite-dimensional projection | `B` only (design parameterization and diagnostics), no theorem-ID changes |
| Exact sector/QEC | keep exact-anchor language; no inverse-problem or entropy inflation (`D`) |
| Exact periodic Helmholtz/Leray | keep operator/functional language; geometry remains supportive (`B`) |
| Bounded-domain/Hodge/CFD | strongest promoted lane (`A`): topology-sensitive obstruction and boundary-gated exactness |
| Maxwell/gauge projection | `B`: orbit/quotient interpretation on projection-compatible classes |
| Asymptotic generator | `A`: spectral-rate sharpening under split/generator assumptions |
| Constrained observation/restricted PVRT | `A`: alignment/kernel invariant stronger than rank; `E`: stability lane |
| Fiber/unified impossibility branch | `A`: anti-classifier interpretation via alignment/kernel invariant; `E`: stability/mismatch robustness extensions |

## Net Integration Decision

The lens report survives integration as an **operator-first + functional-analysis-first** sharpening pass with geometry as a theorem-support layer.

No branch renaming is justified.
No theorem-ID reset is justified.
No universal one-lens theory claim survives.
