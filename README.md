# visitors-observer

Collect and processed incoming events with face on photo

Install from container:
    ```
    docker compose up --build
    ```

Install from container and run as daemon:
    ```
    docker compose up --build -d
    ```

# Autodocumentation swagger:

    localhost:5555/docs
    localhost:5555/redoc


Install for local development:
    ```
    git clone https://github.com/yastcher/visitors-observer.git
    ```

Install requirements:
    ```
    pip install --no-cache-dir -r  requirements.txt
    pip install --no-cache-dir -r  requirements-torch.txt
    pip install --no-cache-dir -r  requirements-compile.txt
    ```

For local development create local_settings.py and overload envs:
    ```
    TELEGRAM_BOT_TOKEN=
    CHAT_ID =
    ```
https://core.telegram.org/bots/api#authorizing-your-bot
https://core.telegram.org/bots/features#botfather
https://t.me/userinfobot = your chat_id

Start app:
    ```
    uvicorn main:app --host 127.0.0.1 --port 5555
    ```

Autodocumentation (swagger):
    ```
    http://127.0.0.1:5555/docs
    http://127.0.0.1:5555/redoc
    ```

Run tests (pytest):
    ```
    pytest
    ```
