# SFPR Formation Candidates

Status: `EXPLORATION / NON-PROMOTED`

Artifact reference: `data/generated/sfpr/formation_witnesses.csv` (`560` rows).

## Objective

Test whether "structure formation" can be formalized as a mechanism that changes target-relevant recoverability, not just generic dynamics.

## Route-by-Route Results

### 1) Constraint generation
- Observed pattern: `80/80` new-structure flags, `80/80` recoverability improvements.
- Status: `VALIDATED / EMPIRICAL ONLY`.
- Validity warning: many witnesses are constructive by setup (added target-aligned constraint), so theorem novelty is limited.

### 2) Symmetry breaking
- Observed pattern: `80/80` new-structure flags, `80/80` recoverability improvements.
- Status: `VALIDATED / EMPIRICAL ONLY`.
- Validity warning: strong constructive bias; needs adversarial symmetric families beyond current templates.

### 3) Context-conditioned differentiation
- Observed pattern: no new-structure flags under current metric; no recoverability change.
- Status: `DISPROVED` for current definition.
- Interpretation: this route did not generate useful structure deltas under tested metric design.

### 4) Feedback-induced organization
- Observed pattern: `74/80` new-structure flags, `0/80` recoverability improvements; `74/80` formation-without-recoverability cases.
- Status: `PLAUSIBLY DISTINCT` empirical failure mode.
- Interpretation: optimization/feedback can improve alignment-like structure while leaving exactness unchanged.

### 5) Local-to-global organization
- Observed pattern: no measurable structure/recoverability changes under current setup.
- Status: `DISPROVED` for current template.

### 6) Intervention-generated structure
- Observed pattern: `80/80` new-structure flags, `80/80` recoverability improvements.
- Status: `VALIDATED / EMPIRICAL ONLY`.
- Overlap note: close to known intervention-cleaning intuition; novelty risk high.

### 7) Optimization-induced structure
- Observed pattern: `69/80` new-structure flags, `0/80` recoverability improvements; `69/80` formation-without-recoverability.
- Status: `PLAUSIBLY DISTINCT` empirical failure mode.
- Interpretation: objective-driven structural refinement does not guarantee exact target recovery.

## Formation Layer Outcome

Strong keep:
- formation-without-recoverability anomaly class (feedback and optimization routes).

Weak/needs redesign:
- context-conditioned differentiation and local-to-global routes (current metrics do not detect meaningful change).

High-risk routes (constructive bias):
- constraint generation, symmetry breaking, intervention-generated structure.

## Immediate Next Formalization Target

Replace route-level narratives with a typed formation operator criterion:
- `F` is nontrivial only if it changes target-fiber geometry (`DLS`, collision profile, or shared-decoder feasibility) under fixed descriptor budgets.
