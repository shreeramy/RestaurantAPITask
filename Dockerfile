# syntax=docker/dockerfile:1
FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get update && apt-get install -y python3.8-dev python3-pip build-essential libpq-dev python3-gdal

COPY ./entrypoint.sh /code/entrypoint.sh


RUN pip3 install --upgrade pip setuptools wheel

RUN pip3 install psycopg2-binary --no-binary psycopg2-binary
RUN chmod +x /code/entrypoint.sh

COPY . /code/

