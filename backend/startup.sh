#!/bin/bash

/usr/local/bin/python manage.py makemigrations
/usr/local/bin/python manage.py migrate
/usr/local/bin/python manage.py makemigrations projects
/usr/local/bin/python manage.py migrate projects
/usr/local/bin/python manage.py collectstatic --no-input


if $IS_LIVE ; then
    echo 'Running production'
    /usr/local/bin/gunicorn personal_site.wsgi:application -w 2 -b :8000
else
   echo "Running development"
   /usr/local/bin/gunicorn personal_site.wsgi:application -w 2 -b :8000 --reload
fi