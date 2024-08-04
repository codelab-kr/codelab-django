# use the official Python full image
FROM python:3.12.3-bullseye

# ARG SERVICE

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /opt/project
# ENV SERVICE=${SERVICE}

WORKDIR /opt/project
COPY . .
# COPY ./scripts/entrypoint.sh /
RUN pip install . && pip install ".[dev]"

WORKDIR /opt/project/theme/static_src
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && apt-get install -y nodejs && npm install -g yarn && yarn set version berry
RUN yarn install --immutable

EXPOSE 8000
# ENTRYPOINT ["/entrypoint.sh", "loc"]
