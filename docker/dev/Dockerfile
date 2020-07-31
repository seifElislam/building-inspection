FROM python:3.7-slim-buster

RUN apt-get update

RUN apt-get install -y build-essential python3-mysqldb default-libmysqlclient-dev

COPY requirements /requirements
WORKDIR /inspection
RUN pip install -r /requirements/base.txt
COPY docker/dev/start_script.sh ./start_script.sh
RUN chmod +x ./start_script.sh
