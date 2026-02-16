# PostgreSQL Environment Variables

## Configuration Variables

The following environment variables are used to configure the PostgreSQL service:

| Variable | Purpose |
|----------|---------|
| `POSTGRES_DB` | Name of the database to create on initialization |
| `POSTGRES_USER` | Username for database access |
| `POSTGRES_PASSWORD` | Password for the database user |

## Setup Instructions

1. Create a `.env` file in the current folder
2. Define each variable with appropriate values
3. Load variables in your `docker-compose.yml` using `env_file` section (example provided in root repository directory)
4. Never commit credentials to version control. Don't remove `.env` from the respective `.gitignore`