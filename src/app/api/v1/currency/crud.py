from datetime import datetime, UTC

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Currency
from .schemas import CurrencyExchangeSchema, CurrencySchema, CurrencyCreate


async def get_currencies(session: AsyncSession) -> list[Currency]:
    stmt = select(Currency).order_by(Currency.id)
    result: Result = await session.execute(stmt)
    currencies = result.scalars().all()
    return list(currencies)


async def get_currency(session: AsyncSession, currency_id: int) -> Currency | None:
    return await session.get(Currency, currency_id)


async def create_currency(
    session: AsyncSession, currency_in: CurrencyCreate
) -> Currency:
    currency = Currency(**currency_in.model_dump())
    session.add(currency)
    await session.commit()
    await session.refresh(currency)
    return currency


async def create_curency(currency: CurrencySchema):
    pass


# def update_exchange_rates(db: Session):
#     rates = get_current_exchange_rates()  # Функция для запроса курсов из внешнего API
#
#     for currency_data in rates:
#         db_currency = db.query(Currency).filter(Currency.code == currency_data["code"]).first()
#
#         if db_currency:
#             db_currency.rate = currency_data["rate"]
#         else:
#             db_currency = Currency(**currency_data)
#             db.add(db_currency)
#
#     db.commit()
#
#
# def exchange_currency(currency_exchange: CurrencyExchangeSchema):
#
#     CurrencyHelper.update_exchange_rates(db)
#     return {"message": "Exchange rates updated successfully"}
