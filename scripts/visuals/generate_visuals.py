#!/usr/bin/env python3
from __future__ import annotations

"""Generate the complete OCP visuals package from exact/supported examples.

Run:
  PYTHONPATH=src uv run --with matplotlib --with pillow python scripts/visuals/generate_visuals.py
"""

import json
from pathlib import Path
from typing import Sequence

import numpy as np

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib import animation
    from matplotlib.colors import BoundaryNorm, ListedColormap
except Exception as exc:  # pragma: no cover - dependency guard
    raise SystemExit(
        'Matplotlib is required for visual generation. '
        'Run with: PYTHONPATH=src uv run --with matplotlib --with pillow python scripts/visuals/generate_visuals.py'
    ) from exc

from ocp.visuals import (
    alignment_landscape_data,
    augmentation_direction_scan_data,
    contamination_sweep_visual_data,
    core_geometry_data,
    cross_system_status_data,
    dynamic_rate_visual_data,
    family_enlargement_visual_data,
    fiber_toy_data,
    minimal_augmentation_data,
    periodic_vs_bounded_data,
    perturbation_fragility_data,
    recoverability_transition_data,
    same_rank_data,
    threshold_surfaces_data,
    visual_summary,
)

ROOT = Path('/Users/stevenreid/Documents/New project/repos/ocp-research-program')
DOC_OUT = ROOT / 'docs/visuals/generated'
DATA_OUT = ROOT / 'data/generated/visuals'

COLORS = {
    'protected': '#1d6f5f',
    'disturbance': '#b34d2e',
    'observation': '#2e5da8',
    'impossible': '#9f1d35',
    'repair': '#8a5a16',
    'neutral': '#36454f',
    'background': '#fffdf8',
}


def _ensure_dirs() -> None:
    DOC_OUT.mkdir(parents=True, exist_ok=True)
    DATA_OUT.mkdir(parents=True, exist_ok=True)


def _save_static(fig: plt.Figure, stem: str) -> None:
    fig.savefig(DOC_OUT / f'{stem}.svg', format='svg', bbox_inches='tight')
    fig.savefig(DOC_OUT / f'{stem}.png', format='png', dpi=320, bbox_inches='tight')
    plt.close(fig)


def _set_axis_2d(ax: plt.Axes, title: str, xlabel: str = 'x₁', ylabel: str = 'x₂') -> None:
    ax.set_facecolor(COLORS['background'])
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(alpha=0.25, linestyle='--', linewidth=0.6)
    ax.set_aspect('equal', adjustable='box')


def _plot_subspace_line(ax: plt.Axes, direction: Sequence[float], color: str, label: str) -> None:
    vec = np.asarray(direction, dtype=float)
    if np.linalg.norm(vec) <= 1e-12:
        return
    vec = vec / np.linalg.norm(vec)
    t = np.linspace(-2.0, 2.0, 50)
    points = np.outer(t, vec)
    ax.plot(points[:, 0], points[:, 1], color=color, linewidth=2.4, label=label)


def figure_a_core_geometry() -> list[str]:
    data = core_geometry_data()
    generated: list[str] = []

    # A1: 2D exact vs orthogonal-projector failure under misalignment.
    fig, axes = plt.subplots(1, 2, figsize=(12, 5), constrained_layout=True)
    exact = data['exact_2d']
    fail = data['misaligned_2d']

    ax = axes[0]
    _set_axis_2d(ax, 'A1. Exact Separable Case (Exact)')
    _plot_subspace_line(ax, np.asarray(exact['S_basis'])[:, 0], COLORS['protected'], 'S (protected)')
    _plot_subspace_line(ax, np.asarray(exact['D_basis'])[:, 0], COLORS['disturbance'], 'D (disturbance)')
    s = np.asarray(exact['s'])
    x = np.asarray(exact['x'])
    px = np.asarray(exact['projection_onto_S'])
    ax.scatter([s[0], x[0], px[0]], [s[1], x[1], px[1]], c=[COLORS['protected'], COLORS['neutral'], COLORS['observation']], s=55)
    ax.plot([0, s[0]], [0, s[1]], color=COLORS['protected'], linewidth=2.0)
    ax.plot([s[0], x[0]], [s[1], x[1]], color=COLORS['disturbance'], linewidth=2.0)
    ax.plot([x[0], px[0]], [x[1], px[1]], color=COLORS['observation'], linestyle='--', linewidth=2.0)
    ax.text(-1.85, 1.6, f'||P_S x - s|| = {exact["projection_error_norm"]:.2e}', fontsize=10)
    ax.legend(loc='lower right', fontsize=8, frameon=False)
    ax.set_xlim(-2.0, 2.0)
    ax.set_ylim(-2.0, 2.0)

    ax = axes[1]
    _set_axis_2d(ax, 'A1. Misaligned Case (No-Go for Orthogonal Projector)')
    _plot_subspace_line(ax, np.asarray(fail['S_basis'])[:, 0], COLORS['protected'], 'S (protected)')
    _plot_subspace_line(ax, np.asarray(fail['D_basis'])[:, 0], COLORS['disturbance'], 'D (misaligned)')
    s = np.asarray(fail['s'])
    x = np.asarray(fail['x'])
    px = np.asarray(fail['projection_onto_S'])
    ax.scatter([s[0], x[0], px[0]], [s[1], x[1], px[1]], c=[COLORS['protected'], COLORS['neutral'], COLORS['observation']], s=55)
    ax.plot([0, s[0]], [0, s[1]], color=COLORS['protected'], linewidth=2.0)
    ax.plot([s[0], x[0]], [s[1], x[1]], color=COLORS['disturbance'], linewidth=2.0)
    ax.plot([x[0], px[0]], [x[1], px[1]], color=COLORS['observation'], linestyle='--', linewidth=2.0)
    ax.text(-1.9, 1.6, f'||P_S x - s|| = {fail["projection_error_norm"]:.3f}', fontsize=10, color=COLORS['impossible'])
    ax.legend(loc='lower right', fontsize=8, frameon=False)
    ax.set_xlim(-2.0, 2.0)
    ax.set_ylim(-2.0, 2.0)

    _save_static(fig, 'A_core_geometry_2d')
    generated.extend(['A_core_geometry_2d.svg', 'A_core_geometry_2d.png'])

    # A2: 3D overlap/non-identifiable decomposition.
    overlap = data['overlap_3d']
    fig = plt.figure(figsize=(8, 6), constrained_layout=True)
    ax3 = fig.add_subplot(111, projection='3d')
    ax3.set_facecolor(COLORS['background'])
    ax3.set_title('A2. Overlap Geometry In 3D (Exact non-uniqueness)')
    s_basis = np.asarray(overlap['S_basis'])
    d_basis = np.asarray(overlap['D_basis'])
    x = np.asarray(overlap['x'])
    s1 = np.asarray(overlap['decomposition_1']['s'])
    d1 = np.asarray(overlap['decomposition_1']['d'])
    s2 = np.asarray(overlap['decomposition_2']['s'])
    d2 = np.asarray(overlap['decomposition_2']['d'])

    origin = np.zeros(3)
    for vec in s_basis.T:
        ax3.quiver(*origin, *vec, color=COLORS['protected'], linewidth=2.2, arrow_length_ratio=0.08)
    for vec in d_basis.T:
        ax3.quiver(*origin, *vec, color=COLORS['disturbance'], linewidth=2.0, arrow_length_ratio=0.08)
    ax3.scatter([x[0]], [x[1]], [x[2]], color=COLORS['neutral'], s=45)
    ax3.plot([0, s1[0]], [0, s1[1]], [0, s1[2]], color=COLORS['protected'], linewidth=2.0)
    ax3.plot([s1[0], x[0]], [s1[1], x[1]], [s1[2], x[2]], color=COLORS['disturbance'], linewidth=2.0)
    ax3.plot([0, s2[0]], [0, s2[1]], [0, s2[2]], color=COLORS['protected'], linestyle='--', linewidth=1.7)
    ax3.plot([s2[0], x[0]], [s2[1], x[1]], [s2[2], x[2]], color=COLORS['disturbance'], linestyle='--', linewidth=1.7)
    ax3.text2D(
        0.03,
        0.92,
        f'intersection dim = {overlap["intersection_dimension"]}; two (s,d) pairs map to same x',
        transform=ax3.transAxes,
        fontsize=10,
    )
    ax3.set_xlabel('x₁')
    ax3.set_ylabel('x₂')
    ax3.set_zlabel('x₃')
    ax3.set_xlim(-0.2, 1.6)
    ax3.set_ylim(-0.2, 1.6)
    ax3.set_zlim(-0.2, 1.4)

    _save_static(fig, 'A_core_geometry_3d')
    generated.extend(['A_core_geometry_3d.svg', 'A_core_geometry_3d.png'])
    return generated


