#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import numpy as np

from ocp.core import FiniteOCPSystem
from ocp.qec import (
    bitflip_three_qubit_code,
    bitflip_three_qubit_recovery_operators,
    coherent_recovery_map,
    knill_laflamme_report,
)
from ocp.mhd import divergence_2d, helmholtz_project_2d, glm_step_2d, orthogonality_residual_2d

ROOT = Path('/Users/stevenreid/Documents/New project/repos/ocp-research-program')
OUT = ROOT / 'data/generated/validations/operator_examples.json'

system = FiniteOCPSystem(
    protected_basis=np.array([[1.0], [0.0], [0.0]]),
    disturbance_basis=np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]]),
)
x0 = np.array([2.0, -1.5, 0.75])

finite_report = {
    'x0': x0.tolist(),
    'exact_recovery': system.exact_recover(x0).tolist(),
    'continuous_correction_t2': system.continuous_correction(x0, rate=1.0, time=2.0).tolist(),
    'initial_disturbance_energy': system.correction_energy(x0),
    'corrected_disturbance_energy': system.correction_energy(system.continuous_correction(x0, rate=1.0, time=2.0)),
}

codewords, errors = bitflip_three_qubit_code()
kl = knill_laflamme_report(codewords, errors)
logical_state = (codewords[0] + codewords[1]) / np.sqrt(2.0)
_, _, recovery_ops = bitflip_three_qubit_recovery_operators()
recovery_errors = []
for idx, error in enumerate(errors):
    recovered = coherent_recovery_map(error @ logical_state, recovery_ops)
    recovery_errors.append(float(np.linalg.norm(recovered - logical_state)))
qec_report = {
    'holds': kl.holds,
    'max_residual': kl.max_residual,
    'pairwise_image_overlap': kl.pairwise_image_overlap,
    'sector_recovery_errors': recovery_errors,
}

nx = ny = 48
dx = dy = 1.0 / nx
x = np.linspace(0.0, 1.0, nx, endpoint=False)
y = np.linspace(0.0, 1.0, ny, endpoint=False)
X, Y = np.meshgrid(x, y, indexing='ij')
psi = np.sin(2.0 * np.pi * X) * np.sin(2.0 * np.pi * Y)
phi = 0.2 * np.cos(4.0 * np.pi * X) * np.cos(2.0 * np.pi * Y)
dpsix = (np.roll(psi, -1, axis=0) - np.roll(psi, 1, axis=0)) / (2.0 * dx)
dpsiy = (np.roll(psi, -1, axis=1) - np.roll(psi, 1, axis=1)) / (2.0 * dy)
Bx_phys = dpsiy
By_phys = -dpsix
gradx = (np.roll(phi, -1, axis=0) - np.roll(phi, 1, axis=0)) / (2.0 * dx)
grady = (np.roll(phi, -1, axis=1) - np.roll(phi, 1, axis=1)) / (2.0 * dy)
Bx = Bx_phys + gradx
By = By_phys + grady
before = float(np.sqrt(np.mean(divergence_2d(Bx, By, dx, dy) ** 2)))
Bx_proj, By_proj, _, _ = helmholtz_project_2d(Bx, By, dx, dy)
after = float(np.sqrt(np.mean(divergence_2d(Bx_proj, By_proj, dx, dy) ** 2)))
psi_glm = np.zeros_like(Bx)
Bx_glm, By_glm = Bx.copy(), By.copy()
for _ in range(8):
    Bx_glm, By_glm, psi_glm = glm_step_2d(Bx_glm, By_glm, psi_glm, dx, dy, dt=0.05, ch=1.0, cp=1.0)
after_glm = float(np.sqrt(np.mean(divergence_2d(Bx_glm, By_glm, dx, dy) ** 2)))

mhd_report = {
    'before_l2_divergence': before,
    'after_projection_l2_divergence': after,
    'after_glm_l2_divergence': after_glm,
    'projection_orthogonality_residual': orthogonality_residual_2d(Bx, By, dx, dy),
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps({'finite_ocp': finite_report, 'qec': qec_report, 'mhd': mhd_report}, indent=2))
print(f'wrote {OUT}')
