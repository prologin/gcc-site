#!/bin/sh
. ./venv/bin/activate
cd gccsite
./manage.py makemigrations
./manage.py migrate
exec ./manage.py runserver 0.0.0.0:8000
