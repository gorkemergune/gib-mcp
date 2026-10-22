#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
export PLAYWRIGHT_BROWSERS_PATH="$PWD/.playwright"
export PYTHONPATH="$PWD/src${PYTHONPATH:+:$PYTHONPATH}"
exec .venv/bin/python -m gib_mcp.discovery "$@"
