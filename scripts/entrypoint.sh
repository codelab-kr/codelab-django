#!/usr/bin/env bash

set -e

# 서비스 이름 설정
SERVICE=${SERVICE:-default}

# manage.py 명령어 설정
RUN_MANAGE_PY="python -m services.${SERVICE}.manage"

# 마이그레이션 실행
echo 'Running migrations...'
$RUN_MANAGE_PY migrate --no-input

# # Tailwind CSS 빌드 명령어
# if [ "$1" = "loc" ]; then
#     echo 'Starting Tailwind CSS in watch mode...'
#     $RUN_MANAGE_PY tailwind start &
# fi

# Django 서버 실행
echo 'Starting server...'
if [ "$1" = "loc" ]; then
    $RUN_MANAGE_PY runserver 0.0.0.0:8000
else
    exec daphne services.${SERVICE}.${SERVICE}.asgi:application -p 8000 -b 0.0.0.0
fi

# 서비스 이름이 shop일 때 celery 작업자 실행
if [ "$SERVICE" = "shop" ]; then
    echo 'Starting Celery worker...'
    celery -A services.shop.shop worker -l info &
fi

# 포그라운드 작업이 백그라운드 작업보다 뒤에 와야 함
wait -n
