#!/bin/sh

set -e

getsecret() {
    FILE_PATH="$(eval "echo -n \"\${${1}_FILE}\"")"
    if [ -n "$FILE_PATH" ]; then
        cat "$FILE_PATH"
    else
        eval "echo -n \"\${${1}}\""
    fi
}


init() {
    ./manage.py collectstatic --noinput
    ./manage.py migrate
}

mkdir -p "$HOME/.ipython/profile_default/"
cp .ipython_config.py "$HOME/.ipython/profile_default/"

if [ -n "$INIT_JOB" ] || { [ -n "$DEV" ] && [ "$#" -eq 0 ]; }; then
    init
fi

if [ -n "$CHECK_DEPLOY" ] || { [ -n "$DEV" ] && [ "$#" -eq 0 ]; }; then
   ./manage.py check --deploy
fi

if [ "$#" -eq 0 ]; then
    if [ -n "$DEV" ]; then
        set -- ./manage.py runserver 0.0.0.0:8000
    else
        set -- gunicorn gccsite.wsgi -b 0.0.0.0:8000 \
                    --workers "${GUNICORN_WORKERS:-2}"
    fi
fi

exec "$@"
