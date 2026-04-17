# Next-Phase Tool Integration (2026-04-16)

## Integration Decision

This pass integrates next-phase mathematics into the validation/tooling pipeline first, and defers UI promotion until theorem-backed labels are mapped in the workbench surface.

Implemented now:
- deterministic next-phase artifact generation in full validation gate,
- reproducibility tests for next-phase artifacts,
- branch-scoped docs linked into main research navigation.

## Implemented Pipeline Hooks

- generator script: [`scripts/compare/run_next_phase_examples.py`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/scripts/compare/run_next_phase_examples.py)
- validation gate hook: [`scripts/validate/run_all.sh`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/scripts/validate/run_all.sh)
- consistency tests: [`tests/examples/test_next_phase_examples_consistency.py`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/tests/examples/test_next_phase_examples_consistency.py)

Generated artifacts:
- [`data/generated/next-phase/next_phase_summary.json`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/data/generated/next-phase/next_phase_summary.json)
- [`data/generated/next-phase/quantitative_profiles.csv`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/data/generated/next-phase/quantitative_profiles.csv)
- [`data/generated/next-phase/fragility_rank_deficient.csv`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/data/generated/next-phase/fragility_rank_deficient.csv)
- [`data/generated/next-phase/fragility_full_rank.csv`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/data/generated/next-phase/fragility_full_rank.csv)
- [`data/generated/next-phase/dynamic_accumulation.csv`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/data/generated/next-phase/dynamic_accumulation.csv)
- [`data/generated/next-phase/generator_dynamics.csv`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/data/generated/next-phase/generator_dynamics.csv)
- [`data/generated/next-phase/cfd_deep_dive.csv`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/data/generated/next-phase/cfd_deep_dive.csv)
- [`data/generated/next-phase/structure_classes.csv`](/Users/stevenreid/Documents/New project/repos/ocp-research-program/data/generated/next-phase/structure_classes.csv)

## Why UI Changes Were Deferred

- No speculative indicator is allowed to appear as theorem-backed.
- The current workbench evidence taxonomy requires explicit theorem-ID mapping before promotion.
- This pass prioritized theorem/test/artifact integrity and branch-scoped falsification.

## Safe Next UI Step

When promoted, add read-only panels with explicit evidence labels:
1. quantitative recoverability profile (`r_row`, `theta_def`, `gamma`, `delta`, `||D||`),
2. fragile-exact vs robust-exact badge,
3. finite-time no-go vs asymptotic-rate badge,
4. bounded-domain boundary-obstruction warning ratio.

All four should remain branch-gated and labeled with proof/validation status.
