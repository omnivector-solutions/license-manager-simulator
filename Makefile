# TARGETS
install:
	poetry install

test: install
	poetry run pytest

lint: install
	poetry run flake8 license_manager_simulator --max-line-length=110
	poetry run isort --check license_manager_simulator
	poetry run black --check license_manager_simulator

format: install
	poetry run black license_manager_simulator
	poetry run isort license_manager_simulator

qa: test lint

clean: clean-eggs clean-build
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '__pycache__' -delete
	@rm -rf .tox

clean-eggs:
	@find . -name '*.egg' -print0|xargs -0 rm -rf --
	@rm -rf .eggs/

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

# SETTINGS
# Use one shell for all commands in a target recipe
.ONESHELL:
# Set default goal
.DEFAULT_GOAL := help
# Use bash shell in Make instead of sh 
SHELL := /bin/bash
