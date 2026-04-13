from __future__ import annotations

import numpy as np

Array = np.ndarray


def _central_diff_symbols(shape: tuple[int, int], dx: float, dy: float) -> tuple[Array, Array]:
    nx, ny = shape
    wx = 2.0 * np.pi * np.fft.fftfreq(nx, d=dx)
    wy = 2.0 * np.pi * np.fft.fftfreq(ny, d=dy)
    dx_symbol = 1j * np.sin(wx * dx)[:, None] / dx
    dy_symbol = 1j * np.sin(wy * dy)[None, :] / dy
    return dx_symbol, dy_symbol


def divergence_2d(Bx: Array, By: Array, dx: float, dy: float) -> Array:
    dBx = (np.roll(Bx, -1, axis=0) - np.roll(Bx, 1, axis=0)) / (2.0 * dx)
    dBy = (np.roll(By, -1, axis=1) - np.roll(By, 1, axis=1)) / (2.0 * dy)
    return dBx + dBy


def _solve_poisson_fft(rhs: Array, dx: float, dy: float) -> Array:
    dx_symbol, dy_symbol = _central_diff_symbols(rhs.shape, dx, dy)
    discrete_k2 = (dx_symbol.conj() * dx_symbol + dy_symbol.conj() * dy_symbol).real
    rhs_hat = np.fft.fftn(rhs)
    phi_hat = np.zeros_like(rhs_hat)
    mask = discrete_k2 > 0.0
    phi_hat[mask] = -rhs_hat[mask] / discrete_k2[mask]
    return np.fft.ifftn(phi_hat).real


def gradient_2d(phi: Array, dx: float, dy: float) -> tuple[Array, Array]:
    dx_symbol, dy_symbol = _central_diff_symbols(phi.shape, dx, dy)
    phi_hat = np.fft.fftn(phi)
    dphix = np.fft.ifftn(dx_symbol * phi_hat).real
    dphiy = np.fft.ifftn(dy_symbol * phi_hat).real
    return dphix, dphiy


def helmholtz_project_2d(Bx: Array, By: Array, dx: float, dy: float) -> tuple[Array, Array, Array, Array]:
    bx_hat = np.fft.fftn(Bx)
    by_hat = np.fft.fftn(By)
    dx_symbol, dy_symbol = _central_diff_symbols(Bx.shape, dx, dy)
    dx_symbol = np.broadcast_to(dx_symbol, Bx.shape)
    dy_symbol = np.broadcast_to(dy_symbol, By.shape)
    norm2 = (dx_symbol.conj() * dx_symbol + dy_symbol.conj() * dy_symbol).real
    div_hat = dx_symbol * bx_hat + dy_symbol * by_hat

    grad_x_hat = np.zeros_like(bx_hat)
    grad_y_hat = np.zeros_like(by_hat)
    mask = norm2 > 0.0
    grad_x_hat[mask] = dx_symbol.conj()[mask] * div_hat[mask] / norm2[mask]
    grad_y_hat[mask] = dy_symbol.conj()[mask] * div_hat[mask] / norm2[mask]

    bx_proj = np.fft.ifftn(bx_hat - grad_x_hat).real
    by_proj = np.fft.ifftn(by_hat - grad_y_hat).real
    gx = np.fft.ifftn(grad_x_hat).real
    gy = np.fft.ifftn(grad_y_hat).real
    return bx_proj, by_proj, gx, gy


def l2_inner_2d(ax: Array, ay: Array, bx: Array, by: Array) -> float:
    return float(np.mean(ax * bx + ay * by))


def orthogonality_residual_2d(Bx: Array, By: Array, dx: float, dy: float) -> float:
    divfree_x, divfree_y, grad_x, grad_y = helmholtz_project_2d(Bx, By, dx, dy)
    return abs(l2_inner_2d(divfree_x, divfree_y, grad_x, grad_y))


def glm_step_2d(
    Bx: Array,
    By: Array,
    psi: Array,
    dx: float,
    dy: float,
    dt: float,
    *,
    ch: float = 1.0,
    cp: float = 1.0,
) -> tuple[Array, Array, Array]:
    dpsix, dpsiy = gradient_2d(psi, dx, dy)
    divB = divergence_2d(Bx, By, dx, dy)
    Bx_new = Bx - dt * dpsix
    By_new = By - dt * dpsiy
    damping = (ch * ch) / max(cp * cp, 1e-12)
    psi_new = psi - dt * (ch * ch * divB + damping * psi)
    return Bx_new, By_new, psi_new
