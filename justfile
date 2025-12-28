# Django development commands

# Run development server
run:
    uv run python config/manage.py runserver

# Run migrations
migrate:
    uv run python config/manage.py migrate

# Make migrations
makemigrations:
    uv run python config/manage.py makemigrations

# Make migrations for a specific app
makemigrations-app app:
    uv run python config/manage.py makemigrations {{app}}

# Collect static files
collectstatic:
    uv run python config/manage.py collectstatic --noinput

# Create a new Django app
createapp name:
    uv run python config/manage.py startapp {{name}}

# Create admin user
createadmin:
    uv run python config/manage.py createadminuser

# Open Django shell
shell:
    uv run python config/manage.py shell

# Run tests
test:
    uv run python config/manage.py test

# Run tests for a specific app
test-app app:
    uv run python config/manage.py test {{app}}

# Check for issues
check:
    uv run python config/manage.py check

# Show migrations status
showmigrations:
    uv run python config/manage.py showmigrations

# Docker commands
up:
    docker-compose up

up-build:
    docker-compose up --build

down:
    docker-compose down

logs:
    docker-compose logs -f
