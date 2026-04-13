from __future__ import annotations

import numpy as np

from ocp.qec import (
    bitflip_three_qubit_code,
    bitflip_three_qubit_recovery_operators,
    code_projector,
    coherent_recovery_map,
    knill_laflamme_report,
)


def test_three_qubit_bitflip_code_satisfies_knill_laflamme() -> None:
    codewords, errors = bitflip_three_qubit_code()
    report = knill_laflamme_report(codewords, errors)
    assert report.holds
    assert report.max_residual < 1e-9
    assert report.pairwise_image_overlap < 1e-9


def test_three_qubit_recovery_operators_recover_each_single_bitflip_sector() -> None:
    codewords, _, recovery_operators = bitflip_three_qubit_recovery_operators()
    _, errors = bitflip_three_qubit_code()
    logical_state = (codewords[0] + codewords[1]) / np.sqrt(2.0)

    for error in errors:
        disturbed = error @ logical_state
        recovered = coherent_recovery_map(disturbed, recovery_operators)
        assert np.allclose(recovered, logical_state)


def test_qec_error_sectors_are_pairwise_orthogonal() -> None:
    codewords, sector_projectors, _ = bitflip_three_qubit_recovery_operators()
    code_proj = code_projector(codewords)
    assert np.allclose(code_proj @ sector_projectors[1], 0.0)
    for i, proj_i in enumerate(sector_projectors):
        for j, proj_j in enumerate(sector_projectors):
            if i == j:
                continue
            assert np.allclose(proj_i @ proj_j, 0.0)
