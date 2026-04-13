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
from ocp.continuous import LinearOCPFlow
from ocp.capacity import exact_linear_capacity, generator_capacity, qec_sector_capacity
from ocp.physics import bounded_domain_projection_counterexample
from ocp.sectors import global_sector_recovery_operator, sector_recovery_report

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

protected_sector_basis = np.column_stack(codewords)
qec_sector_bases = [np.column_stack([error @ v for v in codewords]) for error in errors]
sector_recovery = global_sector_recovery_operator(protected_sector_basis, qec_sector_bases)
sector_report = sector_recovery_report(protected_sector_basis, qec_sector_bases)
qec_report = {
    'holds': kl.holds,
    'max_residual': kl.max_residual,
    'pairwise_image_overlap': kl.pairwise_image_overlap,
    'sector_recovery_errors': recovery_errors,
    'sector_theorem': {
        'pairwise_orthogonal': sector_report.pairwise_orthogonal,
        'max_pairwise_overlap': sector_report.max_pairwise_overlap,
        'exact_recovery_errors': sector_report.exact_recovery_errors,
        'recovery_operator_fro_norm': float(np.linalg.norm(sector_recovery)),
    },
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

boundary_report = bounded_domain_projection_counterexample(32)


block_generator = np.array([
    [0.0, 0.0, 0.0],
    [0.0, 1.0, 1.0],
    [0.0, 0.0, 1.5],
])
ps_basis = np.array([[1.0], [0.0], [0.0]])
pd_basis = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]])
block_flow = LinearOCPFlow(block_generator, ps_basis, pd_basis)
block_x0 = np.array([2.0, -1.0, 0.5])
block_xt = block_flow.flow(block_x0, 2.0)

psd_generator = np.diag([0.0, 0.75, 2.0])
psd_flow = LinearOCPFlow(psd_generator, ps_basis, pd_basis)
psd_x0 = np.array([3.0, -4.0, 1.0])
psd_xt = psd_flow.flow(psd_x0, 1.5)

mix_generator = np.array([
    [0.0, 1.0],
    [0.0, 1.0],
])
mix_flow = LinearOCPFlow(mix_generator, np.array([[1.0], [0.0]]), np.array([[0.0], [1.0]]))
mix_x0 = np.array([0.0, 1.0])
mix_xt = mix_flow.flow(mix_x0, 0.5)


capacity_report = {
    'exact_linear': exact_linear_capacity(system.protected_basis, system.disturbance_basis).__dict__,
    'qec': qec_sector_capacity(codewords, errors).__dict__,
    'generator_invariant_split': generator_capacity(block_generator, ps_basis, pd_basis).__dict__,
    'generator_mixing_failure': generator_capacity(mix_generator, np.array([[1.0], [0.0]]), np.array([[0.0], [1.0]])).__dict__,
}

generator_report = {
    'invariant_split_example': {
        'report': {
            'annihilates_protected': bool(block_flow.report().annihilates_protected),
            'preserves_disturbance': bool(block_flow.report().preserves_disturbance),
            'protected_mixing_norm': float(block_flow.report().protected_mixing_norm),
            'disturbance_from_protected_norm': float(block_flow.report().disturbance_from_protected_norm),
            'disturbance_decay_margin': float(block_flow.report().disturbance_decay_margin),
        },
        'x0': block_x0.tolist(),
        'xt_t2': np.asarray(block_xt).tolist(),
        'protected_preserved': bool(block_flow.preserves_protected_component(block_x0, 2.0)),
        'disturbance_norm_before': block_flow.disturbance_norm(block_x0),
        'disturbance_norm_after': block_flow.disturbance_norm(block_xt),
    },
    'self_adjoint_psd_example': {
        'report': {
            'annihilates_protected': bool(psd_flow.report().annihilates_protected),
            'preserves_disturbance': bool(psd_flow.report().preserves_disturbance),
            'protected_mixing_norm': float(psd_flow.report().protected_mixing_norm),
            'disturbance_from_protected_norm': float(psd_flow.report().disturbance_from_protected_norm),
            'disturbance_decay_margin': float(psd_flow.report().disturbance_decay_margin),
        },
        'x0': psd_x0.tolist(),
        'xt_t1_5': np.asarray(psd_xt).tolist(),
        'disturbance_norm_after': psd_flow.disturbance_norm(psd_xt),
        'spectral_bound_t1_5': psd_flow.asymptotic_bound(psd_x0, 1.5),
    },
    'mixing_failure_example': {
        'report': {
            'annihilates_protected': bool(mix_flow.report().annihilates_protected),
            'preserves_disturbance': bool(mix_flow.report().preserves_disturbance),
            'protected_mixing_norm': float(mix_flow.report().protected_mixing_norm),
            'disturbance_from_protected_norm': float(mix_flow.report().disturbance_from_protected_norm),
            'disturbance_decay_margin': float(mix_flow.report().disturbance_decay_margin),
        },
        'x0': mix_x0.tolist(),
        'xt_t0_5': np.asarray(mix_xt).tolist(),
        'protected_preserved': bool(mix_flow.preserves_protected_component(mix_x0, 0.5)),
    },
    'finite_time_exact_recovery_no_go': {
        'times': [0.25, 1.0, 2.0],
        'exact_recovery_possible': [
            bool(block_flow.finite_time_exact_recovery_possible(0.25)),
            bool(block_flow.finite_time_exact_recovery_possible(1.0)),
            bool(block_flow.finite_time_exact_recovery_possible(2.0)),
        ],
        'exact_recovery_residuals': [
            float(block_flow.exact_recovery_residual(0.25)),
            float(block_flow.exact_recovery_residual(1.0)),
            float(block_flow.exact_recovery_residual(2.0)),
        ],
    },
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps({
    'finite_ocp': finite_report,
    'qec': qec_report,
    'mhd': mhd_report,
    'bounded_domain_projection_limit': boundary_report.__dict__,
    'continuous_generators': generator_report,
    'capacity': capacity_report,
}, indent=2))
print(f'wrote {OUT}')
