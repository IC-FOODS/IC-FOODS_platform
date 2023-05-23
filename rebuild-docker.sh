#!/bin/sh
# rebuild the local environment

docker-compose down -v --remove-orphans &&\
find . -name "*.pyc" -delete &&\
docker-compose build &&\
docker-compose up -d
docker-compose exec django sh -c "./manage.py migrate"
