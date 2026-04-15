from __future__ import annotations

import csv
import json
from pathlib import Path

from ocp.discovery_mixer import discovery_mixer_demo_reports

REPO_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = REPO_ROOT / 'data' / 'generated' / 'discovery_mixer'


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    bundle = discovery_mixer_demo_reports()

    summary_path = OUTPUT_DIR / 'discovery_mixer_summary.json'
    summary_path.write_text(json.dumps(bundle, indent=2), encoding='utf-8')
    print(f'wrote {summary_path}')

    table_path = OUTPUT_DIR / 'discovery_mixer_demo_table.csv'
    with table_path.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(bundle['rows'][0].keys()))
        writer.writeheader()
        writer.writerows(bundle['rows'])
    print(f'wrote {table_path}')


if __name__ == '__main__':
    main()
