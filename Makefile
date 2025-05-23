.PHONY: all env install nopyc clean build build-migrations migrate test

SHELL := /usr/bin/env bash
MYPROJECT_VENV ?= venv
PYTHON_BIN ?= python

all: build migrate test

env:
	cp -n .env.example .env | true
	cp -n ansible/group_vars/web.yml.example ansible/group_vars/web.yml | true
	cp -n ansible/hosts/stage.example ansible/hosts/stage | true

venv:
	$(PYTHON_BIN) -m pip install virtualenv
	$(PYTHON_BIN) -m virtualenv $(MYPROJECT_VENV)

install: env venv
	@( \
		source $(MYPROJECT_VENV)/bin/activate; \
		python -m pip install -r requirements.txt -r requirements-dev.txt; \
	)
	@$(PYTHON_BIN) -m pip install "heliumcli>=1.6.13"

nopyc:
	find . -name '*.pyc' | xargs rm -f || true
	find . -name __pycache__ | xargs rm -rf || true

clean: nopyc
	rm -rf build $(MYPROJECT_VENV)

build: install
	@( \
		source $(MYPROJECT_VENV)/bin/activate; \
		python manage.py collectstatic --noinput; \
	)

build-migrations: install
	@( \
		source $(MYPROJECT_VENV)/bin/activate; \
		python manage.py makemigrations; \
	)

migrate: install
	@( \
		source $(MYPROJECT_VENV)/bin/activate; \
		python manage.py migrate; \
	)

test: install
	@if [ ! -f ansible/stage.yml ]; then echo "ansible/stage.yml not found" & exit 1 ; fi
	@if [ ! -f ansible/group_vars/web.yml ]; then echo "ansible/group_vars/web.yml not found" & exit 1 ; fi
	@if [ ! -f ansible/hosts/stage ]; then echo "ansible/hosts/stage not found" & exit 1 ; fi

	@$(PYTHON_BIN) -c "import heliumcli" || (echo "helium-cli not installed"; exit 1)

	@ansible-playbook ansible/stage.yml --syntax-check

	@( \
		source $(MYPROJECT_VENV)/bin/activate; \
		coverage run manage.py test && coverage report && coverage html && coverage xml; \
	)
