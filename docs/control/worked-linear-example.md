# Worked Linear Control-Style Example

## Plain-Language Summary

This example shows the control-side OCP logic in the most grounded finite-dimensional setting.

We take a linear flow with one protected coordinate and two disturbance coordinates. The generator is chosen so that:
- the protected coordinate is untouched,
- the disturbance coordinates feed only into themselves,
- and the disturbance block is exponentially stable.

## Example

Use the decomposition

```text
H = S ⊕ D,   S = span(e_1),   D = span(e_2, e_3)
```

and the generator

```text
K = [[0, 0, 0],
     [0, 1, 1],
     [0, 0, 3/2]].
```

Then:
- `K` annihilates `S`,
- `K(D) ⊆ D`,
- and the disturbance block has positive real spectrum.

So the flow `x_dot = -Kx` preserves the first coordinate exactly and damps the disturbance coordinates exponentially.

## Why This Example Matters

This is the cleanest control-style demonstration in the repo because it separates three cases clearly:
- good architecture: invariant split plus stable disturbance block,
- weak architecture: stable but not interpretation-safe,
- bad architecture: disturbance mixes into the protected coordinates.

The corresponding failure case is captured in the linear-flow mixing no-go result.
