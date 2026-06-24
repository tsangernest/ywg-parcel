from fastapi import APIRouter
from starlette.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR


router = APIRouter()


@router.post(path="/ask", response_model=None)
async def query_ollama() -> dict:
    return {HTTP_500_INTERNAL_SERVER_ERROR: "yikes!"}

