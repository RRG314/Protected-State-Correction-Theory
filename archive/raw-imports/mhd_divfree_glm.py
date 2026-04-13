from __future__ import annotations

import time
import numpy as np

from .metrics import divergence_2d, div_metrics


def clean_B_glm(
    Bx: np.ndarray,
    By: np.ndarray,
    psi: np.ndarray,
    dx: float,
    dy: float,
    dt: float,
    *,
    ch: float = 1.0,
    cp: float = 1.0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, dict[str, float]]:
    """One Dedner-style GLM cleaning step for 2D B-field."""
    t0 = time.perf_counter()
    before = div_metrics(Bx, By, dx, dy)
    e_before = float(np.mean(0.5 * (Bx * Bx + By * By)))

    dpsix = (np.roll(psi, -1, axis=0) - np.roll(psi, 1, axis=0)) / (2.0 * dx)
    dpsiy = (np.roll(psi, -1, axis=1) - np.roll(psi, 1, axis=1)) / (2.0 * dy)
    divB = divergence_2d(Bx, By, dx, dy)

    Bx_new = Bx - dt * dpsix
    By_new = By - dt * dpsiy
    damping = (ch * ch / max(cp * cp, 1e-12))
    psi_new = psi - dt * (ch * ch * divB + damping * psi)

    after = div_metrics(Bx_new, By_new, dx, dy)
    e_after = float(np.mean(0.5 * (Bx_new * Bx_new + By_new * By_new)))
    runtime = time.perf_counter() - t0

    report = {
        "before_l2_divB": before["l2_divB"],
        "after_l2_divB": after["l2_divB"],
        "before_max_abs_divB": before["max_abs_divB"],
        "after_max_abs_divB": after["max_abs_divB"],
        "energy_change": e_after - e_before,
        "runtime_seconds": runtime,
    }
    return Bx_new, By_new, psi_new, report
