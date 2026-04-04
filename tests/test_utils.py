import pytest

from httpx import AsyncClient
from sqlalchemy import select
from starlette.status import HTTP_200_OK

from app.api.deps import SessionDep


@pytest.mark.anyio
async def test_health_web(aclient: AsyncClient):
    response = await aclient.get(url="/utils/health-web")
    assert HTTP_200_OK == response.status_code
    json_response = response.json()
    assert json_response == {"200": "FastAPI is okay!"}


@pytest.mark.anyio
async def test_health_db(aclient: AsyncClient, session: SessionDep):
    results = await session.execute(select(1))
    result = results.scalar_one_or_none()
    assert 1 == result

