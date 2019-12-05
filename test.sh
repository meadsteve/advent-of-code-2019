#!/usr/bin/env bash
set -ex
pipenv run mypy --ignore-missing-imports --strict-optional --check-untyped-defs advent
pipenv run pytest advent