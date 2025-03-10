from typing import Final

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup

from config import settings
from services.users import UsersService
from schemas.user import UserSchema

router: Final[Router] = Router(name=__name__)


@router.message(CommandStart())
async def start_command(message: Message, users_service: UsersService):
    text = f"🏠 Welcome back, {message.from_user.first_name}!"

    if not await users_service.is_exists(telegram_id=message.from_user.id):
        user = UserSchema(telegram_id=message.from_user.id)
        await users_service.add_user(user=user)
        text = f"🖐 Salute, {message.from_user.first_name}!"

    key_miniapp = InlineKeyboardButton(text='➡️ Tap to Open ⬅️',
                                       web_app=WebAppInfo(
                                           url=settings.mapp.build_mini_app_url()
                                       )
                                       )
    keyboard = [key_miniapp]
    await message.answer(
        text=text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[keyboard])
    )


@router.message(F.via_bot)
async def pong(message: Message):
    await message.answer(text="pong")
