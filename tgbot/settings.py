from pydantic import SecretStr, PostgresDsn, BaseModel
from pydantic_settings import BaseSettings as _BaseSettings, SettingsConfigDict


class BaseSettings(_BaseSettings):
    model_config = SettingsConfigDict(extra="ignore", env_file=".env", env_file_encoding="utf-8")


class PostgresSettings(BaseSettings):
    DATABASE_URL: PostgresDsn


class TelegramBotSettings(BaseSettings):
    TELEGRAM_BOT_TOKEN: SecretStr
    USE_WEBHOOK: bool
    WEBHOOK_RESET: bool
    WEBHOOK_BASE_URL: str
    WEBHOOK_PATH: str
    WEBHOOK_PORT: str
    WEBHOOK_HOST: str

    def build_webhook_url(self) -> str:
        return f"{self.WEBHOOK_BASE_URL}{self.WEBHOOK_PATH}"


class MiniAppSettings(BaseSettings):
    MINIAPP_HOST: str
    MINIAPP_PATH: str
    MINIAPP_PORT: int

    def build_mini_app_url(self) -> str:
        return f"https://{self.MINIAPP_HOST}/{self.MINIAPP_PATH}/"


class CommonSettings(BaseSettings):
    DROP_PENDING_UPDATES: bool


class AppConfig(BaseModel):
    postgres: PostgresSettings
    telegram_bot: TelegramBotSettings
    mini_app: MiniAppSettings
    common: CommonSettings


config = AppConfig(
    postgres=PostgresSettings(),
    telegram_bot=TelegramBotSettings(),
    mini_app=MiniAppSettings(),
    common=CommonSettings(),
)
