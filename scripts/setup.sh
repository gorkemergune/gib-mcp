#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
python3 -m venv .venv
.venv/bin/python -m pip install .
PLAYWRIGHT_BROWSERS_PATH="$PWD/.playwright" .venv/bin/python -m playwright install chromium --only-shell
printf '\nKurulum tamam. Kesif: sh scripts/discover.sh\n'
