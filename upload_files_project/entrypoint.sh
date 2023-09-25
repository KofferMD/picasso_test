#!/bin/ash

echo "Create database migrations"
python manage.py makemigrations
python manage.py migrate

exec "$@"
