import logging

from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.models import db_helper
from .services.currency_helper import CurrencyHelper
from .schemas import (
    CurrencyExchangeSchema,
    DynamicCurrencyResponseSchema,
    CurrencyExchangeResponseSchema,
)


logging.basicConfig(
    filename=settings.LOG_FILE,
    level=settings.LOGGING_LEVEL,
    format="%(asctime)s [%(levelname)s]: %(message)s",
)
LOG = logging.getLogger(__name__)


router = APIRouter(tags=["Currencies"])


@router.post("/update_exchange_rates/")
async def update_exchange_rates(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    message = await CurrencyHelper.update_exchange_rates(session=session)
    if not message:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Couldn't get any data.",
        )
    return {"message": message}


@router.get("/last_update_dates", response_model=DynamicCurrencyResponseSchema)
async def last_update_courses(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    data = await CurrencyHelper.last_update_dates(session=session)
    if not data:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Couldn't get any data.",
        )
    json_data = {"data": data}
    return JSONResponse(content=json_data)


@router.post("/exchange_currency", response_model=CurrencyExchangeResponseSchema)
async def exchange_currency(
    request: CurrencyExchangeSchema,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    if request.from_currency == request.to_currency:
        raise HTTPException(status_code=400, detail="Invalid currency codes")
    if request.amount == 0:
        raise HTTPException(status_code=400, detail="Invalid amount")

    try:
        exchanged_amount = await CurrencyHelper.exchange_currency(
            session=session,
            from_currency=request.from_currency,
            to_currency=request.to_currency,
            amount=request.amount,
        )
    except HTTPException as e:
        raise e

    response_data = {"currency": request.to_currency, "amount": exchanged_amount}
    return JSONResponse(content=response_data)
