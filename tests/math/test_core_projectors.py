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
