import socketio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

fastapp = FastAPI()

origins = ["*"]
fastapp.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"),
    allow_headers=["*"],
)

sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*")
socket_app = socketio.ASGIApp(socketio_server=sio)
