# Claim-Scope Gate

## Purpose

This gate prevents theorem-surface drift into unsupported scope claims.

Script:
- `scripts/validate/check_claim_scope.py`

## Enforced Checks

1. Forbidden ontology-style phrases in active theorem-facing lanes, including:
   - `new theory of information`
   - `information is a/the force`
   - `information is fundamental`
   - `information creates reality`
   - `gravity is made of information`
   - `dark matter is information`
2. Unscoped universal-claim phrasing unless explicitly negated or rejected, including:
   - `universal information law`
   - `universal law of information`
   - `universal scalar invariant`
   - `universal scalar correction capacity`
3. SDS mentions inside theorem-core and restricted-result lanes unless explicitly guarded with scope language.

## Covered Surfaces

- `README.md`
- `docs/theorem-core/`
- `docs/restricted-results/`
- `docs/physics-translation/`
- `docs/overview/`

## Validation Integration

The script is part of the local validation flow through `scripts/validate/run_all.sh`.

Latest sample run artifact:
- `data/generated/validations/claim_scope_gate_latest.txt`

Regression tests:
- `tests/examples/test_claim_scope_gate.py`

## Scope

This is a guardrail. It does not certify theorem correctness. It enforces claim discipline and non-inflation boundaries that were mandated in the overlap and hardening audits.
