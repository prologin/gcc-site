#!/bin/sh

set -e

if [ "$#" -eq 0 ]; then
  if [ -n "$DEV" ]; then
    set -- yarn dev
  else
    set -- node server.js
  fi
fi

exec "$@"
