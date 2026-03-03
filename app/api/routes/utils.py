from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from sqlalchemy import text, select
from starlette.status import (
    HTTP_200_OK,
    HTTP_500_INTERNAL_SERVER_ERROR,
)


from app.api.deps import SessionDep


router = APIRouter(prefix="/utils", tags=["utils"])


@router.get(
    path="/health-check",
    response_class=HTMLResponse,
    responses={HTTP_200_OK: {"db_conn": "healthy!"}, HTTP_500_INTERNAL_SERVER_ERROR: {"db_conn": "definitely dead"}})
async def health_check(session: SessionDep):
    return {"ping": "pong!"}

