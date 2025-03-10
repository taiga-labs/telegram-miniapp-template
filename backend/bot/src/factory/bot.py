from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.types import BotCommand

from config import settings

MENU_COMMANDS: dict[str, str] = {
    '/start': 'kickstart',
}


async def _setup_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(
            command=command,
            description=description
        ) for command, description in MENU_COMMANDS.items()
    ]
    await bot.set_my_commands(main_menu_commands)


def create_bot() -> Bot:
    return Bot(
        token=settings.bot.TOKEN.get_secret_value(),
        default=DefaultBotProperties(parse_mode="HTML"),
    )
