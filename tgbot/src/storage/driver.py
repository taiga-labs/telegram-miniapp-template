from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from src.storage import db_engine


def create_pool():
    return async_sessionmaker(db_engine,
                              class_=AsyncSession,
                              expire_on_commit=False)