def figure_b_fiber_views() -> list[str]:
    data = fiber_toy_data()
    generated: list[str] = []
    states = np.asarray(data['states'], dtype=int)
    observations = np.asarray(data['observations'], dtype=int)
    fibers = [tuple(bucket) for bucket in data['fibers']]
    tau_const = np.asarray(data['tau_constant_on_fibers'], dtype=int)
    tau_nonconst = np.asarray(data['tau_not_constant_on_fibers'], dtype=int)
    palette = plt.cm.tab10(np.linspace(0.05, 0.95, len(fibers)))
    fiber_of_state = np.zeros(len(states), dtype=int)
    for fiber_id, bucket in enumerate(fibers):
        for idx in bucket:
            fiber_of_state[int(idx)] = int(fiber_id)

    # B1 bipartite.
    fig, ax = plt.subplots(figsize=(9, 5), constrained_layout=True)
    ax.set_facecolor(COLORS['background'])
    ax.set_title('B1. Fiber Collapse Bipartite View (Exact)', fontsize=12, fontweight='bold')
    obs_keys = list({tuple(obs.tolist()) for obs in observations})
    obs_keys.sort()
    obs_pos = {key: (1.0, 0.5 + 0.8 * i) for i, key in enumerate(obs_keys)}
    state_pos = {i: (0.0, 0.2 + 0.35 * i) for i in range(len(states))}

    for i, state in enumerate(states):
        key = tuple(observations[i].tolist())
        x0, y0 = state_pos[i]
        x1, y1 = obs_pos[key]
        color = palette[fiber_of_state[i]]
        ax.plot([x0, x1], [y0, y1], color=color, linewidth=1.8, alpha=0.9)

    for i, state in enumerate(states):
        x0, y0 = state_pos[i]
        color = palette[fiber_of_state[i]]
        ax.scatter([x0], [y0], color=color, s=60, zorder=3)
        ax.text(x0 - 0.02, y0, f's{i}:{tuple(state.tolist())}', ha='right', va='center', fontsize=8)
    for key, (x1, y1) in obs_pos.items():
        ax.scatter([x1], [y1], color=COLORS['observation'], s=75, zorder=3)
        ax.text(x1 + 0.02, y1, f'M={key}', ha='left', va='center', fontsize=9)

    ax.text(0.02, -0.05, 'States', transform=ax.transAxes, fontsize=10, fontweight='bold')
    ax.text(0.82, -0.05, 'Observations', transform=ax.transAxes, fontsize=10, fontweight='bold')
    ax.set_xlim(-0.25, 1.35)
    ax.set_ylim(-0.05, max(y for _, y in obs_pos.values()) + 0.4)
    ax.axis('off')
    _save_static(fig, 'B_fiber_bipartite')
    generated.extend(['B_fiber_bipartite.svg', 'B_fiber_bipartite.png'])

    # B2 partition tree.
    fig, ax = plt.subplots(figsize=(9, 5), constrained_layout=True)
    ax.set_facecolor(COLORS['background'])
    ax.set_title('B2. Partition Tree View (Exact)', fontsize=12, fontweight='bold')
    root = (0.5, 0.95)
    ax.scatter([root[0]], [root[1]], color=COLORS['neutral'], s=90)
    ax.text(root[0], root[1] + 0.03, 'state set Ω', ha='center', fontsize=10)

    obs_nodes = {}
    for i, key in enumerate(obs_keys):
        x = 0.1 + 0.8 * i / max(len(obs_keys) - 1, 1)
        y = 0.62
        obs_nodes[key] = (x, y)
        ax.plot([root[0], x], [root[1], y], color=COLORS['observation'], linewidth=1.7)
        ax.scatter([x], [y], color=COLORS['observation'], s=70)
        ax.text(x, y + 0.04, f'fiber M={key}', ha='center', fontsize=8)

    for i, state in enumerate(states):
        key = tuple(observations[i].tolist())
        parent = obs_nodes[key]
        x = parent[0] + (0.06 if (i % 2 == 0) else -0.06)
        y = 0.30 - 0.025 * (i % 2)
        color = palette[fiber_of_state[i]]
        ax.plot([parent[0], x], [parent[1], y], color=color, linewidth=1.5)
        ax.scatter([x], [y], color=color, s=50)
        ax.text(x, y - 0.04, f's{i}', ha='center', fontsize=7)
    ax.text(
        0.01,
        0.03,
        'τ_const is constant on each branch; τ_nonconst is not.',
        transform=ax.transAxes,
        fontsize=10,
    )
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.18, 1.02)
    ax.axis('off')
    _save_static(fig, 'B_fiber_partition_tree')
    generated.extend(['B_fiber_partition_tree.svg', 'B_fiber_partition_tree.png'])

    # B3 table/heatmap view.
    fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
    ax.set_facecolor(COLORS['background'])
    ax.set_title('B3. Fiber / Target Table Heatmap (Exact)', fontsize=12, fontweight='bold')
    obs_index = np.asarray([obs_keys.index(tuple(obs.tolist())) for obs in observations], dtype=float)
    matrix = np.column_stack([obs_index, tau_const, tau_nonconst]).astype(float)
    im = ax.imshow(matrix, cmap='YlGnBu', aspect='auto')
    ax.set_xticks([0, 1, 2], labels=['fiber id', 'τ constant-on-fibers', 'τ nonconstant'])
    ax.set_yticks(np.arange(len(states)), labels=[f's{i}:{tuple(state)}' for i, state in enumerate(states.tolist())], fontsize=8)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            ax.text(j, i, f'{matrix[i, j]:.0f}', ha='center', va='center', fontsize=8, color='black')
    cbar = fig.colorbar(im, ax=ax, fraction=0.03, pad=0.02)
    cbar.ax.set_ylabel('value')
    _save_static(fig, 'B_fiber_table_heatmap')
    generated.extend(['B_fiber_table_heatmap.svg', 'B_fiber_table_heatmap.png'])
    return generated


def figure_c_transition_animation() -> list[str]:
    rows = recoverability_transition_data(alphas=tuple(np.linspace(1.0, 0.0, 25)))['rows']
    generated: list[str] = []
    palette = plt.cm.tab20(np.linspace(0.03, 0.97, 20))

    # C static keyframe comparison.
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8), constrained_layout=True)
    for ax, idx, title in [
        (axes[0], 0, 'C. α = 1.0 (exact)'),
        (axes[1], len(rows) - 1, 'C. α = 0.0 (impossible)'),
    ]:
        row = rows[idx]
        states = np.asarray(row['state_points'], dtype=float)
        fibers = np.asarray(row['fiber_index_per_state'], dtype=int)
        colors = [palette[int(f) % len(palette)] for f in fibers]
        _set_axis_2d(ax, title, xlabel='state x₁', ylabel='state x₂')
        ax.scatter(states[:, 0], states[:, 1], c=colors, s=70, edgecolors='black', linewidths=0.4)
        ax.text(
            0.02,
            0.96,
            f'fibers={row["fiber_count"]}, exact={row["exact_recoverable"]}',
            transform=ax.transAxes,
            va='top',
            fontsize=10,
        )
        ax.set_xlim(-1.3, 1.3)
        ax.set_ylim(-1.3, 1.3)
    _save_static(fig, 'C_transition_keyframes')
    generated.extend(['C_transition_keyframes.svg', 'C_transition_keyframes.png'])

    # C animation.
    fig, (ax_state, ax_obs) = plt.subplots(1, 2, figsize=(12, 5), constrained_layout=True)
    _set_axis_2d(ax_state, 'C1. State-Space Fibers', xlabel='x₁', ylabel='x₂')
    _set_axis_2d(ax_obs, 'C2. Observation Space Mα(x)', xlabel='y₁', ylabel='y₂')
    ax_state.set_xlim(-1.3, 1.3)
    ax_state.set_ylim(-1.3, 1.3)
    ax_obs.set_xlim(-1.3, 1.3)
    ax_obs.set_ylim(-1.3, 1.3)
    ax_obs.axhline(0.0, color='black', linewidth=0.9, alpha=0.35)
    ax_state.axhline(0.0, color='black', linewidth=0.9, alpha=0.35)
    ax_state.axvline(0.0, color='black', linewidth=0.9, alpha=0.35)
    ax_obs.axvline(0.0, color='black', linewidth=0.9, alpha=0.35)

    first = rows[0]
    s_pts = np.asarray(first['state_points'], dtype=float)
    o_pts = np.asarray(first['observation_points'], dtype=float)
    fibers = np.asarray(first['fiber_index_per_state'], dtype=int)
    colors = [palette[int(f) % len(palette)] for f in fibers]

    scat_state = ax_state.scatter(s_pts[:, 0], s_pts[:, 1], c=colors, s=75, edgecolors='black', linewidths=0.35)
    scat_obs = ax_obs.scatter(o_pts[:, 0], o_pts[:, 1], c=colors, s=75, edgecolors='black', linewidths=0.35)
    title = fig.suptitle('', fontsize=12, fontweight='bold')

    def _update(frame_index: int):
        row = rows[int(frame_index)]
        s = np.asarray(row['state_points'], dtype=float)
        o = np.asarray(row['observation_points'], dtype=float)
        fids = np.asarray(row['fiber_index_per_state'], dtype=int)
        c = [palette[int(fid) % len(palette)] for fid in fids]
        scat_state.set_offsets(s)
        scat_state.set_color(c)
        scat_obs.set_offsets(o)
        scat_obs.set_color(c)
        title.set_text(
            f'Exact→Impossible transition: α={row["alpha"]:.3f}, '
            f'exact={row["exact_recoverable"]}, fibers={row["fiber_count"]}, '
            f'collision-gap={row["collision_gap"]:.3f}'
        )
        return scat_state, scat_obs, title

    anim = animation.FuncAnimation(fig, _update, frames=len(rows), interval=220, blit=False)
    gif_path = DOC_OUT / 'C_exact_vs_impossible_transition.gif'
    mp4_path = DOC_OUT / 'C_exact_vs_impossible_transition.mp4'
    anim.save(gif_path, writer=animation.PillowWriter(fps=5))
    anim.save(mp4_path, writer=animation.FFMpegWriter(fps=8, bitrate=1800))
    plt.close(fig)

    generated.extend(['C_exact_vs_impossible_transition.gif', 'C_exact_vs_impossible_transition.mp4'])
    return generated


