FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

ENV MODULE_NAME=license_manager_simulator.main

RUN apt update && apt install -y curl

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* /app/

RUN poetry install --no-root --no-dev

COPY ./license_manager_simulator /app/license_manager_simulator