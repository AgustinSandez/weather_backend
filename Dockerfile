FROM ubuntu:16.04

MAINTANER Your Name "agustinsandez@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENV FLASK_APP /app/main.py
CMD export FLASK_APP=main.py && flask run