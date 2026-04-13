#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path('/Users/stevenreid/Documents/New project/repos/ocp-research-program')
CSV_PATH = ROOT / 'data/generated/inventories/repo_file_inventory.csv'
JSON_PATH = ROOT / 'data/generated/validations/system_summary.json'
SKIP_PREFIXES = {'.git', '.venv', '.pytest_cache'}

rows = []
counts: dict[str, int] = {}
for path in sorted(ROOT.rglob('*')):
    if not path.is_file():
        continue
    rel = path.relative_to(ROOT)
    if rel.parts and rel.parts[0] in SKIP_PREFIXES:
        continue
    area = rel.parts[0] if len(rel.parts) > 1 else 'root'
    counts[area] = counts.get(area, 0) + 1
    rows.append({
        'relative_path': rel.as_posix(),
        'area': area,
        'extension': path.suffix,
        'size_bytes': path.stat().st_size,
    })

CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
with CSV_PATH.open('w', newline='') as fh:
    writer = csv.DictWriter(fh, fieldnames=['relative_path', 'area', 'extension', 'size_bytes'])
    writer.writeheader()
    writer.writerows(rows)

summary = {
    'tracked_like_file_count': len(rows),
    'counts_by_area': counts,
}
JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
JSON_PATH.write_text(json.dumps(summary, indent=2))
print(f'wrote {CSV_PATH}')
print(f'wrote {JSON_PATH}')
