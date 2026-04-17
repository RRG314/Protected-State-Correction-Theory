# Stopping-Logic Compatibility Memo

## Purpose

This note asks whether a serious `stop / switch / augment / change-architecture` layer belongs inside the current fiber-based recoverability / impossibility branch.

The answer after falsification is:
- yes, but only as a **small decision layer** on top of the existing theorem package,
- no, not as a new theory branch,
- and definitely not as generic optimization-style early stopping.

## Where the idea connects naturally

Stopping logic emerges cleanly from the current branch in six places.

1. **Fiber-mixing impossibility**
   - If the target is not constant on the active record fibers, exact pursuit is structurally futile.
   - This is the cleanest stop condition.
   - Backbone: `OCP-030`, overlap/no-go logic, collapse-modulus lower bounds.

2. **Weaker-versus-stronger target splits**
   - If the stronger target fails but a coarsened target is exact on the same record, the natural action is to switch target rather than continue a doomed exact pursuit.
   - Backbone: `OCP-048`, `OCP-051`.

3. **Minimal augmentation structure**
   - If exact recovery fails but the minimal augmentation count is finite and known, the natural decision is augment-versus-stop, not generic persistence.
   - Backbone: `OCP-045` and the restricted-linear design layer.

4. **Architecture mismatch**
   - In bounded-domain and control examples, the right decision is sometimes not “stop everything” but “change architecture.”
   - Backbone: bounded-domain Hodge replacement, finite-history versus observer split.

5. **Family fragility**
   - If exactness survives only on a narrow family and fails immediately under honest enlargement, the right decision is to stop promoting the positive result.
   - Backbone: `OCP-052`.

6. **Model-mismatch instability**
   - If the inverse map is exact on one family but incurs a controlled exact-data error on the true family, the right decision is to stop trusting the decoder until the family model is repaired.
   - Backbone: `OCP-053`.

## Where the idea does not connect naturally

The idea does **not** justify:
- a universal stopping scalar,
- a universal rank/count/budget stopping law,
- a branch rename,
- or a new standalone theorem program.

Those stronger versions fail because the current branch already proves that amount-only classifiers are unsound on supported families.

## Where stopping logic would duplicate existing work badly

Bad duplication appears when “stop” means only:
- “impossible” restated with softer language,
- “minimal augmentation exists” restated without budget context,
- or “be careful” without a theorem-backed false-positive mechanism.

Those versions add very little and should not be promoted.

## What genuinely useful structure survives

A modest but real decision layer survives.

Its honest role is:
- convert exact/no-go/fiber-fragility results into explicit actions,
- improve false-positive handling,
- and help the workbench say **what to do next** without pretending to solve a broader inverse-problem class than the repo actually supports.

## Final compatibility verdict

- compatible with the branch: `yes`
- strong enough for a new branch: `no`
- strongest form: **theorem-linked decision layer inside the current branch**
- strongest value: **stop exact pursuit, switch target, augment, change architecture, or stop promotion when the current theorem package says so**
