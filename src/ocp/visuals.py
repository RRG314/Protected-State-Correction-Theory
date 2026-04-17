from __future__ import annotations

"""Mathematically grounded data builders for the visuals package.

All functions in this module are deterministic and compute figure data from
explicit finite-dimensional examples or canonical branch formulas.
"""

from dataclasses import dataclass
from typing import Iterable

import numpy as np

from .cfd import cfd_projection_summary
from .design import linear_recoverability_design_report, unrestricted_exact_augmentation
from .mhd import divergence_2d, helmholtz_project_2d
from .recoverability import (
    restricted_linear_rowspace_residual,
    restricted_linear_collision_gap,
    restricted_linear_recoverability,
    same_rank_alignment_counterexample,
)
from .fiber_limits import noisy_restricted_linear_target_hierarchy_report
from .recoverability import functional_observability_sweep

Array = np.ndarray


def _orthonormal_columns(matrix: Array, *, tol: float = 1e-10) -> Array:
    mat = np.asarray(matrix, dtype=float)
    if mat.ndim == 1:
        mat = mat[:, None]
    if mat.size == 0:
        return np.zeros((mat.shape[0], 0), dtype=float)
    u, s, _ = np.linalg.svd(mat, full_matrices=False)
    rank = int(np.sum(s > tol))
    if rank == 0:
        return np.zeros((mat.shape[0], 0), dtype=float)
    return u[:, :rank].copy()


def _projector_from_columns(basis_columns: Array, *, tol: float = 1e-10) -> Array:
    q = _orthonormal_columns(np.asarray(basis_columns, dtype=float), tol=tol)
    if q.size == 0:
        return np.zeros((basis_columns.shape[0], basis_columns.shape[0]), dtype=float)
    return q @ q.T


def _rank(matrix: Array, tol: float = 1e-10) -> int:
    return int(np.linalg.matrix_rank(np.asarray(matrix, dtype=float), tol=tol))


def _null_space(matrix: Array, *, tol: float = 1e-10) -> Array:
    mat = np.asarray(matrix, dtype=float)
    _, s, vh = np.linalg.svd(mat, full_matrices=True)
    rank = int(np.sum(s > tol))
    return vh[rank:, :].T.copy()


def _subspace_intersection_dimension(a_columns: Array, b_columns: Array, *, tol: float = 1e-10) -> int:
    qa = _orthonormal_columns(a_columns, tol=tol)
    qb = _orthonormal_columns(b_columns, tol=tol)
    if qa.size == 0 or qb.size == 0:
        return 0
    pa = qa @ qa.T
    pb = qb @ qb.T
    # dim(A ∩ B) = rank([A B]) - rank(A+B complement) via projector test.
    # Here we compute rank of PA*PB restricted to A.
    singular_values = np.linalg.svd(qa.T @ qb, compute_uv=False)
    return int(np.sum(singular_values > 1.0 - 1e-8))


