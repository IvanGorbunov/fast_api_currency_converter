from datetime import datetime, UTC

from .schemas import CurrencyExchangeSchema, CurrencySchema


def create_curency(currency: CurrencySchema):
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
