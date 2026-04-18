# Quantum Alignment Literature Audit

Status: literature-risk positioning for the corrected quantum-alignment lane.

Scope:
- This is a literature-overlap risk audit, not a novelty claim.
- We classify each surviving component before any public-facing promotion language.

## Core overlap assessment

## L1. `alpha_Q = sqrt(F_M/F_Q)` notation

Nearest literature:
- Helstrom information bounds; Braunstein-Caves quantum/classical Fisher relation.

Assessment:
- Substance is standard.
- The `alpha_Q` scalar is a repackaging for diagnostic readability.

Classification:
- `KNOWN IN SUBSTANCE` / `REFRAMED KNOWN RESULT`.

## L2. SLD commutator incompatibility discussion

Nearest literature:
- Matsumoto-style multiparameter compatibility criteria; Holevo multiparameter bounds.

Assessment:
- Noncommuting SLDs as incompatibility signal is standard.
- The lane adds a worked numeric witness, not a new incompatibility theorem.

Classification:
- `KNOWN IN SUBSTANCE`.

## L3. Projective qubit conservation identity (`alpha_1^2 + alpha_2^2 = 1` in diagonal form)

Nearest literature:
- Multiparameter qubit Fisher tradeoff geometry and Gill-Massar-type trace bounds.

Assessment:
- Strong risk this is an explicit qubit special-case restatement of known `trace(F_Q^{-1}F_M)` constraints.
- Current safest language is that this is a clean restricted-class derivation and packaging.

Classification:
- `POSSIBLY IMPLICIT KNOWN SPECIAL CASE` / `REFRAMED KNOWN RESULT` risk is high.

## L4. Coordinate-invariant trace form (`trace(F_Q^{-1}F_M)=1` on restricted qubit class)

Nearest literature:
- Gill-Massar qubit information-region characterizations and related attainable-Fisher geometry.

Assessment:
- Very likely close to known qubit Fisher-geometry constraints.
- In this repo it is useful because it gives a direct, testable branch-limited identity with explicit assumptions.

Classification:
- `CLOSE PRIOR ART / REPACKAGED` with possible narrow derivation-value.

## L5. Mixed-state and unsharp attenuation behavior

Nearest literature:
- Standard non-projective and noisy-measurement Fisher loss in quantum estimation/metrology.

Assessment:
- Expected behavior; no novelty claim justified.

Classification:
- `KNOWN IN SUBSTANCE`.

## L6. Higher-dimensional collapse of qubit constant

Nearest literature:
- Known dimension-sensitive attainable-information geometry; no single qubit constant expected in general.

Assessment:
- Negative result is consistent with known structure.

Classification:
- `KNOWN IN SUBSTANCE` as boundary discipline.

## Safe claim language

Allowed:
- “On a restricted two-parameter qubit class, we prove a clean conservation/tradeoff identity and provide explicit correction and falsification boundaries.”
- “This lane is a branch-limited measurement-design corollary layer.”

Not allowed:
- “New quantum foundation.”
- “Universal alpha conservation law.”
- “Replaces existing multiparameter quantum estimation theory.”

## Literature-risk verdict

Overall risk profile:
- foundational novelty risk: high,
- branch-level packaging value: medium,
- theorem clarity on restricted class: strong,
- safe integration level: narrow quantum measurement-design sub-branch.