def figure_d_same_rank() -> list[str]:
    data = same_rank_data()
    generated: list[str] = []
    protected = np.asarray(data['protected_matrix'], dtype=float)[0]
    exact = np.asarray(data['exact_observation_matrix'], dtype=float)[0]
    fail = np.asarray(data['fail_observation_matrix'], dtype=float)[0]

    fig = plt.figure(figsize=(11, 5), constrained_layout=True)
    ax1 = fig.add_subplot(121, projection='3d')
    ax2 = fig.add_subplot(122, projection='3d')
    for ax, obs, verdict, angle, residual in [
        (ax1, exact, 'exact', data['angle_protected_to_exact_rowspace_deg'], data['exact_rowspace_residual']),
        (ax2, fail, 'impossible', data['angle_protected_to_fail_rowspace_deg'], data['fail_rowspace_residual']),
    ]:
        ax.set_facecolor(COLORS['background'])
        ax.set_title(f'D. Same rank, {verdict} verdict')
        ax.quiver(0, 0, 0, protected[0], protected[1], protected[2], color=COLORS['protected'], linewidth=2.4, arrow_length_ratio=0.09)
        ax.quiver(0, 0, 0, obs[0], obs[1], obs[2], color=COLORS['observation'], linewidth=2.4, arrow_length_ratio=0.09)
        ax.text2D(0.04, 0.9, f'angle={angle:.1f}°, residual={residual:.2f}', transform=ax.transAxes, fontsize=10)
        ax.set_xlim(-0.3, 1.2)
        ax.set_ylim(-0.3, 1.2)
        ax.set_zlim(-0.3, 1.2)
        ax.set_xlabel('e₁')
        ax.set_ylabel('e₂')
        ax.set_zlabel('e₃')
    fig.suptitle(
        f'Same observation rank = {data["rank_exact"]} for both O₁ and O₂; recoverability differs by alignment.',
        fontsize=11,
    )
    _save_static(fig, 'D_same_rank_insufficiency')
    generated.extend(['D_same_rank_insufficiency.svg', 'D_same_rank_insufficiency.png'])
    return generated


def figure_e_augmentation() -> list[str]:
    data = minimal_augmentation_data()
    generated: list[str] = []
    O = np.asarray(data['observation_matrix'], dtype=float)
    L = np.asarray(data['target_matrix'], dtype=float)[0]
    a = np.asarray(data['augmentation_rows'], dtype=float)[0]

    fig = plt.figure(figsize=(12, 5), constrained_layout=True)
    ax1 = fig.add_subplot(121, projection='3d')
    ax2 = fig.add_subplot(122, projection='3d')
    for ax in (ax1, ax2):
        ax.set_facecolor(COLORS['background'])
        ax.set_xlim(-0.3, 1.3)
        ax.set_ylim(-0.3, 1.3)
        ax.set_zlim(-0.3, 1.3)
        ax.set_xlabel('r₁')
        ax.set_ylabel('r₂')
        ax.set_zlabel('r₃')

    # Before.
    ax1.set_title('E1. Before augmentation (impossible)')
    ax1.quiver(0, 0, 0, *O[0], color=COLORS['observation'], linewidth=2.2, arrow_length_ratio=0.08)
    ax1.quiver(0, 0, 0, *O[1], color=COLORS['observation'], linewidth=2.2, arrow_length_ratio=0.08)
    ax1.quiver(0, 0, 0, *L, color=COLORS['protected'], linewidth=2.6, arrow_length_ratio=0.08)
    # span plane
    u = np.linspace(-1.0, 1.0, 20)
    v = np.linspace(-1.0, 1.0, 20)
    U, V = np.meshgrid(u, v)
    X = U * O[0, 0] + V * O[1, 0]
    Y = U * O[0, 1] + V * O[1, 1]
    Z = U * O[0, 2] + V * O[1, 2]
    ax1.plot_surface(X, Y, Z, color=COLORS['observation'], alpha=0.2, linewidth=0.0)
    ax1.text2D(0.03, 0.9, f'δ = rank([OF;LF]) - rank(OF) = {data["delta_formula"]}', transform=ax1.transAxes, fontsize=10)
    ax1.text2D(0.03, 0.84, f'exact before: {data["exact_before"]}', transform=ax1.transAxes, fontsize=10, color=COLORS['impossible'])

    # After.
    ax2.set_title('E2. After minimal augmentation (exact)')
    ax2.quiver(0, 0, 0, *O[0], color=COLORS['observation'], linewidth=2.0, arrow_length_ratio=0.08)
    ax2.quiver(0, 0, 0, *O[1], color=COLORS['observation'], linewidth=2.0, arrow_length_ratio=0.08)
    ax2.quiver(0, 0, 0, *a, color=COLORS['repair'], linewidth=2.5, arrow_length_ratio=0.08)
    ax2.quiver(0, 0, 0, *L, color=COLORS['protected'], linewidth=2.6, arrow_length_ratio=0.08)
    ax2.text2D(0.03, 0.9, f'added rows = {len(data["augmentation_rows"])}', transform=ax2.transAxes, fontsize=10)
    ax2.text2D(0.03, 0.84, f'exact after: {data["exact_after"]}', transform=ax2.transAxes, fontsize=10, color=COLORS['protected'])

    fig.suptitle('Minimal augmentation law: δ(O,L;F) = rank([OF;LF]) - rank(OF)', fontsize=12, fontweight='bold')
    _save_static(fig, 'E_minimal_augmentation')
    generated.extend(['E_minimal_augmentation.svg', 'E_minimal_augmentation.png'])
    return generated


def figure_f_periodic_vs_bounded() -> list[str]:
    data = periodic_vs_bounded_data(n_periodic=48, n_bounded=32, contamination=0.2)
    generated: list[str] = []

    p = data['periodic']
    b = data['bounded_transplant']
    c = data['canonical_summary']
    pb = np.asarray(p['divergence_before'], dtype=float)
    pa = np.asarray(p['divergence_after'], dtype=float)
    bb = np.asarray(b['divergence_before'], dtype=float)
    ba = np.asarray(b['divergence_after'], dtype=float)
    vmax = float(max(np.max(np.abs(pb)), np.max(np.abs(pa)), np.max(np.abs(bb)), np.max(np.abs(ba)), 1e-12))

    fig, axes = plt.subplots(2, 3, figsize=(15, 8.8), constrained_layout=True)
    titles = [
        'F1. Periodic divergence before',
        'F1. Periodic divergence after exact projection',
        'Periodic metrics',
        'F2. Bounded divergence before',
        'F2. Bounded divergence after periodic transplant',
        'Boundary-normal mismatch',
    ]
    arrays = [pb, pa, None, bb, ba, None]
    for ax, title, arr in zip(axes.flatten(), titles, arrays):
        ax.set_facecolor(COLORS['background'])
        ax.set_title(title, fontsize=11)
        if arr is not None:
            im = ax.imshow(arr, cmap='coolwarm', vmin=-vmax, vmax=vmax, origin='lower')
            ax.set_xticks([])
            ax.set_yticks([])
        else:
            ax.set_xticks([])
            ax.set_yticks([])

    axes[0, 2].axis('off')
    axes[0, 2].text(
        0.02,
        0.98,
        (
            f'periodic ||div||₂ before: {p["before_l2_divergence"]:.3e}\n'
            f'periodic ||div||₂ after: {p["after_l2_divergence"]:.3e}\n'
            f'periodic recovery error: {p["recovery_l2_error"]:.3e}\n\n'
            f'canonical summary before: {c["periodic_before_l2_divergence"]:.3e}\n'
            f'canonical summary after: {c["periodic_after_projection_l2_divergence"]:.3e}'
        ),
        va='top',
        fontsize=10.5,
    )

    axes[1, 2].plot(b['boundary_trace_parameter'], b['boundary_normal_physical'], color=COLORS['protected'], linewidth=2.0, label='physical boundary-normal')
    axes[1, 2].plot(b['boundary_trace_parameter'], b['boundary_normal_projected'], color=COLORS['impossible'], linewidth=1.8, label='after periodic transplant')
    axes[1, 2].legend(fontsize=9, frameon=False, loc='upper right')
    axes[1, 2].set_xlabel('boundary trace parameter')
    axes[1, 2].set_ylabel('normal component')
    axes[1, 2].grid(alpha=0.25, linestyle='--', linewidth=0.6)
    axes[1, 2].text(
        0.02,
        0.02,
        (
            f'bounded before ||div||₂: {b["before_l2_divergence"]:.3e}\n'
            f'bounded after ||div||₂: {b["after_l2_divergence"]:.3e}\n'
            f'physical boundary rms: {b["boundary_normal_physical_rms"]:.3e}\n'
            f'projected boundary rms: {b["boundary_normal_projected_rms"]:.3e}\n'
            f'bounded-Hodge boundary rms: {c["bounded_hodge_recovered_boundary_normal_rms"]:.3e}'
        ),
        transform=axes[1, 2].transAxes,
        va='bottom',
        fontsize=9.8,
    )

    fig.suptitle(
        'Periodic exact projection vs bounded-domain transplant failure (Exact + No-Go)',
        fontsize=13.5,
        fontweight='bold',
    )
    _save_static(fig, 'F_periodic_vs_bounded')
    generated.extend(['F_periodic_vs_bounded.svg', 'F_periodic_vs_bounded.png'])
    return generated


