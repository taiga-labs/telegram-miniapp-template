from aiogram import Bot
from aiogram.client.default import DefaultBotProperties

from config import settings


def create_bot() -> Bot:
    return Bot(
        token=settings.bot.TOKEN.get_secret_value(),
        default=DefaultBotProperties(parse_mode="HTML"),
    )
