# osquery-be

## Development

### Start caddy and API server (with Docker)

```sh
docker compose up --build
```

The server is accessible on https://osquery.localhost

### Start only API server (without Docker)

1. Copy `.env.example` to `.env`

```sh
cp .env.example .env
```

2. Uncomment the variables and set the desired values.

3. Install dependencies with poetry:

```sh
poetry install
```

This will create a virtual environment in the project's root directory (`.venv`) and then installs dependencies.

4. Run the API server:

```sh
poetry run uvicorn osquery_be.main:app --reload --host=0.0.0.0 --port=8008 --log-level=debug
```
