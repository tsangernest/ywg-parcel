from sqlalchemy import NullPool, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlmodel import SQLModel

from app.core.config import settings


engine: AsyncEngine = create_async_engine(
    url=str(settings.SQL_MARIADB_URI),
    echo=True,
    future=True,
    poolclass=NullPool,
)


async def init_db():
    async with engine.begin() as conn:
        print(f"\n{engine.engine=}")
        await conn.run_sync(SQLModel.metadata.create_all)
        try:
            await conn.execute(select(1))
            print(f"\n{engine.engine=}\n")
        except IntegrityError:
            pass


