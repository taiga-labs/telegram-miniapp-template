from sqlalchemy.ext.asyncio import AsyncSession

from storage.postgres.dao.users import UsersDAO
from schemas.user import UserSchema


class UsersService:
    def __init__(self, db_session: AsyncSession):
        self.session = db_session
        self.users_dao = UsersDAO(session=db_session)

    async def is_exists(self, telegram_id: int):
        data = await self.users_dao.get_by_params(telegram_id=telegram_id)
        return True if data else False

    async def add_user(self, user: UserSchema):
        await self.users_dao.add(user.model_dump())
        await self.session.commit()
