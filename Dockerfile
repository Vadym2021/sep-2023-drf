FROM python:3.12-alpine

MAINTAINER Some Dev

ENV PYTHONUNBUFFERED=1

RUN apk update
RUN apk add --no-cache gcc musl-dev mariadb-dev pkgconfig
#for pillow
RUN apk add --no-cache jpeg-dev zlib-dev libjpeg

RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install django

COPY requirements.txt /tmp

RUN cd /tmp && pip install -r requirements.txt