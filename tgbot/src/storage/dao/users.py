from sqlalchemy.ext.asyncio import AsyncSession

from src.storage.dao.base import BaseDAO
from src.storage.models import User


class UsersDAO(BaseDAO):
    def __init__(self, session: AsyncSession, model=User):
        super().__init__(model, session)
