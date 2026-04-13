from __future__ import annotations

import numpy as np

from mhd_toolkit.divfree.glm import clean_B_glm
from mhd_toolkit.divfree.metrics import div_metrics
from mhd_toolkit.divfree.projection import clean_B_projection


def test_projection_cleaning_reduces_l2_divergence() -> None:
    nx, ny = 64, 64
    dx = dy = 1.0 / nx
    x = np.linspace(0.0, 1.0, nx, endpoint=False)
    y = np.linspace(0.0, 1.0, ny, endpoint=False)
    X, Y = np.meshgrid(x, y, indexing="ij")

    Bx = np.sin(2.0 * np.pi * X) + 0.03 * np.cos(6.0 * np.pi * Y)
    By = np.cos(2.0 * np.pi * Y) + 0.03 * np.sin(4.0 * np.pi * X)

    before = div_metrics(Bx, By, dx, dy)["l2_divB"]
    bx_new, by_new, _ = clean_B_projection(Bx, By, dx, dy)
    after = div_metrics(bx_new, by_new, dx, dy)["l2_divB"]
    assert after < before


def test_glm_cleaning_reduces_l2_divergence_over_steps() -> None:
    nx, ny = 48, 48
    dx = dy = 1.0 / nx
    x = np.linspace(0.0, 1.0, nx, endpoint=False)
    y = np.linspace(0.0, 1.0, ny, endpoint=False)
    X, Y = np.meshgrid(x, y, indexing="ij")

    Bx = np.sin(2.0 * np.pi * X) + 0.02 * np.sin(4.0 * np.pi * Y)
    By = np.cos(2.0 * np.pi * Y) + 0.02 * np.cos(4.0 * np.pi * X)
    psi = np.zeros_like(Bx)

    before = div_metrics(Bx, By, dx, dy)["l2_divB"]
    for _ in range(8):
        Bx, By, psi, _ = clean_B_glm(Bx, By, psi, dx, dy, dt=0.05, ch=1.0, cp=1.0)
    after = div_metrics(Bx, By, dx, dy)["l2_divB"]
    assert after < before
