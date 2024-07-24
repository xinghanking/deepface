#!/usr/bin/env bash

BASE_ROOT=$(dirname $(dirname "$(readlink -f "$0")"))
cd "$BASE_ROOT"
python -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
chmod +x bin/run.sh
./bin/run.sh start