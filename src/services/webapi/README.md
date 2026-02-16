# Django Web API Environment Variables

## Configuration Variables

The following environment variables are required to run the Django Web API:

| Category | Variable | Description |
|----------|----------|-------------|
| Security | `SECRET_KEY` | Django secret key |
| Hosting | `ALLOWED_HOSTS` | Comma-separated list of allowed hosts (e.g., '["localhost"]')|
| Logging | `DEBUG` | Django debug mode, for development only (true or false) |
| Database | `DB_HOST` | Database service host |
| Database | `DB_PORT` | Database service port |
| Database | `DB_NAME` | Database name |
| Database | `DB_USER` | Database user name |
| Database | `DB_PASSWORD` | Database user password |
| Database | `DB_HEALTH_CHECK` | If Database should be health checked (true or false) |

## Setup Instructions

1. Create a `.env` file in the current folder
2. Define each variable with appropriate values
3. Load variables in your `docker-compose.yml` using `env_file` section (example provided in root repository directory)
4. Never commit credentials to version control. Don't remove `.env` from the respective `.gitignore` 