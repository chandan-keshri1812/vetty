# Vetty Market API

This is a Flask-based REST API for fetching Vetty market updates from the CoinGecko API.

## Features

- List all coins including coin id.
- List coin categories.
- List specific coins according to id or category.
- Pagination support.
- Authentication.
- Swagger documentation.
- Unit tests.
- Docker support.
- Health check and version information.


## Authentication

The API is protected with API Key Authentication. To access the endpoints, include the `X-API-KEY` header in your requests.

Example:
```bash
curl -H "X-API-KEY: supersecretkey" http://localhost:5000/crypto/coins


## Installation

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the application: `python run.py`.

## Docker

Build and run the Docker container:

```bash
docker-compose up --build