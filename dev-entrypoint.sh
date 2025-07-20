#!/bin/bash

mkdir -p build && cd build && cmake .. && make -j4
echo "Copying binaries to /eqemu_bin/"
cp /app/Server/build/bin/* /eqemu_bin/
envsubst < /app/login.template.ini > /eqemu_bin/login.ini
envsubst < /app/eqemu_config.template.json > /eqemu_bin/eqemu_config.json
cp /app/Server/loginserver/login_util/login.json /eqemu_bin/login.json
cp /app/Server/loginserver/login_util/*.conf /eqemu_bin/
cp /app/Server/utils/patches/*.conf /eqemu_bin/

echo "[dev-entrypoint] Running in container as PID $$"
echo "[dev-entrypoint] DATABASE_USER is: $DATABASE_USER"
echo "[dev-entrypoint] DATABASE_PASSWORD is: $DATABASE_PASSWORD"
echo "[dev-entrypoint] DATABASE_HOST is: $DATABASE_HOST"
echo "[dev-entrypoint] DATABASE_PORT is: $DATABASE_PORT"
echo "[dev-entrypoint] DATABASE_NAME is: $DATABASE_NAME"

bash