def figure_g_threshold_surfaces() -> list[str]:
    data = threshold_surfaces_data()
    generated: list[str] = []
    labels = data['regime_labels']

    regime_cmap = ListedColormap([
        '#9f1d35',  # impossible
        '#2e5da8',  # asymptotic
        '#1d6f5f',  # exact
        '#8a5a16',  # approximate
    ])
    norm = BoundaryNorm([-0.5, 0.5, 1.5, 2.5, 3.5], regime_cmap.N)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5.2), constrained_layout=True)
    control = data['control_surface']
    noise = data['noise_surface']
    cm = np.asarray(control['regime_matrix'], dtype=int)
    nm = np.asarray(noise['regime_matrix'], dtype=int)

    ax = axes[0]
    ax.set_facecolor(COLORS['background'])
    im0 = ax.imshow(cm, cmap=regime_cmap, norm=norm, origin='lower', aspect='auto')
    ax.set_title('G1. Control history threshold surface (Exact/Asymptotic/Impossible)', fontsize=10)
    ax.set_xticks(np.arange(len(control['epsilons'])), labels=[f'{v:.2f}' for v in control['epsilons']])
    ax.set_yticks(np.arange(len(control['horizons'])), labels=[str(v) for v in control['horizons']])
    ax.set_xlabel('ε (observation mixing parameter)')
    ax.set_ylabel('finite history horizon')

    ax = axes[1]
    ax.set_facecolor(COLORS['background'])
    ax.imshow(nm, cmap=regime_cmap, norm=norm, origin='lower', aspect='auto')
    ax.set_title('G2. Noisy target hierarchy surface (Exact/Approx/Impossible)', fontsize=10)
    ax.set_xticks(np.arange(len(noise['noise_radii'])), labels=[f'{v:.2f}' for v in noise['noise_radii']])
    ax.set_yticks(np.arange(len(noise['target_labels'])), labels=noise['target_labels'])
    ax.set_xlabel('noise radius η')
    ax.set_ylabel('target strength')

    cbar = fig.colorbar(im0, ax=axes.ravel().tolist(), fraction=0.025, pad=0.02)
    cbar.set_ticks([0, 1, 2, 3], labels=[labels[str(k)] if isinstance(labels, dict) and str(k) in labels else labels[k] for k in [0, 1, 2, 3]])
    fig.suptitle('Recoverability regime surfaces (branch-supported, not universal)', fontsize=12, fontweight='bold')
    _save_static(fig, 'G_threshold_surfaces')
    generated.extend(['G_threshold_surfaces.svg', 'G_threshold_surfaces.png'])
    return generated


def figure_h_cross_system_map() -> list[str]:
    data = cross_system_status_data()
    generated: list[str] = []
    fig, ax = plt.subplots(figsize=(14, 8.5), constrained_layout=True)
    ax.set_facecolor(COLORS['background'])
    ax.set_title('H. Cross-system structural map (Schematic, status-faithful)', fontsize=14, fontweight='bold')

    status_color = {
        'exact_anchor': COLORS['protected'],
        'asymptotic_only': COLORS['observation'],
        'no_go_boundary': COLORS['impossible'],
        'branch_limited_theory': COLORS['repair'],
        'analogy_only': '#777777',
    }

    abstraction_positions = {}
    for i, node in enumerate(data['abstractions']):
        abstraction_positions[node['id']] = (0.5, 0.15 + 0.18 * i)
    system_positions = {}
    for i, node in enumerate(data['systems']):
        x = 0.12 if i % 2 == 0 else 0.88
        y = 0.2 + 0.155 * i
        if y > 0.9:
            y = 0.88
        system_positions[node['id']] = (x, y)

    for edge in data['edges']:
        s = system_positions[edge['source']]
        t = abstraction_positions[edge['target']]
        ax.plot([s[0], t[0]], [s[1], t[1]], color='#7b8794', linewidth=1.1, alpha=0.8)

    for node in data['abstractions']:
        x, y = abstraction_positions[node['id']]
        ax.scatter([x], [y], color=COLORS['neutral'], s=230, zorder=3)
        ax.text(x, y, node['label'], color='white', fontsize=9.2, ha='center', va='center')

    for node in data['systems']:
        x, y = system_positions[node['id']]
        color = status_color[node['status']]
        ax.scatter([x], [y], color=color, s=310, zorder=3)
        ax.text(x, y + 0.048, node['label'], fontsize=10, ha='center', va='bottom')
        ax.text(x, y - 0.05, ','.join(node['claims']), fontsize=8.4, ha='center', va='top')

    legend_rows = [
        ('exact_anchor', 'exact anchor'),
        ('asymptotic_only', 'asymptotic only'),
        ('no_go_boundary', 'no-go boundary'),
        ('branch_limited_theory', 'branch-limited theorem package'),
    ]
    for i, (key, label) in enumerate(legend_rows):
        y = 0.98 - 0.05 * i
        ax.scatter([0.02], [y], color=status_color[key], s=65, transform=ax.transAxes, clip_on=False)
        ax.text(0.05, y, label, transform=ax.transAxes, va='center', fontsize=10)

    ax.text(
        0.02,
        0.03,
        'Schematic: topology/layout is explanatory; statuses and claim IDs are exact branch labels.',
        transform=ax.transAxes,
        fontsize=10,
    )
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, 1.02)
    ax.axis('off')

    _save_static(fig, 'H_cross_system_structural_map')
    generated.extend(['H_cross_system_structural_map.svg', 'H_cross_system_structural_map.png'])
    return generated


def figure_i_alignment_landscape() -> list[str]:
    data = alignment_landscape_data()
    generated: list[str] = []

    theta = np.asarray(data['theta_values'], dtype=float)
    phi = np.asarray(data['phi_values'], dtype=float)
    residual = np.asarray(data['rowspace_residual_matrix'], dtype=float)
    gap = np.asarray(data['collision_gap_matrix'], dtype=float)
    exact = np.asarray(data['exact_mask_matrix'], dtype=int)

    fig, axes = plt.subplots(1, 3, figsize=(14, 4.8), constrained_layout=True)
    extent = [float(phi[0]), float(phi[-1]), float(theta[0]), float(theta[-1])]

    ax = axes[0]
    ax.set_facecolor(COLORS['background'])
    im0 = ax.imshow(residual, origin='lower', extent=extent, aspect='auto', cmap='viridis')
    ax.set_title('I1. Row-space residual (rank fixed = 1)')
    ax.set_xlabel('azimuth ϕ (rad)')
    ax.set_ylabel('polar angle θ from protected axis')
    fig.colorbar(im0, ax=ax, fraction=0.045, pad=0.03)

    ax = axes[1]
    ax.set_facecolor(COLORS['background'])
    im1 = ax.imshow(gap, origin='lower', extent=extent, aspect='auto', cmap='magma')
    ax.set_title('I2. Collision gap over orientation sphere')
    ax.set_xlabel('azimuth ϕ (rad)')
    ax.set_ylabel('polar angle θ from protected axis')
    fig.colorbar(im1, ax=ax, fraction=0.045, pad=0.03)

    ax = axes[2]
    ax.set_facecolor(COLORS['background'])
    im2 = ax.imshow(exact, origin='lower', extent=extent, aspect='auto', cmap=ListedColormap([COLORS['impossible'], COLORS['protected']]))
    ax.set_title('I3. Exactness mask (binary theorem verdict)')
    ax.set_xlabel('azimuth ϕ (rad)')
    ax.set_ylabel('polar angle θ from protected axis')
    cbar = fig.colorbar(im2, ax=ax, fraction=0.045, pad=0.03)
    cbar.set_ticks([0, 1], labels=['impossible', 'exact'])

    fig.suptitle('Alignment landscape: rank is constant, recoverability is not (Exact)', fontsize=12, fontweight='bold')
    _save_static(fig, 'I_alignment_landscape')
    generated.extend(['I_alignment_landscape.svg', 'I_alignment_landscape.png'])
    return generated


