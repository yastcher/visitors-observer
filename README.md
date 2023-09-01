# visitors-observer

Collect and processed incoming events with face on photo

## Rename .env.example to .env end fill :

    CHAT_ID=                (Use https://t.me/userinfobot for get ids)
    TELEGRAM_BOT_TOKEN=     (Use https://t.me/BotFather for create bot token)

## Install from container:

    ```
    docker compose up --build
    ```

## Install from container and run as daemon:

    ```
    docker compose up --build -d
    ```

## Autodocumentation swagger:

    ```
    localhost:5555/docs
    localhost:5555/redoc
    ```

## Install for local development:

    ```
    git clone https://github.com/yastcher/visitors-observer.git
    ```

## Install requirements:

    ```
    pip install --no-cache-dir -r  requirements.txt
    pip install --no-cache-dir -r  requirements-torch.txt
    pip install --no-cache-dir -r  requirements-compile.txt
    ```

## For local development rename .env.example to .env end overload envs:

    ```
    TELEGRAM_BOT_TOKEN=     (Use https://t.me/BotFather for create bot token)
    CHAT_ID=                (Use https://t.me/userinfobot for get ids)

    https://core.telegram.org/bots/api#authorizing-your-bot
    https://core.telegram.org/bots/features#botfather
    https://t.me/userinfobot = your chat_id
    ```

## Start app:

    ```
    uvicorn main:app --host 127.0.0.1 --port 5555
    ```

## Run tests (pytest):

    ```
    pytest -v
    ```
