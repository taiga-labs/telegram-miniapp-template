from aiogram import Bot, Dispatcher

from settings import config
from src.bot.factory.bot import create_bot
from src.bot.factory.dispatcher import create_dispatcher
from src.bot.runners import run_polling, run_webhook

bot: Bot = create_bot()
dispatcher: Dispatcher = create_dispatcher()
if config.telegram_bot.USE_WEBHOOK:
    run_webhook(dispatcher=dispatcher)
run_polling(dispatcher=dispatcher, bot=bot)