def figure_j_perturbation_fragility() -> list[str]:
    data = perturbation_fragility_data()
    generated: list[str] = []

    grid = np.asarray(data['perturb_values'], dtype=float)
    residual = np.asarray(data['rowspace_residual_matrix'], dtype=float)
    gap = np.asarray(data['collision_gap_matrix'], dtype=float)
    exact = np.asarray(data['exact_mask_matrix'], dtype=int)
    center_index = int(data['center_index'])

    fig, axes = plt.subplots(1, 3, figsize=(14, 4.8), constrained_layout=True)
    extent = [float(grid[0]), float(grid[-1]), float(grid[0]), float(grid[-1])]

    ax = axes[0]
    ax.set_facecolor(COLORS['background'])
    im0 = ax.imshow(residual, origin='lower', extent=extent, aspect='auto', cmap='viridis')
    ax.scatter([0.0], [0.0], c='white', edgecolors='black', s=45, zorder=3)
    ax.set_title('J1. Residual under perturbation')
    ax.set_xlabel('perturbation u (row component e₂)')
    ax.set_ylabel('perturbation v (row component e₃)')
    fig.colorbar(im0, ax=ax, fraction=0.045, pad=0.03)

    ax = axes[1]
    ax.set_facecolor(COLORS['background'])
    im1 = ax.imshow(gap, origin='lower', extent=extent, aspect='auto', cmap='magma')
    ax.scatter([0.0], [0.0], c='white', edgecolors='black', s=45, zorder=3)
    ax.set_title('J2. Collision gap under perturbation')
    ax.set_xlabel('perturbation u (row component e₂)')
    ax.set_ylabel('perturbation v (row component e₃)')
    fig.colorbar(im1, ax=ax, fraction=0.045, pad=0.03)

    ax = axes[2]
    ax.set_facecolor(COLORS['background'])
    im2 = ax.imshow(exact, origin='lower', extent=extent, aspect='auto', cmap=ListedColormap([COLORS['impossible'], COLORS['protected']]))
    ax.scatter([grid[center_index]], [grid[center_index]], c='white', edgecolors='black', s=45, zorder=3)
    ax.set_title('J3. Exactness mask')
    ax.set_xlabel('perturbation u (row component e₂)')
    ax.set_ylabel('perturbation v (row component e₃)')
    cbar = fig.colorbar(im2, ax=ax, fraction=0.045, pad=0.03)
    cbar.set_ticks([0, 1], labels=['impossible', 'exact'])

    fig.suptitle('Perturbation fragility around an exact rank-1 setup (Exact at isolated point)', fontsize=12, fontweight='bold')
    _save_static(fig, 'J_perturbation_fragility')
    generated.extend(['J_perturbation_fragility.svg', 'J_perturbation_fragility.png'])
    return generated


def figure_k_family_enlargement() -> list[str]:
    data = family_enlargement_visual_data()
    generated: list[str] = []

    small = data['small_family']
    large = data['enlarged_family']
    obs_small = np.asarray(small['observations'], dtype=float)
    obs_large = np.asarray(large['observations'], dtype=float)
    tgt_small = np.asarray(small['target_values'], dtype=float)
    tgt_large = np.asarray(large['target_values'], dtype=float)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5), constrained_layout=True)
    cmap = plt.get_cmap('coolwarm')

    # Small family: each fiber has a singleton target set.
    ax = axes[0]
    _set_axis_2d(ax, 'K1. Small family F₀ (Exact)')
    ax.scatter(obs_small[:, 0], obs_small[:, 1], c=tgt_small, cmap=cmap, vmin=-1.0, vmax=1.0, s=85, edgecolors='black', linewidths=0.4)
    for bucket, values in zip(small['fibers'], small['fiber_target_sets']):
        rep = obs_small[int(bucket[0])]
        ax.text(rep[0] + 0.04, rep[1] + 0.04, f'{values}', fontsize=8)
    ax.text(
        0.02,
        0.96,
        (
            f'exact={small["exact_recoverable"]}\n'
            f'rowspace residual={small["rowspace_residual"]:.2e}\n'
            f'collision gap={small["collision_gap"]:.2e}'
        ),
        transform=ax.transAxes,
        va='top',
        fontsize=9.5,
    )
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)

    # Enlarged family: same observations, mixed target values per fiber.
    ax = axes[1]
    _set_axis_2d(ax, 'K2. Enlarged family F₁ (No-Go)')
    center_points = []
    for bucket, values in zip(large['fibers'], large['fiber_target_sets']):
        center = obs_large[int(bucket[0])]
        center_points.append(center)
        for value in values:
            y_offset = 0.09 * float(value)
            ax.plot([center[0], center[0]], [center[1], center[1] + y_offset], color='#6b7280', linewidth=0.9, alpha=0.8)
            ax.scatter([center[0]], [center[1] + y_offset], c=[value], cmap=cmap, vmin=-1.0, vmax=1.0, s=70, edgecolors='black', linewidths=0.35)
        ax.scatter([center[0]], [center[1]], c='none', edgecolors='#334155', s=90, linewidths=1.0)
        ax.text(center[0] + 0.04, center[1] + 0.04, f'{values}', fontsize=8)
    if center_points:
        centers = np.asarray(center_points, dtype=float)
        ax.scatter(centers[:, 0], centers[:, 1], c='#334155', s=10)
    ax.text(
        0.02,
        0.96,
        (
            f'exact={large["exact_recoverable"]}\n'
            f'rowspace residual={large["rowspace_residual"]:.2e}\n'
            f'collision gap={large["collision_gap"]:.2f}'
        ),
        transform=ax.transAxes,
        va='top',
        fontsize=9.5,
        color=COLORS['impossible'],
    )
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)

    fig.suptitle('Family-enlargement false positive: exact on F₀ can fail on F₁ (Exact witness)', fontsize=12, fontweight='bold')
    _save_static(fig, 'K_family_enlargement_failure')
    generated.extend(['K_family_enlargement_failure.svg', 'K_family_enlargement_failure.png'])
    return generated


def figure_l_dynamic_rates() -> list[str]:
    data = dynamic_rate_visual_data()
    generated: list[str] = []
    epsilons = np.asarray(data['epsilons'], dtype=float)
    horizons = np.asarray(data['horizons'], dtype=int)
    exact_matrix = np.asarray(data['exact_matrix'], dtype=int)
    margin_matrix = np.asarray(data['recoverability_margin_matrix'], dtype=float)
    observer_reports = data['observer_reports']

    fig, axes = plt.subplots(1, 3, figsize=(15, 5), constrained_layout=True)

    ax = axes[0]
    ax.set_facecolor(COLORS['background'])
    ax.set_title('L1. Observer protected-error decay')
    for report in observer_reports:
        errors = np.asarray(report['protected_error_history'], dtype=float)
        steps = np.arange(errors.size)
        ax.semilogy(
            steps,
            errors + 1e-12,
            linewidth=1.9,
            label=f'ε={report["epsilon"]:.2f}, ρ={report["spectral_radius"]:.2f}',
        )
    ax.set_xlabel('time step')
    ax.set_ylabel('protected error |x₂-hat - x₂|')
    ax.grid(alpha=0.3, linestyle='--', linewidth=0.6)
    ax.legend(fontsize=7, frameon=False, loc='upper right')

    ax = axes[1]
    ax.set_facecolor(COLORS['background'])
    im1 = ax.imshow(exact_matrix, cmap=ListedColormap([COLORS['impossible'], COLORS['protected']]), origin='lower', aspect='auto')
    ax.set_title('L2. Exactness by (horizon, ε)')
    ax.set_xticks(np.arange(epsilons.size), labels=[f'{v:.2f}' for v in epsilons], rotation=45)
    ax.set_yticks(np.arange(horizons.size), labels=[str(v) for v in horizons])
    ax.set_xlabel('ε')
    ax.set_ylabel('history horizon')
    cbar1 = fig.colorbar(im1, ax=ax, fraction=0.045, pad=0.03)
    cbar1.set_ticks([0, 1], labels=['impossible', 'exact'])

    ax = axes[2]
    ax.set_facecolor(COLORS['background'])
    im2 = ax.imshow(margin_matrix, cmap='plasma', origin='lower', aspect='auto')
    ax.set_title('L3. Recoverability margin by (horizon, ε)')
    ax.set_xticks(np.arange(epsilons.size), labels=[f'{v:.2f}' for v in epsilons], rotation=45)
    ax.set_yticks(np.arange(horizons.size), labels=[str(v) for v in horizons])
    ax.set_xlabel('ε')
    ax.set_ylabel('history horizon')
    fig.colorbar(im2, ax=ax, fraction=0.045, pad=0.03)

    fig.suptitle('Dynamic correction layer: finite-history exactness + asymptotic rates (Exact/Validated)', fontsize=12, fontweight='bold')
    _save_static(fig, 'L_dynamic_rate_layer')
    generated.extend(['L_dynamic_rate_layer.svg', 'L_dynamic_rate_layer.png'])
    return generated


