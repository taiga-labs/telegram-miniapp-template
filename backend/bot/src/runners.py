from __future__ import annotations

from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from bot_logger import bot_logger
from config import settings


async def polling_startup(bots: list[Bot]) -> None:
    for bot in bots:
        await bot.delete_webhook(drop_pending_updates=settings.bot.DROP_PENDING_UPDATES)
    if settings.bot.DROP_PENDING_UPDATES:
        bot_logger.info("Updates skipped successfully")


async def webhook_startup(dispatcher: Dispatcher, bot: Bot) -> None:
    webhook_url: str = settings.bot.build_webhook_url()
    if await bot.set_webhook(
            url=webhook_url,
            allowed_updates=dispatcher.resolve_used_update_types(),
            drop_pending_updates=settings.bot.DROP_PENDING_UPDATES,
            secret_token=settings.bot.WEBHOOK_SECRET.get_secret_value(),
    ):
        return bot_logger.info(f"Bot webhook successfully set on url {webhook_url}")
    return bot_logger.error(f"Failed to set main bot webhook on url {webhook_url}")


async def webhook_shutdown(bot: Bot) -> None:
    if not settings.bot.WEBHOOK_RESET:
        return
    if await bot.delete_webhook():
        bot_logger.info("Dropped main bot webhook.")
    else:
        bot_logger.error("Failed to drop main bot webhook.")
    await bot.session.close()


def run_polling(dispatcher: Dispatcher, bot: Bot) -> None:
    dispatcher.startup.register(polling_startup)
    return dispatcher.run_polling(bot)


def run_webhook(dispatcher: Dispatcher, bot: Bot) -> None:
    dispatcher.startup.register(webhook_startup)
    dispatcher.shutdown.register(webhook_shutdown)

    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dispatcher,
        bot=bot,
        secret_token=settings.bot.WEBHOOK_SECRET.get_secret_value(),
    )
    webhook_requests_handler.register(app, path=settings.wh.WEBHOOK_PATH)
    setup_application(app, dispatcher, bot=bot)
    web.run_app(
        app,
        host=settings.wh.WEBHOOK_HOST,
        port=settings.bot.WEBHOOK_PORT,
    )
