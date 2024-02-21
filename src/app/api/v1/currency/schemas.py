from typing import Annotated

from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, ConfigDict


class CurrencyBase(BaseModel):
    code: Annotated[str, MinLen(3), MaxLen(3)]


class CurrencyCreate(CurrencyBase):
    pass


class Currency(CurrencyBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class CurrencyRate(BaseModel):
    currency_code_id: int

    rate: float
    # updated_at: datetime


class CurrencyExchangeSchema(BaseModel):
    from_currency: Annotated[str, MinLen(3), MaxLen(3)]
    to_currency: Annotated[str, MinLen(3), MaxLen(3)]
    amount: float


class CurrencySchema(BaseModel):
    code: Annotated[str, MinLen(3), MaxLen(3)]
