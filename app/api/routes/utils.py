from fastapi import APIRouter
from fastapi import status
from sqlalchemy import text, select

from app.api.deps import SessionDep


router = APIRouter(prefix="/utils", tags=["utils"])


@router.get(path="/health-web", response_model=None)
async def health_web_check() -> dict:
    return {status.HTTP_200_OK: "FastAPI is okay!"}


@router.get(path="/health-db", response_model=None)
async def health_db_check(session: SessionDep) -> dict:
    return {status.HTTP_500_INTERNAL_SERVER_ERROR: "No database detected?"}

