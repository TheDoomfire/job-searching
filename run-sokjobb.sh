#!/bin/bash
cd "$(dirname "$0")"  # Navigate to script's directory
source .venv/bin/activate
python3 main.py
deactivate
