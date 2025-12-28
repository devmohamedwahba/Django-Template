# Backend Template

A Django REST API backend template with Docker and PostgreSQL.

## Tech Stack

- Python 3.14
- Django 6.0
- Django REST Framework
- PostgreSQL 17
- UV (package manager)
- Docker

## Project Structure

```
├── config/                 # Django project
│   ├── config/             # Settings, URLs, WSGI/ASGI
│   ├── apps/               # Django applications
│   └── assets/             # Static and media files
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── justfile
```

## Using as Template

1. Clone and remove existing git history:
   ```bash
   cd my-project
   rm -rf .git
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. Configure environment variables in `config/.env`:
   ```env
   DJANGO_SECRET_KEY=your-secret-key
   DJANGO_SUPERUSER_EMAIL=admin@example.com
   DJANGO_SUPERUSER_PASSWORD=your-password

   POSTGRES_DB=mydatabase
   POSTGRES_USER=your-db-user
   POSTGRES_PASSWORD=your-db-password
   DB_HOST=db
   DB_PORT=5432
   ```

3. Build and run:
   ```bash
   docker-compose up --build
   ```

4. Access at `http://localhost:8000`

## Useful Commands

| Command | Description |
|---------|-------------|
| `just run` | Start development server |
| `just migrate` | Run database migrations |
| `just makemigrations` | Create new migrations |
| `just createapp <name>` | Create a new Django app |
| `just createadmin` | Create an admin user |
| `just shell` | Open Django shell |
| `just test` | Run tests |
| `just up` | Start Docker containers |
| `just up-build` | Build and start Docker |
| `just down` | Stop Docker containers |
| `just logs` | View Docker logs |

## Environment Variables

| Variable | Description |
|----------|-------------|
| `DJANGO_SECRET_KEY` | Django secret key |
| `DJANGO_SUPERUSER_EMAIL` | Admin user email |
| `DJANGO_SUPERUSER_PASSWORD` | Admin user password |
| `POSTGRES_DB` | Database name |
| `POSTGRES_USER` | Database user |
| `POSTGRES_PASSWORD` | Database password |
| `DB_HOST` | Database host |
| `DB_PORT` | Database port |

## Features

- Django 6.0 + Django REST Framework
- PostgreSQL 17 database
- Docker & Docker Compose setup
- UV package manager (fast & modern)
- Pre-commit hooks for code quality
- Actions to check the PRs
- Just commands for common tasks
- Custom User model (Flixable)
- Background Tasks
- Assets & template configurations
- Debugging Toolbar
