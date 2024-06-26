FROM python:3.12-slim as base

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
    apt-get install -y --no-install-recommends \
        awscli \
        git make \
        curl ca-certificates gnupg apt-transport-https \
        libpq-dev postgresql-client \
        libssl-dev \
        libmagic1

FROM base as builder

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc python3-dev bison

RUN --mount=type=bind,target=./pyproject.toml,src=./pyproject.toml \
    --mount=type=bind,target=./poetry.lock,src=./poetry.lock \
    --mount=type=cache,target=/root/.cache/pypoetry \
    python -m venv /opt/venv/ && \
    pip3 install --upgrade pip && \
    pip3 install poetry==1.7.1 && \
    poetry install --only=main

FROM base

ARG WORKDIR=/app/gccsite
ARG DJANGO_UID=1000
ARG DJANGO_GID=1000

COPY --from=builder /opt/venv/ /opt/venv/

RUN mkdir -p /app && \
    useradd -d /app -r -u ${DJANGO_UID} app && \
    chown app:${DJANGO_GID} -R /app && \
    mkdir -p ${WORKDIR}/staticfiles && \
    chown app:${DJANGO_GID} -R ${WORKDIR}/staticfiles

USER app:${DJANGO_GID}

WORKDIR ${WORKDIR}

COPY ./ ./

ENTRYPOINT ["/app/gccsite/entrypoint.sh"]
