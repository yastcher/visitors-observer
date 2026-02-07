from telegram import Bot

from config import settings

bot = Bot(token=settings.telegram_bot_token)
