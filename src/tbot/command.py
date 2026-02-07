from telegram import Bot

from src.config import settings

bot = Bot(token=settings.telegram_bot_token)
