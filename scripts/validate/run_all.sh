#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
python3 scripts/search/build_inventory.py
python3 scripts/report/build_claim_registry.py
python3 scripts/report/build_system_report.py
PYTHONPATH=src python3 scripts/compare/run_operator_examples.py
python3 scripts/validate/check_links.py
if command -v uv >/dev/null 2>&1; then
  PYTHONPATH=src uv run --with pytest python -m pytest -q
else
  PYTHONPATH=src python3 -m pytest -q
fi
