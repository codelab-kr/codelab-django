# use the official Python full image
FROM python:3.12.3-bullseye

# 빌드 인수 정의
# ARG SERVICE

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /opt/project
# ENV SERVICE=${SERVICE}

WORKDIR /opt/project
COPY ./scripts/entrypoint.sh /
COPY . .
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && apt-get install -y nodejs
RUN pip install . && pip install ".[dev]" && (cd theme; cd static_src; npm install;)

EXPOSE 8000
# ENTRYPOINT ["/entrypoint.sh", "loc"]