def figure_m_augmentation_direction_scan() -> list[str]:
    data = augmentation_direction_scan_data()
    generated: list[str] = []
    theta = np.asarray(data['theta_values'], dtype=float)
    theta_deg = np.degrees(theta)
    residual = np.asarray(data['rowspace_residuals'], dtype=float)
    gap = np.asarray(data['collision_gaps'], dtype=float)
    exact = np.asarray(data['exact_flags'], dtype=int)
    aug_rows = np.asarray(data['augmentation_rows'], dtype=float)

    fig, axes = plt.subplots(1, 2, figsize=(13, 5), constrained_layout=True)

    ax = axes[0]
    ax.set_facecolor(COLORS['background'])
    ax.set_title('M1. One-row augmentation direction scan')
    ax.plot(theta_deg, residual, color=COLORS['observation'], linewidth=2.0, label='row-space residual')
    ax.plot(theta_deg, gap, color=COLORS['impossible'], linewidth=1.8, linestyle='--', label='collision gap')
    fail_theta = theta_deg[exact == 0]
    if fail_theta.size > 0:
        for value in fail_theta[:: max(1, fail_theta.size // 5)]:
            ax.axvline(float(value), color='#6b7280', linewidth=0.8, alpha=0.35)
    ax.set_xlabel('augmentation direction angle θ (deg)')
    ax.set_ylabel('metric value')
    ax.grid(alpha=0.25, linestyle='--', linewidth=0.6)
    ax.legend(frameon=False, fontsize=8, loc='upper right')

    ax = axes[1]
    ax.set_facecolor(COLORS['background'])
    ax.set_title('M2. Augmentation direction geometry in (e₂,e₃)')
    ax.axhline(0.0, color='black', linewidth=0.8, alpha=0.35)
    ax.axvline(0.0, color='black', linewidth=0.8, alpha=0.35)
    colors = np.where(exact > 0, COLORS['protected'], COLORS['impossible'])
    ax.scatter(aug_rows[:, 1], aug_rows[:, 2], c=colors, s=18, alpha=0.9, edgecolors='none')
    base = np.asarray(data['base_observation_matrix'], dtype=float)
    base_dir = base[1, 1:] / max(np.linalg.norm(base[1, 1:]), 1e-12)
    ax.arrow(0.0, 0.0, float(base_dir[0]), float(base_dir[1]), color=COLORS['observation'], width=0.008, length_includes_head=True)
    ax.text(0.03, 0.96, 'green=exact, red=impossible', transform=ax.transAxes, va='top', fontsize=9)
    ax.set_xlabel('augmentation row component on e₂')
    ax.set_ylabel('augmentation row component on e₃')
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(-1.15, 1.15)
    ax.set_ylim(-1.15, 1.15)
    ax.grid(alpha=0.2, linestyle='--', linewidth=0.5)

    fig.suptitle('Minimal augmentation beyond count: direction choice controls exact repair (Exact)', fontsize=12, fontweight='bold')
    _save_static(fig, 'M_augmentation_direction_scan')
    generated.extend(['M_augmentation_direction_scan.svg', 'M_augmentation_direction_scan.png'])
    return generated


def figure_n_contamination_sweep() -> list[str]:
    data = contamination_sweep_visual_data()
    generated: list[str] = []

    rows = data['rows']
    c = np.asarray([row['contamination'] for row in rows], dtype=float)
    p_before = np.asarray([row['periodic_before_l2_divergence'] for row in rows], dtype=float)
    p_after = np.asarray([row['periodic_after_l2_divergence'] for row in rows], dtype=float)
    p_err = np.asarray([row['periodic_recovery_l2_error'] for row in rows], dtype=float)
    b_before = np.asarray([row['bounded_before_l2_divergence'] for row in rows], dtype=float)
    b_after = np.asarray([row['bounded_after_l2_divergence'] for row in rows], dtype=float)
    b_phys = np.asarray([row['bounded_boundary_normal_physical_rms'] for row in rows], dtype=float)
    b_proj = np.asarray([row['bounded_boundary_normal_projected_rms'] for row in rows], dtype=float)
    b_hodge = np.asarray([row['bounded_hodge_recovered_boundary_normal_rms'] for row in rows], dtype=float)

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.8), constrained_layout=True)

    ax = axes[0]
    ax.set_facecolor(COLORS['background'])
    ax.set_title('N1. Divergence suppression vs contamination')
    ax.plot(c, p_before, color='#6b7280', linewidth=1.5, label='periodic before')
    ax.plot(c, p_after, color=COLORS['protected'], linewidth=2.0, label='periodic after projection')
    ax.plot(c, b_before, color='#475569', linewidth=1.5, linestyle=':', label='bounded before')
    ax.plot(c, b_after, color=COLORS['impossible'], linewidth=1.8, label='bounded after transplant')
    ax.set_xlabel('contamination amplitude')
    ax.set_ylabel('L2 divergence')
    ax.set_yscale('log')
    ax.grid(alpha=0.25, linestyle='--', linewidth=0.6)
    ax.legend(frameon=False, fontsize=7.5, loc='upper left')

    ax = axes[1]
    ax.set_facecolor(COLORS['background'])
    ax.set_title('N2. Boundary-normal mismatch')
    ax.plot(c, b_phys, color=COLORS['protected'], linewidth=2.0, label='physical boundary rms')
    ax.plot(c, b_proj, color=COLORS['impossible'], linewidth=1.9, label='periodic transplant boundary rms')
    ax.plot(c, b_hodge, color=COLORS['repair'], linewidth=1.8, linestyle='--', label='bounded Hodge boundary rms')
    ax.set_xlabel('contamination amplitude')
    ax.set_ylabel('boundary-normal rms')
    ax.set_yscale('log')
    ax.grid(alpha=0.25, linestyle='--', linewidth=0.6)
    ax.legend(frameon=False, fontsize=7.5, loc='upper left')

    ax = axes[2]
    ax.set_facecolor(COLORS['background'])
    ratio = b_proj / np.maximum(b_hodge, 1e-12)
    ax.plot(c, p_err, color=COLORS['observation'], linewidth=2.0, label='periodic recovery L2 error')
    ax.plot(c, ratio, color=COLORS['repair'], linewidth=1.9, label='boundary mismatch ratio (proj/hodge)')
    ax.axhline(1.0, color='#6b7280', linewidth=0.8, alpha=0.7)
    ax.set_xlabel('contamination amplitude')
    ax.set_ylabel('error / ratio')
    ax.set_yscale('log')
    ax.grid(alpha=0.25, linestyle='--', linewidth=0.6)
    ax.legend(frameon=False, fontsize=7.5, loc='upper left')

    fig.suptitle('Periodic exactness vs bounded-domain obstruction across contamination levels (Validated)', fontsize=12, fontweight='bold')
    _save_static(fig, 'N_periodic_bounded_contamination_sweep')
    generated.extend(['N_periodic_bounded_contamination_sweep.svg', 'N_periodic_bounded_contamination_sweep.png'])
    return generated


def figure_o_visual_atlas(generated_files: Sequence[str]) -> list[str]:
    generated: list[str] = []
    png_paths = []
    for filename in generated_files:
        if filename.endswith('.png') and filename != 'O_visual_contact_sheet.png':
            path = DOC_OUT / filename
            if path.exists():
                png_paths.append(path)
    if not png_paths:
        return generated

    # Contact sheet for fast in-repo visual browsing.
    cols = 3
    rows = int(np.ceil(len(png_paths) / cols))
    fig, axes = plt.subplots(rows, cols, figsize=(cols * 4.6, rows * 3.2), constrained_layout=True)
    axes_list = np.atleast_1d(axes).ravel()
    for ax, path in zip(axes_list, png_paths):
        image = plt.imread(path)
        ax.imshow(image)
        ax.set_title(path.stem, fontsize=8.5)
        ax.axis('off')
    for ax in axes_list[len(png_paths):]:
        ax.axis('off')
    fig.suptitle('OCP Visual Contact Sheet (Exact/Schematic as labeled per panel)', fontsize=12, fontweight='bold')
    _save_static(fig, 'O_visual_contact_sheet')
    generated.extend(['O_visual_contact_sheet.svg', 'O_visual_contact_sheet.png'])

    # Multipage PDF atlas for a single-document image bundle.
    from matplotlib.backends.backend_pdf import PdfPages  # Local import keeps startup light.

    atlas_path = DOC_OUT / 'visual-atlas.pdf'
    with PdfPages(atlas_path) as pdf:
        for path in png_paths:
            page = plt.figure(figsize=(11, 8.5), constrained_layout=True)
            ax = page.add_subplot(111)
            ax.imshow(plt.imread(path))
            ax.axis('off')
            ax.set_title(path.stem, fontsize=13)
            pdf.savefig(page, bbox_inches='tight')
            plt.close(page)
    generated.append('visual-atlas.pdf')
    return generated


