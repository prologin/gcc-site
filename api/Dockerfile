FROM python:3.10-slim as base

ENV DEBIAN_FRONTEND=noninteractive \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    VENV_PATH="/opt/venv" \
    PATH="/opt/venv/bin:$PATH"

RUN apt-get update && \
    apt-get install -y --no-install-recommends libpq5

FROM base as builder

ARG INSTALL_PROJECT=true
ARG INCLUDE_DEV_DEPS=false

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python-dev libpq-dev

RUN --mount=type=bind,target=./pyproject.toml,src=./pyproject.toml \
    --mount=type=bind,target=./poetry.lock,src=./poetry.lock \
    --mount=type=cache,target=/root/.cache/pypoetry \
    python -m venv /opt/venv && \
    pip3 install --upgrade pip && \
    pip3 install poetry && \
    poetry install $(if [ $INSTALL_PROJECT = "false" ]; then echo "--no-root"; fi) $(if [ $INCLUDE_DEV_DEPS = "false" ]; then echo "--no-dev"; fi)

FROM base

RUN mkdir -p /var/prologin/api/gccsite
WORKDIR /var/prologin/api/gccsite

COPY --from=builder /opt/venv /opt/venv
COPY docker-entrypoint.dev.sh /docker-entrypoint.dev.sh

ENTRYPOINT [ "/docker-entrypoint.dev.sh" ]
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
