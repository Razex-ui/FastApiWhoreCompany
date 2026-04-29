SHELL := /bin/bash

# --- init project ---

.PHONY: requirements
requirements: pyproject.toml
	poetry lock
	poetry install --no-root

# --- alembic ---

.PHONY: alembic_upgrade
alembic_upgrade: requirements
	poetry run alembic upgrade head

.PHONY: alembic_autogenerate
alembic_autogenerate: alembic_upgrade
	poetry run alembic revision --autogenerate -m "$(ARGS)"

# --- run app ---

.PHONY: run_uvicorn
run_uvicorn: requirements
	poetry run uvicorn src.main:app --reload

.PHONY: run_db
run_db: postgresql.sh
	./postgresql.sh