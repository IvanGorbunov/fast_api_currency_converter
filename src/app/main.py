"""
Main entry point
"""

from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

# from app.api.v1.api import api_router
from app.api.v1 import router as router_v1
from app.config import settings
from app.models import Base, db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan,
)

# app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(router_v1, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host=settings.HOST, port=settings.PORT)
