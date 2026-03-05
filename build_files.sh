#!/bin/bash
echo "BUILD START"
mkdir -p staticfiles_build
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput --clear
echo "BUILD END"
