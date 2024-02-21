from sqlalchemy.orm import Session

from app.api.v1.currency.schemas import CurrencyExchangeSchema
from app.api.v1.currency.services.external_api import get_current_exchange_rates
from app.models import Currency


class CurrencyHelper:
    """
    Helper class for work with currencies
    """

    @staticmethod
    def update_exchange_rates(db: Session):
        rates = (
            get_current_exchange_rates()
        )  # get current exchange rates from external API

        for currency_data in rates:
            db_currency = (
                db.query(Currency)
                .filter(Currency.code == currency_data["code"])
                .first()
            )

            if db_currency:
                db_currency.rate = currency_data["rate"]
            else:
                db_currency = Currency(**currency_data)
                db.add(db_currency)

        db.commit()

    @staticmethod
    def exchange_currency(currency_exchange: CurrencyExchangeSchema):
        pass

    @staticmethod
    def last_update_courses():
        pass
