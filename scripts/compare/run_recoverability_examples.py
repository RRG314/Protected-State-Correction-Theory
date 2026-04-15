#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Iterable

import numpy as np

from ocp.recoverability import (
    analytic_collapse_modulus,
    analytic_noise_lower_bound_sweep,
    control_minimal_complexity_sweep,
    diagonal_polynomial_threshold_sweep,
    diagonal_functional_complexity_sweep,
    functional_observability_sweep,
    nested_linear_threshold_profile,
    periodic_cutoff_recoverability_sweep,
    periodic_threshold_stress_sweep,
    periodic_functional_complexity_sweep,
    periodic_protected_complexity_sweep,
    periodic_velocity_recoverability_sweep,
    qubit_record_collapse_sweep,
)

ROOT = Path('/Users/stevenreid/Documents/New project/repos/ocp-research-program')
DATA_OUT = ROOT / 'data/generated/recoverability'
DOC_OUT = ROOT / 'docs/assets/recoverability'


COLORS = ['#8d5428', '#2a6f97', '#356c4a', '#a63229', '#6f4e7c']


def ensure_dirs() -> None:
    DATA_OUT.mkdir(parents=True, exist_ok=True)
    DOC_OUT.mkdir(parents=True, exist_ok=True)



def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        return
    with path.open('w', newline='') as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)



def line_svg(
    series: list[dict[str, object]],
    *,
    width: int = 760,
    height: int = 420,
    title: str,
    x_label: str,
    y_label: str,
) -> str:
    margin = {'left': 72, 'right': 24, 'top': 48, 'bottom': 64}
    xs = [x for item in series for x in item['x']]
    ys = [y for item in series for y in item['y']]
    x_min, x_max = min(xs), max(xs)
    y_min, y_max = min(ys), max(ys)
    if abs(x_max - x_min) < 1e-12:
        x_max = x_min + 1.0
    if abs(y_max - y_min) < 1e-12:
        y_max = y_min + 1.0
    plot_w = width - margin['left'] - margin['right']
    plot_h = height - margin['top'] - margin['bottom']

    def px(x: float) -> float:
        return margin['left'] + (x - x_min) * plot_w / (x_max - x_min)

    def py(y: float) -> float:
        return height - margin['bottom'] - (y - y_min) * plot_h / (y_max - y_min)

    y_ticks = np.linspace(y_min, y_max, 5)
    x_ticks = np.linspace(x_min, x_max, 5)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#fffdf8" rx="18"/>',
        f'<text x="{margin["left"]}" y="28" font-family="Source Sans 3, sans-serif" font-size="22" font-weight="700" fill="#1c1d21">{title}</text>',
    ]
    for tick in y_ticks:
        y = py(float(tick))
        parts.append(f'<line x1="{margin["left"]}" x2="{width - margin["right"]}" y1="{y:.2f}" y2="{y:.2f}" stroke="#e6ded2"/>')
        parts.append(f'<text x="{margin["left"] - 10}" y="{y + 4:.2f}" text-anchor="end" font-size="12" fill="#5c605d">{tick:.2f}</text>')
    for tick in x_ticks:
        x = px(float(tick))
        parts.append(f'<line x1="{x:.2f}" x2="{x:.2f}" y1="{margin["top"]}" y2="{height - margin["bottom"]}" stroke="#f0e7db"/>')
        parts.append(f'<text x="{x:.2f}" y="{height - margin["bottom"] + 24}" text-anchor="middle" font-size="12" fill="#5c605d">{tick:.2f}</text>')
    parts.append(f'<line x1="{margin["left"]}" x2="{margin["left"]}" y1="{margin["top"]}" y2="{height - margin["bottom"]}" stroke="#1c1d21"/>')
    parts.append(f'<line x1="{margin["left"]}" x2="{width - margin["right"]}" y1="{height - margin["bottom"]}" y2="{height - margin["bottom"]}" stroke="#1c1d21"/>')

    for index, item in enumerate(series):
        color = item.get('color', COLORS[index % len(COLORS)])
        coords = ' '.join(f'{px(float(x)):.2f},{py(float(y)):.2f}' for x, y in zip(item['x'], item['y']))
        parts.append(f'<polyline fill="none" stroke="{color}" stroke-width="3" points="{coords}"/>')
    legend_x = width - margin['right'] - 180
    legend_y = margin['top'] + 10
    for index, item in enumerate(series):
        color = item.get('color', COLORS[index % len(COLORS)])
        y = legend_y + 22 * index
        parts.append(f'<line x1="{legend_x}" x2="{legend_x + 20}" y1="{y}" y2="{y}" stroke="{color}" stroke-width="3"/>')
        parts.append(f'<text x="{legend_x + 28}" y="{y + 4}" font-size="12" fill="#1c1d21">{item["label"]}</text>')
    parts.append(f'<text x="{width / 2:.2f}" y="{height - 14}" text-anchor="middle" font-size="13" fill="#5c605d">{x_label}</text>')
    parts.append(f'<text x="20" y="{height / 2:.2f}" transform="rotate(-90 20 {height / 2:.2f})" text-anchor="middle" font-size="13" fill="#5c605d">{y_label}</text>')
    parts.append('</svg>')
    return ''.join(parts)



