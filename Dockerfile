FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl

COPY requirements.txt requirements.txt

RUN ["pip", "install", "-r", "requirements.txt"]

COPY src /app

CMD ["bash", "-c", "wait-for-it -s $DB_HOST:5432; alembic upgrade head; python -B main.py"]
