#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from pathlib import Path
import sys

ROOT = Path('/Users/stevenreid/Documents/New project/repos/ocp-research-program')
sys.path.insert(0, str(ROOT / 'src'))

from ocp.structural_discovery import structural_discovery_demo_reports

DATA_OUT = ROOT / 'data/generated/structural_discovery'
DOC_OUT = ROOT / 'docs/assets/structural-discovery'


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        return
    with path.open('w', newline='') as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def grouped_bar_svg(rows: list[dict[str, object]], *, title: str) -> str:
    width, height = 840, 420
    margin = {'left': 84, 'right': 40, 'top': 56, 'bottom': 96}
    plot_w = width - margin['left'] - margin['right']
    plot_h = height - margin['top'] - margin['bottom']
    labels = [str(row['demo']) for row in rows]
    max_value = max(
        max(float(row['metric_before']), float(row['metric_after']))
        for row in rows
    ) if rows else 1.0
    max_value = max(max_value, 1e-6)

    def py(value: float) -> float:
        return height - margin['bottom'] - value * plot_h / max_value

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#fffdf8" rx="20"/>',
        f'<text x="{margin["left"]}" y="30" font-family="Source Sans 3, sans-serif" font-size="24" font-weight="700" fill="#1c1d21">{title}</text>',
        f'<line x1="{margin["left"]}" x2="{margin["left"]}" y1="{margin["top"]}" y2="{height - margin["bottom"]}" stroke="#1c1d21"/>',
        f'<line x1="{margin["left"]}" x2="{width - margin["right"]}" y1="{height - margin["bottom"]}" y2="{height - margin["bottom"]}" stroke="#1c1d21"/>',
        '<text x="22" y="210" transform="rotate(-90 22 210)" text-anchor="middle" font-size="13" fill="#5c605d">diagnostic metric</text>',
    ]
    group_w = plot_w / max(len(rows), 1)
    bar_w = group_w * 0.28
    colors = {'before': '#a63229', 'after': '#356c4a'}
    for index, row in enumerate(rows):
        x0 = margin['left'] + index * group_w + group_w * 0.18
        before = float(row['metric_before'])
        after = float(row['metric_after'])
        y_before = py(before)
        y_after = py(after)
        parts.append(f'<rect x="{x0:.2f}" y="{y_before:.2f}" width="{bar_w:.2f}" height="{height - margin["bottom"] - y_before:.2f}" rx="8" fill="{colors["before"]}"/>')
        parts.append(f'<rect x="{x0 + bar_w + group_w * 0.08:.2f}" y="{y_after:.2f}" width="{bar_w:.2f}" height="{height - margin["bottom"] - y_after:.2f}" rx="8" fill="{colors["after"]}"/>')
        parts.append(f'<text x="{x0 + group_w * 0.28:.2f}" y="{height - margin["bottom"] + 18}" text-anchor="middle" font-size="12" fill="#5c605d">{labels[index]}</text>')
        parts.append(f'<text x="{x0 + bar_w / 2:.2f}" y="{y_before - 8:.2f}" text-anchor="middle" font-size="11" fill="#1c1d21">{before:.2f}</text>')
        parts.append(f'<text x="{x0 + bar_w + group_w * 0.08 + bar_w / 2:.2f}" y="{y_after - 8:.2f}" text-anchor="middle" font-size="11" fill="#1c1d21">{after:.2f}</text>')
    parts.append('<rect x="620" y="70" width="16" height="16" rx="4" fill="#a63229"/>')
    parts.append('<text x="644" y="83" font-size="12" fill="#1c1d21">before</text>')
    parts.append('<rect x="620" y="96" width="16" height="16" rx="4" fill="#356c4a"/>')
    parts.append('<text x="644" y="109" font-size="12" fill="#1c1d21">after</text>')
    parts.append('</svg>')
    return ''.join(parts)


def main() -> None:
    DATA_OUT.mkdir(parents=True, exist_ok=True)
    DOC_OUT.mkdir(parents=True, exist_ok=True)

    payload = structural_discovery_demo_reports()
    (DATA_OUT / 'structural_discovery_summary.json').write_text(json.dumps(payload, indent=2))

    table_rows = []
    for demo_name, report in payload['demos'].items():
        comparison = report.get('comparison')
        chosen_fix = report.get('chosen_fix')
        table_rows.append(
            {
                'demo': demo_name,
                'family': report['family'],
                'before_regime': report['current_regime'],
                'after_regime': comparison['after_regime'] if comparison else report['current_regime'],
                'failure_modes': '; '.join(report['failure_modes']),
                'missing_structure': report['missing_structure'],
                'chosen_fix': chosen_fix['title'] if chosen_fix else 'keep current',
                'action_kind': chosen_fix['action_kind'] if chosen_fix else 'keep',
                'theorem_status': chosen_fix['theorem_status'] if chosen_fix else report['theorem_status'],
                'metric_name': comparison['key_metric_name'] if comparison else 'not_applicable',
                'metric_before': comparison['key_metric_before'] if comparison else 0.0,
                'metric_after': comparison['key_metric_after'] if comparison else 0.0,
                'regime_changed': comparison['regime_changed'] if comparison else False,
                'exact_after': comparison['exact_after'] if comparison else report['exact'],
            }
        )
    write_csv(DATA_OUT / 'structural_discovery_demo_table.csv', table_rows)
    (DOC_OUT / 'structural-discovery-before-after.svg').write_text(
        grouped_bar_svg(table_rows, title='Structural Discovery demo improvements')
    )
    print(f'wrote {DATA_OUT / "structural_discovery_summary.json"}')
    print(f'wrote {DATA_OUT / "structural_discovery_demo_table.csv"}')
    print(f'wrote {DOC_OUT / "structural-discovery-before-after.svg"}')


if __name__ == '__main__':
    main()
