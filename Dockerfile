# use the official Python full image
FROM python:3.12.3-slim

RUN apt-get update -qq \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /opt/project
ENV NODE_OPTIONS="--max-old-space-size=4096"

WORKDIR /opt/project
COPY setup.* .
RUN pip install . && pip install ".[dev]"

# Install system dependencies for WeasyPrint
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    libcairo2 \
    libpango1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    shared-mime-info \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . .

WORKDIR /opt/project/theme/static_src
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && npm install -g yarn && yarn set version berry
RUN yarn install --immutable

EXPOSE 8000
