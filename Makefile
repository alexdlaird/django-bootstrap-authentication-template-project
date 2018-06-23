.PHONY: all env virtualenv install build build-migrations migrate test

SHELL := /usr/bin/env bash
MYPROJECT_VENV ?= .venv

all: env virtualenv install build migrate test

env:
	cp -n .env.example .env | true
	cp -n ansible/group_vars/stage.yml.example ansible/group_vars/stage.yml | true
	cp -n ansible/hosts/stage.example ansible/hosts/stage | true

virtualenv:
	@if [ ! -d "$(MYPROJECT_VENV)" ]; then \
		python3 -m pip install virtualenv; \
        python3 -m virtualenv $(MYPROJECT_VENV); \
	fi

install: env virtualenv
	@( \
		source $(MYPROJECT_VENV)/bin/activate; \
		python -m pip install -r requirements.txt; \
	)
	@python3 -m pip install "heliumcli>=1.2" "ansible>=2.5"

build: virtualenv
	@( \
		source $(MYPROJECT_VENV)/bin/activate; \
		python manage.py collectstatic --noinput; \
	)

build-migrations: env virtualenv install
	@( \
		source $(MYPROJECT_VENV)/bin/activate; \
		python manage.py makemigrations; \
	)

migrate: virtualenv
	@( \
		source $(MYPROJECT_VENV)/bin/activate; \
		python manage.py migrate; \
	)

test: virtualenv
	@( \
		source $(MYPROJECT_VENV)/bin/activate; \
		python -m coverage run --source='.' manage.py test && python -m coverage html; \
	)
