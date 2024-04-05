from pydantic import BaseModel


class UserModel(BaseModel):
    telegram_id: int
