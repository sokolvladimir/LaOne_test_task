#Подготовка
FROM python:3.10-slim as builder

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y libpq-dev gcc

RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /src/wheels -r requirements.txt

# Финальный этап
FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y libpq-dev

COPY --from=builder /src/wheels /wheels
COPY --from=builder /src/requirements.txt .

COPY requirements.txt .

RUN pip install --no-cache /wheels/*

COPY src src