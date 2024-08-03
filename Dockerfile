# use the official Python full image
FROM python:3.12.3-bullseye

# 빌드 인수 정의
ARG SERVICE

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /opt/project
ENV SERVICE=${SERVICE}

WORKDIR /opt/project
COPY ./scripts/entrypoint.sh /
COPY . .
RUN set -xe \
    && mkdir -p /opt/project/staticfiles \
    && apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && pip install . && pip install ".[dev]" \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh", "loc"]
