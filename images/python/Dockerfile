FROM --platform=linux/amd64 python:3.10-buster

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

ENV DOCKER_CONTENT_TRUST 1

ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=DontWarn

COPY ./conf/requirements.txt /app/requirements.txt

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y curl apt-transport-https \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18 unixodbc-dev \
    && apt-get install -y libgssapi-krb5-2 \
    && apt-get -y install python3-pip \
    && apt-get install -y freetds-dev freetds-bin

RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip cache purge

ADD . /app

ARG APP_ID=1000

RUN groupadd -g "$APP_ID" app \
  && useradd -g "$APP_ID" -u "$APP_ID" -d /app -s /bin/bash app

USER app:app