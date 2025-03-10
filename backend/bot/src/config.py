from pydantic import SecretStr, PostgresDsn, BaseModel
from pydantic_settings import BaseSettings as _BaseSettings, SettingsConfigDict


class BaseSettings(_BaseSettings):
    model_config = SettingsConfigDict(extra="ignore",
                                      # env_file=".env",
                                      case_sensitive=False,
                                      env_nested_delimiter="__",
                                      env_prefix="APP_CONFIG__",
                                      env_file_encoding="utf-8"
                                      )


class PostgresSettings(BaseModel):
    URL: PostgresDsn
    ECHO: bool = False
    ECHO_POOL: bool = False
    POOL_SIZE: int = 5
    MAX_OVERFLOW: int = 10


class TelegramBotSettings(BaseModel):
    TOKEN: SecretStr
    USE_WEBHOOK: bool
    WEBHOOK_RESET: bool
    WEBHOOK_BASE_URL: str
    WEBHOOK_HOST: str
    WEBHOOK_PATH: str
    WEBHOOK_PORT: str
    WEBHOOK_SECRET: SecretStr
    DROP_PENDING_UPDATES: bool

    def build_webhook_url(self) -> str:
        return f"{self.WEBHOOK_BASE_URL}{self.WEBHOOK_PATH}"


class MiniAppSettings(BaseModel):
    HOST: str
    PATH: str

    def build_mini_app_url(self) -> str:
        return f"https://{self.HOST}/{self.PATH}/"


class Settings(BaseSettings):
    db: PostgresSettings
    bot: TelegramBotSettings
    mapp: MiniAppSettings


settings = Settings()
