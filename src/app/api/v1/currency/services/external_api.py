import logging
from freecurrencyapi import Client
from typing import List, Dict

from app.config import settings

logging.basicConfig(
    filename=settings.LOG_FILE,
    level=settings.LOGGING_LEVEL,
    format="%(asctime)s [%(levelname)s]: %(message)s",
)
LOG = logging.getLogger(__name__)


class ExchangeRatesAPIHelper:
    client = Client(api_key=settings.API_KEY_RATE)

    @classmethod
    async def get_remaining_quota(cls) -> int:
        try:
            status = cls.client.status()
            if settings.DEBUG:
                LOG.info(f"Third-party service quotas remaining: {status["quotas"]["month"]["remaining"]}")
        except Exception as e:
            LOG.error(f"Error getting third-party service`s status: {e}")
            return 0
        return status["quotas"]["month"]["remaining"]

    @classmethod
    async def get_currencies(cls) -> Dict | None:
        try:
            currencies = cls.client.currencies()
            currencies = currencies.get("data", {})
        except Exception as e:
            LOG.error(f"Error getting currencies: {e}")
            return None
        return currencies

    @classmethod
    async def get_current_exchange_rates(cls) -> Dict | None:
        try:
            latest_rate = cls.client.latest()
            latest_rate = latest_rate.get("data", {})
        except Exception as e:
            LOG.error(f"Error getting exchange rates: {e}")
            return None
        return latest_rate
