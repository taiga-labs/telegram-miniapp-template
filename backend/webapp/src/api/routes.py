import hmac
import hashlib
from urllib import parse

from aiogram import types
from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from starlette import status

from api import create_bot
from api.schemas import AuthSchema
from config import settings

router = APIRouter()


@router.post("/auth")
async def auth(data: AuthSchema):
    data_check_string = parse.unquote(data.data_check_string)

    secret_key = hmac.new(
        key="WebAppData".encode(),
        msg=settings.bot.TOKEN.get_secret_value().encode(),
        digestmod=hashlib.sha256,
    )

    hash_check = hmac.new(
        key=secret_key.digest(),
        msg=data_check_string.encode(),
        digestmod=hashlib.sha256,
    )

    if hash_check.hexdigest() != data.hash:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Authentication failed",
        )


@router.get("/ping")
async def ping(query_id: str):
    bot = create_bot()
    result = types.InlineQueryResultArticle(
        id=query_id,
        title="pong",
        input_message_content=types.InputTextMessageContent(message_text="ping"),
    )
    await bot.answer_web_app_query(web_app_query_id=query_id, result=result)
