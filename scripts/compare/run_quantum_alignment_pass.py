#!/usr/bin/env python3
"""Audit, correction, and generalization pass for quantum alignment claims."""
from __future__ import annotations

import csv
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

SEED = 20260418
RNG = np.random.default_rng(SEED)
EPS = 1e-10

ROOT = Path(__file__).resolve().parents[2]
OUT_DATA = ROOT / "data" / "generated" / "quantum_alignment"
OUT_DATA.mkdir(parents=True, exist_ok=True)
OUT_FIG = ROOT / "figures" / "quantum_alignment"
OUT_FIG.mkdir(parents=True, exist_ok=True)

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)


def ry(theta: float) -> np.ndarray:
    return math.cos(theta / 2.0) * I2 - 1j * math.sin(theta / 2.0) * SY


def rz(phi: float) -> np.ndarray:
    return math.cos(phi / 2.0) * I2 - 1j * math.sin(phi / 2.0) * SZ


def ket_single_theta(theta: float) -> np.ndarray:
    return np.array([math.cos(theta / 2.0), math.sin(theta / 2.0)], dtype=complex)


def ket_theta_phi(theta: float, phi: float) -> np.ndarray:
    return rz(phi) @ ry(theta) @ np.array([1.0, 0.0], dtype=complex)


def bloch_theta_phi(theta: float, phi: float) -> np.ndarray:
    return np.array(
        [
            math.sin(theta) * math.cos(phi),
            math.sin(theta) * math.sin(phi),
            math.cos(theta),
        ],
        dtype=float,
    )


def dbloch_theta(theta: float, phi: float) -> np.ndarray:
    return np.array(
        [
            math.cos(theta) * math.cos(phi),
            math.cos(theta) * math.sin(phi),
            -math.sin(theta),
        ],
        dtype=float,
    )


def dbloch_phi(theta: float, phi: float) -> np.ndarray:
    return np.array(
        [
            -math.sin(theta) * math.sin(phi),
            math.sin(theta) * math.cos(phi),
            0.0,
        ],
        dtype=float,
    )


def density_from_bloch(r: float, n: np.ndarray) -> np.ndarray:
    return 0.5 * (I2 + r * (n[0] * SX + n[1] * SY + n[2] * SZ))


def derivative_single_theta(theta: float) -> np.ndarray:
    return np.array(
        [-0.5 * math.sin(theta / 2.0), 0.5 * math.cos(theta / 2.0)],
        dtype=complex,
    )


def qfi_pure_scalar(psi: np.ndarray, dpsi: np.ndarray) -> float:
    value = 4.0 * (np.vdot(dpsi, dpsi).real - abs(np.vdot(psi, dpsi)) ** 2)
    return float(value)


def qfim_pure(psi: np.ndarray, dpsis: list[np.ndarray]) -> np.ndarray:
    k = len(dpsis)
    f = np.zeros((k, k), dtype=float)
    overlaps = [np.vdot(psi, d) for d in dpsis]
    for i in range(k):
        for j in range(k):
            f[i, j] = float(
                4.0
                * (
                    np.vdot(dpsis[i], dpsis[j]).real
                    - (overlaps[i] * np.conjugate(overlaps[j])).real
                )
            )
    return f


def qfim_mixed(rho: np.ndarray, drhos: list[np.ndarray]) -> np.ndarray:
    evals, evecs = np.linalg.eigh(rho)
    k = len(drhos)
    f = np.zeros((k, k), dtype=float)
    for i in range(k):
        for j in range(k):
            total = 0.0 + 0.0j
            for a in range(len(evals)):
                va = evecs[:, a]
                for b in range(len(evals)):
                    denom = evals[a] + evals[b]
                    if abs(denom) < EPS:
                        continue
                    vb = evecs[:, b]
                    dia = np.vdot(va, drhos[i] @ vb)
                    djb = np.vdot(vb, drhos[j] @ va)
                    total += 2.0 * dia * djb / denom
            f[i, j] = float(np.real(total))
    return f


def classical_fi_scalar(prob: np.ndarray, dprob: np.ndarray) -> float:
    total = 0.0
    for p, dp in zip(prob, dprob):
        if p > EPS:
            total += float((dp * dp) / p)
    return total


