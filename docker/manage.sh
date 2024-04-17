#!/bin/sh

exec docker exec docker-backend_dev-1 ./manage.py "$@"
