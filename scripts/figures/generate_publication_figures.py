#!/usr/bin/env python3
"""Generate publication figures for recoverability, MHD, and bridge papers.

All figures are computed from explicit linear-algebraic or analytic formulas used in the papers.
Outputs are saved as both PNG and PDF for publication workflows.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Rectangle
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

ROOT = Path(__file__).resolve().parents[2]
FIG_ROOT = ROOT / "figures"
OUT_JSON = ROOT / "data/generated/figures/publication_figure_metrics.json"


def setup_style() -> None:
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update(
        {
            "figure.dpi": 140,
            "savefig.dpi": 300,
            "font.size": 11,
            "axes.titlesize": 12,
            "axes.labelsize": 11,
            "legend.fontsize": 10,
        }
    )


def save_both(fig: plt.Figure, subdir: str, name: str) -> dict[str, str]:
    target_dir = FIG_ROOT / subdir
    target_dir.mkdir(parents=True, exist_ok=True)
    png = target_dir / f"{name}.png"
    pdf = target_dir / f"{name}.pdf"
    fig.tight_layout()
    fig.savefig(png, bbox_inches="tight")
    fig.savefig(pdf, bbox_inches="tight")
    plt.close(fig)
    return {"png": str(png), "pdf": str(pdf)}


def row_space_residual(l_row: np.ndarray, o_mat: np.ndarray) -> float:
    """Distance from target row to row-space of observation matrix."""
    # Solve O^T c ~= l^T for least-squares projection.
    c, *_ = np.linalg.lstsq(o_mat.T, l_row.T, rcond=None)
    proj = (o_mat.T @ c).T
    return float(np.linalg.norm(l_row - proj))


def gamma_box_bruteforce(o_mat: np.ndarray, l_row: np.ndarray, b: float, ngrid: int = 101) -> float:
    """Brute-force collision-gap on 3D coefficient box for small examples.

    We evaluate sup |l h| over h in [-2B,2B]^n with O h = 0.
    """
    n = o_mat.shape[1]
    vals = np.linspace(-2.0 * b, 2.0 * b, ngrid)
    mesh = np.meshgrid(*([vals] * n), indexing="ij")
    points = np.stack([m.reshape(-1) for m in mesh], axis=1)
    mask = np.linalg.norm(points @ o_mat.T, axis=1) <= 1e-10
    feasible = points[mask]
    if feasible.size == 0:
        return 0.0
    objective = np.abs(feasible @ l_row.T)
    return float(np.max(objective))


def recoverability_figures(metrics: dict) -> None:
    l = np.array([[1.0, 0.0]])
    o_exact = np.array([[1.0, 0.0]])
    o_fail = np.array([[0.0, 1.0]])

    res_exact = row_space_residual(l, o_exact)
    res_fail = row_space_residual(l, o_fail)
    metrics["recoverability_residuals"] = {"exact": res_exact, "fail": res_fail}

    # Figure 1: row-space inclusion vs failure geometry
    fig, axs = plt.subplots(1, 2, figsize=(10, 4))
    examples = [
        ("Inclusion (Exact)", o_exact, "#2a9d8f", res_exact),
        ("Exclusion (Failure)", o_fail, "#e76f51", res_fail),
    ]
    for ax, (title, o, color, residual) in zip(axs, examples):
        row_vec = o[0]
        t = np.linspace(-1.4, 1.4, 200)
        line = np.outer(t, row_vec / np.linalg.norm(row_vec))
        ax.plot(line[:, 0], line[:, 1], color=color, linewidth=2.2, label="row(O)")
        ax.arrow(0, 0, l[0, 0], l[0, 1], width=0.01, color="#264653", length_includes_head=True, label="target row")
        ax.scatter([l[0, 0]], [l[0, 1]], color="#264653", s=40)
        ax.set_title(f"{title}\nresidual = {residual:.2f}")
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.set_xlabel("component 1")
        ax.set_ylabel("component 2")
        ax.set_aspect("equal")
        ax.legend(loc="upper right")
    save_both(fig, "recoverability", "recoverability_rowspace_inclusion")

    # Figure 2: same-rank insufficiency scatter
    fig, ax = plt.subplots(figsize=(6.8, 4.4))
    ranks = [np.linalg.matrix_rank(o_exact), np.linalg.matrix_rank(o_fail)]
    residuals = [res_exact, res_fail]
    labels = ["O1 exact", "O2 impossible"]
    colors = ["#2a9d8f", "#e76f51"]
    for x, y, label, c in zip(ranks, residuals, labels, colors):
        ax.scatter(x, y, s=120, color=c)
        ax.annotate(label, (x + 0.02, y + 0.03), fontsize=10)
    ax.set_xticks([1])
    ax.set_xlabel("observation rank rank(OF)")
    ax.set_ylabel("row-space residual ||LF - Proj_row(OF)(LF)||")
    ax.set_title("Same-rank insufficiency: equal rank, opposite exactness verdict")
    ax.set_ylim(-0.05, 1.15)
    save_both(fig, "recoverability", "recoverability_same_rank_insufficiency")

    # Figure 3: collision-gap threshold Gamma_r(B)
    b = 1.0
    f = np.eye(3)
    l3 = np.array([[0.0, 0.0, 1.0]])
    o_levels = [
        np.array([[1.0, 0.0, 0.0]]),
        np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]),
        np.eye(3),
    ]
    gammas = [gamma_box_bruteforce(o @ f, l3 @ f, b=b, ngrid=101) for o in o_levels]
    metrics["recoverability_gamma"] = {"B": b, "values": gammas}

    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    r_idx = np.arange(1, len(gammas) + 1)
    ax.plot(r_idx, gammas, marker="o", linewidth=2.2, color="#264653")
    ax.axhline(0.0, color="black", linewidth=1)
    threshold = int(np.where(np.array(gammas) <= 1e-9)[0][0] + 1)
    ax.axvline(threshold, linestyle="--", color="#e76f51", linewidth=1.6, label=f"exactness threshold r*={threshold}")
    ax.set_xticks(r_idx)
    ax.set_xlabel("record level r")
    ax.set_ylabel("collision gap Γ_r(B)")
    ax.set_title("Nested collision-gap threshold law")
    ax.legend(loc="upper right")
    save_both(fig, "recoverability", "recoverability_collision_gap_threshold")

    # Figure 4: exact vs impossible regime transition by misalignment angle
    theta = np.linspace(0.0, np.pi / 2.0, 300)
    residual = []
    for t in theta:
        o = np.array([[np.cos(t), np.sin(t)]])
        residual.append(row_space_residual(l, o))
    residual = np.array(residual)
    eps_approx = 0.1

    fig, ax = plt.subplots(figsize=(7.4, 4.6))
    ax.plot(np.degrees(theta), residual, color="#1d3557", linewidth=2.2, label="row-space residual")
    ax.axhline(eps_approx, color="#2a9d8f", linestyle="--", linewidth=1.6, label=f"approximate zone cutoff ({eps_approx:.2f})")
    ax.fill_between(np.degrees(theta), 0, residual, where=residual <= eps_approx, color="#2a9d8f", alpha=0.25)
    ax.scatter([0], [0], color="#2a9d8f", s=70, label="exact point")
    ax.set_xlabel("misalignment angle (degrees)")
    ax.set_ylabel("target ambiguity surrogate")
    ax.set_title("Exact-to-impossible transition under observation misalignment")
    ax.legend(loc="upper left")
    metrics["recoverability_transition"] = {
        "epsilon_approx": eps_approx,
        "residual_at_0": float(residual[0]),
        "residual_at_90": float(residual[-1]),
    }
    save_both(fig, "recoverability", "recoverability_regime_transition")


def mixed_remainder_abs(r: np.ndarray, eta: np.ndarray, eta_prime: np.ndarray, a: float = 1.0, q0: float = 1.0, kappa: float = 0.5) -> np.ndarray:
    num = a * (kappa * r**2 * eta_prime + 2.0 * q0 * r * eta_prime + 4.0 * q0 * eta)
    return np.abs(num / r**4)


def mhd_figures(metrics: dict) -> None:
    r = np.linspace(0.05, 2.0, 800)

    # Figure 1: |R(r)| for constant eta and variable eta=r^k
    eta_const = np.ones_like(r)
    eta_const_prime = np.zeros_like(r)
    eta_var = r**2
    eta_var_prime = 2.0 * r

    r_const = mixed_remainder_abs(r, eta_const, eta_const_prime)
    r_var = mixed_remainder_abs(r, eta_var, eta_var_prime)

    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    ax.plot(r, r_const, color="#264653", linewidth=2.2, label="constant η = 1")
    ax.plot(r, r_var, color="#e76f51", linewidth=2.2, label="variable η = r²")
    ax.set_yscale("log")
    ax.set_xlabel("r")
    ax.set_ylabel("|R(r)|")
    ax.set_title("Closure-defect magnitude for constant vs variable resistivity")
    ax.legend(loc="upper right")
    save_both(fig, "mhd", "mhd_remainder_constant_vs_variable_eta")

    # Figure 2: singularity behavior near r->0
    r_small = np.logspace(-4, -1, 500)
    curves = {
        "η=1": mixed_remainder_abs(r_small, np.ones_like(r_small), np.zeros_like(r_small)),
        "η=r": mixed_remainder_abs(r_small, r_small, np.ones_like(r_small)),
        "η=r²": mixed_remainder_abs(r_small, r_small**2, 2.0 * r_small),
        "η=r³": mixed_remainder_abs(r_small, r_small**3, 3.0 * r_small**2),
    }
    fig, ax = plt.subplots(figsize=(7.4, 4.8))
    for label, vals in curves.items():
        ax.loglog(r_small, vals, linewidth=2.0, label=label)
    ax.set_xlabel("r")
    ax.set_ylabel("|R(r)|")
    ax.set_title("Near-axis singular behavior of the closure remainder")
    ax.legend(loc="upper right")
    save_both(fig, "mhd", "mhd_singularity_near_axis")

    # Figure 3: sheet-thinning scaling max|R| ~ eps/delta
    eta0 = 1.0
    eps = 0.02
    r0 = 1.0
    deltas = np.array([0.40, 0.30, 0.22, 0.16, 0.12, 0.09, 0.07, 0.05])
    # Gradient-dominated annular window to isolate the sheet-thinning contribution.
    r_grid = np.linspace(0.60, 1.40, 3000)

    max_vals = []
    for d in deltas:
        eta = eta0 + eps * np.tanh((r_grid - r0) / d)
        sech2 = 1.0 / np.cosh((r_grid - r0) / d) ** 2
        eta_prime = eps * sech2 / d
        max_vals.append(float(np.max(mixed_remainder_abs(r_grid, eta, eta_prime, q0=0.0, kappa=1.0))))
    max_vals = np.array(max_vals)

    x = 1.0 / deltas
    slope, intercept = np.polyfit(x, max_vals, 1)

    fig, axs = plt.subplots(1, 2, figsize=(11.0, 4.2))
    axs[0].plot(x, max_vals, "o-", color="#1d3557", label="computed maxima")
    axs[0].plot(x, slope * x + intercept, "--", color="#e76f51", label=f"linear fit (slope={slope:.3f})")
    axs[0].set_xlabel("1/δ")
    axs[0].set_ylabel("max |R|")
    axs[0].set_title("Sheet-thinning scaling (gradient-dominated lane)")
    axs[0].legend(loc="upper left")

    normalized = max_vals * deltas / eps
    axs[1].plot(deltas, normalized, "o-", color="#2a9d8f")
    axs[1].set_xlabel("δ")
    axs[1].set_ylabel("max|R| · δ / ε")
    axs[1].set_title("Normalization check for ~ ε/δ behavior")
    axs[1].invert_xaxis()

    metrics["mhd_sheet_scaling"] = {
        "deltas": deltas.tolist(),
        "max_values": max_vals.tolist(),
        "fit_slope": float(slope),
        "fit_intercept": float(intercept),
    }
    save_both(fig, "mhd", "mhd_sheet_thinning_scaling")

    # Figure 4: axis-touching vs annular domain behavior
    r_min = np.logspace(-4, -0.15, 250)
    l2_log = np.sqrt(1.0 / r_min - 1.0)  # integral of (1/r)^2 on [r_min,1]
    l2_sqrt = np.sqrt(0.25 * np.log(1.0 / r_min))  # integral of (1/(2sqrt(r)))^2 on [r_min,1]

    fig, ax = plt.subplots(figsize=(7.4, 4.8))
    ax.loglog(r_min, l2_log, color="#e63946", linewidth=2.2, label="f(r)=log r survivor profile")
    ax.loglog(r_min, l2_sqrt, color="#457b9d", linewidth=2.2, label="f(r)=sqrt(r) survivor profile")
    ax.axvline(0.2, color="black", linestyle="--", linewidth=1.2, label="example annular cutoff r_min=0.2")
    ax.set_xlabel("inner radius r_min")
    ax.set_ylabel("||f'(r)||_{L2([r_min,1])}")
    ax.set_title("Axis-touching limit vs annular regularization")
    ax.legend(loc="upper right")
    metrics["mhd_domain_behavior"] = {
        "l2_log_at_0p2": float(np.interp(0.2, r_min, l2_log)),
        "l2_sqrt_at_0p2": float(np.interp(0.2, r_min, l2_sqrt)),
    }
    save_both(fig, "mhd", "mhd_axis_vs_annular_behavior")


@dataclass
class BridgeData:
    x: np.ndarray
    p_true: np.ndarray
    c_periodic: np.ndarray
    c_bounded: np.ndarray


def build_bridge_data(seed: int = 12, n: int = 3000) -> BridgeData:
    rng = np.random.default_rng(seed)
    s = rng.normal(0.0, 1.0, n)
    d_div = rng.normal(0.0, 1.0, n)
    d_bdry = rng.normal(0.0, 1.0, n)
    x = np.stack([s, d_div, d_bdry], axis=1)
    p_true = np.stack([s, np.zeros_like(s), np.zeros_like(s)], axis=1)
    c_periodic = np.diag([1.0, 0.0, 0.0])
    c_bounded = np.diag([1.0, 0.0, 1.0])
    return BridgeData(x=x, p_true=p_true, c_periodic=c_periodic, c_bounded=c_bounded)


def bridge_figures(metrics: dict) -> None:
    data = build_bridge_data()
    x = data.x
    p_true = data.p_true

    x_per = x @ data.c_periodic.T
    x_bad = x @ data.c_bounded.T

    # divergence metric: second coordinate magnitude
    div_before = np.abs(x[:, 1])
    div_after_per = np.abs(x_per[:, 1])
    div_after_bad = np.abs(x_bad[:, 1])

    err_per = np.linalg.norm(x_per - p_true, axis=1)
    err_bad = np.linalg.norm(x_bad - p_true, axis=1)

    metrics["bridge_errors"] = {
        "mean_div_after_periodic": float(np.mean(div_after_per)),
        "mean_div_after_bounded": float(np.mean(div_after_bad)),
        "mean_error_periodic": float(np.mean(err_per)),
        "mean_error_bounded": float(np.mean(err_bad)),
    }

    # Figure 1: divergence reduction vs actual recovery
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.4))
    sample = slice(0, 1200)
    axs[0].scatter(div_after_per[sample], err_per[sample], s=10, alpha=0.45, color="#2a9d8f", label="periodic exact lane")
    axs[0].scatter(div_after_bad[sample], err_bad[sample], s=10, alpha=0.45, color="#e76f51", label="bounded transplant lane")
    axs[0].set_xlabel("post-correction divergence magnitude")
    axs[0].set_ylabel("protected-state recovery error")
    axs[0].set_title("Divergence reduction does not imply exact recovery")
    axs[0].legend(loc="upper right")

    labels = ["periodic", "bounded"]
    mean_div = [np.mean(div_after_per), np.mean(div_after_bad)]
    mean_err = [np.mean(err_per), np.mean(err_bad)]
    x_pos = np.arange(len(labels))
    w = 0.35
    axs[1].bar(x_pos - w / 2, mean_div, width=w, color="#457b9d", label="mean post-correction divergence")
    axs[1].bar(x_pos + w / 2, mean_err, width=w, color="#e63946", label="mean recovery error")
    axs[1].set_xticks(x_pos)
    axs[1].set_xticklabels(labels)
    axs[1].set_title("Periodic vs bounded transplant summary")
    axs[1].legend(loc="upper right")

    save_both(fig, "bridge", "bridge_divergence_vs_recovery")

    # Figure 2: projection success vs failure in 3D state space
    x0 = np.array([1.0, 1.0, 1.2])
    x0_per = data.c_periodic @ x0
    x0_bad = data.c_bounded @ x0
    p0 = np.array([1.0, 0.0, 0.0])

    fig = plt.figure(figsize=(8.0, 6.0))
    ax = fig.add_subplot(111, projection="3d")

    def draw_vec(v: np.ndarray, color: str, label: str):
        ax.quiver(0, 0, 0, v[0], v[1], v[2], color=color, linewidth=2.5)
        ax.text(v[0], v[1], v[2], label, color=color)

    draw_vec(x0, "#6d597a", "state x")
    draw_vec(p0, "#2a9d8f", "protected component")
    draw_vec(x0_per, "#1d3557", "C_periodic x")
    draw_vec(x0_bad, "#e76f51", "C_bounded x")

    ax.set_xlabel("protected axis")
    ax.set_ylabel("divergence axis")
    ax.set_zlabel("boundary-mismatch axis")
    ax.set_title("Projection success vs failure on one representative state")
    lim = 1.4
    ax.set_xlim(0, lim)
    ax.set_ylim(0, lim)
    ax.set_zlim(0, lim)
    save_both(fig, "bridge", "bridge_projection_success_vs_failure")

    # Figure 3: operator-component diagram (data-driven labels)
    mean_abs = np.mean(np.abs(x), axis=0)
    mean_err_per = float(np.mean(err_per))
    mean_err_bad = float(np.mean(err_bad))

    fig, ax = plt.subplots(figsize=(10.0, 4.8))
    ax.set_axis_off()

    def box(xy, w, h, text, fc="#f8f9fa", ec="#343a40"):
        rect = Rectangle(xy, w, h, facecolor=fc, edgecolor=ec, linewidth=1.5)
        ax.add_patch(rect)
        ax.text(xy[0] + w / 2, xy[1] + h / 2, text, ha="center", va="center")

    box((0.03, 0.60), 0.24, 0.28, f"State x\nmean |s|={mean_abs[0]:.2f}\nmean |d_div|={mean_abs[1]:.2f}\nmean |d_bdry|={mean_abs[2]:.2f}")
    box((0.36, 0.70), 0.22, 0.18, "C_periodic\n(Helmholtz/Leray lane)", fc="#e8f7f2")
    box((0.36, 0.42), 0.22, 0.18, "C_bounded transplant\n(mismatched boundary lane)", fc="#fdecea")
    box((0.68, 0.70), 0.26, 0.18, f"Output: periodic\nmean error={mean_err_per:.3f}", fc="#e8f7f2")
    box((0.68, 0.42), 0.26, 0.18, f"Output: bounded\nmean error={mean_err_bad:.3f}", fc="#fdecea")

    arrows = [
        ((0.27, 0.79), (0.36, 0.79)),
        ((0.27, 0.51), (0.36, 0.51)),
        ((0.58, 0.79), (0.68, 0.79)),
        ((0.58, 0.51), (0.68, 0.51)),
    ]
    for p0, p1 in arrows:
        arr = FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=15, linewidth=1.5, color="#495057")
        ax.add_patch(arr)

    ax.text(0.5, 0.18, "Both lanes reduce divergence components; only the periodic-compatible lane recovers the protected state exactly.", ha="center", fontsize=10)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title("Protected + disturbance + correction architecture (computed summary)")
    save_both(fig, "bridge", "bridge_operator_component_diagram")


def main() -> None:
    setup_style()
    metrics: dict[str, object] = {}
    recoverability_figures(metrics)
    mhd_figures(metrics)
    bridge_figures(metrics)

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUT_JSON.open("w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    print("Generated publication figures and metrics:")
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