def core_geometry_data() -> dict[str, object]:
    """Return exact and failure geometry examples for Figures A (2D/3D)."""

    # 2D exact split: S ⟂ D
    s2_basis = np.asarray([[1.0], [0.0]], dtype=float)
    d2_exact_basis = np.asarray([[0.0], [1.0]], dtype=float)
    p2 = _projector_from_columns(s2_basis)
    s_coeff = 1.25
    d_coeff = 0.85
    s_vec = (s2_basis[:, 0] * s_coeff)
    d_exact_vec = (d2_exact_basis[:, 0] * d_coeff)
    x_exact = s_vec + d_exact_vec
    proj_exact = p2 @ x_exact

    # 2D misaligned split: S and D are distinct lines but not orthogonal.
    d2_misaligned_basis = _orthonormal_columns(np.asarray([[1.0], [1.0]], dtype=float))
    d_misaligned_vec = d2_misaligned_basis[:, 0] * d_coeff
    x_misaligned = s_vec + d_misaligned_vec
    proj_misaligned = p2 @ x_misaligned

    # 3D overlap split: S ∩ D nontrivial
    s3_basis = np.asarray(
        [
            [1.0, 0.0],
            [0.0, 1.0],
            [0.0, 0.0],
        ],
        dtype=float,
    )
    d3_basis = np.asarray(
        [
            [0.0, 0.0],
            [1.0, 0.0],
            [0.0, 1.0],
        ],
        dtype=float,
    )
    p3 = _projector_from_columns(s3_basis)
    s3 = np.asarray([1.1, 0.6, 0.0], dtype=float)
    d3 = np.asarray([0.0, 0.4, 0.9], dtype=float)
    x3 = s3 + d3
    overlap_direction = np.asarray([0.0, 1.0, 0.0], dtype=float)
    alt_shift = 0.35
    s3_alt = s3 + alt_shift * overlap_direction
    d3_alt = d3 - alt_shift * overlap_direction
    proj3 = p3 @ x3

    return {
        'exact_2d': {
            'S_basis': s2_basis.tolist(),
            'D_basis': d2_exact_basis.tolist(),
            's': s_vec.tolist(),
            'd': d_exact_vec.tolist(),
            'x': x_exact.tolist(),
            'projection_onto_S': proj_exact.tolist(),
            'projection_error_norm': float(np.linalg.norm(proj_exact - s_vec)),
            'classification': 'exact',
        },
        'misaligned_2d': {
            'S_basis': s2_basis.tolist(),
            'D_basis': d2_misaligned_basis.tolist(),
            's': s_vec.tolist(),
            'd': d_misaligned_vec.tolist(),
            'x': x_misaligned.tolist(),
            'projection_onto_S': proj_misaligned.tolist(),
            'projection_error_norm': float(np.linalg.norm(proj_misaligned - s_vec)),
            'classification': 'impossible_for_orthogonal_projector',
        },
        'overlap_3d': {
            'S_basis': s3_basis.tolist(),
            'D_basis': d3_basis.tolist(),
            'intersection_dimension': int(_subspace_intersection_dimension(s3_basis, d3_basis)),
            'x': x3.tolist(),
            'decomposition_1': {'s': s3.tolist(), 'd': d3.tolist()},
            'decomposition_2': {'s': s3_alt.tolist(), 'd': d3_alt.tolist()},
            'same_state_residual_norm': float(np.linalg.norm((s3 + d3) - (s3_alt + d3_alt))),
            'projection_onto_S': proj3.tolist(),
            'classification': 'overlap_nonidentifiable_split',
        },
    }


def _fiber_partition(observations: Array, *, tol: float = 1e-12) -> tuple[tuple[int, ...], ...]:
    fibers: list[list[int]] = []
    obs = np.asarray(observations, dtype=float)
    for idx, row in enumerate(obs):
        assigned = False
        for bucket in fibers:
            if np.linalg.norm(row - obs[bucket[0]]) <= tol:
                bucket.append(idx)
                assigned = True
                break
        if not assigned:
            fibers.append([idx])
    return tuple(tuple(bucket) for bucket in fibers)


def fiber_toy_data() -> dict[str, object]:
    """Return finite-state map data for Figure B."""

    states = np.asarray(
        [[x1, x2, x3] for x1 in (0, 1) for x2 in (0, 1) for x3 in (0, 1)],
        dtype=int,
    )
    observation = states[:, :2].copy()  # M(x1,x2,x3) = (x1,x2)
    fibers = _fiber_partition(observation.astype(float))
    tau_const = states[:, 0] + 2 * states[:, 1]
    tau_nonconst = states[:, 0] + states[:, 2]

    fiber_constancy_const = []
    fiber_constancy_nonconst = []
    for bucket in fibers:
        const_values = {int(tau_const[index]) for index in bucket}
        nonconst_values = {int(tau_nonconst[index]) for index in bucket}
        fiber_constancy_const.append(len(const_values) == 1)
        fiber_constancy_nonconst.append(len(nonconst_values) == 1)

    return {
        'states': states.tolist(),
        'observations': observation.tolist(),
        'fibers': [list(bucket) for bucket in fibers],
        'tau_constant_on_fibers': tau_const.tolist(),
        'tau_not_constant_on_fibers': tau_nonconst.tolist(),
        'fiber_constancy_tau_constant': fiber_constancy_const,
        'fiber_constancy_tau_nonconstant': fiber_constancy_nonconst,
    }


def recoverability_transition_data(
    alphas: Iterable[float] = tuple(np.linspace(1.0, 0.0, 21)),
) -> dict[str, object]:
    """Return threshold transition data for Figure C animation."""

    grid_values = (-1.0, 0.0, 1.0)
    states = np.asarray([[x1, x2] for x1 in grid_values for x2 in grid_values], dtype=float)
    target = np.asarray([[0.0, 1.0]], dtype=float)

    rows: list[dict[str, object]] = []
    fail_alpha = None
    for raw_alpha in alphas:
        alpha = float(raw_alpha)
        observation = np.asarray([[1.0, 0.0], [0.0, alpha]], dtype=float)
        report = restricted_linear_recoverability(observation, target)
        gap = restricted_linear_collision_gap(observation, target, box_radius=1.0)
        obs_points = (observation @ states.T).T
        fibers = _fiber_partition(obs_points)
        fiber_index = np.zeros(len(states), dtype=int)
        for bucket_id, bucket in enumerate(fibers):
            for index in bucket:
                fiber_index[int(index)] = int(bucket_id)
        row = {
            'alpha': alpha,
            'exact_recoverable': bool(report.exact_recoverable),
            'rowspace_residual': float(report.residual_norm),
            'collision_gap': float(gap),
            'fiber_count': int(len(fibers)),
            'state_points': states.tolist(),
            'observation_points': obs_points.tolist(),
            'fiber_index_per_state': fiber_index.tolist(),
        }
        rows.append(row)
        if fail_alpha is None and (not report.exact_recoverable):
            fail_alpha = alpha

    return {
        'target_matrix': target.tolist(),
        'rows': rows,
        'exact_to_impossible_threshold_alpha': fail_alpha,
    }


