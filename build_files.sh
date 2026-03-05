#!/bin/bash
echo "BUILD START"
mkdir -p staticfiles_build
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.9
python3.9 -m pip install -r requirements.txt --break-system-packages
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"