def figure_p_transition_tutorial_animation() -> list[str]:
    data = recoverability_transition_data(alphas=tuple(np.linspace(1.0, 0.0, 31)))
    rows = data['rows']
    generated: list[str] = []
    palette = plt.cm.tab20(np.linspace(0.03, 0.97, 20))
    alphas = np.asarray([float(row['alpha']) for row in rows], dtype=float)
    fiber_counts = np.asarray([int(row['fiber_count']) for row in rows], dtype=float)
    collision_gaps = np.asarray([float(row['collision_gap']) for row in rows], dtype=float)
    exact_flags = np.asarray([1.0 if bool(row['exact_recoverable']) else 0.0 for row in rows], dtype=float)

    # Static teaching panel.
    fig, axes = plt.subplots(2, 2, figsize=(13, 8), constrained_layout=True)
    key_indices = [0, len(rows) // 2, len(rows) - 1]
    for col, idx in enumerate(key_indices[:2]):
        row = rows[idx]
        ax = axes[0, col]
        _set_axis_2d(
            ax,
            f'P1. State fibers at α={row["alpha"]:.2f}',
            xlabel='state x₁',
            ylabel='state x₂',
        )
        states = np.asarray(row['state_points'], dtype=float)
        fids = np.asarray(row['fiber_index_per_state'], dtype=int)
        colors = [palette[int(fid) % len(palette)] for fid in fids]
        ax.scatter(states[:, 0], states[:, 1], c=colors, s=70, edgecolors='black', linewidths=0.35)
        ax.set_xlim(-1.3, 1.3)
        ax.set_ylim(-1.3, 1.3)
        ax.text(0.02, 0.95, f'fibers={row["fiber_count"]}', transform=ax.transAxes, va='top', fontsize=10)

    last = rows[key_indices[-1]]
    ax = axes[0, 1]
    _set_axis_2d(ax, f'P1. State fibers at α={last["alpha"]:.2f}', xlabel='state x₁', ylabel='state x₂')
    states = np.asarray(last['state_points'], dtype=float)
    fids = np.asarray(last['fiber_index_per_state'], dtype=int)
    colors = [palette[int(fid) % len(palette)] for fid in fids]
    ax.scatter(states[:, 0], states[:, 1], c=colors, s=70, edgecolors='black', linewidths=0.35)
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.text(
        0.02,
        0.95,
        f'fibers={last["fiber_count"]}, exact={last["exact_recoverable"]}',
        transform=ax.transAxes,
        va='top',
        fontsize=10,
        color=COLORS['impossible'],
    )

    ax = axes[1, 0]
    ax.set_facecolor(COLORS['background'])
    ax.set_title('P2. Fiber count and collision gap vs α', fontsize=11)
    ax.plot(alphas, fiber_counts, color=COLORS['observation'], linewidth=2.0, label='fiber count')
    ax.plot(alphas, collision_gaps, color=COLORS['impossible'], linewidth=2.0, linestyle='--', label='collision gap')
    ax.axvline(0.0, color='#475569', linewidth=1.0, alpha=0.7)
    ax.set_xlabel('α in Oα = [[1,0],[0,α]]')
    ax.set_ylabel('metric value')
    ax.grid(alpha=0.25, linestyle='--', linewidth=0.6)
    ax.legend(frameon=False, fontsize=8)

    ax = axes[1, 1]
    ax.set_facecolor(COLORS['background'])
    ax.set_title('P3. Exactness indicator', fontsize=11)
    ax.plot(alphas, exact_flags, color=COLORS['protected'], linewidth=2.0)
    ax.fill_between(alphas, 0, exact_flags, color=COLORS['protected'], alpha=0.2)
    ax.set_ylim(-0.05, 1.05)
    ax.set_yticks([0, 1], labels=['impossible', 'exact'])
    ax.set_xlabel('α')
    ax.set_ylabel('theorem verdict')
    ax.grid(alpha=0.25, linestyle='--', linewidth=0.6)
    ax.text(
        0.02,
        0.15,
        'Layperson reading:\nAs α shrinks, measurements collapse.\nAt α=0 different states become\nindistinguishable, so exact recovery fails.',
        transform=ax.transAxes,
        fontsize=9.5,
    )

    fig.suptitle('P. Why exact recovery can suddenly fail (Exact tutorial panel)', fontsize=13, fontweight='bold')
    _save_static(fig, 'P_transition_tutorial_panel')
    generated.extend(['P_transition_tutorial_panel.svg', 'P_transition_tutorial_panel.png'])

    # Tutorial animation with metrics and threshold narration.
    fig, axes = plt.subplots(2, 2, figsize=(13, 8), constrained_layout=True)
    ax_state, ax_obs = axes[0, 0], axes[0, 1]
    ax_metrics, ax_verdict = axes[1, 0], axes[1, 1]
    _set_axis_2d(ax_state, 'P4. State space (colored by current fibers)', xlabel='x₁', ylabel='x₂')
    _set_axis_2d(ax_obs, 'P5. Observation space Mα(x)', xlabel='y₁', ylabel='y₂')
    ax_state.set_xlim(-1.3, 1.3)
    ax_state.set_ylim(-1.3, 1.3)
    ax_obs.set_xlim(-1.3, 1.3)
    ax_obs.set_ylim(-1.3, 1.3)
    ax_obs.axhline(0.0, color='black', linewidth=0.8, alpha=0.4)
    ax_obs.axvline(0.0, color='black', linewidth=0.8, alpha=0.4)
    ax_state.axhline(0.0, color='black', linewidth=0.8, alpha=0.4)
    ax_state.axvline(0.0, color='black', linewidth=0.8, alpha=0.4)

    ax_metrics.set_facecolor(COLORS['background'])
    ax_metrics.set_title('P6. Metrics over α')
    ax_metrics.plot(alphas, fiber_counts, color=COLORS['observation'], linewidth=2.0, label='fiber count')
    ax_metrics.plot(alphas, collision_gaps, color=COLORS['impossible'], linewidth=2.0, linestyle='--', label='collision gap')
    ax_metrics.set_xlabel('α')
    ax_metrics.set_ylabel('metric')
    ax_metrics.grid(alpha=0.25, linestyle='--', linewidth=0.6)
    ax_metrics.legend(frameon=False, fontsize=8)
    marker_metrics = ax_metrics.scatter([alphas[0]], [fiber_counts[0]], c='black', s=45, zorder=4)

    ax_verdict.set_facecolor(COLORS['background'])
    ax_verdict.set_title('P7. Exactness verdict over α')
    ax_verdict.plot(alphas, exact_flags, color=COLORS['protected'], linewidth=2.0)
    ax_verdict.set_ylim(-0.05, 1.05)
    ax_verdict.set_yticks([0, 1], labels=['impossible', 'exact'])
    ax_verdict.set_xlabel('α')
    ax_verdict.set_ylabel('verdict')
    ax_verdict.grid(alpha=0.25, linestyle='--', linewidth=0.6)
    marker_verdict = ax_verdict.scatter([alphas[0]], [exact_flags[0]], c='black', s=45, zorder=4)
    annotation = ax_verdict.text(0.02, 0.12, '', transform=ax_verdict.transAxes, fontsize=9.5)

    first = rows[0]
    s_pts = np.asarray(first['state_points'], dtype=float)
    o_pts = np.asarray(first['observation_points'], dtype=float)
    fids = np.asarray(first['fiber_index_per_state'], dtype=int)
    colors = [palette[int(fid) % len(palette)] for fid in fids]
    scat_state = ax_state.scatter(s_pts[:, 0], s_pts[:, 1], c=colors, s=70, edgecolors='black', linewidths=0.35)
    scat_obs = ax_obs.scatter(o_pts[:, 0], o_pts[:, 1], c=colors, s=70, edgecolors='black', linewidths=0.35)
    title = fig.suptitle('', fontsize=12, fontweight='bold')

    def _update(frame_index: int):
        row = rows[int(frame_index)]
        s = np.asarray(row['state_points'], dtype=float)
        o = np.asarray(row['observation_points'], dtype=float)
        f = np.asarray(row['fiber_index_per_state'], dtype=int)
        c = [palette[int(fid) % len(palette)] for fid in f]
        a = float(row['alpha'])
        gap = float(row['collision_gap'])
        exact = bool(row['exact_recoverable'])
        fibers = int(row['fiber_count'])

        scat_state.set_offsets(s)
        scat_state.set_color(c)
        scat_obs.set_offsets(o)
        scat_obs.set_color(c)
        marker_metrics.set_offsets(np.asarray([[a, fibers]], dtype=float))
        marker_verdict.set_offsets(np.asarray([[a, 1.0 if exact else 0.0]], dtype=float))
        annotation.set_text(
            (
                f'α={a:.2f} | fibers={fibers} | gap={gap:.2f}\n'
                + ('Exact recovery still possible.' if exact else 'No-go: merged fibers break exact recovery.')
            )
        )
        title.set_text('Exact-to-impossible transition explained by fiber merging')
        return scat_state, scat_obs, marker_metrics, marker_verdict, annotation, title

    anim = animation.FuncAnimation(fig, _update, frames=len(rows), interval=260, blit=False)
    gif_path = DOC_OUT / 'P_transition_tutorial_animation.gif'
    mp4_path = DOC_OUT / 'P_transition_tutorial_animation.mp4'
    anim.save(gif_path, writer=animation.PillowWriter(fps=4))
    anim.save(mp4_path, writer=animation.FFMpegWriter(fps=6, bitrate=2000))
    plt.close(fig)
    generated.extend(['P_transition_tutorial_animation.gif', 'P_transition_tutorial_animation.mp4'])
    return generated


def figure_q_augmentation_tutorial_animation() -> list[str]:
    data = augmentation_direction_scan_data()
    generated: list[str] = []
    theta = np.asarray(data['theta_values'], dtype=float)
    theta_deg = np.degrees(theta)
    residual = np.asarray(data['rowspace_residuals'], dtype=float)
    gap = np.asarray(data['collision_gaps'], dtype=float)
    exact = np.asarray(data['exact_flags'], dtype=int)
    rows = np.asarray(data['augmentation_rows'], dtype=float)

    # Static panel.
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.8), constrained_layout=True)
    ax = axes[0]
    ax.set_facecolor(COLORS['background'])
    ax.set_title('Q1. Residual and gap vs augmentation direction')
    ax.plot(theta_deg, residual, color=COLORS['observation'], linewidth=2.0, label='row-space residual')
    ax.plot(theta_deg, gap, color=COLORS['impossible'], linewidth=2.0, linestyle='--', label='collision gap')
    ax.set_xlabel('direction angle θ (deg)')
    ax.set_ylabel('metric value')
    ax.grid(alpha=0.25, linestyle='--', linewidth=0.6)
    ax.legend(frameon=False, fontsize=8)

    ax = axes[1]
    ax.set_facecolor(COLORS['background'])
    ax.set_title('Q2. Direction circle (green exact, red fail)')
    colors = np.where(exact > 0, COLORS['protected'], COLORS['impossible'])
    ax.scatter(rows[:, 1], rows[:, 2], c=colors, s=18, edgecolors='none')
    ax.axhline(0.0, color='black', linewidth=0.8, alpha=0.35)
    ax.axvline(0.0, color='black', linewidth=0.8, alpha=0.35)
    ax.set_xlabel('component on e₂')
    ax.set_ylabel('component on e₃')
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(-1.15, 1.15)
    ax.set_ylim(-1.15, 1.15)
    ax.grid(alpha=0.2, linestyle='--', linewidth=0.5)

    ax = axes[2]
    ax.set_facecolor(COLORS['background'])
    ax.set_title('Q3. Layperson reading')
    ax.axis('off')
    ax.text(
        0.02,
        0.96,
        (
            'Adding one measurement is not enough by itself.\n\n'
            'You need the right direction.\n\n'
            'Same count can be exact or impossible,\n'
            'depending on alignment with the target.'
        ),
        va='top',
        fontsize=11,
    )
    fig.suptitle('Q. Minimal augmentation tutorial (Exact, direction-sensitive)', fontsize=12.5, fontweight='bold')
    _save_static(fig, 'Q_augmentation_tutorial_panel')
    generated.extend(['Q_augmentation_tutorial_panel.svg', 'Q_augmentation_tutorial_panel.png'])

    # Animation.
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.8), constrained_layout=True)
    ax_curve, ax_circle, ax_text = axes
    ax_curve.set_facecolor(COLORS['background'])
    ax_curve.set_title('Q4. Metrics vs direction angle')
    ax_curve.plot(theta_deg, residual, color=COLORS['observation'], linewidth=2.0, label='row-space residual')
    ax_curve.plot(theta_deg, gap, color=COLORS['impossible'], linewidth=2.0, linestyle='--', label='collision gap')
    ax_curve.set_xlabel('θ (deg)')
    ax_curve.set_ylabel('value')
    ax_curve.grid(alpha=0.25, linestyle='--', linewidth=0.6)
    ax_curve.legend(frameon=False, fontsize=8)

    ax_circle.set_facecolor(COLORS['background'])
    ax_circle.set_title('Q5. Augmentation row direction')
    ax_circle.scatter(rows[:, 1], rows[:, 2], c=np.where(exact > 0, COLORS['protected'], COLORS['impossible']), s=16, edgecolors='none', alpha=0.7)
    ax_circle.axhline(0.0, color='black', linewidth=0.8, alpha=0.35)
    ax_circle.axvline(0.0, color='black', linewidth=0.8, alpha=0.35)
    ax_circle.set_xlabel('e₂ component')
    ax_circle.set_ylabel('e₃ component')
    ax_circle.set_aspect('equal', adjustable='box')
    ax_circle.set_xlim(-1.15, 1.15)
    ax_circle.set_ylim(-1.15, 1.15)
    ax_circle.grid(alpha=0.2, linestyle='--', linewidth=0.5)

    ax_text.set_facecolor(COLORS['background'])
    ax_text.set_title('Q6. Current verdict')
    ax_text.axis('off')
    text_box = ax_text.text(0.02, 0.96, '', va='top', fontsize=11)
    marker_curve = ax_curve.scatter([theta_deg[0]], [residual[0]], c='black', s=45, zorder=4)
    marker_circle = ax_circle.scatter([rows[0, 1]], [rows[0, 2]], c='black', s=55, zorder=5)
    title = fig.suptitle('', fontsize=12.5, fontweight='bold')

    def _update(frame_index: int):
        i = int(frame_index)
        deg = float(theta_deg[i])
        r = float(residual[i])
        g = float(gap[i])
        is_exact = bool(exact[i] > 0)
        marker_curve.set_offsets(np.asarray([[deg, r]], dtype=float))
        marker_circle.set_offsets(np.asarray([[rows[i, 1], rows[i, 2]]], dtype=float))
        text_box.set_text(
            (
                f'θ={deg:.1f}°\n'
                f'row-space residual={r:.3f}\n'
                f'collision gap={g:.3f}\n'
                f'verdict={"EXACT" if is_exact else "IMPOSSIBLE"}'
            )
        )
        text_box.set_color(COLORS['protected'] if is_exact else COLORS['impossible'])
        title.set_text('Minimal augmentation: direction determines whether repair works')
        return marker_curve, marker_circle, text_box, title

    anim = animation.FuncAnimation(fig, _update, frames=len(theta_deg), interval=90, blit=False)
    gif_path = DOC_OUT / 'Q_augmentation_tutorial_animation.gif'
    mp4_path = DOC_OUT / 'Q_augmentation_tutorial_animation.mp4'
    anim.save(gif_path, writer=animation.PillowWriter(fps=10))
    anim.save(mp4_path, writer=animation.FFMpegWriter(fps=12, bitrate=2200))
    plt.close(fig)
    generated.extend(['Q_augmentation_tutorial_animation.gif', 'Q_augmentation_tutorial_animation.mp4'])
    return generated


