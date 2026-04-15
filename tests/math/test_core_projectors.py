from __future__ import annotations

import numpy as np
import pytest

from ocp.core import FiniteOCPSystem, exact_projection_recovery


def test_exact_projection_recovery_recovers_protected_component() -> None:
    system = FiniteOCPSystem(
        protected_basis=np.array([[1.0], [0.0], [0.0]]),
        disturbance_basis=np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]]),
    )
    x = np.array([2.0, -3.0, 4.0])
    recovered = system.exact_recover(x)
    assert np.allclose(recovered, np.array([2.0, 0.0, 0.0]))
    assert np.allclose(exact_projection_recovery(x, system.protected_basis), recovered)


def test_continuous_correction_exponentially_damps_disturbance() -> None:
    system = FiniteOCPSystem(
        protected_basis=np.array([[1.0], [0.0]]),
        disturbance_basis=np.array([[0.0], [1.0]]),
    )
    x0 = np.array([3.0, 5.0])
    xt = system.continuous_correction(x0, rate=2.0, time=1.5)
    assert np.isclose(xt[0], 3.0)
    assert np.isclose(xt[1], 5.0 * np.exp(-3.0))
    assert system.correction_energy(xt) < system.correction_energy(x0)


def test_overlapping_subspaces_raise_value_error() -> None:
    with pytest.raises(ValueError):
        FiniteOCPSystem(
            protected_basis=np.array([[1.0], [0.0]]),
            disturbance_basis=np.array([[1.0], [1.0]]),
        )


def test_random_orthogonal_splits_recover_exactly_across_multiple_instances() -> None:
    rng = np.random.default_rng(7)
    for _ in range(8):
        q, _ = np.linalg.qr(rng.normal(size=(4, 4)))
        protected = q[:, :2]
        disturbance = q[:, 2:]
        system = FiniteOCPSystem(protected_basis=protected, disturbance_basis=disturbance)
        x = rng.normal(size=4)
        s, _ = system.decompose(x)
        recovered = system.exact_recover(x)
        assert np.allclose(recovered, s)


def test_decomposition_is_orthogonal_and_exact_across_multiple_dimensions() -> None:
    rng = np.random.default_rng(19)
    for ambient_dim, protected_dim in ((5, 1), (5, 2), (6, 3), (8, 2)):
        for _ in range(5):
            q, _ = np.linalg.qr(rng.normal(size=(ambient_dim, ambient_dim)))
            protected = q[:, :protected_dim]
            disturbance = q[:, protected_dim:]
            system = FiniteOCPSystem(protected_basis=protected, disturbance_basis=disturbance)
            x = rng.normal(size=ambient_dim)
            s, d = system.decompose(x)
            recovered = system.exact_recover(x)
            assert np.allclose(s + d, x)
            assert abs(float(np.vdot(s, d))) < 1e-10
            assert np.allclose(recovered, s)
            assert np.allclose(system.exact_recover(s), s)
            assert np.allclose(system.exact_recover(d), np.zeros_like(d))


def test_continuous_correction_energy_is_monotone_over_time_grid() -> None:
    system = FiniteOCPSystem(
        protected_basis=np.array([[1.0], [0.0], [0.0], [0.0]]),
        disturbance_basis=np.array(
            [
                [0.0, 0.0, 0.0],
                [1.0, 0.0, 0.0],
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 1.0],
            ]
        ),
    )
    x0 = np.array([1.25, -2.0, 0.5, 3.0])
    expected_protected = system.exact_recover(x0)
    times = np.linspace(0.0, 2.5, 7)
    energies = []
    for time in times:
        xt = system.continuous_correction(x0, rate=1.6, time=float(time))
        energies.append(system.correction_energy(xt))
        assert np.allclose(system.exact_recover(xt), expected_protected)
    assert all(left >= right - 1e-12 for left, right in zip(energies, energies[1:]))
