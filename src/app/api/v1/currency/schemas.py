from datetime import datetime
from typing import Annotated, Dict

from annotated_types import MinLen, MaxLen
from pydantic import BaseModel


class CurrencyRate(BaseModel):
    code: str
    name: str
    rate: float
    updated_at: datetime


class CurrencyCreateCreate(BaseModel):
    code: str
    name: str
    rate: float


class DynamicCurrencyDateSchema(BaseModel):
    pass


class DynamicCurrencyResponseSchema(BaseModel):
    data: Dict[str, DynamicCurrencyDateSchema]


class CurrencyExchangeSchema(BaseModel):
    from_currency: Annotated[str, MinLen(3), MaxLen(3)]
    to_currency: Annotated[str, MinLen(3), MaxLen(3)]
    amount: float


class CurrencyExchangeResponseSchema(BaseModel):
    currency: str
    amount: float
