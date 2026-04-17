# Theory Candidate Comparison (2026-04-16)

## Goal

Test whether the integrated lens survivors support a genuine theory candidate rather than a bundle of rephrasings.

A candidate is accepted only if it has:
- clear central object,
- clear invariant family,
- explicit regime classification,
- positive and negative laws,
- and real design/diagnostic leverage.

## Candidate 1 — Restricted Recoverability-Structure Theory (RRT)

Definition:
- Object: recoverability of protected targets under constrained observation on admissible families.
- Core invariants: fiber constancy/factorization, row-space-kernel alignment (`ker(T*)`/row inclusion), collision gap, augmentation deficiency.
- Regimes: exact, stable approximate, asymptotic, impossible, repairable-by-augmentation.

Cross-branch test:
- constrained-observation branch: strong fit (`OCP-030` through `OCP-047`).
- fiber/unified limits branch: strong fit (`OCP-048` through `OCP-053`).
- design/decision layer: strong fit (`OCP-045` and structured recommendations).
- exact projector/QEC/periodic exact branches: only partial transfer (mostly interpretation).
- bounded-domain/Hodge: indirect but compatible (obstruction can be expressed as structural hidden directions).

Nontrivial predictions:
- same-rank and same-budget can yield opposite exactness verdicts,
- weak-target exactness can coexist with strong-target impossibility,
- exact-on-small-family can fail on enlarged family,
- minimal unrestricted augmentation count is computable and predictive.

Collapse test:
- does it reduce to rank-only language? no.
- does it reduce to pure restatement of one theorem? no.
- does it overclaim universality? only if extended beyond restricted/family-aware scope.

Verdict: `SURVIVES` (branch-limited, strong).

## Candidate 2 — Boundary-Topology Sensitive Exactness Theory (BTSET)

Definition:
- Object: exact correction compatibility on bounded domains.
- Core invariants: boundary compatibility class, Hodge decomposition class, topology-sensitive obstruction signals (`b1` lane), domain-aware projector availability.
- Regimes: exact bounded projection, conditional exactness, asymptotic-only, impossible.

Cross-branch test:
- bounded-domain/CFD branch: strong fit (`OCP-023`, `OCP-028`, `OCP-029`, `OCP-044`).
- periodic Helmholtz branch: fit as boundary-free baseline.
- Maxwell/gauge and asymptotic generator: partial compatibility only.
- constrained-observation/fiber branches: weak transfer (different central object).

Nontrivial predictions:
- divergence-only or boundary-oblivious transplants fail on bounded protected classes,
- exactness can survive on explicit boundary-compatible finite-mode families,
- topology/domain class can determine whether projector correction is viable.

Collapse test:
- does it add more than known Hodge facts? partially, through OCP-specific exact/no-go packaging and executable witnesses.
- does it currently cover broad PDE families? no.

Verdict: `PARTIAL` (real branch theory lane, not yet broad enough for top-level repo theory).

## Candidate 3 — Universal Quotient/Fiber Theory Across All Branches

Definition:
- Object: every branch reduced to one quotient/fiber geometry law.

Cross-branch test:
- constrained/fiber branches: works.
- exact projector/QEC/periodic branches: often collapses to trivial restatement.
- bounded-domain and asymptotic branches: misses boundary/spectral machinery unless augmented by non-fiber structure.

Collapse test:
- does it preserve branch-specific theorem power? no.
- does it avoid branch flattening? no.

Verdict: `COLLAPSES`.

## Candidate 4 — Operator-Semigroup Unified Correction Theory

Definition:
- Object: correction/recoverability characterized by operators, kernels, spectra, and factorization.
- Core invariants: kernel obstruction, row-space inclusion, spectral gap/abscissa, bounded-domain operator class compatibility.

Cross-branch test:
- exact projector/QEC/periodic/asymptotic: strong fit.
- constrained/fiber: strong fit for linear and restricted families.
- bounded-domain: strong only when paired with FA/Hodge/topology terms.
- workbench/design: useful because invariants are computable.

Collapse test:
- does it produce new laws beyond rewording? yes in restricted branches (anti-classifier, family-enlargement, mismatch package) but not uniformly.
- is one operator law enough globally? no; boundary/topology and family restrictions remain essential.

Verdict: `PARTIAL` (best broad language backbone, but not a single complete theory).

## Comparative Verdict Matrix

| Candidate | Positive law strength | No-go strength | Cross-branch transfer | Design value | Verdict |
| --- | --- | --- | --- | --- | --- |
| Restricted Recoverability-Structure Theory | high | high | medium | high | `SURVIVES` |
| Boundary-Topology Sensitive Exactness Theory | medium | high | low-medium | medium | `PARTIAL` |
| Universal Quotient/Fiber Theory | low | medium | low | low | `COLLAPSES` |
| Operator-Semigroup Unified Correction Theory | medium-high | medium-high | medium-high | high | `PARTIAL` |

## Theory Formation Implication

The strongest honest outcome is:
- one serious **partial theory candidate** survives (restricted recoverability-structure lane),
- one bounded-domain theory lane is promising but still branch-limited,
- universal single-law unification does not survive falsification.

This supports repository-level decision `B` (partial candidate survives, still branch-limited).
