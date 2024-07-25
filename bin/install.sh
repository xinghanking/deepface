#!/usr/bin/env bash

BASE_ROOT=$(dirname $(dirname "$(readlink -f "$0")"))
cd "$BASE_ROOT"
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
mkdir -p log
chmod +x bin/run.sh
./bin/run.sh start