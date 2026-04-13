from __future__ import annotations

from dataclasses import dataclass
import numpy as np

from .mhd import divergence_2d, helmholtz_project_2d, orthogonality_residual_2d
from .physics import BoundaryProjectionReport, bounded_domain_projection_counterexample

Array = np.ndarray


def _periodic_gradient(field: Array, h: float, axis: int) -> Array:
    if axis == 0:
        return (np.roll(field, -1, axis=0) - np.roll(field, 1, axis=0)) / (2.0 * h)
    return (np.roll(field, -1, axis=1) - np.roll(field, 1, axis=1)) / (2.0 * h)


def _bounded_gradient(field: Array, h: float, axis: int) -> Array:
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


def _bounded_divergence(Ux: Array, Uy: Array, h: float) -> Array:
    return _bounded_gradient(Ux, h, axis=0) + _bounded_gradient(Uy, h, axis=1)


@dataclass(frozen=True)
class PeriodicIncompressibleProjectionReport:
    before_l2_divergence: float
    after_projection_l2_divergence: float
    recovery_l2_error: float
    idempotence_l2_error: float
    orthogonality_residual: float


@dataclass(frozen=True)
class DivergenceOnlyNoGoWitness:
    first_state_divergence_rms: float
    second_state_divergence_rms: float
    state_separation_rms: float


@dataclass(frozen=True)
class CfdProjectionSummary:
    periodic: PeriodicIncompressibleProjectionReport
    bounded_transplant: BoundaryProjectionReport
    divergence_only_witness: DivergenceOnlyNoGoWitness


def periodic_incompressible_projection_report(n: int = 48, contamination: float = 0.2) -> PeriodicIncompressibleProjectionReport:
    if n < 8:
        raise ValueError('n must be at least 8 for the periodic incompressible projection report')
    h = 1.0 / n
    x = np.linspace(0.0, 1.0, n, endpoint=False)
    y = np.linspace(0.0, 1.0, n, endpoint=False)
    X, Y = np.meshgrid(x, y, indexing='ij')

    psi = np.sin(2.0 * np.pi * X) * np.sin(2.0 * np.pi * Y)
    phi = contamination * np.cos(4.0 * np.pi * X) * np.cos(2.0 * np.pi * Y)

    dpsix = _periodic_gradient(psi, h, axis=0)
    dpsiy = _periodic_gradient(psi, h, axis=1)
    gradx = _periodic_gradient(phi, h, axis=0)
    grady = _periodic_gradient(phi, h, axis=1)

    ux_phys = -dpsiy
    uy_phys = dpsix
    ux = ux_phys + gradx
    uy = uy_phys + grady

    before = float(np.sqrt(np.mean(divergence_2d(ux, uy, h, h) ** 2)))
    ux_proj, uy_proj, _, _ = helmholtz_project_2d(ux, uy, h, h)
    after = float(np.sqrt(np.mean(divergence_2d(ux_proj, uy_proj, h, h) ** 2)))
    recovery = float(np.sqrt(np.mean((ux_proj - ux_phys) ** 2 + (uy_proj - uy_phys) ** 2)))
    ux_proj2, uy_proj2, _, _ = helmholtz_project_2d(ux_proj, uy_proj, h, h)
    idempotence = float(np.sqrt(np.mean((ux_proj2 - ux_proj) ** 2 + (uy_proj2 - uy_proj) ** 2)))

    return PeriodicIncompressibleProjectionReport(
        before_l2_divergence=before,
        after_projection_l2_divergence=after,
        recovery_l2_error=recovery,
        idempotence_l2_error=idempotence,
        orthogonality_residual=orthogonality_residual_2d(ux, uy, h, h),
    )


def divergence_only_bounded_no_go_witness(n: int = 32) -> DivergenceOnlyNoGoWitness:
    if n < 8:
        raise ValueError('n must be at least 8 for the bounded-domain witness')
    h = 1.0 / (n - 1)
    x = np.linspace(0.0, 1.0, n)
    y = np.linspace(0.0, 1.0, n)
    X, Y = np.meshgrid(x, y, indexing='ij')

    psi_1 = np.sin(np.pi * X) ** 2 * np.sin(np.pi * Y) ** 2
    psi_2 = np.sin(2.0 * np.pi * X) ** 2 * np.sin(np.pi * Y) ** 2

    dpsi1x = _bounded_gradient(psi_1, h, axis=0)
    dpsi1y = _bounded_gradient(psi_1, h, axis=1)
    dpsi2x = _bounded_gradient(psi_2, h, axis=0)
    dpsi2y = _bounded_gradient(psi_2, h, axis=1)

    u1x = -dpsi1y
    u1y = dpsi1x
    u2x = -dpsi2y
    u2y = dpsi2x

    div1 = float(np.sqrt(np.mean(_bounded_divergence(u1x, u1y, h) ** 2)))
    div2 = float(np.sqrt(np.mean(_bounded_divergence(u2x, u2y, h) ** 2)))
    separation = float(np.sqrt(np.mean((u1x - u2x) ** 2 + (u1y - u2y) ** 2)))

    return DivergenceOnlyNoGoWitness(
        first_state_divergence_rms=div1,
        second_state_divergence_rms=div2,
        state_separation_rms=separation,
    )


def cfd_projection_summary(n_periodic: int = 48, n_bounded: int = 32, contamination: float = 0.2) -> CfdProjectionSummary:
    return CfdProjectionSummary(
        periodic=periodic_incompressible_projection_report(n=n_periodic, contamination=contamination),
        bounded_transplant=bounded_domain_projection_counterexample(n_bounded),
        divergence_only_witness=divergence_only_bounded_no_go_witness(n=n_bounded),
    )
