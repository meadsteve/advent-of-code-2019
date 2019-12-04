#!/usr/bin/env bash

pipenv run mypy --ignore-missing-imports --strict-optional --check-untyped-defs advent
pipenv run pytest advent