# 프로젝트 설정
PROJECT_MODULE := services.base
SETTINGS_MODULE := services.base.base.settings

# Python 및 Poetry 명령어
PYTHON := poetry run python
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
	@echo "  init				 Make __init__ files in python dirs"
	@echo "  install             Install dependencies using Poetry."
	@echo "  runserver           Run the Django development server."
	@echo "  migrations      	 Create new database migrations."
	@echo "  migrations-auth 	 Create new database migrations for common.auth."
	@echo "  migrate             Apply database migrations."
	@echo "  superuser    		 Create a superuser for the Django admin."
	@echo "  shell               Open the Django shell."
	@echo "  test                Run the test suite."
	@echo "  tree                Display the project directory structure."
	@echo "  css 				 tailwind start"

# __init__ 파일 생성
.PHONY: init
init:
	python scripts/add_init.py

# 종속성 설치
#  && (cd theme; cd static_src; npm install;)
.PHONY: install
install:
	poetry install --no-root

# Django 개발 서버 실행
.PHONY: runserver
runserver:
	$(MANAGE_PY) runserver

# 마이그레이션 파일 생성
.PHONY: migrations
migrations:
	$(MANAGE_PY) makemigrations

# common.auth 마이그레이션 파일 생성
.PHONY: migrations-auth
migrations-auth:
	$(MANAGE_PY) makemigrations common.auth

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
	$(MANAGE_PY) test

# 프로젝트 디렉토리 구조 출력
.PHONY: tree
tree:
	tree -I '__pycache__|*.pyc|*.pyo|theme'

# tailwind 실행
.PHONY: css
css:
	$(MANAGE_PY) tailwind start
