from fastapi import APIRouter
from fastapi import status
from sqlalchemy import text, select

from app.api.deps import SessionDep


router = APIRouter(prefix="/utils", tags=["utils"])


@router.get(path="/health/")
async def health_check(session: SessionDep) -> dict:
    return {status.HTTP_500_INTERNAL_SERVER_ERROR: "No db connection"}

