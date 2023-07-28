# visitors-observer

Collect and processed incoming events with face on photo 


# Autodocumentation swagger:

ip_address:port/docs
ip_address:port/redoc


Install for local development:

    ```
    git clone https://github.com/yastcher/visitors-observer.git
    ```

Install poetry:

    ```
    pip install poetry
    ```

Run or install virtual environments:

    ```
    poetry env
    ```

Install requirements:

    ```
    poetry install
    ```

For local development create local_settings.py and overload envs:
    ```
    TELEGRAM_BOT_TOKEN=
    ```
https://core.telegram.org/bots/api#authorizing-your-bot
https://core.telegram.org/bots/features#botfather

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
