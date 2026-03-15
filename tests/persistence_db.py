from httpx import AsyncClient
import pytest




@pytest.mark.asyncio.fixture(scope="function")
async def client(c: AsyncClient) ->  AsyncClient:
    return c

