from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.bot.factory.bot import _setup_main_menu
from src.bot.handlers.routes import router
from src.bot.middlewares.database import DatabaseMiddleware
from src.bot.middlewares.services import UserServiceMiddleware
from src.storage.driver import create_pool


def _setup_outer_middlewares(dispatcher: Dispatcher) -> None:
    db_session_pool = create_pool()
    dispatcher.update.outer_middleware(DatabaseMiddleware(session_pool=db_session_pool))
    dispatcher.update.outer_middleware(UserServiceMiddleware())


def create_dispatcher() -> Dispatcher:
    dispatcher: Dispatcher = Dispatcher(
        name="main_dispatcher",
        storage=MemoryStorage(),  # TODO migrate to redis
    )
    dispatcher.startup.register(_setup_main_menu)
    dispatcher.include_routers(router)

    _setup_outer_middlewares(dispatcher=dispatcher)
    return dispatcher
