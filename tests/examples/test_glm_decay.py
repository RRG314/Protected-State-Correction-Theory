from __future__ import annotations

import numpy as np

from ocp.mhd import divergence_2d, glm_step_2d


def test_glm_step_reduces_divergence_over_multiple_steps() -> None:
    nx = ny = 48
    dx = dy = 1.0 / nx
    x = np.linspace(0.0, 1.0, nx, endpoint=False)
    y = np.linspace(0.0, 1.0, ny, endpoint=False)
    X, Y = np.meshgrid(x, y, indexing="ij")

    Bx = np.sin(2.0 * np.pi * X) + 0.03 * np.sin(4.0 * np.pi * Y)
    By = np.cos(2.0 * np.pi * Y) + 0.03 * np.cos(4.0 * np.pi * X)
    psi = np.zeros_like(Bx)

    before = float(np.sqrt(np.mean(divergence_2d(Bx, By, dx, dy) ** 2)))
    for _ in range(8):
        Bx, By, psi = glm_step_2d(Bx, By, psi, dx, dy, dt=0.05, ch=1.0, cp=1.0)
    after = float(np.sqrt(np.mean(divergence_2d(Bx, By, dx, dy) ** 2)))
    assert after < before
