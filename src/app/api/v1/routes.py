from fastapi import APIRouter, Depends
from pydantic import BaseModel
# from sqlalchemy.orm import Session
# from app.config import settings
# from app.services.currency_helper import CurrencyHelper
# from app.services.database import get_db

router = APIRouter()


class Status(BaseModel):
    status: str = 'ok'


@router.get("/")
async def status():
    return Status()


# @router.post("/update_exchange_rates")
# async def update_exchange_rates_route(api_key: str, db: Session = Depends(get_db)):
#     if api_key != settings.API_KEY_RATE:
#         return {"error": "Invalid API key"}
#
#     CurrencyHelper.update_exchange_rates(db)
#     return {"message": "Exchange rates updated successfully"}
