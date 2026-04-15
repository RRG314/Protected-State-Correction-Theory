# Branch Audit

## Purpose

This note audits the repository as a branch-based research program rather than as a finished framework. Every branch is treated honestly: strongest result, strongest failure, strongest limitation, and whether it is worth pushing harder.

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
| Restricted-linear / design-engine layer | measurement sufficiency, minimal augmentation, and design diagnostics on restricted families | OCP-T6 restricted-linear minimal augmentation theorem | below-deficiency augmentation impossibility | limited to restricted finite-dimensional linear families | strongest practical theorem-to-tool branch | yes, heavily |
| Practical workbench / studio layer | turning the theory into decisions, diagnosis, and next-step guidance | real recoverability / correction studio with artifact-backed outputs | fake or weak interactivity gets caught by browser and static tests | usefulness depends on keeping it wired to the actual math | tool layer | yes, but only when coupled to clean branch results |
| Rejected / demoted directions | optimizer, generic constrained-Hamiltonian automatic fit, universal scalar capacity | none | broad claims fail repeatedly | not worth renewed effort without new operators or theorems | frozen | no |

## Strongest Current Backbone

The repo's current backbone is:
- exact branch as the finite-dimensional anchor,
- exact sector/QEC branch as the clean sector-conditioned anchor,
- exact periodic projection as the clean continuous anchor,
- asymptotic generator branch as the strongest finished continuous theorem branch,
- constrained-observation and restricted-linear design layers as the strongest current open theorem/program branches,
- no-go layer as the main scope-control mechanism.

## Strongest Current Contribution Candidates

1. constrained-observation / restricted-linear threshold and augmentation theorems
2. bounded-domain exact correction under explicit boundary-compatible Hodge assumptions
3. asymptotic generator completion beyond invariant splits, if a sharper theorem survives

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
