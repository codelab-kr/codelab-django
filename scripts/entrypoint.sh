#!/usr/bin/env bash

set -e

# 서비스 이름 설정
SERVICE=${SERVICE:-default}

# manage.py 명령어 설정
RUN_MANAGE_PY="python -m services.${SERVICE}.manage"


echo 'Collecting static files...'
$RUN_MANAGE_PY collectstatic --no-input

echo 'Running migrations...'
$RUN_MANAGE_PY migrate --no-input

echo 'Running tests...'
# $RUN_MANAGE_PY test --no-input

echo 'Starting server...'

if [ "$1" = "loc" ]; then
    # $RUN_MANAGE_PY runserver_plus --cert-file cert.crt  0.0.0.0:8000
    $RUN_MANAGE_PY runserver 0.0.0.0:8000
else
    exec poetry run daphne services.${SERVICE}.${SERVICE}.asgi:application -p 8000 -b 0.0.0.0
fi

# 서비스 이름이 shop일 때 celery 작업자 실행
if [ "$SERVICE" = "shop" ]; then
    echo 'Starting Celery worker...'
    celery -A services.shop.shop worker -l info &

    echo 'Starting stripe...'
    stripe listen --forward-to 127.0.0.1:8002/payment/webhook/
fi

# 포그라운드 작업이 백그라운드 작업보다 뒤에 와야 함
wait -n

# 이 스크립트는 서비스 이름이 shop일 경우 Celery 작업자를 백그라운드에서 실행하고, Django 서버는 포그라운드에서 실행합니다. wait -n 명령어는 포그라운드 작업이 완료될 때까지 스크립트가 종료되지 않도록 합니다.
