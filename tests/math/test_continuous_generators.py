from __future__ import annotations

import numpy as np

from ocp.continuous import LinearOCPFlow


PROTECTED_BASIS_1D = np.array([[1.0], [0.0], [0.0]])
DISTURBANCE_BASIS_2D = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]])


def test_block_stable_generator_preserves_protected_component_and_decays_disturbance() -> None:
    generator = np.array(
        [
            [0.0, 0.0, 0.0],
            [0.0, 1.0, 1.0],
            [0.0, 0.0, 1.5],
        ]
    )
    flow = LinearOCPFlow(generator, PROTECTED_BASIS_1D, DISTURBANCE_BASIS_2D)
    report = flow.report()

    assert report.annihilates_protected
    assert report.preserves_disturbance
    assert report.disturbance_decay_margin > 0.99

    x0 = np.array([2.0, -1.0, 0.5])
    xt = flow.flow(x0, 2.0)
    assert np.isclose(xt[0], 2.0)
    assert flow.disturbance_norm(xt) < flow.disturbance_norm(x0)
    assert flow.preserves_protected_component(x0, 2.0)


def test_self_adjoint_psd_generator_satisfies_spectral_gap_bound() -> None:
    generator = np.diag([0.0, 0.75, 2.0])
    flow = LinearOCPFlow(generator, PROTECTED_BASIS_1D, DISTURBANCE_BASIS_2D)
    report = flow.report()

    assert report.annihilates_protected
    assert report.preserves_disturbance
    assert np.isclose(report.disturbance_decay_margin, 0.75)

    x0 = np.array([3.0, -4.0, 1.0])
    xt = flow.flow(x0, 1.5)
    assert np.isclose(xt[0], 3.0)
    assert flow.disturbance_norm(xt) <= flow.asymptotic_bound(x0, 1.5) + 1e-10


def test_mixing_generator_fails_protected_component_preservation() -> None:
    generator = np.array(
        [
            [0.0, 1.0],
            [0.0, 1.0],
        ]
    )
    protected_basis = np.array([[1.0], [0.0]])
    disturbance_basis = np.array([[0.0], [1.0]])
    flow = LinearOCPFlow(generator, protected_basis, disturbance_basis)
    report = flow.report()

    assert report.protected_mixing_norm > 0.9
    x0 = np.array([0.0, 1.0])
    xt = flow.flow(x0, 0.5)
    assert not np.isclose(xt[0], 0.0)
    assert not flow.preserves_protected_component(x0, 0.5)


def test_multiple_diagonal_psd_generators_contract_disturbance() -> None:
    rng = np.random.default_rng(11)
    for _ in range(6):
        lam2 = float(rng.uniform(0.2, 1.0))
        lam3 = float(rng.uniform(1.0, 2.5))
        generator = np.diag([0.0, lam2, lam3])
        flow = LinearOCPFlow(generator, PROTECTED_BASIS_1D, DISTURBANCE_BASIS_2D)
        x0 = np.array([1.5, rng.normal(), rng.normal()])
        xt = flow.flow(x0, 1.2)
        assert np.isclose(xt[0], x0[0])
        assert flow.disturbance_norm(xt) <= flow.disturbance_norm(x0)