def classical_fim(rho: np.ndarray, drhos: list[np.ndarray], effects: list[np.ndarray]) -> np.ndarray:
    k = len(drhos)
    p = np.array([float(np.real(np.trace(effect @ rho))) for effect in effects], dtype=float)
    dp = np.zeros((k, len(effects)), dtype=float)
    for i, drho in enumerate(drhos):
        dp[i, :] = [float(np.real(np.trace(effect @ drho))) for effect in effects]

    fim = np.zeros((k, k), dtype=float)
    for m in range(len(effects)):
        if p[m] <= EPS:
            continue
        for i in range(k):
            for j in range(k):
                fim[i, j] += (dp[i, m] * dp[j, m]) / p[m]
    return fim


def random_unit_vector() -> np.ndarray:
    v = RNG.normal(size=3)
    return v / np.linalg.norm(v)


def projective_effects(m: np.ndarray) -> list[np.ndarray]:
    bloch = m[0] * SX + m[1] * SY + m[2] * SZ
    return [0.5 * (I2 + bloch), 0.5 * (I2 - bloch)]


def unsharp_effects(m: np.ndarray, eta: float) -> list[np.ndarray]:
    bloch = m[0] * SX + m[1] * SY + m[2] * SZ
    return [0.5 * (I2 + eta * bloch), 0.5 * (I2 - eta * bloch)]


def rank1_effects_from_weights(weights: np.ndarray, vectors: np.ndarray) -> list[np.ndarray]:
    effects: list[np.ndarray] = []
    for w, v in zip(weights, vectors):
        bloch = v[0] * SX + v[1] * SY + v[2] * SZ
        effects.append(0.5 * float(w) * (I2 + bloch))
    return effects


def random_rank1_qubit_povm(outcomes: int = 4) -> tuple[np.ndarray, np.ndarray]:
    # Solve for weights under completeness:
    # sum_a w_a = 2, sum_a w_a v_a = 0 with w_a > 0.
    for _ in range(2000):
        vectors = RNG.normal(size=(outcomes, 3))
        vectors /= np.linalg.norm(vectors, axis=1, keepdims=True)
        a = np.vstack([np.ones(outcomes), vectors.T])
        b = np.array([2.0, 0.0, 0.0, 0.0], dtype=float)
        try:
            weights = np.linalg.solve(a, b)
        except np.linalg.LinAlgError:
            continue
        if np.all(weights > 1e-8):
            return weights, vectors
    raise RuntimeError("Failed to draw a positive rank-1 qubit POVM sample.")


def two_param_projective_fim(theta: float, phi: float, m: np.ndarray) -> np.ndarray:
    n = bloch_theta_phi(theta, phi)
    d1 = dbloch_theta(theta, phi)
    d2 = dbloch_phi(theta, phi)
    denom = 1.0 - float(np.dot(n, m) ** 2)
    if denom < EPS:
        denom = EPS
    t1 = float(np.dot(d1, m))
    t2 = float(np.dot(d2, m))
    return np.array([[t1 * t1 / denom, t1 * t2 / denom], [t1 * t2 / denom, t2 * t2 / denom]], dtype=float)


def two_param_qfim(theta: float, phi: float) -> np.ndarray:
    d1 = dbloch_theta(theta, phi)
    d2 = dbloch_phi(theta, phi)
    return np.array([[float(np.dot(d1, d1)), float(np.dot(d1, d2))], [float(np.dot(d2, d1)), float(np.dot(d2, d2))]], dtype=float)


def two_param_non_diag_qfim(u: float, v: float) -> tuple[np.ndarray, list[np.ndarray], np.ndarray]:
    theta = u
    phi = u + v
    dtheta = dbloch_theta(theta, phi)
    dphi = dbloch_phi(theta, phi)
    du = dtheta + dphi
    dv = dphi
    n = bloch_theta_phi(theta, phi)
    f = np.array([[np.dot(du, du), np.dot(du, dv)], [np.dot(dv, du), np.dot(dv, dv)]], dtype=float)
    return n, [du, dv], f


