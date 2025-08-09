FROM python:alpine3.21

COPY ./main.py /usr/src/app/
WORKDIR /usr/src/app

RUN pip install flask gunicorn

EXPOSE 8001

ARG APP_NAME=DEFAULT_NAME
ENV APP_NAME=$APP_NAME

CMD ["gunicorn", "--bind", "0.0.0.0:8001", "main:app"]

