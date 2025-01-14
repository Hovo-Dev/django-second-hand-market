# Second-Hand Clothes Marketplace API

#### This repository contains a RESTful API for a second-hand clothes marketplace, built with Python and Django. The API allows users to publish, update, and manage their garments, as well as authenticate and interact with the platform.

## Features

- **Accounts App**: Handles user authentication and profile management, including login, logout, registration, and retrieving user details (e.g., ID, full name, address).
- **Garment App**: Manages garment data, including type (e.g., shirt, pants), description, size, price, and associated publisher. Provides CRUD operations for authenticated users.
- **JWT Authentication**: Securely authenticates users by generating, validating, and refreshing JSON Web Tokens (JWTs) to manage session-based interactions.
- **Writing Tests**: Comprehensive unit and integration tests are included to ensure functionality and prevent regressions across the API.
- **Security**: Implements strict access controls, allowing users to manage only their garments and sensitive information.

## Run Locally

Clone the project

```bash
  git clone <repository-url>
```

Go to the project directory

```bash
  cd <repository-folder>
```

Create a `.env` file

```bash
  cp .env.example .env
```

Update the `.env` file with the required environment variables.

Install dependencies

```bash
  pip install -r requirements.txt
```

Run database migrations

```bash
  python manage.py makemigrations
  python manage.py migrate
```

Start the development server

```bash
  python manage.py runserver
```

Access the application

Open your browser and navigate to `http://127.0.0.1:8000`.

## Running Tests

Run tests to ensure the application functions as expected.

```bash
  python manage.py test
```

## Running with Makefile

To simplify running migrations, builds and starting the application, use the provided `Makefile`:

1. Run database migrations:
   ```bash
   make build
   ```

2. Build and start the containers:
   ```bash
   make migrate
   ```

3. Run the application:
   ```bash
   make test
   ```

## API Endpoints

### Garment Endpoints

- **`GET /api/garment/list/`**: Retrieve a list of all garments (searchable via query parameters).

- **`GET /api/garment/<int:id>/`**: Retrieve details of a specific garment.

- **`POST /api/garment/create/`**: Publish a new garment.

- **`PATCH /api/garment/<int:id>/update/`**: Update an existing garment.

- **`DELETE /api/garment/<int:id>/delete/`**: Unpublish a garment (only by the owner).
    
### Authentication Endpoints

- **`POST api/accounts/login/`**: Authenticate the user and return a JWT token. 
- **`POST api/accounts/logout/`**: Log the user out by invalidating their JWT token. 
- **`POST api/accounts/refresh-token/`**: Refresh the JWT token for the authenticated user. 
- **`POST api/accounts/register/`**: Register a new user account. 
- **`GET api/accounts/me/`**: Retrieve the authenticated user's profile information.
 
## Project Structure and Apps

- `garment/`: App containing models, views, and serializers for the marketplace.
- `accounts/`: App containing the custom user model and authentication logic.
- `Dockerfile`: Docker image setup.
- `docker-compose.yml`: Multi-container orchestration.

## Contact

For any questions or suggestions, please contact me at [hovhannes.baghdasaryan.03@gmail.com](mailto:hovhannes.baghdasaryan.03@gmail.com)