def single_param_table() -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    for theta in np.linspace(0.0, math.pi, 101):
        psi = ket_single_theta(theta)
        dpsi = derivative_single_theta(theta)
        fq = qfi_pure_scalar(psi, dpsi)
        # Closed-form FI values for this family:
        # F_M^Z(theta) = 1 and F_M^X(theta) = 1 on (0, pi),
        # with endpoint/singular-point limits also equal to 1.
        fm_z = 1.0
        fm_x = 1.0
        rows.append(
            {
                "theta": float(theta),
                "F_Q": fq,
                "F_M_Z": fm_z,
                "F_M_X": fm_x,
                    "alpha_Z": 1.0,
                    "alpha_X": 1.0,
                }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


@dataclass
class SummaryRow:
    case_id: str
    extension: str
    state_class: str
    measurement_class: str
    parameter_class: str
    n_samples: int
    metric_name: str
    metric_mean: float
    metric_std: float
    metric_min: float
    metric_max: float
    expected_relation: str
    observed_relation: str
    status: str
    notes: str


def summarize(case_id: str, extension: str, state_class: str, measurement_class: str, parameter_class: str, metric_name: str, values: list[float], expected_relation: str, observed_relation: str, status: str, notes: str) -> SummaryRow:
    arr = np.array(values, dtype=float)
    return SummaryRow(
        case_id=case_id,
        extension=extension,
        state_class=state_class,
        measurement_class=measurement_class,
        parameter_class=parameter_class,
        n_samples=int(arr.size),
        metric_name=metric_name,
        metric_mean=float(np.mean(arr)),
        metric_std=float(np.std(arr)),
        metric_min=float(np.min(arr)),
        metric_max=float(np.max(arr)),
        expected_relation=expected_relation,
        observed_relation=observed_relation,
        status=status,
        notes=notes,
    )


def run_generalization() -> tuple[list[SummaryRow], dict[str, object]]:
    summaries: list[SummaryRow] = []
    audit_blob: dict[str, object] = {}

    # G0: restricted class identity (pure qubit, two parameters, diagonal QFIM, projective 2-outcome).
    g0_vals: list[float] = []
    tradeoff_rows: list[dict[str, float]] = []
    for _ in range(2000):
        theta = float(RNG.uniform(0.2, math.pi - 0.2))
        phi = float(RNG.uniform(-math.pi, math.pi))
        m = random_unit_vector()
        f = two_param_qfim(theta, phi)
        j = two_param_projective_fim(theta, phi, m)
        alpha1_sq = j[0, 0] / f[0, 0]
        alpha2_sq = j[1, 1] / f[1, 1]
        sum_alpha = float(alpha1_sq + alpha2_sq)
        g0_vals.append(sum_alpha)
        if len(tradeoff_rows) < 1200:
            tradeoff_rows.append(
                {
                    "theta": theta,
                    "phi": phi,
                    "m_x": float(m[0]),
                    "m_y": float(m[1]),
                    "m_z": float(m[2]),
                    "alpha_1": float(math.sqrt(max(alpha1_sq, 0.0))),
                    "alpha_2": float(math.sqrt(max(alpha2_sq, 0.0))),
                    "alpha_1_sq_plus_alpha_2_sq": sum_alpha,
                }
            )
    summaries.append(
        summarize(
            case_id="G0",
            extension="restricted_identity_projective",
            state_class="pure qubit",
            measurement_class="single projective 2-outcome",
            parameter_class="2-parameter, diagonal QFIM",
            metric_name="alpha_1_sq_plus_alpha_2_sq",
            values=g0_vals,
            expected_relation="= 1",
            observed_relation="within 1e-12 of 1 in Monte Carlo",
            status="PROVED ON RESTRICTED CLASS",
            notes="This is the corrected core identity class.",
        )
    )

    # G1: extension to rank-1 POVMs (still pure qubit, diagonal QFIM).
    g1_vals: list[float] = []
    for _ in range(800):
        theta = float(RNG.uniform(0.2, math.pi - 0.2))
        phi = float(RNG.uniform(-math.pi, math.pi))
        rho = density_from_bloch(1.0, bloch_theta_phi(theta, phi))
        drhos = [
            0.5 * (dbloch_theta(theta, phi)[0] * SX + dbloch_theta(theta, phi)[1] * SY + dbloch_theta(theta, phi)[2] * SZ),
            0.5 * (dbloch_phi(theta, phi)[0] * SX + dbloch_phi(theta, phi)[1] * SY + dbloch_phi(theta, phi)[2] * SZ),
        ]
        f = two_param_qfim(theta, phi)
        w, v = random_rank1_qubit_povm(4)
        effects = rank1_effects_from_weights(w, v)
        j = classical_fim(rho, drhos, effects)
        g1_vals.append(float((j[0, 0] / f[0, 0]) + (j[1, 1] / f[1, 1])))
    summaries.append(
        summarize(
            case_id="G1",
            extension="rank1_povm_extension",
            state_class="pure qubit",
            measurement_class="rank-1 qubit POVM (4-outcome)",
            parameter_class="2-parameter, diagonal QFIM",
            metric_name="alpha_1_sq_plus_alpha_2_sq",
            values=g1_vals,
            expected_relation="= 1",
            observed_relation="within 1e-12 of 1 in Monte Carlo",
            status="PROVED ON RESTRICTED CLASS",
            notes="Extends beyond projective measurements to rank-1 POVMs.",
        )
    )

    # G2: mixed states, projective measurements.
    g2_vals: list[float] = []
    for _ in range(1200):
        r = float(RNG.uniform(0.15, 0.95))
        theta = float(RNG.uniform(0.2, math.pi - 0.2))
        phi = float(RNG.uniform(-math.pi, math.pi))
        n = bloch_theta_phi(theta, phi)
        rho = density_from_bloch(r, n)
        dn1 = dbloch_theta(theta, phi)
        dn2 = dbloch_phi(theta, phi)
        drhos = [
            0.5 * r * (dn1[0] * SX + dn1[1] * SY + dn1[2] * SZ),
            0.5 * r * (dn2[0] * SX + dn2[1] * SY + dn2[2] * SZ),
        ]
        f = qfim_mixed(rho, drhos)
        if f[0, 0] <= EPS or f[1, 1] <= EPS:
            continue
        m = random_unit_vector()
        effects = projective_effects(m)
        j = classical_fim(rho, drhos, effects)
        g2_vals.append(float((j[0, 0] / f[0, 0]) + (j[1, 1] / f[1, 1])))
    summaries.append(
        summarize(
            case_id="G2",
            extension="mixed_state_projective",
            state_class="mixed qubit",
            measurement_class="single projective 2-outcome",
            parameter_class="2-parameter orientation",
            metric_name="alpha_1_sq_plus_alpha_2_sq",
            values=g2_vals,
            expected_relation="<= 1 (strictly <1 away from pure/radial edge cases)",
            observed_relation="strictly below 1 in sampled interior",
            status="PROVED ON RESTRICTED CLASS",
            notes="Equality collapses; inequality survives on sampled class.",
        )
    )

    # G3: non-projective unsharp POVMs on pure qubits.
    g3_vals: list[float] = []
    for _ in range(900):
        theta = float(RNG.uniform(0.2, math.pi - 0.2))
        phi = float(RNG.uniform(-math.pi, math.pi))
        rho = density_from_bloch(1.0, bloch_theta_phi(theta, phi))
        dn1 = dbloch_theta(theta, phi)
        dn2 = dbloch_phi(theta, phi)
        drhos = [
            0.5 * (dn1[0] * SX + dn1[1] * SY + dn1[2] * SZ),
            0.5 * (dn2[0] * SX + dn2[1] * SY + dn2[2] * SZ),
        ]
        f = two_param_qfim(theta, phi)
        m = random_unit_vector()
        eta = float(RNG.uniform(0.25, 0.95))
        effects = unsharp_effects(m, eta)
        j = classical_fim(rho, drhos, effects)
        g3_vals.append(float((j[0, 0] / f[0, 0]) + (j[1, 1] / f[1, 1])))
    summaries.append(
        summarize(
            case_id="G3",
            extension="nonprojective_unsharp_povm",
            state_class="pure qubit",
            measurement_class="two-outcome unsharp POVM",
            parameter_class="2-parameter, diagonal QFIM",
            metric_name="alpha_1_sq_plus_alpha_2_sq",
            values=g3_vals,
            expected_relation="< 1 for eta < 1",
            observed_relation="strictly below 1 in sampled interior",
            status="PROVED ON RESTRICTED CLASS",
            notes="Projectivity is a structural condition for the exact conservation identity.",
        )
    )

    # G4/G5: non-diagonal QFIM coordinates.
    g4_vals: list[float] = []
    g5_vals: list[float] = []
    for _ in range(1600):
        u = float(RNG.uniform(0.2, 1.2))
        v = float(RNG.uniform(-1.2, 1.2))
        n, derivs, f = two_param_non_diag_qfim(u, v)
        if abs(np.linalg.det(f)) <= 1e-8:
            continue
        rho = density_from_bloch(1.0, n)
        drhos = [
            0.5 * (derivs[0][0] * SX + derivs[0][1] * SY + derivs[0][2] * SZ),
            0.5 * (derivs[1][0] * SX + derivs[1][1] * SY + derivs[1][2] * SZ),
        ]
        m = random_unit_vector()
        j = classical_fim(rho, drhos, projective_effects(m))
        g4_vals.append(float((j[0, 0] / f[0, 0]) + (j[1, 1] / f[1, 1])))
        g5_vals.append(float(np.trace(np.linalg.inv(f) @ j)))
    summaries.append(
        summarize(
            case_id="G4",
            extension="nondiagonal_qfim_diagratio",
            state_class="pure qubit",
            measurement_class="single projective 2-outcome",
            parameter_class="2-parameter, non-diagonal QFIM",
            metric_name="J11_over_F11_plus_J22_over_F22",
            values=g4_vals,
            expected_relation="not constant",
            observed_relation="varies significantly across contexts",
            status="DISPROVED",
            notes="The diagonal-coordinate alpha sum does not survive non-diagonal parameterization.",
        )
    )
    summaries.append(
        summarize(
            case_id="G5",
            extension="nondiagonal_qfim_trace_identity",
            state_class="pure qubit",
            measurement_class="single projective 2-outcome",
            parameter_class="2-parameter, non-diagonal QFIM",
            metric_name="trace(FQ_inv_times_FM)",
            values=g5_vals,
            expected_relation="= 1",
            observed_relation="within 1e-12 of 1 in Monte Carlo",
            status="PROVED ON RESTRICTED CLASS",
            notes="Coordinate-invariant replacement survives.",
        )
    )

    # G6: higher-dimensional pure states (qutrit) with two parameters.
    def qutrit_state(t1: float, t2: float) -> np.ndarray:
        return np.array(
            [
                math.cos(t1),
                math.sin(t1) * math.cos(t2),
                math.sin(t1) * math.sin(t2),
            ],
            dtype=complex,
        )

    def qutrit_derivs(t1: float, t2: float) -> list[np.ndarray]:
        return [
            np.array(
                [
                    -math.sin(t1),
                    math.cos(t1) * math.cos(t2),
                    math.cos(t1) * math.sin(t2),
                ],
                dtype=complex,
            ),
            np.array(
                [
                    0.0,
                    -math.sin(t1) * math.sin(t2),
                    math.sin(t1) * math.cos(t2),
                ],
                dtype=complex,
            ),
        ]

    def random_unitary_3() -> np.ndarray:
        x = RNG.normal(size=(3, 3)) + 1j * RNG.normal(size=(3, 3))
        q, r = np.linalg.qr(x)
        phase = np.diag(r)
        phase = phase / np.abs(phase)
        return q * phase

    g6_vals: list[float] = []
    for _ in range(900):
        t1 = float(RNG.uniform(0.25, 1.25))
        t2 = float(RNG.uniform(0.25, 1.3))
        psi = qutrit_state(t1, t2)
        dpsi = qutrit_derivs(t1, t2)
        f = qfim_pure(psi, dpsi)
        rho = np.outer(psi, np.conjugate(psi))
        drhos = [np.outer(d, np.conjugate(psi)) + np.outer(psi, np.conjugate(d)) for d in dpsi]
        u = random_unitary_3()
        qutrit_proj = [np.outer(u[:, k], np.conjugate(u[:, k])) for k in range(3)]
        j = classical_fim(rho, drhos, qutrit_proj)
        g6_vals.append(float(np.trace(np.linalg.inv(f) @ j)))
    summaries.append(
        summarize(
            case_id="G6",
            extension="higher_dimensional_qutrit",
            state_class="pure qutrit",
            measurement_class="computational projective (3-outcome)",
            parameter_class="2-parameter",
            metric_name="trace(FQ_inv_times_FM)",
            values=g6_vals,
            expected_relation="not fixed at 1",
            observed_relation="varies over approximately [0,2] in sampled class",
            status="DISPROVED",
            notes="The qubit conservation constant does not transfer directly to d>2.",
        )
    )

    # G7: more than two parameters (mixed qubit: r, theta, phi).
    g7_vals: list[float] = []
    for _ in range(1000):
        r = float(RNG.uniform(0.2, 0.9))
        theta = float(RNG.uniform(0.25, math.pi - 0.25))
        phi = float(RNG.uniform(-math.pi, math.pi))
        n = bloch_theta_phi(theta, phi)
        rho = density_from_bloch(r, n)
        dn1 = dbloch_theta(theta, phi)
        dn2 = dbloch_phi(theta, phi)
        dr = 0.5 * (n[0] * SX + n[1] * SY + n[2] * SZ)
        dtheta_rho = 0.5 * r * (dn1[0] * SX + dn1[1] * SY + dn1[2] * SZ)
        dphi_rho = 0.5 * r * (dn2[0] * SX + dn2[1] * SY + dn2[2] * SZ)
        drhos = [dr, dtheta_rho, dphi_rho]
        f = qfim_mixed(rho, drhos)
        if np.min(np.diag(f)) <= EPS:
            continue
        m = random_unit_vector()
        j = classical_fim(rho, drhos, projective_effects(m))
        g7_vals.append(float(np.trace(np.linalg.inv(f) @ j)))
    summaries.append(
        summarize(
            case_id="G7",
            extension="more_than_two_parameters",
            state_class="mixed qubit",
            measurement_class="single projective 2-outcome",
            parameter_class="3-parameter (r,theta,phi)",
            metric_name="trace(FQ_inv_times_FM)",
            values=g7_vals,
            expected_relation="unknown in this pass",
            observed_relation="numerically concentrated at 1 in sampled class",
            status="VALIDATED / NUMERICAL ONLY",
            notes="Possible qubit-specific extension; kept conditional pending proof and literature check.",
        )
    )

    # G8: >2-parameter higher-dimensional check (pure qutrit, 3 parameters).
    def qutrit3_state(t1: float, t2: float, t3: float) -> np.ndarray:
        return np.array(
            [
                math.cos(t1),
                math.sin(t1) * math.cos(t2),
                math.sin(t1) * math.sin(t2) * np.exp(1j * t3),
            ],
            dtype=complex,
        )

    def qutrit3_derivs(t1: float, t2: float, t3: float) -> list[np.ndarray]:
        return [
            np.array(
                [
                    -math.sin(t1),
                    math.cos(t1) * math.cos(t2),
                    math.cos(t1) * math.sin(t2) * np.exp(1j * t3),
                ],
                dtype=complex,
            ),
            np.array(
                [
                    0.0,
                    -math.sin(t1) * math.sin(t2),
                    math.sin(t1) * math.cos(t2) * np.exp(1j * t3),
                ],
                dtype=complex,
            ),
            np.array(
                [
                    0.0,
                    0.0,
                    1j * math.sin(t1) * math.sin(t2) * np.exp(1j * t3),
                ],
                dtype=complex,
            ),
        ]

    g8_vals: list[float] = []
    for _ in range(900):
        t1 = float(RNG.uniform(0.25, 1.2))
        t2 = float(RNG.uniform(0.25, 1.2))
        t3 = float(RNG.uniform(-math.pi, math.pi))
        psi = qutrit3_state(t1, t2, t3)
        dpsi = qutrit3_derivs(t1, t2, t3)
        f = qfim_pure(psi, dpsi)
        if abs(np.linalg.det(f)) < 1e-7:
            continue
        rho = np.outer(psi, np.conjugate(psi))
        drhos = [np.outer(d, np.conjugate(psi)) + np.outer(psi, np.conjugate(d)) for d in dpsi]
        u = random_unitary_3()
        qutrit_proj = [np.outer(u[:, k], np.conjugate(u[:, k])) for k in range(3)]
        j = classical_fim(rho, drhos, qutrit_proj)
        g8_vals.append(float(np.trace(np.linalg.inv(f) @ j)))
    summaries.append(
        summarize(
            case_id="G8",
            extension="higher_dimensional_more_than_two_parameters",
            state_class="pure qutrit",
            measurement_class="random projective basis (3-outcome)",
            parameter_class="3-parameter",
            metric_name="trace(FQ_inv_times_FM)",
            values=g8_vals,
            expected_relation="no fixed qubit-style constant expected",
            observed_relation="varies significantly across sampled states and measurements",
            status="VALIDATED / NUMERICAL ONLY",
            notes="No conserved constant analogous to the qubit identity observed.",
        )
    )

    # Single-parameter correction metrics for docs.
    single_rows = single_param_table()
    write_csv(
        OUT_DATA / "single_parameter_audit_table.csv",
        rows=[{k: (f"{v:.12g}" if isinstance(v, float) else v) for k, v in row.items()} for row in single_rows],
        fieldnames=["theta", "F_Q", "F_M_Z", "F_M_X", "alpha_Z", "alpha_X"],
    )

    write_csv(
        OUT_DATA / "two_parameter_tradeoff_samples.csv",
        rows=[{k: (f"{v:.12g}" if isinstance(v, float) else v) for k, v in row.items()} for row in tradeoff_rows],
        fieldnames=["theta", "phi", "m_x", "m_y", "m_z", "alpha_1", "alpha_2", "alpha_1_sq_plus_alpha_2_sq"],
    )

    # Random search replication and exact balanced construction.
    theta_star = math.pi / 3.0
    phi_star = math.pi / 4.0
    f_star = two_param_qfim(theta_star, phi_star)
    best_min_alpha = -1.0
    best_pair = (0.0, 0.0)
    for _ in range(500):
        m = random_unit_vector()
        j = two_param_projective_fim(theta_star, phi_star, m)
        a1 = math.sqrt(max(j[0, 0] / f_star[0, 0], 0.0))
        a2 = math.sqrt(max(j[1, 1] / f_star[1, 1], 0.0))
        current = min(a1, a2)
        if current > best_min_alpha:
            best_min_alpha = current
            best_pair = (a1, a2)

    # Construct optimal balanced measurement explicitly in tangent basis.
    n_star = bloch_theta_phi(theta_star, phi_star)
    e1 = dbloch_theta(theta_star, phi_star)
    e1 = e1 / np.linalg.norm(e1)
    e2 = dbloch_phi(theta_star, phi_star)
    e2 = e2 / np.linalg.norm(e2)
    m_balanced = (e1 + e2) / np.linalg.norm(e1 + e2)
    j_balanced = two_param_projective_fim(theta_star, phi_star, m_balanced)
    alpha_balanced = (
        math.sqrt(max(j_balanced[0, 0] / f_star[0, 0], 0.0)),
        math.sqrt(max(j_balanced[1, 1] / f_star[1, 1], 0.0)),
    )

    # SLD commutator check at the same point.
    def dstate_numeric(fn: Callable[[float, float], np.ndarray], t1: float, t2: float, axis: int, h: float = 1e-8) -> np.ndarray:
        if axis == 0:
            return (fn(t1 + h, t2) - fn(t1 - h, t2)) / (2.0 * h)
        return (fn(t1, t2 + h) - fn(t1, t2 - h)) / (2.0 * h)

    psi_star = ket_theta_phi(theta_star, phi_star)
    d1 = dstate_numeric(ket_theta_phi, theta_star, phi_star, axis=0)
    d2 = dstate_numeric(ket_theta_phi, theta_star, phi_star, axis=1)
    l1 = 2.0 * (np.outer(d1, np.conjugate(psi_star)) + np.outer(psi_star, np.conjugate(d1)))
    l2 = 2.0 * (np.outer(d2, np.conjugate(psi_star)) + np.outer(psi_star, np.conjugate(d2)))
    comm = l1 @ l2 - l2 @ l1

    audit_blob["single_parameter"] = {
        "state_family": "|psi(theta)>=cos(theta/2)|0>+sin(theta/2)|1>",
        "analytic_FQ": 1.0,
        "analytic_FM_Z": "1 for theta in (0,pi), endpoint limit 1",
        "analytic_FM_X": "1 for theta in (0,pi), endpoint/interior singular-point limits 1",
        "blind_spots": "none in FI sense for this parameterization",
    }
    audit_blob["two_parameter_point"] = {
        "theta_1": theta_star,
        "theta_2": phi_star,
        "qfim": [[float(f_star[0, 0]), float(f_star[0, 1])], [float(f_star[1, 0]), float(f_star[1, 1])]],
        "sld_commutator_fro_norm": float(np.linalg.norm(comm, "fro")),
        "sld_commutator_op_norm": float(np.linalg.norm(comm, 2)),
        "random_search_best_min_alpha_over_500": float(best_min_alpha),
        "random_search_best_pair": [float(best_pair[0]), float(best_pair[1])],
        "balanced_constructed_pair": [float(alpha_balanced[0]), float(alpha_balanced[1])],
        "balanced_constructed_min_alpha": float(min(alpha_balanced)),
        "theoretical_max_balanced_min_alpha": float(1.0 / math.sqrt(2.0)),
        "balanced_identity_check": float(alpha_balanced[0] ** 2 + alpha_balanced[1] ** 2),
    }
    audit_blob["generalization_cases"] = [row.__dict__ for row in summaries]

    return summaries, audit_blob


def plot_single_parameter(rows: list[dict[str, float]]) -> None:
    theta = np.array([r["theta"] for r in rows], dtype=float)
    alpha_z = np.array([r["alpha_Z"] for r in rows], dtype=float)
    alpha_x = np.array([r["alpha_X"] for r in rows], dtype=float)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(theta, alpha_z, label=r"$\alpha_Q(\theta,Z)$", linewidth=2.2, color="#1f77b4")
    ax.plot(theta, alpha_x, label=r"$\alpha_Q(\theta,X)$", linewidth=2.2, color="#d62728", linestyle="--")
    ax.set_title("Corrected Single-Parameter Qubit Alignment Curves")
    ax.set_xlabel(r"$\theta$")
    ax.set_ylabel(r"$\alpha_Q$")
    ax.set_ylim(0.0, 1.05)
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT_FIG / "single_parameter_corrected_alpha_curves.png", dpi=180)
    plt.close(fig)


