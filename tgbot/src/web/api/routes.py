import hmac
import hashlib
from urllib import parse

from aiogram import Bot, types
from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from starlette import status

from settings import config
from src.web.api import get_bot
from src.web.api.models import AuthModel

router = APIRouter()


@router.post("/auth")
async def auth(data: AuthModel):
    data_check_string = parse.unquote(data.data_check_string)

    secret_key = hmac.new(
        key="WebAppData".encode(),
        msg=config.telegram_bot.TELEGRAM_BOT_TOKEN.get_secret_value().encode(),
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
            detail=f"Authentication failed",
        )


@router.get("/ping")
async def ping(query_id: str, bot: Bot = Depends(get_bot)):
    result = types.InlineQueryResultArticle(
        id=query_id,
        title="pong",
        input_message_content=types.InputTextMessageContent(message_text=f"ping"),
    )
    await bot.answer_web_app_query(web_app_query_id=query_id, result=result)
