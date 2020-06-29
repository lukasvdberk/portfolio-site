#!/bin/bash

/usr/local/bin/python manage.py makemigrations
/usr/local/bin/python manage.py makemigrations familyfridge
/usr/local/bin/python manage.py migrate
/usr/local/bin/python manage.py migrate familyfridge
/usr/local/bin/python manage.py loaddata config.json
/usr/local/bin/python manage.py collectstatic --no-input


if $IS_LIVE ; then
    echo 'Running production'
    /usr/local/bin/gunicorn personal_site.wsgi:application -w 2 -b :8000
else
   echo "Running development"
   /usr/local/bin/gunicorn personal_site.wsgi:application -w 2 -b :8000 --reload
fi