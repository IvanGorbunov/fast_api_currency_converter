from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from app.config import settings
from . import crud
from app.models import db_helper
from .services.currency_helper import CurrencyHelper
from .schemas import CurrencyExchangeSchema, CurrencyCreate, Currency

# from app.services.database import get_db

router = APIRouter(tags=["Currencies"])


@router.get("/", response_model=list[Currency])
async def get_currencies(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_currencies(session=session)


@router.post("/", response_model=Currency)
async def create_currency(
    currency_in: CurrencyCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.create_currency(session=session, currency_in=currency_in)


@router.get("/{currency_id}/", response_model=Currency)
async def get_currency(
    currency_id: int, session: AsyncSession = Depends(db_helper.session_dependency)
):
    currency = await crud.get_currency(session=session, currency_id=currency_id)
    if currency:
        return currency

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Currency {currency_id} not found.",
    )


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
