FROM python:3.9.2-alpine

WORKDIR /usr/src/password_api

COPY requirements.txt ./

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install -U pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

COPY . .

ENTRYPOINT ./run.sh
