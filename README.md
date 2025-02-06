# Bot cron job EmagicEyes

## Requirement

- Python 3.10

## Run dev

- install requirements

```sh
 pip install poetry
```

```sh
 poetry install --no-root
```

## Add file .env

```aiignore
DEBUG=true
REDIS_HOST=localhost
REDIS_PORT=6379
URL_API=http://127.0.0.1:8000
EMAIL_HOST=mail.rainscales.com.vn
EMAIL_HOST_PASSWORD=Support@12345
EMAIL_HOST_USER=support.emagiceyes@rainscales.com.vn
EMAIL_PORT=587
```

## Run celery

```sh
 celery -A app.gateway.celery_worker:celery_instance worker --beat --loglevel=info
```

## Run app

```sh
 uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Build docker compose

```sh
 docker compose up --build
```