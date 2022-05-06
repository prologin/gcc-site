#!/usr/bin/env bash

set -xe

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

exec "$@"
