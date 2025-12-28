#!/bin/bash
set -e

echo "Running migrations..."
uv run python config/manage.py migrate --noinput

echo "Collecting static files..."
uv run python config/manage.py collectstatic --noinput


echo "Create Superuser"
uv run python config/manage.py createadminuser --email "$DJANGO_SUPERUSER_EMAIL" --password "$DJANGO_SUPERUSER_PASSWORD"

echo "Starting server..."
exec uv run python config/manage.py runserver_plus 0.0.0.0:8000