def bar_svg(rows: list[dict[str, object]], *, key: str, title: str, y_label: str) -> str:
    width, height = 760, 420
    margin = {'left': 72, 'right': 24, 'top': 48, 'bottom': 72}
    values = [float(row[key]) for row in rows]
    vmax = max(values) if values else 1.0
    vmax = max(vmax, 1e-6)
    plot_w = width - margin['left'] - margin['right']
    plot_h = height - margin['top'] - margin['bottom']
    bar_w = plot_w / max(len(rows), 1)

    def py(v: float) -> float:
        return height - margin['bottom'] - v * plot_h / vmax

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#fffdf8" rx="18"/>',
        f'<text x="{margin["left"]}" y="28" font-family="Source Sans 3, sans-serif" font-size="22" font-weight="700" fill="#1c1d21">{title}</text>',
        f'<line x1="{margin["left"]}" x2="{margin["left"]}" y1="{margin["top"]}" y2="{height - margin["bottom"]}" stroke="#1c1d21"/>',
        f'<line x1="{margin["left"]}" x2="{width - margin["right"]}" y1="{height - margin["bottom"]}" y2="{height - margin["bottom"]}" stroke="#1c1d21"/>',
    ]
    for idx, row in enumerate(rows):
        x = margin['left'] + idx * bar_w + bar_w * 0.18
        y = py(float(row[key]))
        h = height - margin['bottom'] - y
        color = COLORS[idx % len(COLORS)]
        label = row.get('observation') or row.get('protected_variable') or f'row {idx + 1}'
        parts.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{bar_w * 0.64:.2f}" height="{h:.2f}" fill="{color}" rx="8"/>')
        parts.append(f'<text x="{x + bar_w * 0.32:.2f}" y="{height - margin["bottom"] + 18}" text-anchor="middle" font-size="12" fill="#5c605d">{label}</text>')
        parts.append(f'<text x="{x + bar_w * 0.32:.2f}" y="{y - 6:.2f}" text-anchor="middle" font-size="12" fill="#1c1d21">{float(row[key]):.3f}</text>')
    parts.append(f'<text x="20" y="{height / 2:.2f}" transform="rotate(-90 20 {height / 2:.2f})" text-anchor="middle" font-size="13" fill="#5c605d">{y_label}</text>')
    parts.append('</svg>')
    return ''.join(parts)



def write_text(path: Path, text: str) -> None:
    path.write_text(text)
    print(f'wrote {path}')



