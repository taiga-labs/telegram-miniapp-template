from aiogram import Bot, Dispatcher

from factory.bot import create_bot
from factory.dispatcher import create_dispatcher
from runners import run_webhook, run_polling
from config import settings

bot: Bot = create_bot()
dispatcher: Dispatcher = create_dispatcher()
if settings.bot.USE_WEBHOOK:
    run_webhook(dispatcher=dispatcher, bot=bot)
run_polling(dispatcher=dispatcher, bot=bot)
