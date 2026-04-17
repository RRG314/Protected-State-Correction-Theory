# Workbench Guidance

The recoverability studio now carries explicit warning surfaces for this branch.

## New warning classes

Supported recoverability analyses can now surface:
- family-restriction warnings,
- target-strength warnings,
- model-mismatch warnings,
- discretization/refinement warnings,
- wrong-architecture warnings,
- anti-classifier warnings.

## How to read an exact verdict

An exact verdict should now be read as:
- exact on the current declared family,
- with the current target,
- under the current architecture,
- and only with the current support/evidence scope label.

It should **not** be read as automatic evidence for:
- larger admissible families,
- nearby unmodeled families,
- stronger targets,
- finer discretizations,
- or different architectures.

## What changed in the workbench

Recoverability analyses and exported reports now include:
- a support-scope label,
- a decision-posture label,
- fiber-language explanations,
- false-positive warnings tied to the current family,
- and stronger reminders when success is weaker-target-only or family-restricted.

## How to read the new decision posture

The decision posture is useful only because it is derived from existing theorem-backed or validated-family recommendations.

It can now say:
- continue exact recovery attempt,
- switch to a weaker target,
- augment the record,
- change architecture,
- stop exact pursuit,
- or continue only with fragility caution on the current family.

It should not be read as:
- a universal stopping theorem,
- a solver-independent optimal policy,
- or evidence that the repo supports arbitrary inverse-problem architecture design.