def main() -> None:
    ensure_dirs()

    delta_grid = np.linspace(0.0, 1.0, 50)
    benchmark = {
        'rows': [analytic_collapse_modulus(epsilon, delta_grid).__dict__ for epsilon in (0.0, 0.1, 0.25, 0.5)],
        'delta_grid': list(float(x) for x in delta_grid),
    }
    qubit = qubit_record_collapse_sweep()
    periodic = periodic_velocity_recoverability_sweep()
    periodic_cutoff = periodic_cutoff_recoverability_sweep()
    periodic_protected = periodic_protected_complexity_sweep()
    periodic_functional = periodic_functional_complexity_sweep()
    periodic_stress = periodic_threshold_stress_sweep()
    functional = functional_observability_sweep()
    control_complexity = control_minimal_complexity_sweep()
    diagonal_functional = diagonal_functional_complexity_sweep()
    diagonal_polynomial = diagonal_polynomial_threshold_sweep()
    noise_lower_bound = analytic_noise_lower_bound_sweep(epsilon=0.25)
    nested_linear = nested_linear_threshold_profile(
        [
            np.zeros((1, 4), dtype=float),
            np.diag([1.0, 0.0, 0.0, 0.0]),
            np.diag([1.0, 1.0, 0.0, 0.0]),
            np.diag([1.0, 1.0, 1.0, 0.0]),
            np.diag([1.0, 1.0, 1.0, 1.0]),
        ],
        np.array([[1.0, -0.5, 0.75, 0.25]], dtype=float),
        box_radius=1.0,
        level_labels=[0, 1, 2, 3, 4],
    )

    summary = {
        'analytic_benchmark': benchmark,
        'analytic_noise_lower_bound': noise_lower_bound,
        'qubit_record_sweep': qubit,
        'periodic_velocity_sweep': periodic,
        'periodic_cutoff_sweep': periodic_cutoff,
        'periodic_protected_complexity_sweep': periodic_protected,
        'periodic_functional_complexity_sweep': periodic_functional,
        'periodic_threshold_stress_sweep': periodic_stress,
        'functional_observability_sweep': functional,
        'control_minimal_complexity_sweep': control_complexity,
        'diagonal_functional_complexity_sweep': diagonal_functional,
        'diagonal_polynomial_threshold_sweep': diagonal_polynomial,
        'nested_linear_threshold_profile': nested_linear,
    }
    write_text(DATA_OUT / 'recoverability_summary.json', json.dumps(summary, indent=2))

    write_csv(DATA_OUT / 'qubit_record_sweep.csv', qubit['rows'])
    write_csv(DATA_OUT / 'periodic_velocity_sweep.csv', periodic['rows'])
    write_csv(DATA_OUT / 'periodic_cutoff_sweep.csv', periodic_cutoff['rows'])
    write_csv(DATA_OUT / 'periodic_protected_complexity_sweep.csv', periodic_protected['rows'])
    write_csv(DATA_OUT / 'periodic_functional_complexity_sweep.csv', periodic_functional['rows'])
    write_csv(DATA_OUT / 'periodic_threshold_stress_sweep.csv', periodic_stress['rows'])
    write_csv(DATA_OUT / 'functional_observability_sweep.csv', functional['rows'])
    write_csv(DATA_OUT / 'control_minimal_complexity_sweep.csv', control_complexity['rows'])
    write_csv(DATA_OUT / 'diagonal_functional_complexity_sweep.csv', diagonal_functional['rows'])
    write_csv(DATA_OUT / 'diagonal_polynomial_threshold_sweep.csv', diagonal_polynomial['rows'])
    write_csv(DATA_OUT / 'analytic_collapse_benchmark.csv', benchmark['rows'])
    write_csv(DATA_OUT / 'analytic_noise_lower_bound.csv', noise_lower_bound['rows'])

    analytic_series = [
        {
            'label': f"ε = {row['epsilon']:.2f}",
            'x': benchmark['delta_grid'],
            'y': row['collapse_values'],
        }
        for row in benchmark['rows']
    ]
    write_text(
        DOC_OUT / 'analytic-collapse-benchmark.svg',
        line_svg(analytic_series, title='Collapse-modulus benchmark', x_label='δ', y_label='κ(δ)'),
    )

    qubit_rows = qubit['rows']
    bloch_rows = [row for row in qubit_rows if row['protected_variable'] == 'bloch_vector']
    z_rows = [row for row in qubit_rows if row['protected_variable'] == 'z_coordinate']
    write_text(
        DOC_OUT / 'qubit-phase-loss.svg',
        line_svg(
            [
                {
                    'label': 'full Bloch vector',
                    'x': [row['phase_window_deg'] for row in bloch_rows],
                    'y': [row['collision_max_protected_distance'] for row in bloch_rows],
                },
                {
                    'label': 'z coordinate only',
                    'x': [row['phase_window_deg'] for row in z_rows],
                    'y': [row['collision_max_protected_distance'] for row in z_rows],
                },
                {
                    'label': 'analytic Bloch prediction',
                    'x': qubit['phase_windows_deg'],
                    'y': qubit['analytic_boundary']['bloch_vector'],
                },
            ],
            title='Qubit fixed-basis phase-loss boundary',
            x_label='phase window (degrees)',
            y_label='κ(0)',
        ),
    )

    write_text(
        DOC_OUT / 'periodic-velocity-errors.svg',
        bar_svg(periodic['rows'], key='mean_recovery_error', title='Periodic velocity recovery error', y_label='mean RMS error'),
    )

    write_text(
        DOC_OUT / 'periodic-cutoff-threshold.svg',
        line_svg(
            [
                {
                    'label': 'κ(0)',
                    'x': [row['cutoff'] for row in periodic_cutoff['rows']],
                    'y': [row['collision_max_protected_distance'] for row in periodic_cutoff['rows']],
                },
                {
                    'label': 'mean recovery error',
                    'x': [row['cutoff'] for row in periodic_cutoff['rows']],
                    'y': [row['mean_recovery_error'] for row in periodic_cutoff['rows']],
                },
            ],
            title='Periodic Fourier cutoff threshold',
            x_label='spectral cutoff',
            y_label='recoverability loss',
        ),
    )

    protected_rows = periodic_protected['rows']
    protected_series = []
    for protected_name in ('mode_1_coefficient', 'modes_1_2_coefficients', 'full_modal_coefficients'):
        subset = [row for row in protected_rows if row['protected_variable'] == protected_name]
        protected_series.append(
            {
                'label': protected_name.replace('_', ' '),
                'x': [row['cutoff'] for row in subset],
                'y': [row['collision_max_protected_distance'] for row in subset],
            }
        )
    write_text(
        DOC_OUT / 'periodic-protected-threshold.svg',
        line_svg(
            protected_series,
            title='Periodic protected-variable cutoff thresholds',
            x_label='spectral cutoff',
            y_label='κ(0)',
        ),
    )

    functional_threshold_rows = periodic_functional['rows']
    functional_threshold_series = []
    for functional_name in ('low_mode_sum', 'bandlimited_contrast', 'full_weighted_sum'):
        subset = [row for row in functional_threshold_rows if row['functional_name'] == functional_name]
        functional_threshold_series.append(
            {
                'label': functional_name.replace('_', ' '),
                'x': [row['cutoff'] for row in subset],
                'y': [row['collision_max_protected_distance'] for row in subset],
            }
        )
    write_text(
        DOC_OUT / 'periodic-functional-threshold.svg',
        line_svg(
            functional_threshold_series,
            title='Periodic functional recoverability thresholds',
            x_label='spectral cutoff',
            y_label='κ(0)',
        ),
    )

    exact_rows = [row for row in functional['rows'] if row['horizon'] in (1, 2)]
    series = []
    for horizon in (1, 2):
        subset = [row for row in exact_rows if row['horizon'] == horizon]
        series.append({
            'label': f'horizon {horizon}',
            'x': [row['epsilon'] for row in subset],
            'y': [row['recoverability_margin'] for row in subset],
        })
    write_text(
        DOC_OUT / 'functional-observability-margin.svg',
        line_svg(series, title='Functional observability margin', x_label='ε', y_label='recoverability margin'),
    )

    observer = next(report for report in functional['observer_reports'] if abs(report['epsilon'] - 0.2) < 1e-12)
    write_text(
        DOC_OUT / 'observer-convergence.svg',
        line_svg(
            [
                {
                    'label': 'protected-variable observer error',
                    'x': list(range(len(observer['protected_error_history']))),
                    'y': observer['protected_error_history'],
                }
            ],
            title='Observer convergence for protected variable',
            x_label='step',
            y_label='|error in protected variable|',
        ),
    )

    eps_02_rows = [row for row in functional['rows'] if abs(row['epsilon'] - 0.2) < 1e-12]
    write_text(
        DOC_OUT / 'control-history-threshold.svg',
        line_svg(
            [
                {
                    'label': 'κ(0)',
                    'x': [row['horizon'] for row in eps_02_rows],
                    'y': [row['collision_max_protected_distance'] for row in eps_02_rows],
                },
                {
                    'label': 'recoverability margin',
                    'x': [row['horizon'] for row in eps_02_rows],
                    'y': [row['recoverability_margin'] for row in eps_02_rows],
                },
            ],
            title='Control-history threshold at ε = 0.2',
            x_label='record horizon',
            y_label='threshold metric',
        ),
    )

    complexity_rows = control_complexity['rows']
    complexity_series = []
    for sensor_profile in ('three_active', 'two_active', 'protected_hidden'):
        subset = [row for row in complexity_rows if row['sensor_profile'] == sensor_profile]
        complexity_series.append(
            {
                'label': sensor_profile.replace('_', ' '),
                'x': [row['horizon'] for row in subset],
                'y': [row['collision_max_protected_distance'] for row in subset],
            }
        )
    write_text(
        DOC_OUT / 'control-minimal-horizon.svg',
        line_svg(
            complexity_series,
            title='Diagonal control minimal-history thresholds',
            x_label='record horizon',
            y_label='κ(0)',
        ),
    )

    diagonal_functional_rows = diagonal_functional['rows']
    diagonal_functional_series = []
    for functional_name in ('sensor_sum', 'first_moment', 'second_moment', 'protected_coordinate'):
        subset = [
            row
            for row in diagonal_functional_rows
            if row['sensor_profile'] == 'three_active' and row['functional_name'] == functional_name
        ]
        diagonal_functional_series.append(
            {
                'label': functional_name.replace('_', ' '),
                'x': [row['horizon'] for row in subset],
                'y': [row['collision_max_protected_distance'] for row in subset],
            }
        )
    write_text(
        DOC_OUT / 'diagonal-functional-threshold.svg',
        line_svg(
            diagonal_functional_series,
            title='Diagonal functional recoverability thresholds',
            x_label='record horizon',
            y_label='κ(0)',
        ),
    )

    repeated_cutoff_rows = [
        row for row in periodic_stress['rows'] if row['case_name'] == 'repeated_cutoffs' and row['functional_name'] in ('repeated_cutoff_mass', 'mixed_tail')
    ]
    repeated_cutoff_series = []
    for functional_name in ('repeated_cutoff_mass', 'mixed_tail'):
        subset = [row for row in repeated_cutoff_rows if row['functional_name'] == functional_name]
        repeated_cutoff_series.append(
            {
                'label': functional_name.replace('_', ' '),
                'x': [row['cutoff'] for row in subset],
                'y': [row['collision_gap'] for row in subset],
            }
        )
    write_text(
        DOC_OUT / 'periodic-threshold-stress.svg',
        line_svg(
            repeated_cutoff_series,
            title='Periodic threshold stress test (repeated cutoffs)',
            x_label='spectral cutoff',
            y_label='box collision gap',
        ),
    )

    diagonal_polynomial_rows = [row for row in diagonal_polynomial['rows'] if row['case_name'] == 'four_active']
    diagonal_polynomial_series = []
    for functional_name in ('degree_0_constant', 'degree_1_affine', 'degree_2_quadratic', 'degree_3_cubic'):
        subset = [row for row in diagonal_polynomial_rows if row['functional_name'] == functional_name]
        diagonal_polynomial_series.append(
            {
                'label': functional_name.replace('_', ' '),
                'x': [row['horizon'] for row in subset],
                'y': [row['collision_gap'] for row in subset],
            }
        )
    write_text(
        DOC_OUT / 'diagonal-polynomial-threshold.svg',
        line_svg(
            diagonal_polynomial_series,
            title='Diagonal polynomial threshold stress test',
            x_label='record horizon',
            y_label='box collision gap',
        ),
    )

    write_text(
        DOC_OUT / 'nested-linear-threshold.svg',
        line_svg(
            [
                {
                    'label': 'box collision gap',
                    'x': nested_linear['level_labels'],
                    'y': [row['collision_gap'] for row in nested_linear['rows']],
                },
                {
                    'label': 'zero-noise lower bound',
                    'x': nested_linear['level_labels'],
                    'y': [row['zero_noise_lower_bound'] for row in nested_linear['rows']],
                },
            ],
            title='Nested restricted-linear threshold profile',
            x_label='observation level',
            y_label='gap / lower bound',
        ),
    )

    write_text(
        DOC_OUT / 'analytic-noise-lower-bound.svg',
        line_svg(
            [
                {
                    'label': 'minimax lower bound ≥ κ(η)/2',
                    'x': [row['noise_radius'] for row in noise_lower_bound['rows']],
                    'y': [row['lower_bound'] for row in noise_lower_bound['rows']],
                }
            ],
            title='Analytic noise lower bound',
            x_label='noise radius η',
            y_label='worst-case protected-variable error lower bound',
        ),
    )


if __name__ == '__main__':
    main()
