from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from factory.bot import _setup_main_menu
from handlers.routes import router
from middlewares.database import DatabaseMiddleware
from middlewares.services import UserServiceMiddleware
from storage.postgres.driver import db_driver


def _setup_outer_middlewares(dispatcher: Dispatcher) -> None:
    dispatcher.update.outer_middleware(DatabaseMiddleware(session_pool=db_driver.session_factory))
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
