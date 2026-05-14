from fastapi import APIRouter

from app.api.route import utils


api_router = APIRouter()
api_router.include_router(utils.router)

