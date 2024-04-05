import uvicorn

from settings import config
from src.web import fastapp, socket_app, sio
from src.web.api.events import reg
from src.web.api.routes import router

fastapp.mount("/socket.io", socket_app)
fastapp.include_router(router=router)

reg(sio=sio)

uvicorn.run(
    app=fastapp,
    host="0.0.0.0",
    port=config.mini_app.MINIAPP_PORT,
    proxy_headers=True,
    forwarded_allow_ips="*",
)
