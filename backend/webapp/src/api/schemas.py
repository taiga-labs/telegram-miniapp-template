from pydantic import BaseModel


class AuthSchema(BaseModel):
    data_check_string: str
    hash: str
