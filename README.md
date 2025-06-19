# Flask MongoDB User Management API

This is a Flask application designed for basic user management (CRUD operations) via a REST API, backed by a MongoDB database. It's fully containerized using Docker for easy setup and deployment.

## Requirements

* **Docker Desktop** (includes Docker Engine and Docker Compose)

## Setup and Run

1.  **Clone the repository:**

    git clone <your-repo-link>
    cd flask_mongo_crud

2.  **Build and run the Docker containers:**
    This command will build your Flask application's Docker image and start both the Flask and MongoDB containers.

    docker-compose up --build

    The application will be accessible at `http://localhost:5000`.

## API Endpoints (Using Postman)

Once the containers are running, you can test the API using Postman or a similar tool.

### User Resource

**Base URL:** `http://localhost:5000/users`

1.  **GET /users**
    * **Description:** Returns a list of all users.
    * **Method:** `GET`
    * **Example Response:**
        [
            {
                "id": "60c72b1f9c1e7a001c8e4d1a",
                "name": "John Doe",
                "email": "john.doe@example.com"
            }
        ]

2.  **GET /users/<id>**
    * **Description:** Returns the user with the specified ID.
    * **Method:** `GET`
    * **Example URL:** `http://localhost:5000/users/60c72b1f9c1e7a001c8e4d1a`
    * **Example Response:**
        {
            "id": "60c72b1f9c1e7a001c8e4d1a",
            "name": "John Doe",
            "email": "john.doe@example.com"
        }

3.  **POST /users**
    * **Description:** Creates a new user with the specified data.
    * **Method:** `POST`
    * **Headers:** `Content-Type: application/json`
    * **Request Body (JSON):**
        {
            "name": "Jane Smith",
            "email": "jane.smith@example.com",
            "password": "securepassword123"
        }
    * **Example Response (201 Created):**
        ```json
        {
            "id": "60c72b1f9c1e7a001c8e4d1b",
            "name": "Jane Smith",
            "email": "jane.smith@example.com"
        }

4.  **PUT /users/<id>**
    * **Description:** Updates the user with the specified ID with new data.
    * **Method:** `PUT`
    * **Example URL:** `http://localhost:5000/users/60c72b1f9c1e7a001c8e4d1a`
    * **Headers:** `Content-Type: application/json`
    * **Request Body (JSON):**
        {
            "name": "Johnathan Doe",
            "email": "johnathan.doe@newemail.com"
        }
    * **Example Response:**
        {
            "id": "60c72b1f9c1e7a001c8e4d1a",
            "name": "Johnathan Doe",
            "email": "johnathan.doe@newemail.com"
        }

5.  **DELETE /users/<id>**
    * **Description:** Deletes the user with the specified ID.
    * **Method:** `DELETE`
    * **Example URL:** `http://localhost:5000/users/60c72b1f9c1e7a001c8e4d1a`
    * **Example Response (204 No Content):**

## Stopping the Application

To stop the Docker containers, press `Ctrl+C` in your terminal where `docker-compose up` is running.
To stop and remove the containers, networks, and volumes created by `up`, run:

docker-compose down -v