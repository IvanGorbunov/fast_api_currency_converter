from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=['Tests'])


class Status(BaseModel):
    status: str = 'ok'


@router.get("/")
async def status():
    return Status()
