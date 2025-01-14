# Makefile for Django Project with Docker Compose

.PHONY: build migrate test clean

# Build the Docker containers
build:
	docker compose up --build

# Run database migrations
migrate:
	docker compose exec web python manage.py makemigrations
	docker compose exec web python manage.py migrate

# Run tests
 test:
	docker compose exec web python manage.py test  -v 2

# Clean up unused Docker resources
clean:
	docker compose down -v
