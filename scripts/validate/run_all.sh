#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
python3 scripts/search/build_inventory.py
python3 scripts/report/build_claim_registry.py
python3 scripts/report/build_system_report.py
PYTHONPATH=src python3 scripts/compare/run_operator_examples.py
PYTHONPATH=src python3 scripts/compare/run_recoverability_examples.py
PYTHONPATH=src python3 scripts/compare/run_design_examples.py
PYTHONPATH=src python3 scripts/compare/run_structural_discovery_examples.py
PYTHONPATH=src python3 scripts/compare/run_discovery_mixer_examples.py
if command -v node >/dev/null 2>&1; then
  node scripts/compare/build_workbench_examples.mjs
  node --test tests/consistency/*.test.mjs
fi
python3 scripts/validate/check_links.py
python3 scripts/validate/check_naming.py
python3 scripts/validate/check_workbench_static.py
if command -v uv >/dev/null 2>&1; then
  PYTHONPATH=src uv run --with pytest python -m pytest -q
else
  PYTHONPATH=src python3 -m pytest -q
fi
