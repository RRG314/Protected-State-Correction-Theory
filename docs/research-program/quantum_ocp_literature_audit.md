# Quantum-OCP Literature Audit

Status: literature-aware conceptual audit for quantum mapping of the OCP/recoverability corpus.

This document does not claim literature novelty by default. It classifies where the pass lands relative to standard quantum mechanics and quantum information structures.

## A. Quantum Measurement Theory

Nearest standard areas:
- projective/POVM measurement models,
- informational completeness,
- incompatibility of measurement bases for full-state recovery.

Pass finding:
- `QW001-QW004` reproduce basis-sensitive recovery and one-added-basis restoration in finite sampled families.

Classification:
- **ALREADY KNOWN IN SUBSTANCE** for fixed-basis phase-loss.
- **CLOSE PRIOR ART / REPACKAGED** for OCP framing of target-specific recoverability from incomplete measurements.

## B. State Distinguishability / Discrimination

Nearest standard areas:
- Helstrom-style discrimination limits,
- measurement-induced indistinguishability classes.

Pass finding:
- explicit record-collision no-go appears as finite fiber collision (`QW001`, `QA004`).

Classification:
- **ALREADY KNOWN IN SUBSTANCE** at theorem core.
- OCP contribution is packaging at target/family language level.

## C. Channels and Recoverability

Nearest standard areas:
- channel recoverability,
- Petz/recovery map literature,
- sufficiency and coarse-graining.

Pass finding:
- dephasing sweep (`QW011-QW017`) reproduces target fragility and collapse behavior in a finite target class.

Classification:
- **ALREADY KNOWN IN SUBSTANCE** for channel-side mechanism.
- **CLOSE PRIOR ART / REPACKAGED** for anti-classifier-style presentation of target collapse.

## D. QEC and Sector Structure

Nearest standard areas:
- Knill-Laflamme conditions,
- syndrome-sector correctability.

Pass finding:
- `QW018` confirms exact anchor behavior through existing repo code.

Classification:
- **ALREADY KNOWN IN SUBSTANCE**.
- Kept as canonical anchor; no novelty claim.

## E. Quantum Fisher / Estimation / Cramér-Rao

Nearest standard areas:
- classical/quantum Fisher information for parameter estimation,
- measurement design for parameter sensitivity.

Pass finding:
- same-setting-count but opposite target FI split retained (`QW019-QW024`, `QA009`).

Classification:
- **CLOSE PRIOR ART / REPACKAGED** for theorem content.
- **PLAUSIBLY DISTINCT PACKAGING** as a strict target-recoverability diagnostic lane tied to anti-classifier logic.

## F. Contextuality / Basis Dependence

Nearest standard areas:
- basis dependence,
- incompatible observables,
- contextual measurement dependence.

Pass finding:
- context-gain family (`QW005-QW008`) yields conditioned exactness with invariant failure and one-step shared augmentation restoration.

Classification:
- **PLAUSIBLY DISTINCT** as a scoped “conditioned vs invariant decoder” package.
- Not a claim of new contextuality theorem in the Kochen-Specker sense.

## G. Quantum Control / Observability / Tomography

Nearest standard areas:
- quantum observability,
- minimal tomographic settings,
- measurement scheduling.

Pass finding:
- one-added-setting restoration (`QW003/QW004`) and context-augmentation split (`QW005-QW008`) provide direct finite design witnesses.

Classification:
- **CLOSE PRIOR ART / REPACKAGED** for core facts.
- **PLAUSIBLY DISTINCT** in unified anti-classifier + augmentation-threshold packaging.

## H. Distributed / Multipartite Allocation

Nearest standard areas:
- distributed sensing,
- local-vs-global measurement limitations,
- entangled observable access.

Pass finding:
- same budget opposite verdict from allocation geometry (`QW009/QW010`, `QA007`).

Classification:
- **PLAUSIBLY DISTINCT** in scoped formulation as target-specific allocation no-go.
- Mechanism itself is close to known local/global measurement distinctions.

## I. Open Systems / Decoherence

Nearest standard areas:
- coherence decay,
- environment-induced information loss.

Pass finding:
- explicit finite target collapse at complete dephasing in this family (`QW011-QW017`, `QA008`).

Classification:
- **ALREADY KNOWN IN SUBSTANCE**.
- Useful as fragility benchmark tied back to OCP target language.

## J. Foundations (Optional)

No broad foundational promotion survives this pass.

Classification:
- **ANALOGY ONLY** for broad interpretive claims.

## Literature-Risk Conclusion

- Theorem novelty risk is high if claims are framed as new quantum mechanics.
- A narrow lane survives: target-specific measurement/design and context-sensitive decoder compatibility, with explicit finite witnesses and strict scope labels.
- Safe lane characterization: **quantum design/measurement extension of OCP language**, not a replacement for quantum theory.
