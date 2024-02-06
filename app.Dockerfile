FROM python:3.10.13-bookworm

COPY ./app /app

RUN pip install -r /app/requirements.txt