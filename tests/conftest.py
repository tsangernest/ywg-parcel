import asyncio
import pytest

from httpx import AsyncClient
from typing import AsyncGenerator

from app.main import get_application
from app.core.db import init_db

@pytest.fixture(scope="function")
async def session():
    """
    async for session in get_session(): # because we have multiple session of multiple users
        await session.execute()
        await session.commit()
    """

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
    async with AsyncClient(base_url="http://0.0.0.0:8000") as aclient:
        yield aclient

