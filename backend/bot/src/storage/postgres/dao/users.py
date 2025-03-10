from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseDAO
from storage.postgres.models import User


class UsersDAO(BaseDAO):
    def __init__(self, session: AsyncSession, model=User):
        super().__init__(model, session)

    # fill this class with custom methods
