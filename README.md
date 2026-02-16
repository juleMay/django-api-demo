# django-api-demo
## Description
A Full-stack application with a dockerized setup for easy development and deployment.

## Prerequisites
- Docker
- Docker Compose

## Getting Started

### Environment Variables
Before running the application, configure your database environment and api variables. See [database.env](database/README.md) and [webapi.env](src/services/webapi/README.md) for required variables.

### Running with Docker Compose
```bash
docker-compose up
```

The application will start with all necessary services (database, db manager, unit tests and api) configured automatically.

### Stopping the Application
```bash
docker-compose down
```

### Development Routes
- **Swagger UI**: http://localhost:8000/api/docs/
- **OpenAPI JSON**: http://localhost:8000/api/schema/
- **Redoc**: http://localhost:8000/api/redoc/
- **adminer**: http://localhost:8080

## Features
- Create, read, update, and delete records
- Persistent data storage with Docker volumes
- Isolated development environment

## Disclaimer
This project was developed as a learning exercise with assistance from AI tools and is intended for educational purposes only. No guarantees are made regarding the correctness, security, completeness or suitability of the code for any particular purpose, so use it at your own discretion. Finally, this disclaimer is not meant to replace or invalidate the license of the project. See [LICENSE](LICENSE).
