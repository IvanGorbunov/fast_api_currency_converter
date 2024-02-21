from typing import Annotated

from annotated_types import MinLen, MaxLen
from pydantic import BaseModel


class CurrencyExchangeSchema(BaseModel):
    from_currency: Annotated[str, MinLen(3), MaxLen(3)]
    to_currency: Annotated[str, MinLen(3), MaxLen(3)]
    amount: float


class CurrencySchema(BaseModel):
    code: Annotated[str, MinLen(3), MaxLen(3)]