def same_rank_data() -> dict[str, object]:
    """Return same-rank opposite-verdict data for Figure D."""

    witness = same_rank_alignment_counterexample(ambient_dimension=3, protected_rank=1, observation_rank=1)
    protected = np.asarray(witness.protected_matrix, dtype=float)
    exact_obs = np.asarray(witness.exact_observation_matrix, dtype=float)
    fail_obs = np.asarray(witness.fail_observation_matrix, dtype=float)
    l_dir = protected[0] / max(np.linalg.norm(protected[0]), 1e-12)
    e_dir = exact_obs[0] / max(np.linalg.norm(exact_obs[0]), 1e-12)
    f_dir = fail_obs[0] / max(np.linalg.norm(fail_obs[0]), 1e-12)

    def angle(a: Array, b: Array) -> float:
        val = float(np.clip(abs(np.dot(a, b)), 0.0, 1.0))
        return float(np.degrees(np.arccos(val)))

    return {
        'protected_matrix': protected.tolist(),
        'exact_observation_matrix': exact_obs.tolist(),
        'fail_observation_matrix': fail_obs.tolist(),
        'rank_exact': _rank(exact_obs),
        'rank_fail': _rank(fail_obs),
        'exact_recoverable': True,
        'fail_recoverable': False,
        'exact_rowspace_residual': float(witness.exact_rowspace_residual),
        'fail_rowspace_residual': float(witness.fail_rowspace_residual),
        'exact_collision_gap': float(witness.exact_collision_gap),
        'fail_collision_gap': float(witness.fail_collision_gap),
        'angle_protected_to_exact_rowspace_deg': angle(l_dir, e_dir),
        'angle_protected_to_fail_rowspace_deg': angle(l_dir, f_dir),
    }


def minimal_augmentation_data() -> dict[str, object]:
    """Return exact augmentation witness data for Figure E."""

    observation = np.asarray(
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 1.0],
        ],
        dtype=float,
    )
    target = np.asarray([[0.0, 0.0, 1.0]], dtype=float)
    design = linear_recoverability_design_report(observation, target)
    unrestricted = unrestricted_exact_augmentation(observation, target)
    augmented = np.vstack([observation, unrestricted.ambient_augmentation_rows])
    exact_before = restricted_linear_recoverability(observation, target)
    exact_after = restricted_linear_recoverability(augmented, target)

    delta_formula = _rank(np.vstack([observation, target])) - _rank(observation)

    return {
        'observation_matrix': observation.tolist(),
        'target_matrix': target.tolist(),
        'rank_observation': _rank(observation),
        'rank_augmented_stack': _rank(np.vstack([observation, target])),
        'delta_formula': int(delta_formula),
        'design_unrestricted_minimal_added_measurements': int(design.unrestricted_minimal_added_measurements),
        'augmentation_rows': unrestricted.ambient_augmentation_rows.tolist(),
        'exact_before': bool(exact_before.exact_recoverable),
        'exact_after': bool(exact_after.exact_recoverable),
        'residual_before': float(exact_before.residual_norm),
        'residual_after': float(exact_after.residual_norm),
        'rowspace_residuals_before': [float(v) for v in design.row_space_residuals],
    }


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


def _boundary_normal_trace(ux: Array, uy: Array) -> tuple[Array, Array]:
    top = ux[0, :]
    bottom = ux[-1, :]
    left = uy[:, 0]
    right = uy[:, -1]
    values = np.concatenate([top, bottom, left, right])
    t = np.linspace(0.0, 1.0, values.size)
    return t, values


