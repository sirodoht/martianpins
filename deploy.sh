#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noinput
kill -9 $(cat pid-uwsgi)
uwsgi --ini=uwsgi.ini
