from fastapi import FastAPI

from app.api.main import api_router
from app.core.db import init_db


async def on_startup():
    await init_db()


def get_application() -> FastAPI:
    application = FastAPI()
    application.add_event_handler("startup", on_startup)
    application.include_router(api_router)
    return application


app = get_application()


