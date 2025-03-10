import uvicorn

from app import fastapp, socket_app, sio
from config import settings
from api.events import reg
from api.routes import router

fastapp.mount("/socket.io", socket_app)
fastapp.include_router(router=router)

reg(sio=sio)

uvicorn.run(
    app=fastapp,
    host="0.0.0.0",
    port=settings.mapp.PORT,
    proxy_headers=True,
    forwarded_allow_ips="*",
)
