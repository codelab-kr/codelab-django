# 프로젝트 설정
PROJECT_MODULE := services.blog
SETTINGS_MODULE := services.blog.blog.settings

# Python 명령어
PYTHON := python
MANAGE_PY := $(PYTHON) -m $(PROJECT_MODULE).manage

# 기본 목표
.DEFAULT_GOAL := help

# 도움말
.PHONY: help
help:
	@echo "Usage:"
	@echo "  make <target>"
	@echo ""
	@echo "Targets:"
	@echo "  help                Show this help message."
	@echo "  add-init			 Make __init__ files in python dirs"
	@echo "  venv	             Create venv and activate venv."
	@echo "  install             Install dependencies."
	@echo "  runserver           Run the Django development server."
	@echo "  migrations      	 Create new database migrations."
	@echo "  migrate             Apply database migrations."
	@echo "  superuser    		 Create a superuser for the Django admin."
	@echo "  shell               Open the Django shell."
	@echo "  test                Run the test suite."
	@echo "  coverage            Create coverage file."
	@echo "  tree                Display the project directory structure."
	@echo "  css 				 tailwind start."
	@echo "  lint				 Check lints."
	@echo "  clean				 Clean build files."
	@echo "  bandit				 Run bandit."
	@echo "  whl				 Make wheel build file."


# __init__ 파일 생성
.PHONY: add-init
add-init:
	python scripts/add_init.py

# 가상환경 생성 및 활성화
.PHONY: .venv
venv:
	python -m venv .venv && source .venv/bin/activate

# 종속성 설치
.PHONY: install
install:
	pip install . && pip install ".[dev]" && (cd theme; cd static_src; npm install;) && pre-commit install

# Django 개발 서버 실행
.PHONY: runserver
runserver:
	$(MANAGE_PY) runserver

# common.auth 마이그레이션 파일 생성
.PHONY: migrations-auth
migrations-auth:
	$(MANAGE_PY) makemigrations common_auth

# 마이그레이션 파일 생성
.PHONY: migrations
migrations:
	$(MANAGE_PY) makemigrations common_auth
	$(MANAGE_PY) makemigrations

# 데이터베이스 마이그레이션 적용
.PHONY: migrate
migrate:
	$(MANAGE_PY) migrate

# 슈퍼유저 생성
.PHONY: superuser
superuser:
	$(MANAGE_PY) createsuperuser

# Django 쉘 실행
.PHONY: shell
shell:
	$(MANAGE_PY) shell

# 테스트 실행
.PHONY: test
test:
	python -m pytest --cov=services.blog

# coverage file 생성
coverage:
	python -m pytest --cov=services.blog --cov-report=html

# 프로젝트 디렉토리 구조 출력
.PHONY: tree
tree:
	tree -I '__pycache__|*.pyc|*.pyo|theme' > tree

# tailwind 실행
.PHONY: css
css:
	$(MANAGE_PY) tailwind start

# lint 실행
.PHONY: lint
lint:
	pre-commit run --all-files

# build files 삭제
.PHONY: clean
clean:
	rm -rf dist build

# Bandit 보안 검사 실행
.PHONY: bandit
bandit:
	python -m bandit -c bandit.yaml -r services.blog

# wheel build file 생성
.PHONY: whl
whl:
	pip install build
	python -m build --wheel
