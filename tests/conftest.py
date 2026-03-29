import asyncio
from typing import AsyncGenerator

import pytest
from httpx import AsyncClient
from sqlalchemy import select

from app.api.deps import SessionDep
from app.core.db import init_db
from app.main import get_application


@pytest.fixture(scope="function")
async def session() -> AsyncGenerator[SessionDep, None]:
    """
    async for session in SessionDep: # because we have multiple session of multiple users
        await session.execute()
        await session.commit()
    """
    async for session in SessionDep:
        await session.execute(select(1))
        await session.commit()
        yield session


@pytest.fixture(scope="module")
def event_loop():
    yield asyncio.get_event_loop()


@pytest.fixture(scope="module")
async def app():
    """
    app = get_application()
    await init_db()
    yield app
    """
    app = get_application()
    await init_db()
    print(f"{app.host=}")
    yield app


@pytest.fixture(scope="module")
async def aclient(app) ->  AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(base_url="http://localhost:8000") as aclient:
        yield aclient

