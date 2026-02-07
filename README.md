# visitor-observer

Accepts photos via HTTP API, detects faces (MTCNN) and sends the result to a Telegram bot.

[Документация на русском](README.ru.md)

## Quick start (uv)

```bash
cp .env.example .env
# Fill in TELEGRAM_BOT_TOKEN and CHAT_ID in .env

uv sync
uv run uvicorn src.app:app --host 127.0.0.1 --port 5555
```

## Docker

```bash
cp .env.example visitor_observer.env
# Fill in TELEGRAM_BOT_TOKEN and CHAT_ID in visitor_observer.env

docker compose up --build
```

## Deploy to server

```bash
sudo apt update && sudo apt upgrade
sudo apt install -y pkg-config curl

# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone repo
git clone https://github.com/yastcher/visitors-observer.git
cd visitors-observer

cp .env.example .env
# Fill in TELEGRAM_BOT_TOKEN and CHAT_ID in .env

uv sync
uv run uvicorn src.app:app --host 0.0.0.0 --port 5555
```

## API

**POST /api/check_photo** — upload a photo to check for faces.

```bash
curl -X POST http://localhost:5555/api/check_photo \
  -F "file=@photo.jpg"
```

Response: `{"message": "1 faces founded", "data": "...", "status": 0}`

Swagger: [localhost:5555/docs](http://localhost:5555/docs)

## Configuration (.env)

| Variable | Description | Default |
|---|---|---|
| `TELEGRAM_BOT_TOKEN` | Bot token from [@BotFather](https://t.me/BotFather) | — |
| `CHAT_ID` | Chat ID from [@userinfobot](https://t.me/userinfobot) | — |
| `INFERENCE_DEVICE` | ML device (`cpu` / `cuda`) | `cpu` |
| `DEBUG` | Enable Swagger and debug logs | `true` |
| `CORS_ALLOW_ORIGINS` | JSON list of origins | `["*"]` |

## Tests

```bash
uv sync --group dev
uv run pytest -v
```
