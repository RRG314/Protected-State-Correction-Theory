#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from dataclasses import asdict, is_dataclass
from pathlib import Path

import numpy as np

from ocp.continuous import LinearOCPFlow
from ocp.next_phase import (
    canonical_rank_deficient_fragility_sweep,
    canonical_structure_classes,
    canonical_time_accumulation_example,
    cfd_deep_dive_sweep,
    full_rank_robustness_sweep,
    generator_dynamics_profile,
    quantitative_recoverability_profile,
)

ROOT = Path('/Users/stevenreid/Documents/New project/repos/ocp-research-program')
OUT = ROOT / 'data/generated/next-phase'


def _serialize(value):
    if is_dataclass(value):
        return {key: _serialize(item) for key, item in asdict(value).items()}
    if isinstance(value, dict):
        return {str(key): _serialize(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_serialize(item) for item in value]
    if isinstance(value, (np.floating, np.integer)):
        return value.item()
    return value


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        return
    with path.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def _profile_rows() -> list[dict[str, object]]:
    cases = (
        (
            'robust-full-information',
            np.asarray(
                [
                    [1.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0],
                    [0.0, 0.0, 1.0],
                ],
                dtype=float,
            ),
            np.asarray([[0.2, -0.7, 1.1]], dtype=float),
        ),
        (
            'exact-but-fragile',
            np.asarray(
                [
                    [1.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0],
                ],
                dtype=float,
            ),
            np.asarray([[1.0, 0.0, 0.0]], dtype=float),
        ),
        (
            'augmentation-repairable',
            np.asarray(
                [
                    [1.0, 0.0, 0.0],
                    [0.0, 1.0, 1.0],
                ],
                dtype=float,
            ),
            np.asarray([[0.0, 0.0, 1.0]], dtype=float),
        ),
        (
            'collision-dominated',
            np.asarray(
                [
                    [1.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0],
                ],
                dtype=float,
            ),
            np.asarray([[0.0, 0.0, 1.0]], dtype=float),
        ),
    )

    rows: list[dict[str, object]] = []
    for name, observation, protected in cases:
        profile = quantitative_recoverability_profile(observation, protected, box_radius=1.0)
        rows.append({'case': name, **_serialize(profile)})
    return rows


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    quantitative_rows = _profile_rows()
    rank_fragile = canonical_rank_deficient_fragility_sweep((0.0, 1e-4, 1e-3, 1e-2, 1e-1))
    full_rank = full_rank_robustness_sweep((0.0, 1e-2, 5e-2, 1e-1, 2e-1))
    accumulation = canonical_time_accumulation_example()
    structures = canonical_structure_classes()

    flow = LinearOCPFlow(
        generator=np.asarray(
            [
                [0.0, 0.0, 0.0],
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 2.0],
            ],
            dtype=float,
        ),
        protected_basis=np.asarray([[1.0], [0.0], [0.0]], dtype=float),
        disturbance_basis=np.asarray([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]], dtype=float),
    )
    generator = generator_dynamics_profile(flow, np.asarray([1.0, 1.0, 1.0], dtype=float), (0.0, 0.5, 1.0, 2.0, 3.0))

    cfd_rows = cfd_deep_dive_sweep((17, 25, 33), (0.1, 0.2, 0.3))

    summary = {
        'quantitative_profiles': quantitative_rows,
        'rank_deficient_fragility': _serialize(rank_fragile),
        'full_rank_robustness': _serialize(full_rank),
        'time_accumulation': _serialize(accumulation),
        'generator_dynamics': _serialize(generator),
        'structure_classes': _serialize(structures),
        'cfd_deep_dive': _serialize(cfd_rows),
    }
    (OUT / 'next_phase_summary.json').write_text(json.dumps(summary, indent=2), encoding='utf-8')

    write_csv(OUT / 'quantitative_profiles.csv', quantitative_rows)
    write_csv(
        OUT / 'fragility_rank_deficient.csv',
        [_serialize(row) for row in rank_fragile.rows],
    )
    write_csv(
        OUT / 'fragility_full_rank.csv',
        [_serialize(row) for row in full_rank.rows],
    )
    write_csv(
        OUT / 'dynamic_accumulation.csv',
        [_serialize(row) for row in accumulation.rows],
    )
    write_csv(
        OUT / 'generator_dynamics.csv',
        [_serialize(row) for row in generator.rows],
    )
    write_csv(
        OUT / 'structure_classes.csv',
        [_serialize(row) for row in structures],
    )
    write_csv(
        OUT / 'cfd_deep_dive.csv',
        [_serialize(row) for row in cfd_rows],
    )

    print(f'wrote {OUT / "next_phase_summary.json"}')
    print(f'wrote {OUT / "quantitative_profiles.csv"}')
    print(f'wrote {OUT / "fragility_rank_deficient.csv"}')
    print(f'wrote {OUT / "fragility_full_rank.csv"}')
    print(f'wrote {OUT / "dynamic_accumulation.csv"}')
    print(f'wrote {OUT / "generator_dynamics.csv"}')
    print(f'wrote {OUT / "structure_classes.csv"}')
    print(f'wrote {OUT / "cfd_deep_dive.csv"}')


if __name__ == '__main__':
    main()
