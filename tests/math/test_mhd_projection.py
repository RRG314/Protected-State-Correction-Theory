from __future__ import annotations

import numpy as np

from ocp.mhd import divergence_2d, helmholtz_project_2d, orthogonality_residual_2d


def _gradient_2d(phi: np.ndarray, dx: float, dy: float) -> tuple[np.ndarray, np.ndarray]:
    gx = (np.roll(phi, -1, axis=0) - np.roll(phi, 1, axis=0)) / (2.0 * dx)
    gy = (np.roll(phi, -1, axis=1) - np.roll(phi, 1, axis=1)) / (2.0 * dy)
    return gx, gy


def _divfree_from_stream(psi: np.ndarray, dx: float, dy: float) -> tuple[np.ndarray, np.ndarray]:
    dpsix = (np.roll(psi, -1, axis=0) - np.roll(psi, 1, axis=0)) / (2.0 * dx)
    dpsiy = (np.roll(psi, -1, axis=1) - np.roll(psi, 1, axis=1)) / (2.0 * dy)
    return dpsiy, -dpsix


def test_helmholtz_projection_recovers_divergence_free_component() -> None:
    nx = ny = 64
    dx = dy = 1.0 / nx
    x = np.linspace(0.0, 1.0, nx, endpoint=False)
    y = np.linspace(0.0, 1.0, ny, endpoint=False)
    X, Y = np.meshgrid(x, y, indexing="ij")

    psi = np.sin(2.0 * np.pi * X) * np.sin(2.0 * np.pi * Y)
    phi = 0.2 * np.cos(4.0 * np.pi * X) * np.cos(2.0 * np.pi * Y)

    bx_phys, by_phys = _divfree_from_stream(psi, dx, dy)
    gx, gy = _gradient_2d(phi, dx, dy)
    bx = bx_phys + gx
    by = by_phys + gy

    before = np.sqrt(np.mean(divergence_2d(bx, by, dx, dy) ** 2))
    bx_proj, by_proj, _, _ = helmholtz_project_2d(bx, by, dx, dy)
    after = np.sqrt(np.mean(divergence_2d(bx_proj, by_proj, dx, dy) ** 2))

    assert after < before * 1e-2
    assert np.allclose(bx_proj, bx_phys, atol=5e-3)
    assert np.allclose(by_proj, by_phys, atol=5e-3)
    assert orthogonality_residual_2d(bx, by, dx, dy) < 1e-5
