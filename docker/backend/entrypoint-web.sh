#!/bin/sh

apt install gettext -y

# Для БД на хосте
#netstat -nr | grep '^0\.0\.0\.0' | awk '{print $2" host.docker.internal"}' >> /etc/hosts

# На случай если БД бдует долго запускаться
#while ! curl postgres:5432/ 2>&1 | grep '52'; do sleep 1; done

cd /core/src

# Миграции и статика
poetry run alembic upgrade head

# Запуск самого проекта
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8001

exec "$@"