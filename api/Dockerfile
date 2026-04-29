FROM python:3.12-alpine

WORKDIR /app

ENV PYTHONPATH .
ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# curl for healthchecks
RUN apk add --no-cache poetry curl

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY ./src ./src
COPY ./alembic.ini ./alembic.ini
COPY ./migrations ./migrations

COPY ./entrypoint.sh ./entrypoint.sh

RUN chmod +x entrypoint.sh

EXPOSE 8000

# Run migrations
ENTRYPOINT [ "./entrypoint.sh" ]

CMD ["poetry", "run", "uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]