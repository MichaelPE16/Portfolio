#!/bin/bash
echo "BUILD START"
mkdir -p staticfiles_build

if command -v python3.12 &>/dev/null; then
    PYTHON_CMD=python3.12
elif command -v python3.11 &>/dev/null; then
    PYTHON_CMD=python3.11
elif command -v python3.10 &>/dev/null; then
    PYTHON_CMD=python3.10
else
    PYTHON_CMD=python3
fi

echo "Using Python executable: $PYTHON_CMD"
$PYTHON_CMD --version

curl -sS https://bootstrap.pypa.io/get-pip.py | $PYTHON_CMD
$PYTHON_CMD -m pip install -r requirements.txt --break-system-packages
$PYTHON_CMD manage.py collectstatic --noinput --clear
echo "BUILD END"
