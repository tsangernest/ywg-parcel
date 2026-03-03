from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy import text, select

from app.api.deps import SessionDep


router = APIRouter(prefix="/utils", tags=["utils"])


@router.get(path="/health/")
async def health_check(session: SessionDep):
    return JSONResponse(
        status_code=500,
        content={"message": "yikes, probably no db connected"},
    )

