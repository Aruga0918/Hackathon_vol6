FROM python:3.7

ENV APP_DIR=/app
WORKDIR ${APP_DIR}
RUN mkdir -p ${APP_DIR}
COPY ./src ${APP_DIR}

RUN pip install -r requirements.txt