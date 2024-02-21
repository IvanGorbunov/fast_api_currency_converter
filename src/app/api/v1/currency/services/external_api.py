import logging
from freecurrencyapi import Client
from typing import List, Dict
from app.config import settings

logging.basicConfig(filename=settings.LOG_FILE, level=settings.LOGGING_LEVEL, format="%(asctime)s [%(levelname)s]: %(message)s")
logger = logging.getLogger(__name__)


class ExchangeRatesAPI:

    # @staticmethod
    # def get_current_exchange_rates() -> List[Dict[str, float]]:
    #     client = Client(api_key=API_KEY_RATE)
    #     try:
    #         status = client.status()
    #     except Exception as e:
    #         logger.error(f"Error getting exchange rates: {e}")
    #         return []
    #     if status != 200:
    #         logger.error(f"Service responded: {status}")
    #         return []
    #

    @staticmethod
    async def update_currency_rates():
        api_key = settings.API_KEY_RATE

        try:
            # Создаем объект API с использованием ключа
            client = Client(api_key=settings.API_KEY_RATE)

            # Получаем текущие курсы обмена
            rates = await client.latest()

            # # Обновляем базу данных
            # async with get_db() as db:
            #     for currency_code, rate in rates.items():
            #         await create_currency_rate(db, currency_code=currency_code, rate=rate)

            logger.info("Currency rates updated successfully")

        except Exception as e:
            # Логирование ошибок запроса
            logger.error(f"Error updating currency rates: {e}")


def get_current_exchange_rates():
    pass
