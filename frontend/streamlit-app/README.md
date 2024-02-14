# streamlit-app

## Development

#### Redis

Start redis server as it is needed to cache user's auth token (temporary measure, will be replaced later):

```sh
cd backend/redis
docker compose up
# optionally, if you want to run it on detached mode
docker compose up -d
```

#### `streamlit-app`

Make sure you have `poetry` installed on your system. Then install dependencies:

```sh
cd frontend/streamlit-app
poetry install
```

Start the Streamlit app:

```sh
poetry run streamlit run streamlit_app/dashboard.py
```

Alternatively, you can open streamlit-app in Dev Container as it's already been set up. But you need to install Dev Containers extension on VSCode first.

## To-Do

- [ ] Add docker compose file to start both redis and streamlit-app, we already have Dockerfile for streamlit-app.
