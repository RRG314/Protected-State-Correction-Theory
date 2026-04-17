# What A Fiber Is And Why It Matters

A fiber is the set of admissible states that produce the same record.

If your measurement map is `M`, then the fiber over the observed value `y` is:

```text
Fib_M(y) = { x in F : M(x) = y }.
```

Why this matters:
- if the protected target is the same for every state in that fiber, the record can still determine the target exactly
- if different target values live in the same fiber, exact recovery is impossible

This is the cleanest way to say what information loss really is.
It is not just “low rank” or “too few sensors.”
It is target-relevant ambiguity inside the fiber.

## Practical translation

When a setup fails, ask:
- what states look identical to the record?
- do those states still disagree on the target?
- if yes, can I refine the record fibers by adding measurements?
- if not, can I weaken the target until it becomes constant on the current fibers?

That is the main practical use of this branch.
