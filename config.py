import json
import logging
import os
import sys


DEBUG = bool(int(os.getenv("DEBUG", True)))


KWARGS_OPEN_API = {
    "title": "Visitor observer", "docs_url": "/docs", "redoc_url": "/redoc",
} if DEBUG else {"docs_url": None, "redoc_url": None}


LOG_SAVE_TO_FILE = bool(int(os.getenv("LOG_SAVE_TO_FILE", False)))
console_out = logging.StreamHandler(stream=sys.stdout)
if LOG_SAVE_TO_FILE:
    log_file = os.path.join(os.path.abspath(os.getcwd()), "log", "debug.log")
    file_log = logging.FileHandler(log_file)
    handlers = (file_log, console_out, )
else:
    handlers = (console_out, )

LOGGING = {
    "handlers": handlers,
    "format": "[%(asctime)s: %(levelname)s] %(message)s",
    "level": logging.DEBUG if DEBUG else logging.INFO,
    "datefmt": "%Y-%m-%d %H:%M:%S",
}
logging.basicConfig(**LOGGING)


CORS_ALLOW_ORIGINS = json.dumps(
    os.getenv("CORS_ALLOW_ORIGINS", "[*]")
)


TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "Use https://t.me/BotFather for create bot token")
CHAT_ID = os.getenv("CHAT_ID", "Use https://t.me/userinfobot for get ids")


try:
    from local_settings import *
except ImportError:
    pass
