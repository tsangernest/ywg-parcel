from fastapi import APIRouter

from api.routes import utils


api_router = APIRouter()
api_router.include_router(utils.router)

