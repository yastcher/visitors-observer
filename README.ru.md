# visitor-observer

Принимает фото через HTTP API, детектит лица (MTCNN) и отправляет результат в Telegram-бот.

[English documentation](README.md)

## Быстрый старт (uv)

```bash
cp .env.example .env
# Заполните TELEGRAM_BOT_TOKEN и CHAT_ID в .env

uv sync
uv run uvicorn src.app:app --host 127.0.0.1 --port 5555
```

## Docker

```bash
cp .env.example visitor_observer.env
# Заполните TELEGRAM_BOT_TOKEN и CHAT_ID в visitor_observer.env

docker compose up --build
```

## Развёртывание на сервере

```bash
sudo apt update && sudo apt upgrade
sudo apt install -y pkg-config curl

# Установка uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Клонировать репозиторий
git clone https://github.com/yastcher/visitors-observer.git
cd visitors-observer

cp .env.example .env
# Заполните TELEGRAM_BOT_TOKEN и CHAT_ID в .env

uv sync
uv run uvicorn src.app:app --host 0.0.0.0 --port 5555
```

## API

**POST /api/check_photo** — загрузить фото для проверки лиц.

```bash
curl -X POST http://localhost:5555/api/check_photo \
  -F "file=@photo.jpg"
```

Ответ: `{"message": "1 faces founded", "data": "...", "status": 0}`

Swagger: [localhost:5555/docs](http://localhost:5555/docs)

## Настройка (.env)

| Переменная | Описание | По умолчанию |
|---|---|---|
| `TELEGRAM_BOT_TOKEN` | Токен бота от [@BotFather](https://t.me/BotFather) | — |
| `CHAT_ID` | ID чата от [@userinfobot](https://t.me/userinfobot) | — |
| `INFERENCE_DEVICE` | Устройство для ML (`cpu` / `cuda`) | `cpu` |
| `DEBUG` | Включить Swagger и отладочные логи | `true` |
| `CORS_ALLOW_ORIGINS` | JSON-список разрешённых origin | `["*"]` |

## Тесты

```bash
uv sync --group dev
uv run pytest -v
```
