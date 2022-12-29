# Production Dockerfile

FROM node:18 as base

ENV DEBIAN_FRONTEND=noninteractive \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    NODE_OPTIONS=--openssl-legacy-provider

FROM base as builder

ENV YARN_CACHE_FOLDER=/root/.yarn

WORKDIR /build

RUN --mount=type=bind,target=./package.json,src=./package.json \
    --mount=type=bind,target=./yarn.lock,src=./yarn.lock \
    --mount=type=cache,target=/root/.yarn \
    yarn install --frozen-lockfile

COPY ./ ./

RUN yarn build

FROM base

RUN userdel node
ARG NODE_UID=1000
ARG NODE_GID=1000

RUN mkdir -p /app && \
    useradd -d /app -r -u ${NODE_UID} app && \
    chown app:${NODE_UID} -R /app

WORKDIR /app

COPY --from=builder /build/package.json /app/package.json
COPY --from=builder /build/entrypoint.sh /app/entrypoint.sh
COPY --from=builder /build/.nuxt /app/gccsite

WORKDIR /app/gccsite

USER app:${NODE_GID}

ENV NODE_ENV=production

ENTRYPOINT ["/app/entrypoint.sh"]