def periodic_vs_bounded_data(
    *,
    n_periodic: int = 48,
    n_bounded: int = 32,
    contamination: float = 0.2,
) -> dict[str, object]:
    """Return field/divergence/boundary data for Figure F."""

    # Periodic exact branch
    hp = 1.0 / n_periodic
    xp = np.linspace(0.0, 1.0, n_periodic, endpoint=False)
    yp = np.linspace(0.0, 1.0, n_periodic, endpoint=False)
    XP, YP = np.meshgrid(xp, yp, indexing='ij')
    psi_p = np.sin(2.0 * np.pi * XP) * np.sin(2.0 * np.pi * YP)
    phi_p = contamination * np.cos(4.0 * np.pi * XP) * np.cos(2.0 * np.pi * YP)

    dpsix_p = _periodic_gradient(psi_p, hp, axis=0)
    dpsiy_p = _periodic_gradient(psi_p, hp, axis=1)
    gradx_p = _periodic_gradient(phi_p, hp, axis=0)
    grady_p = _periodic_gradient(phi_p, hp, axis=1)
    ux_phys_p = -dpsiy_p
    uy_phys_p = dpsix_p
    ux_p = ux_phys_p + gradx_p
    uy_p = uy_phys_p + grady_p
    ux_proj_p, uy_proj_p, _, _ = helmholtz_project_2d(ux_p, uy_p, hp, hp)
    div_before_p = divergence_2d(ux_p, uy_p, hp, hp)
    div_after_p = divergence_2d(ux_proj_p, uy_proj_p, hp, hp)

    # Bounded transplant failure branch
    hb = 1.0 / (n_bounded - 1)
    xb = np.linspace(0.0, 1.0, n_bounded)
    yb = np.linspace(0.0, 1.0, n_bounded)
    XB, YB = np.meshgrid(xb, yb, indexing='ij')
    psi_b = np.sin(np.pi * XB) ** 2 * np.sin(np.pi * YB) ** 2
    phi_b = XB * (1.0 - XB) * np.sin(np.pi * YB)

    dpsix_b = _bounded_gradient(psi_b, hb, axis=0)
    dpsiy_b = _bounded_gradient(psi_b, hb, axis=1)
    gradx_b = _bounded_gradient(phi_b, hb, axis=0)
    grady_b = _bounded_gradient(phi_b, hb, axis=1)
    ux_phys_b = -dpsiy_b
    uy_phys_b = dpsix_b
    ux_b = ux_phys_b + gradx_b
    uy_b = uy_phys_b + grady_b
    ux_proj_b, uy_proj_b, _, _ = helmholtz_project_2d(ux_b, uy_b, hb, hb)
    div_before_b = divergence_2d(ux_b, uy_b, hb, hb)
    div_after_b = divergence_2d(ux_proj_b, uy_proj_b, hb, hb)

    tb, boundary_phys = _boundary_normal_trace(ux_phys_b, uy_phys_b)
    _, boundary_proj = _boundary_normal_trace(ux_proj_b, uy_proj_b)

    summary = cfd_projection_summary(n_periodic=n_periodic, n_bounded=n_bounded, contamination=contamination)
    return {
        'periodic': {
            'divergence_before': div_before_p.tolist(),
            'divergence_after': div_after_p.tolist(),
            'before_l2_divergence': float(np.sqrt(np.mean(div_before_p**2))),
            'after_l2_divergence': float(np.sqrt(np.mean(div_after_p**2))),
            'recovery_l2_error': float(np.sqrt(np.mean((ux_proj_p - ux_phys_p) ** 2 + (uy_proj_p - uy_phys_p) ** 2))),
        },
        'bounded_transplant': {
            'divergence_before': div_before_b.tolist(),
            'divergence_after': div_after_b.tolist(),
            'before_l2_divergence': float(np.sqrt(np.mean(div_before_b**2))),
            'after_l2_divergence': float(np.sqrt(np.mean(div_after_b**2))),
            'boundary_trace_parameter': tb.tolist(),
            'boundary_normal_physical': boundary_phys.tolist(),
            'boundary_normal_projected': boundary_proj.tolist(),
            'boundary_normal_physical_rms': float(np.sqrt(np.mean(boundary_phys**2))),
            'boundary_normal_projected_rms': float(np.sqrt(np.mean(boundary_proj**2))),
        },
        'canonical_summary': {
            'periodic_before_l2_divergence': float(summary.periodic.before_l2_divergence),
            'periodic_after_projection_l2_divergence': float(summary.periodic.after_projection_l2_divergence),
            'bounded_transplant_projected_boundary_normal_rms': float(summary.bounded_transplant.projected_boundary_normal_rms),
            'bounded_hodge_recovered_boundary_normal_rms': float(summary.bounded_hodge_exact.recovered_boundary_normal_rms),
            'bounded_hodge_recovery_l2_error': float(summary.bounded_hodge_exact.recovery_l2_error),
        },
    }