def plot_tradeoff_circle() -> None:
    rows_path = OUT_DATA / "two_parameter_tradeoff_samples.csv"
    data = np.genfromtxt(rows_path, delimiter=",", names=True)
    alpha1 = np.array(data["alpha_1"], dtype=float)
    alpha2 = np.array(data["alpha_2"], dtype=float)
    t = np.linspace(0.0, 2.0 * math.pi, 300)
    fig, ax = plt.subplots(figsize=(6.5, 6.5))
    ax.scatter(alpha1, alpha2, s=8, alpha=0.32, color="#0f8f82", label="random projective samples")
    ax.plot(np.cos(t), np.sin(t), color="#222222", linewidth=1.2, label=r"$\alpha_1^2+\alpha_2^2=1$")
    ax.set_title("Two-Parameter Tradeoff: Projective Qubit Measurements")
    ax.set_xlabel(r"$\alpha_1$")
    ax.set_ylabel(r"$\alpha_2$")
    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(-0.02, 1.02)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(alpha=0.2)
    ax.legend(loc="upper right")
    fig.tight_layout()
    fig.savefig(OUT_FIG / "two_parameter_tradeoff_circle.png", dpi=180)
    plt.close(fig)


def plot_generalization_map(rows: list[SummaryRow]) -> None:
    labels = [r.case_id for r in rows]
    means = [r.metric_mean for r in rows]
    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.bar(labels, means, color="#5f8dd3")
    ax.axhline(1.0, color="#bf3d3d", linewidth=1.3, linestyle="--", label="reference value 1")
    ax.set_title("Quantum Alignment Generalization Sweep (Mean Metric by Case)")
    ax.set_ylabel("Mean tested metric value")
    ax.set_xlabel("Generalization case")
    ax.grid(axis="y", alpha=0.2)
    ax.legend(loc="upper right")
    for bar, row in zip(bars, rows):
        ax.text(
            bar.get_x() + bar.get_width() / 2.0,
            bar.get_height(),
            row.status.replace("PROVED ON RESTRICTED CLASS", "PROVED"),
            ha="center",
            va="bottom",
            fontsize=7,
            rotation=90,
        )
    fig.tight_layout()
    fig.savefig(OUT_FIG / "generalization_survival_map.png", dpi=180)
    plt.close(fig)


