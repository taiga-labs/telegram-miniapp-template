from __future__ import annotations

from aiogram import Bot, Dispatcher

from src.bot import logger
from settings import config


async def polling_startup(bots: list[Bot]) -> None:
    for bot in bots:
        await bot.delete_webhook(drop_pending_updates=config.common.DROP_PENDING_UPDATES)
    if config.common.DROP_PENDING_UPDATES:
        logger.info("Updates skipped successfully")


async def webhook_startup(dispatcher: Dispatcher, bot: Bot) -> None:
    webhook_url: str = config.telegram_bot.build_webhook_url()
    if await bot.set_webhook(
        url=webhook_url,
        allowed_updates=dispatcher.resolve_used_update_types(),
        drop_pending_updates=config.common.DROP_PENDING_UPDATES,
    ):
        return logger.info(f"Bot webhook successfully set on url {webhook_url}")
    return logger.error(f"Failed to set main bot webhook on url {webhook_url}")


async def webhook_shutdown(bot: Bot) -> None:
    if not config.telegram_bot.WEBHOOK_RESET:
        return
    if await bot.delete_webhook():
        logger.info("Dropped main bot webhook.")
    else:
        logger.error("Failed to drop main bot webhook.")
    await bot.session.close()


def run_polling(dispatcher: Dispatcher, bot: Bot) -> None:
    dispatcher.startup.register(polling_startup)
    return dispatcher.run_polling(bot)


def run_webhook(dispatcher: Dispatcher) -> None:
    dispatcher.startup.register(webhook_startup)
    dispatcher.shutdown.register(webhook_shutdown)
