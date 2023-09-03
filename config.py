import torch

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict()

    debug: bool = True

    inference_device: str = "cuda" if torch.cuda.is_available() else "cpu"

    cors_allow_origins: str = "[*]"

    telegram_bot_token: str = "Use https://t.me/BotFather for create bot token"
    chat_id: str = "Use https://t.me/userinfobot for get ids"


settings: Settings = Settings(_env_file=".env")
