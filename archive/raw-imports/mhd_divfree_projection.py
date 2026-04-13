from __future__ import annotations

import time
import numpy as np

from .metrics import divergence_2d, div_metrics


def _solve_poisson_fft(rhs: np.ndarray, dx: float, dy: float) -> np.ndarray:
    nx, ny = rhs.shape
    kx = 2.0 * np.pi * np.fft.fftfreq(nx, d=dx)
    ky = 2.0 * np.pi * np.fft.fftfreq(ny, d=dy)
    KX, KY = np.meshgrid(kx, ky, indexing="ij")
    k2 = KX * KX + KY * KY
    rhs_hat = np.fft.fftn(rhs)
    phi_hat = np.zeros_like(rhs_hat)
    mask = k2 > 0.0
    phi_hat[mask] = -rhs_hat[mask] / k2[mask]
    phi_hat[~mask] = 0.0
    return np.fft.ifftn(phi_hat).real


def _solve_poisson_jacobi(rhs: np.ndarray, dx: float, dy: float, max_iter: int = 400, tol: float = 1e-8) -> np.ndarray:
    phi = np.zeros_like(rhs)
    inv = 1.0 / (2.0 / (dx * dx) + 2.0 / (dy * dy))
    for _ in range(max_iter):
        old = phi.copy()
        phi = (
            (np.roll(phi, 1, axis=0) + np.roll(phi, -1, axis=0)) / (dx * dx)
            + (np.roll(phi, 1, axis=1) + np.roll(phi, -1, axis=1)) / (dy * dy)
            - rhs
        ) * inv
        if float(np.sqrt(np.mean((phi - old) ** 2))) < tol:
            break
    return phi


def clean_B_projection(
    Bx: np.ndarray,
    By: np.ndarray,
    dx: float,
    dy: float,
    *,
    periodic: bool = True,
    method: str = "fft",
    max_iter: int = 400,
) -> tuple[np.ndarray, np.ndarray, dict[str, float]]:
    """Projection clean B by solving laplacian(phi)=div(B), then B <- B - grad(phi)."""
    t0 = time.perf_counter()
    before = div_metrics(Bx, By, dx, dy)
    e_before = float(np.mean(0.5 * (Bx * Bx + By * By)))

    rhs = divergence_2d(Bx, By, dx, dy)
    if periodic and method == "fft":
        phi = _solve_poisson_fft(rhs, dx, dy)
    else:
        phi = _solve_poisson_jacobi(rhs, dx, dy, max_iter=max_iter)

    dphix = (np.roll(phi, -1, axis=0) - np.roll(phi, 1, axis=0)) / (2.0 * dx)
    dphiy = (np.roll(phi, -1, axis=1) - np.roll(phi, 1, axis=1)) / (2.0 * dy)
    Bx_new = Bx - dphix
    By_new = By - dphiy

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
    return Bx_new, By_new, report