def threshold_surfaces_data() -> dict[str, object]:
    """Return branch-supported regime maps for Figure G."""

    control = functional_observability_sweep(
        epsilon_values=(0.0, 0.05, 0.1, 0.2, 0.4),
        horizons=(1, 2, 3),
    )
    epsilons = sorted({float(row['epsilon']) for row in control['rows']})
    horizons = sorted({int(row['horizon']) for row in control['rows']})
    control_matrix = np.zeros((len(horizons), len(epsilons)), dtype=int)
    # regime ids: 0 impossible, 1 asymptotic-only, 2 exact, 3 approximate
    for row in control['rows']:
        ei = epsilons.index(float(row['epsilon']))
        hi = horizons.index(int(row['horizon']))
        if bool(row['exact_recoverable']):
            regime = 2
        elif float(row['epsilon']) > 0.0:
            regime = 1
        else:
            regime = 0
        control_matrix[hi, ei] = regime

    noisy = noisy_restricted_linear_target_hierarchy_report(
        np.asarray(
            [
                [1.0, 0.0, 0.0],
                [0.0, 1.0, 1.0],
            ],
            dtype=float,
        ),
        np.asarray([[0.0, 1.0, 1.0]], dtype=float),
        np.asarray([[0.0, 0.0, 1.0]], dtype=float),
        noise_radii=(0.0, 0.1, 0.25, 0.5, 1.0),
        box_radius=1.0,
    )
    noise_radii = [float(row.noise_radius) for row in noisy.rows]
    target_labels = ('weak_target', 'strong_target')
    noise_matrix = np.zeros((len(target_labels), len(noise_radii)), dtype=int)
    for j, row in enumerate(noisy.rows):
        # weak target: exact at eta=0, approximate for eta>0
        noise_matrix[0, j] = 2 if float(row.noise_radius) <= 1e-12 else 3
        # strong target: impossible on this family (collision gap > 0)
        noise_matrix[1, j] = 0

    return {
        'regime_labels': {
            0: 'impossible',
            1: 'asymptotic_only',
            2: 'exact',
            3: 'approximate',
        },
        'control_surface': {
            'epsilons': epsilons,
            'horizons': horizons,
            'regime_matrix': control_matrix.tolist(),
        },
        'noise_surface': {
            'noise_radii': noise_radii,
            'target_labels': list(target_labels),
            'regime_matrix': noise_matrix.tolist(),
            'strong_uniform_lower_bound': float(noisy.strong_uniform_lower_bound),
            'weak_decoder_operator_norm': float(noisy.weak_decoder_operator_norm),
        },
    }


def alignment_landscape_data(
    *,
    theta_count: int = 121,
    phi_count: int = 181,
) -> dict[str, object]:
    """Return same-rank alignment landscape data for Figure I."""

    thetas = np.linspace(0.0, np.pi, int(theta_count))
    phis = np.linspace(0.0, 2.0 * np.pi, int(phi_count))
    target = np.asarray([[1.0, 0.0, 0.0]], dtype=float)
    residual = np.zeros((thetas.size, phis.size), dtype=float)
    collision_gap = np.zeros((thetas.size, phis.size), dtype=float)
    exact = np.zeros((thetas.size, phis.size), dtype=int)
    angle_deg = np.zeros((thetas.size, phis.size), dtype=float)

    for i, theta in enumerate(thetas):
        for j, phi in enumerate(phis):
            direction = np.asarray(
                [
                    np.cos(theta),
                    np.sin(theta) * np.cos(phi),
                    np.sin(theta) * np.sin(phi),
                ],
                dtype=float,
            )
            direction = direction / max(np.linalg.norm(direction), 1e-12)
            observation = direction[None, :]
            residual[i, j] = restricted_linear_rowspace_residual(observation, target)
            collision_gap[i, j] = restricted_linear_collision_gap(observation, target, box_radius=1.0)
            exact[i, j] = int(restricted_linear_recoverability(observation, target).exact_recoverable)
            angle_deg[i, j] = float(np.degrees(np.arccos(np.clip(abs(direction[0]), 0.0, 1.0))))

    return {
        'theta_values': thetas.tolist(),
        'phi_values': phis.tolist(),
        'target_matrix': target.tolist(),
        'rowspace_residual_matrix': residual.tolist(),
        'collision_gap_matrix': collision_gap.tolist(),
        'exact_mask_matrix': exact.tolist(),
        'principal_angle_matrix_deg': angle_deg.tolist(),
        'exact_fraction': float(np.mean(exact)),
    }


