# Divergence Control

This toolkit includes two divergence-cleaning methods for 2D magnetic fields.

## Projection Cleaning

Algorithm:

1. Compute `divB = dBx/dx + dBy/dy`
2. Solve `laplacian(phi) = divB`
3. Correct:
   - `Bx <- Bx - dphi/dx`
   - `By <- By - dphi/dy`

Implementation:
- `mhd_toolkit.divfree.projection.clean_B_projection`
- periodic FFT solver by default
- Jacobi fallback available

Pros:
- Strong immediate reduction of `||divB||`
- Deterministic for fixed grid and data

Tradeoffs:
- Requires Poisson solve
- Can introduce small magnetic-energy changes

## GLM Cleaning

Dedner-style lightweight cleaning with scalar `psi`:

- `B <- B - dt * grad(psi)`
- `psi <- psi - dt * (ch^2 * divB + (ch^2/cp^2) * psi)`

Implementation:
- `mhd_toolkit.divfree.glm.clean_B_glm`

Pros:
- Local and cheap per-step update
- Easy to integrate into explicit stepping loop

Tradeoffs:
- Usually needs multiple steps for strong cleaning
- Parameter sensitivity (`ch`, `cp`, `dt`)

## Usage

```bash
python -m mhd_toolkit divfree demo --problem orszag-tang --method projection,glm
```

The output JSON includes before/after divergence norms, energy change, and runtime.
