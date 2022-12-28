#!/bin/sh

exec docker-compose -p gccsite exec backend_dev ./manage.py "$@"