def perturbation_fragility_data(
    *,
    perturb_values: Iterable[float] = tuple(np.linspace(-0.8, 0.8, 81)),
) -> dict[str, object]:
    """Return perturbation fragility data around an exact rank-1 configuration."""

    values = np.asarray(tuple(float(v) for v in perturb_values), dtype=float)
    target = np.asarray([[1.0, 0.0, 0.0]], dtype=float)
    residual = np.zeros((values.size, values.size), dtype=float)
    collision_gap = np.zeros((values.size, values.size), dtype=float)
    exact = np.zeros((values.size, values.size), dtype=int)
    angle_deg = np.zeros((values.size, values.size), dtype=float)
    perturb_norm = np.zeros((values.size, values.size), dtype=float)

    for i, u in enumerate(values):
        for j, v in enumerate(values):
            direction = np.asarray([1.0, u, v], dtype=float)
            direction = direction / max(np.linalg.norm(direction), 1e-12)
            observation = direction[None, :]
            residual[i, j] = restricted_linear_rowspace_residual(observation, target)
            collision_gap[i, j] = restricted_linear_collision_gap(observation, target, box_radius=1.0)
            exact[i, j] = int(restricted_linear_recoverability(observation, target).exact_recoverable)
            angle_deg[i, j] = float(np.degrees(np.arccos(np.clip(abs(direction[0]), 0.0, 1.0))))
            perturb_norm[i, j] = float(np.sqrt(u**2 + v**2))

    center_index = int(np.argmin(np.abs(values)))
    return {
        'perturb_values': values.tolist(),
        'target_matrix': target.tolist(),
        'rowspace_residual_matrix': residual.tolist(),
        'collision_gap_matrix': collision_gap.tolist(),
        'exact_mask_matrix': exact.tolist(),
        'principal_angle_matrix_deg': angle_deg.tolist(),
        'perturbation_norm_matrix': perturb_norm.tolist(),
        'center_index': center_index,
        'exact_fraction': float(np.mean(exact)),
    }


def family_enlargement_visual_data() -> dict[str, object]:
    """Return exact-on-small-family and failure-on-enlarged-family witness data."""

    observation = np.asarray(
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
        ],
        dtype=float,
    )
    target = np.asarray([[0.0, 0.0, 1.0]], dtype=float)
    values = (-1.0, 0.0, 1.0)
    states_small = np.asarray([[x1, x2, 0.0] for x1 in values for x2 in values], dtype=float)
    states_large = np.asarray([[x1, x2, x3] for x1 in values for x2 in values for x3 in values], dtype=float)

    obs_small = (observation @ states_small.T).T
    obs_large = (observation @ states_large.T).T
    tgt_small = (target @ states_small.T).reshape(-1)
    tgt_large = (target @ states_large.T).reshape(-1)

    fibers_small = _fiber_partition(obs_small)
    fibers_large = _fiber_partition(obs_large)
    fiber_target_sets_small = [[float(v) for v in sorted({float(tgt_small[idx]) for idx in bucket})] for bucket in fibers_small]
    fiber_target_sets_large = [[float(v) for v in sorted({float(tgt_large[idx]) for idx in bucket})] for bucket in fibers_large]

    family_basis_small = np.asarray(
        [
            [1.0, 0.0],
            [0.0, 1.0],
            [0.0, 0.0],
        ],
        dtype=float,
    )
    small_report = restricted_linear_recoverability(observation, target, family_basis=family_basis_small)
    large_report = restricted_linear_recoverability(observation, target)
    small_gap = restricted_linear_collision_gap(observation, target, family_basis=family_basis_small, box_radius=1.0)
    large_gap = restricted_linear_collision_gap(observation, target, box_radius=1.0)
    small_residual = restricted_linear_rowspace_residual(observation, target, family_basis=family_basis_small)
    large_residual = restricted_linear_rowspace_residual(observation, target)

    return {
        'observation_matrix': observation.tolist(),
        'target_matrix': target.tolist(),
        'small_family': {
            'states': states_small.tolist(),
            'observations': obs_small.tolist(),
            'target_values': tgt_small.tolist(),
            'fibers': [list(bucket) for bucket in fibers_small],
            'fiber_target_sets': fiber_target_sets_small,
            'exact_recoverable': bool(small_report.exact_recoverable),
            'rowspace_residual': float(small_residual),
            'collision_gap': float(small_gap),
        },
        'enlarged_family': {
            'states': states_large.tolist(),
            'observations': obs_large.tolist(),
            'target_values': tgt_large.tolist(),
            'fibers': [list(bucket) for bucket in fibers_large],
            'fiber_target_sets': fiber_target_sets_large,
            'exact_recoverable': bool(large_report.exact_recoverable),
            'rowspace_residual': float(large_residual),
            'collision_gap': float(large_gap),
        },
    }