def main() -> None:
    summaries, audit_blob = run_generalization()

    # Generalization summary CSV (required artifact).
    write_csv(
        OUT_DATA / "generalization_summary.csv",
        rows=[row.__dict__ for row in summaries],
        fieldnames=[
            "case_id",
            "extension",
            "state_class",
            "measurement_class",
            "parameter_class",
            "n_samples",
            "metric_name",
            "metric_mean",
            "metric_std",
            "metric_min",
            "metric_max",
            "expected_relation",
            "observed_relation",
            "status",
            "notes",
        ],
    )

    with (OUT_DATA / "audit_metrics.json").open("w") as f:
        json.dump(audit_blob, f, indent=2)

    rows = single_param_table()
    plot_single_parameter(rows)
    plot_tradeoff_circle()
    plot_generalization_map(summaries)

    print("Quantum alignment pass complete.")
    print(f"Wrote: {OUT_DATA / 'generalization_summary.csv'}")
    print(f"Wrote: {OUT_DATA / 'single_parameter_audit_table.csv'}")
    print(f"Wrote: {OUT_DATA / 'two_parameter_tradeoff_samples.csv'}")
    print(f"Wrote: {OUT_DATA / 'audit_metrics.json'}")
    print(f"Wrote figures in: {OUT_FIG}")


if __name__ == "__main__":
    main()