def figure_r_program_story_map() -> list[str]:
    generated: list[str] = []
    fig, ax = plt.subplots(figsize=(14, 9), constrained_layout=True)
    ax.set_facecolor(COLORS['background'])
    ax.axis('off')

    # Main narrative nodes.
    nodes = [
        (0.5, 0.9, 'Step 1: Problem setup\nState = protected S + disturbance D', COLORS['neutral']),
        (0.5, 0.76, 'Step 2: Observation map M\nWhat collapses together?', COLORS['observation']),
        (0.5, 0.62, 'Step 3: Fiber / alignment tests\nCan target survive collapse?', COLORS['protected']),
        (0.5, 0.48, 'Step 4: Verdict\nExact / Asymptotic / Impossible', COLORS['repair']),
        (0.25, 0.32, 'Step 5A: Repair lane\nMinimal augmentation + direction', COLORS['repair']),
        (0.75, 0.32, 'Step 5B: Boundary lane\nPeriodic exact vs bounded no-go', COLORS['impossible']),
        (0.5, 0.15, 'Step 6: Program integration\nWorkbench + theorem docs + validations', COLORS['neutral']),
    ]
    for x, y, text, color in nodes:
        ax.text(
            x,
            y,
            text,
            ha='center',
            va='center',
            fontsize=11,
            color='white',
            bbox=dict(boxstyle='round,pad=0.42', facecolor=color, edgecolor='none', alpha=0.94),
        )

    edges = [
        ((0.5, 0.86), (0.5, 0.80)),
        ((0.5, 0.72), (0.5, 0.66)),
        ((0.5, 0.58), (0.5, 0.52)),
        ((0.5, 0.44), (0.29, 0.36)),
        ((0.5, 0.44), (0.71, 0.36)),
        ((0.25, 0.28), (0.46, 0.18)),
        ((0.75, 0.28), (0.54, 0.18)),
    ]
    for (x0, y0), (x1, y1) in edges:
        ax.annotate('', xy=(x1, y1), xytext=(x0, y0), arrowprops=dict(arrowstyle='->', color='#475569', linewidth=1.6))

    # Program location panel.
    panel_text = (
        'Where each step lives in the repo:\\n'
        '1) Core theorem spine: docs/finalization/theorem-spine-final.md\\n'
        '2) Fiber/recoverability branch: docs/fiber-based-recoverability-and-impossibility/\\n'
        '3) Same-rank and anti-classifier logic: docs/research-program/theorem-normalization-report.md\\n'
        '4) Dynamic/asymptotic layer: docs/theory/dynamic-correction-layer.md\\n'
        '5) Bounded-domain lane: docs/cfd/restricted-flow-recoverability.md\\n'
        '6) Workbench entry: docs/workbench/index.html'
    )
    ax.text(
        0.02,
        0.02,
        panel_text,
        ha='left',
        va='bottom',
        fontsize=10,
        family='monospace',
        color='#111827',
        bbox=dict(boxstyle='round,pad=0.35', facecolor='#f8fafc', edgecolor='#cbd5e1'),
    )
    ax.set_title('R. Complete OCP program story map (Schematic with exact repo pointers)', fontsize=14, fontweight='bold')
    _save_static(fig, 'R_ocp_program_story_map')
    generated.extend(['R_ocp_program_story_map.svg', 'R_ocp_program_story_map.png'])
    return generated


def main() -> None:
    _ensure_dirs()
    generated_files: list[str] = []

    summary = visual_summary()
    (DATA_OUT / 'visual_summary.json').write_text(json.dumps(summary, indent=2), encoding='utf-8')
    generated_files.append(str(Path('data/generated/visuals/visual_summary.json')))

    generated_files.extend(figure_a_core_geometry())
    generated_files.extend(figure_b_fiber_views())
    generated_files.extend(figure_c_transition_animation())
    generated_files.extend(figure_d_same_rank())
    generated_files.extend(figure_e_augmentation())
    generated_files.extend(figure_f_periodic_vs_bounded())
    generated_files.extend(figure_g_threshold_surfaces())
    generated_files.extend(figure_h_cross_system_map())
    generated_files.extend(figure_i_alignment_landscape())
    generated_files.extend(figure_j_perturbation_fragility())
    generated_files.extend(figure_k_family_enlargement())
    generated_files.extend(figure_l_dynamic_rates())
    generated_files.extend(figure_m_augmentation_direction_scan())
    generated_files.extend(figure_n_contamination_sweep())
    generated_files.extend(figure_p_transition_tutorial_animation())
    generated_files.extend(figure_q_augmentation_tutorial_animation())
    generated_files.extend(figure_r_program_story_map())
    generated_files.extend(figure_o_visual_atlas(generated_files))

    manifest = {
        'output_directory': str(DOC_OUT),
        'generated_files': generated_files,
    }
    (DOC_OUT / 'manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(f'wrote {DATA_OUT / "visual_summary.json"}')
    print(f'wrote {DOC_OUT / "manifest.json"}')
    for filename in generated_files:
        if filename.startswith('data/'):
            continue
        print(f'wrote {DOC_OUT / filename}')


if __name__ == '__main__':
    main()
