from sqlalchemy import NullPool, text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlmodel import SQLModel

from app.core.config import settings


engine: AsyncEngine = create_async_engine(
    url=str(settings.SQLALCHEMY_DATABASE_URI),
    echo=True,
    future=True,
    poolclass=NullPool,
)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
        try:
            await conn.execute(text("SELECT 1"))
        except IntegrityError:
            pass


