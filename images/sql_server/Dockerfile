FROM --platform=linux/amd64 python:3.8.6

# Prevents Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Causes all output to stdout to be flushed immediately
ENV PYTHONUNBUFFERED 1

# Mark the image as trusted
ENV DOCKER_CONTENT_TRUST 1

ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=DontWarn

WORKDIR /code

COPY ./conf/requirements.txt /code/requirements.txt

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

COPY . /code/