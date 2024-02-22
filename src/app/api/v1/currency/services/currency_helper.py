import logging

from sqlalchemy.ext.asyncio import AsyncSession

from app.api.v1.currency.crud import (
    create_currency_rate,
    last_update_dates,
    get_exchange_rate,
)
from app.api.v1.currency.schemas import CurrencyCreateCreate
from app.api.v1.currency.services.external_api import ExchangeRatesAPIHelper
from app.config import settings

logging.basicConfig(
    filename=settings.LOG_FILE,
    level=settings.LOGGING_LEVEL,
    format="%(asctime)s [%(levelname)s]: %(message)s",
)
LOG = logging.getLogger(__name__)


class CurrencyHelper:
    """
    Helper class for work with currencies
    """

    @staticmethod
    async def update_exchange_rates(session: AsyncSession) -> str | None:
        # check permissions
        remaining_quota = await ExchangeRatesAPIHelper.get_remaining_quota()
        if not remaining_quota:
            LOG.error("No remaining")
            return

        # get and save currencies
        currencies = await ExchangeRatesAPIHelper.get_currencies()
        if not currencies:
            LOG.error("Couldn't get any currency.")
            return

        # get and save rates
        rates = await ExchangeRatesAPIHelper.get_current_exchange_rates()
        if not rates:
            LOG.error("Couldn't get any rates.")
            return
        for code, rate in rates.items():
            currency = currencies.get(code, {})
            rate = await create_currency_rate(
                session=session,
                rates_in=CurrencyCreateCreate(
                    code=currency.get("code", ""),
                    name=currency.get("name", ""),
                    rate=rate,
                ),
            )

        return "Exchange rates updated successfully."

    @staticmethod
    async def exchange_currency(
        session: AsyncSession, from_currency: str, to_currency: str, amount: float
    ) -> float:

        if from_currency == settings.SYS_CURRENCY:
            rate = await get_exchange_rate(session=session, currency_code=to_currency)
            if not rate or rate == 0:
                raise ValueError(f"Currency {to_currency} has no exchange rate.")
            exchanged_amount = round(amount * round(rate, 2), 2)
        elif to_currency == settings.SYS_CURRENCY:
            rate = await get_exchange_rate(session=session, currency_code=from_currency)
            if not rate or rate == 0:
                raise ValueError(f"Currency {from_currency} has no exchange rate.")
            exchanged_amount = round(amount / round(rate, 2), 2)
        else:
            rate_from = await get_exchange_rate(
                session=session, currency_code=from_currency
            )
            if not rate_from or rate_from == 0:
                raise ValueError(f"Currency {from_currency} has no exchange rate.")

            rate_to = await get_exchange_rate(
                session=session, currency_code=to_currency
            )
            if not rate_to or rate_to == 0:
                raise ValueError(f"Currency {to_currency} has no exchange rate.")

            amount_in_sys_currency = round(amount / round(rate_from, 2), 2)
            exchanged_amount = round(amount_in_sys_currency * round(rate_to, 2), 2)

        return exchanged_amount

    @staticmethod
    async def last_update_dates(session: AsyncSession) -> dict | None:
        data = await last_update_dates(session=session)
        last_updates = {key: date.strftime("%Y-%m-%d %H:%M:%S") for key, date in data}
        return last_updates
