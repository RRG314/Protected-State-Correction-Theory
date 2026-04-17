# Unified Paper Template (Program Standard)

This template enforces shared style while allowing field-specific emphasis.

## Canonical author block
- Name: Steven Reid
- Affiliation line: Independent Researcher
- ORCID line: ORCID: 0009-0003-9132-3410
- Email line: sreid1118@gmail.com
- Date line: Month Year

## Front matter layout
1. Title
2. Author block (4 lines above)
3. Date
4. Abstract (single paragraph)
5. Keywords (single line)
6. Optional: MSC classifications (for math-facing versions)

## Required section skeleton (all papers)
1. Introduction
2. Problem Setup / Mathematical Setup
3. Main Results
4. Proofs / Derivations
5. Examples / Validation / Computations
6. Interpretation and Implications
7. Limitations and Scope
8. Conclusion
9. References
10. Appendix (if needed)

## Status labeling rules (mandatory)
Every promoted result gets one label:
- `PROVED`
- `VALIDATED`
- `CONDITIONAL`
- `OPEN`
- `INTERPRETATION`

Never use `VALIDATED` to imply theorem-level certainty.

## Theorem style
- Numbered environments in text style:
  - Theorem n
  - Proposition n
  - Corollary n
  - Example n
- Follow each formal statement with:
  - status label,
  - explicit assumptions,
  - short proof sketch or pointer.

## Table style
Recommended summary table columns:
- Result
- Claim (1-line statement)
- Status
- Evidence
- Scope

## Field emphasis variants

### MHD paper variant
- Heavier derivation and domain-classification sections.
- Distinguish constant-coefficient exactness from variable-coefficient obstruction.
- Keep symbolic checks as verification, not proof replacement.

### OCP core paper variant
- Heavier theorem/counterexample density.
- Include restricted-linear criterion and anti-classifier no-go theorems.
- Include minimal augmentation theorem and explicit repaired example.

### Bridge paper variant
- Heavier contrast architecture (exact periodic vs bounded failure).
- Include mechanism section explaining boundary compatibility.
- Strong explicit scope control; avoid unification inflation.

## Abstract checklist
Abstract must include, in order:
1. problem class,
2. main positive result(s),
3. main no-go/failure result(s),
4. scope/limitation clause.

## References checklist
- Include foundational mathematical references and method references.
- Include only claims actually used.
- Keep novelty statements conservative and explicit.
