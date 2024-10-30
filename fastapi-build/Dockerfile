FROM python:3.10-bullseye
LABEL maintainer="Jabba"

ENV PYTHONUNBUFFERED 1
ENV PYTHONPYCACHEPREFIX=/tmp/pycache

## Install dependencies (before copying the app to use cache)
COPY ./fastapi-build/requirements.txt /requirements.txt
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install --no-cache-dir -r /requirements.txt

COPY ./fastapi-build/scripts /scripts
COPY ./app /app

WORKDIR /app

RUN adduser fastapi && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER fastapi

CMD [ "run.sh" ]