from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config import settings
from .services.currency_helper import CurrencyHelper
from .schemas import CurrencyExchangeSchema

# from app.services.database import get_db

router = APIRouter(prefix='/currency', tags=['Currency'])


@router.post("/update_exchange_rates")
async def update_exchange_rates():
    await CurrencyHelper.update_exchange_rates()
    return {"message": "Exchange rates updated successfully"}


@router.get("/last_update_courses")
async def last_update_courses():
    await CurrencyHelper.last_update_courses()
    return {"message": "Exchange rates updated successfully"}


@router.post("/exchange_currency")
async def exchange_currency(currency_exchange: CurrencyExchangeSchema):

    await CurrencyHelper.exchange_currency(currency_exchange)
    return {"message": "Exchange rates successfully"}
