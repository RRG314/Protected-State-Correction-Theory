from __future__ import annotations

import numpy as np

from ocp.capacity import exact_linear_capacity, generator_capacity, qec_sector_capacity
from ocp.qec import bitflip_three_qubit_code


def test_exact_linear_capacity_recovers_dimension_lower_bounds() -> None:
    protected = np.array([[1.0], [0.0], [0.0]])
    disturbance = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]])
    capacity = exact_linear_capacity(protected, disturbance)

    assert capacity.exact_recovery_possible
    assert capacity.protected_dim == 1
    assert capacity.disturbance_dim == 2
    assert capacity.min_recovery_rank == 1
    assert capacity.min_correction_rank == 2


def test_exact_linear_capacity_detects_overlap_impossibility() -> None:
    protected = np.array([[1.0], [0.0]])
    disturbance = np.array([[1.0], [0.0]])
    capacity = exact_linear_capacity(protected, disturbance)

    assert not capacity.exact_recovery_possible
    assert capacity.intersection_dim >= 1
    assert capacity.min_recovery_rank is None
    assert capacity.min_correction_rank is None


def test_qec_sector_capacity_counts_distinguishable_error_sectors() -> None:
    codewords, errors = bitflip_three_qubit_code()
    capacity = qec_sector_capacity(codewords, errors)

    assert capacity.sector_count == 4
    assert capacity.pairwise_orthogonal
    assert capacity.minimum_syndrome_outcomes == 4


def test_generator_capacity_identifies_stable_disturbance_block() -> None:
    generator = np.diag([0.0, 0.75, 2.0])
    protected = np.array([[1.0], [0.0], [0.0]])
    disturbance = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]])
    capacity = generator_capacity(generator, protected, disturbance)

    assert capacity.split_preserving
    assert capacity.stable_disturbance_dim == 2
    assert capacity.neutral_disturbance_dim == 0
    assert capacity.unstable_disturbance_dim == 0


def test_generator_capacity_detects_mixing_failure() -> None:
    generator = np.array([[0.0, 1.0], [0.0, 1.0]])
    protected = np.array([[1.0], [0.0]])
    disturbance = np.array([[0.0], [1.0]])
    capacity = generator_capacity(generator, protected, disturbance)

    assert not capacity.split_preserving
    assert capacity.protected_mixing_norm > 0.9
