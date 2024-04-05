from aiogram import Bot
from aiogram.types import BotCommand

from settings import config

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
    return Bot(token=config.telegram_bot.TELEGRAM_BOT_TOKEN.get_secret_value(), parse_mode="HTML")