def dynamic_rate_visual_data() -> dict[str, object]:
    """Return observer-rate and finite-history exactness data for Figure L."""

    sweep = functional_observability_sweep(
        epsilon_values=(0.0, 0.05, 0.1, 0.2, 0.35, 0.5, 0.8),
        horizons=(1, 2, 3, 4),
    )
    rows = sweep['rows']
    epsilons = sorted({float(row['epsilon']) for row in rows})
    horizons = sorted({int(row['horizon']) for row in rows})
    exact_matrix = np.zeros((len(horizons), len(epsilons)), dtype=int)
    margin_matrix = np.zeros((len(horizons), len(epsilons)), dtype=float)
    mean_error_matrix = np.zeros((len(horizons), len(epsilons)), dtype=float)

    for row in rows:
        ei = epsilons.index(float(row['epsilon']))
        hi = horizons.index(int(row['horizon']))
        exact_matrix[hi, ei] = int(bool(row['exact_recoverable']))
        margin_matrix[hi, ei] = float(row['recoverability_margin'])
        mean_error_matrix[hi, ei] = float(row['mean_recovery_error'])

    observer_rows: list[dict[str, object]] = []
    for report in sweep['observer_reports']:
        errors = np.asarray(report['protected_error_history'], dtype=float)
        observer_rows.append(
            {
                'epsilon': float(report['epsilon']),
                'spectral_radius': float(report['spectral_radius']),
                'gain': [float(value) for value in np.asarray(report['gain'], dtype=float).reshape(-1)],
                'protected_error_history': errors.tolist(),
                'error_ratio_final_to_initial': float(errors[-1] / max(errors[0], 1e-12)),
            }
        )

    return {
        'epsilons': epsilons,
        'horizons': horizons,
        'exact_matrix': exact_matrix.tolist(),
        'recoverability_margin_matrix': margin_matrix.tolist(),
        'mean_error_matrix': mean_error_matrix.tolist(),
        'observer_reports': observer_rows,
    }


def augmentation_direction_scan_data(
    *,
    theta_values: Iterable[float] = tuple(np.linspace(0.0, 2.0 * np.pi, 361)),
) -> dict[str, object]:
    """Return one-row augmentation direction scan data for Figure M."""

    base_observation = np.asarray(
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 1.0],
        ],
        dtype=float,
    )
    target = np.asarray([[0.0, 0.0, 1.0]], dtype=float)
    thetas = np.asarray(tuple(float(v) for v in theta_values), dtype=float)
    residuals = np.zeros(thetas.size, dtype=float)
    gaps = np.zeros(thetas.size, dtype=float)
    exact = np.zeros(thetas.size, dtype=int)
    ranks = np.zeros(thetas.size, dtype=int)
    augmentation_rows = np.zeros((thetas.size, 3), dtype=float)

    for i, theta in enumerate(thetas):
        augment_row = np.asarray([0.0, np.cos(theta), np.sin(theta)], dtype=float)
        augmented = np.vstack([base_observation, augment_row[None, :]])
        report = restricted_linear_recoverability(augmented, target)
        residuals[i] = restricted_linear_rowspace_residual(augmented, target)
        gaps[i] = restricted_linear_collision_gap(augmented, target, box_radius=1.0)
        exact[i] = int(bool(report.exact_recoverable))
        ranks[i] = int(np.linalg.matrix_rank(augmented))
        augmentation_rows[i] = augment_row

    fail_indices = [int(i) for i, value in enumerate(exact.tolist()) if value == 0]
    return {
        'theta_values': thetas.tolist(),
        'base_observation_matrix': base_observation.tolist(),
        'target_matrix': target.tolist(),
        'augmentation_rows': augmentation_rows.tolist(),
        'rowspace_residuals': residuals.tolist(),
        'collision_gaps': gaps.tolist(),
        'exact_flags': exact.tolist(),
        'augmented_ranks': ranks.tolist(),
        'fail_indices': fail_indices,
    }


