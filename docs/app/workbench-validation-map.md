# Workbench Validation Map

## Core workbench regression surfaces
- `tests/consistency/workbench_static.test.mjs`
- `tests/consistency/discovery_mixer_static.test.mjs`
- `tests/consistency/workbench_store.test.mjs`

## Artifact and report consistency
- `tests/examples/test_workbench_examples_consistency.py`
- `tests/examples/test_validation_consistency.py`

## Known-answer and adversarial coverage
- `tests/math/test_professional_known_answers.py`
- `tests/math/test_adversarial_validation.py`

## Repo-wide gate
- `scripts/validate/run_all.sh`

## Independence notes
Strongest checks:
- Node static workbench tests against expected structured outputs
- Python known-answer and adversarial tests
- generated artifact consistency tests

Partially circular checks that remain intentionally limited:
- some generated-artifact freshness checks still verify consistency against current generator code rather than an independent mathematical engine
- figure export is still validated through UI-path behavior rather than an independent renderer
