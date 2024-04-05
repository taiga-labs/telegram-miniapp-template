from socketio import AsyncServer

from src.web import web_logger


async def connect(sid, data):
    print('sockonnect')
    web_logger.info(f"connect | socket connection open | sid: {sid}")


async def disconnect(sid):
    web_logger.info(f"disconnect | socket connection closed | sid: {sid}")


def reg(sio: AsyncServer):
    sio.on("connect", connect)
    sio.on("disconnect", disconnect)