def contamination_sweep_visual_data(
    *,
    contamination_values: Iterable[float] = (0.05, 0.1, 0.15, 0.2, 0.3, 0.4),
) -> dict[str, object]:
    """Return periodic-vs-bounded contamination sweep data for Figure N."""

    values = [float(v) for v in contamination_values]
    rows: list[dict[str, float]] = []
    for contamination in values:
        report = periodic_vs_bounded_data(
            n_periodic=40,
            n_bounded=24,
            contamination=contamination,
        )
        periodic = report['periodic']
        bounded = report['bounded_transplant']
        canonical = report['canonical_summary']
        rows.append(
            {
                'contamination': float(contamination),
                'periodic_before_l2_divergence': float(periodic['before_l2_divergence']),
                'periodic_after_l2_divergence': float(periodic['after_l2_divergence']),
                'periodic_recovery_l2_error': float(periodic['recovery_l2_error']),
                'bounded_before_l2_divergence': float(bounded['before_l2_divergence']),
                'bounded_after_l2_divergence': float(bounded['after_l2_divergence']),
                'bounded_boundary_normal_physical_rms': float(bounded['boundary_normal_physical_rms']),
                'bounded_boundary_normal_projected_rms': float(bounded['boundary_normal_projected_rms']),
                'bounded_hodge_recovered_boundary_normal_rms': float(canonical['bounded_hodge_recovered_boundary_normal_rms']),
            }
        )
    return {
        'rows': rows,
        'contamination_values': values,
    }


def cross_system_status_data() -> dict[str, object]:
    """Return schematic status map data for Figure H."""

    systems = [
        {
            'id': 'qec_sector',
            'label': 'QEC sector recovery',
            'status': 'exact_anchor',
            'claims': ['OCP-005', 'OCP-019'],
        },
        {
            'id': 'periodic_projection',
            'label': 'Periodic Helmholtz/Leray projection',
            'status': 'exact_anchor',
            'claims': ['OCP-006', 'OCP-027'],
        },
        {
            'id': 'bounded_domain',
            'label': 'Bounded-domain transplant',
            'status': 'no_go_boundary',
            'claims': ['OCP-023', 'OCP-028', 'OCP-044'],
        },
        {
            'id': 'constrained_observation',
            'label': 'Constrained observation / fibers',
            'status': 'branch_limited_theory',
            'claims': ['OCP-031', 'OCP-043', 'OCP-045', 'OCP-049', 'OCP-050'],
        },
        {
            'id': 'asymptotic_generator',
            'label': 'Asymptotic generator correction',
            'status': 'asymptotic_only',
            'claims': ['OCP-013', 'OCP-014', 'OCP-020'],
        },
    ]
    abstractions = [
        {'id': 'protected', 'label': 'Protected structure S'},
        {'id': 'disturbance', 'label': 'Disturbance structure D'},
        {'id': 'observation', 'label': 'Observation/collapse map M'},
        {'id': 'fiber', 'label': 'Fiber constancy condition'},
        {'id': 'architecture', 'label': 'Correction architecture'},
    ]
    edges = [
        ('qec_sector', 'protected'),
        ('qec_sector', 'disturbance'),
        ('qec_sector', 'observation'),
        ('periodic_projection', 'protected'),
        ('periodic_projection', 'disturbance'),
        ('periodic_projection', 'architecture'),
        ('bounded_domain', 'architecture'),
        ('bounded_domain', 'observation'),
        ('constrained_observation', 'observation'),
        ('constrained_observation', 'fiber'),
        ('constrained_observation', 'architecture'),
        ('asymptotic_generator', 'protected'),
        ('asymptotic_generator', 'disturbance'),
        ('asymptotic_generator', 'architecture'),
    ]
    return {
        'systems': systems,
        'abstractions': abstractions,
        'edges': [{'source': s, 'target': t} for s, t in edges],
        'figure_type': 'schematic_status_map',
    }


def visual_summary() -> dict[str, object]:
    return {
        'A_core_geometry': core_geometry_data(),
        'B_fiber_toy': fiber_toy_data(),
        'C_transition': recoverability_transition_data(),
        'D_same_rank': same_rank_data(),
        'E_minimal_augmentation': minimal_augmentation_data(),
        'F_periodic_vs_bounded': periodic_vs_bounded_data(),
        'G_threshold_surfaces': threshold_surfaces_data(),
        'I_alignment_landscape': alignment_landscape_data(),
        'J_perturbation_fragility': perturbation_fragility_data(),
        'K_family_enlargement': family_enlargement_visual_data(),
        'L_dynamic_rates': dynamic_rate_visual_data(),
        'M_augmentation_direction_scan': augmentation_direction_scan_data(),
        'N_contamination_sweep': contamination_sweep_visual_data(),
        'H_cross_system_map': cross_system_status_data(),
    }


__all__ = [
    'core_geometry_data',
    'fiber_toy_data',
    'recoverability_transition_data',
    'same_rank_data',
    'minimal_augmentation_data',
    'periodic_vs_bounded_data',
    'threshold_surfaces_data',
    'alignment_landscape_data',
    'perturbation_fragility_data',
    'family_enlargement_visual_data',
    'dynamic_rate_visual_data',
    'augmentation_direction_scan_data',
    'contamination_sweep_visual_data',
    'cross_system_status_data',
    'visual_summary',
]
