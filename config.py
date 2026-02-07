from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict()

    debug: bool = True

    inference_device: str = "cpu"

    cors_allow_origins: list[str] = ["*"]

    telegram_bot_token: str = "Use https://t.me/BotFather for create bot token"  # noqa: S105
    chat_id: str = "Use https://t.me/userinfobot for get ids"


settings: Settings = Settings(_env_file=".env")
