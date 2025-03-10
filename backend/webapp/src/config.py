from pydantic import SecretStr, BaseModel
from pydantic_settings import BaseSettings as _BaseSettings, SettingsConfigDict


class BaseSettings(_BaseSettings):
    model_config = SettingsConfigDict(extra="ignore",
                                      # env_file=".env",
                                      case_sensitive=False,
                                      env_nested_delimiter="__",
                                      env_prefix="APP_CONFIG__",
                                      env_file_encoding="utf-8"
                                      )


class TelegramBotSettings(BaseModel):
    TOKEN: SecretStr


class MiniAppSettings(BaseModel):
    PORT: int


class Settings(BaseSettings):
    bot: TelegramBotSettings
    mapp: MiniAppSettings


settings = Settings()
