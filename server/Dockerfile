FROM python:3.10.0-slim-buster

SHELL ["/bin/bash", "-c"]

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN pip install fastapi uvicorn