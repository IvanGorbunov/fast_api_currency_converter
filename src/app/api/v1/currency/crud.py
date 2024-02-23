import logging

from sqlalchemy import select, func
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import (
    CurrencyRate,
)
from app.config import settings
from .schemas import (
    CurrencyCreateCreate,
)


logging.basicConfig(
    filename=settings.LOG_FILE,
    level=settings.LOGGING_LEVEL,
    format="%(asctime)s [%(levelname)s]: %(message)s",
)
LOG = logging.getLogger(__name__)


async def get_exchange_rate(
    session: AsyncSession,
    currency_code: str,
) -> float | None:

    # TODO: refactor it
    stmt = (
        select(CurrencyRate.rate)
        .where(CurrencyRate.code == currency_code)
        .order_by(CurrencyRate.updated_at.desc())
    )

    result: Result = await session.execute(stmt)
    rate = result.scalars().first()
    return rate


async def create_currency_rate(
    session: AsyncSession,
    rates_in: CurrencyCreateCreate,
) -> CurrencyRate:
    rates = CurrencyRate(**rates_in.model_dump())
    session.add(rates)
    await session.commit()
    await session.refresh(rates)
    return rates


async def last_update_dates(
    session: AsyncSession,
) -> list | None:
    stmt = (
        select(CurrencyRate.code, func.max(CurrencyRate.updated_at).label("max_date"))
        .group_by(CurrencyRate.code)
        .order_by(func.max(CurrencyRate.updated_at).desc())
    )
    result: Result = await session.execute(stmt)
    dates = list(result.all())
    return dates
