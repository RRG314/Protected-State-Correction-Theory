from __future__ import annotations

import numpy as np
import pytest

from ocp.qec import bitflip_three_qubit_code
from ocp.sectors import (
    global_sector_recovery_operator,
    pairwise_sector_overlap_matrix,
    sector_recovery_report,
)


def _bitflip_sector_bases() -> tuple[np.ndarray, list[np.ndarray]]:
    codewords, errors = bitflip_three_qubit_code()
    protected_basis = np.column_stack(codewords)
    sector_bases = [np.column_stack([error @ v for v in codewords]) for error in errors]
    return protected_basis, sector_bases


def test_global_sector_recovery_recovers_each_orthogonal_qec_sector_exactly() -> None:
    protected_basis, sector_bases = _bitflip_sector_bases()
    recovery = global_sector_recovery_operator(protected_basis, sector_bases)
    coeffs = np.array([1.0, -2.0], dtype=complex)
    coeffs = coeffs / np.linalg.norm(coeffs)
    target = protected_basis @ coeffs

    for sector_basis in sector_bases:
        disturbed = sector_basis @ coeffs
        recovered = recovery @ disturbed
        assert np.allclose(recovered, target)


def test_sector_recovery_report_confirms_pairwise_orthogonality_and_exactness() -> None:
    protected_basis, sector_bases = _bitflip_sector_bases()
    report = sector_recovery_report(protected_basis, sector_bases)
    assert report.pairwise_orthogonal
    assert report.max_pairwise_overlap < 1e-9
    assert max(report.exact_recovery_errors) < 1e-9


def test_overlapping_sectors_do_not_admit_single_exact_sector_recovery_operator() -> None:
    protected_basis = np.array([[1.0], [0.0], [0.0]])
    sector_1 = np.array([[0.0], [1.0], [0.0]])
    sector_2 = np.array([[0.0], [1.0], [1.0]])
    overlaps = pairwise_sector_overlap_matrix([sector_1, sector_2])
    assert overlaps[0, 1] > 0.7
    with pytest.raises(ValueError):
        global_sector_recovery_operator(protected_basis, [sector_1, sector_2])


def test_random_pairwise_orthogonal_sector_families_recover_exactly() -> None:
    rng = np.random.default_rng(29)
    ambient_dim = 12
    protected_dim = 2
    sector_count = 4
    for _ in range(4):
        q, _ = np.linalg.qr(rng.normal(size=(ambient_dim, ambient_dim)))
        protected_basis = q[:, :protected_dim]
        sector_bases = [
            q[:, protected_dim * (index + 1):protected_dim * (index + 2)]
            for index in range(sector_count)
        ]
        overlaps = pairwise_sector_overlap_matrix(sector_bases)
        off_diag = overlaps[~np.eye(overlaps.shape[0], dtype=bool)]
        assert np.max(off_diag) < 1e-10

        recovery = global_sector_recovery_operator(protected_basis, sector_bases)
        report = sector_recovery_report(protected_basis, sector_bases)
        assert report.pairwise_orthogonal
        assert max(report.exact_recovery_errors) < 1e-9

        for _ in range(3):
            coeffs = rng.normal(size=protected_dim)
            coeffs = coeffs / np.linalg.norm(coeffs)
            target = protected_basis @ coeffs
            for sector_basis in sector_bases:
                disturbed = sector_basis @ coeffs
                recovered = recovery @ disturbed
                assert np.allclose(recovered, target, atol=1e-9)
