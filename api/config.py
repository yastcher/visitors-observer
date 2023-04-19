import json
import logging
import os
import sys


DEBUG = bool(int(os.environ.get("DEBUG", True)))


KWARGS_OPEN_API = {
    "title": "Back", "docs_url": "/docs", "redoc_url": "/redoc",
} if DEBUG else {"docs_url": None, "redoc_url": None}


LOG_SAVE_TO_FILE = bool(int(os.environ.get("LOG_SAVE_TO_FILE", False)))
console_out = logging.StreamHandler(stream=sys.stdout)
if LOG_SAVE_TO_FILE:
    log_file = os.path.join(os.path.abspath(os.getcwd()), "..", "debug.log")
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
