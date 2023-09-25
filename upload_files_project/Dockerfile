FROM python:3.9-alpine3.16

WORKDIR /usr/src/app/

RUN pip install --upgrade pip

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

RUN apk add postgresql-client build-base postgresql-dev

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
COPY . /usr/src/app/


ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]
