from __future__ import annotations

from dataclasses import dataclass
import numpy as np

from .mhd import divergence_2d, helmholtz_project_2d

Array = np.ndarray


def _boundary_gradient(field: Array, h: float, axis: int) -> Array:
    out = np.zeros_like(field)
    if axis == 0:
        out[0, :] = (field[1, :] - field[0, :]) / h
        out[-1, :] = (field[-1, :] - field[-2, :]) / h
        out[1:-1, :] = (field[2:, :] - field[:-2, :]) / (2.0 * h)
        return out
    out[:, 0] = (field[:, 1] - field[:, 0]) / h
    out[:, -1] = (field[:, -1] - field[:, -2]) / h
    out[:, 1:-1] = (field[:, 2:] - field[:, :-2]) / (2.0 * h)
    return out


def _boundary_normal_rms(Bx: Array, By: Array) -> float:
    edge_values = np.concatenate([Bx[0, :], Bx[-1, :], By[:, 0], By[:, -1]])
    return float(np.sqrt(np.mean(edge_values**2)))


@dataclass(frozen=True)
class BoundaryProjectionReport:
    before_l2_divergence: float
    after_periodic_projection_l2_divergence: float
    physical_boundary_normal_rms: float
    projected_boundary_normal_rms: float


def bounded_domain_projection_counterexample(n: int = 32) -> BoundaryProjectionReport:
    if n < 8:
        raise ValueError('n must be at least 8 for the bounded-domain counterexample')
    h = 1.0 / (n - 1)
    x = np.linspace(0.0, 1.0, n)
    y = np.linspace(0.0, 1.0, n)
    X, Y = np.meshgrid(x, y, indexing='ij')

    psi = np.sin(np.pi * X) ** 2 * np.sin(np.pi * Y) ** 2
    phi = X * (1.0 - X) * np.sin(np.pi * Y)

    dpsix = _boundary_gradient(psi, h, axis=0)
    dpsiy = _boundary_gradient(psi, h, axis=1)
    gradx = _boundary_gradient(phi, h, axis=0)
    grady = _boundary_gradient(phi, h, axis=1)

    Bx_phys = -dpsiy
    By_phys = dpsix
    Bx = Bx_phys + gradx
    By = By_phys + grady

    before_div = float(np.sqrt(np.mean(divergence_2d(Bx, By, h, h) ** 2)))
    Bx_proj, By_proj, _, _ = helmholtz_project_2d(Bx, By, h, h)
    after_div = float(np.sqrt(np.mean(divergence_2d(Bx_proj, By_proj, h, h) ** 2)))

    return BoundaryProjectionReport(
        before_l2_divergence=before_div,
        after_periodic_projection_l2_divergence=after_div,
        physical_boundary_normal_rms=_boundary_normal_rms(Bx_phys, By_phys),
        projected_boundary_normal_rms=_boundary_normal_rms(Bx_proj, By_proj),
    )
