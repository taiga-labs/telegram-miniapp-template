from pydantic import BaseModel


class AuthModel(BaseModel):
    data_check_string: str
    hash: str
