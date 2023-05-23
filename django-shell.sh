#!/bin/sh
# Django shell using shell_plus and ipython

docker-compose exec django sh -c "./manage.py shell_plus --ipython"
