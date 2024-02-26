from unittest.mock import patch

import httpx
import pytest
import pytest_asyncio
from typing import AsyncIterator

from app.api.v1.currency.schemas import CurrencyExchangeSchema
from app.api.v1.currency.services.currency_helper import CurrencyHelper
from app.main import app
from app.config import settings


@pytest_asyncio.fixture
async def client() -> AsyncIterator[httpx.AsyncClient]:
    async with httpx.AsyncClient(app=app, base_url="http://testserver") as client:
        yield client


# @pytest.mark.asyncio
# @patch.object(CurrencyHelper, "exchange_currency")
# async def test_exchange_currency_success(
#     mock_exchange_currency,
#     client: httpx.AsyncClient,
# ):
#     mock_exchange_currency.return_value = 92.46
#     request = CurrencyExchangeSchema(from_currency="USD", to_currency="EUR", amount=100)
#
#     response = await client.post(
#         settings.API_V1_STR + "/currencies/exchange_currency/", json=request.dict()
#     )
#     assert response.status_code == 200
#     assert response.json() == {"currency": "EUR", "amount": 92.46}


# @pytest.mark.asyncio
# async def test_exchange_currency_invalid_currencies(
#     client: httpx.AsyncClient,
# ):
#     request = CurrencyExchangeSchema(from_currency="USD", to_currency="USD", amount=100)
#
#     response = await client.post(
#         settings.API_V1_STR + "/currencies/exchange_currency/", json=request.dict()
#     )
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Invalid currency codes"}
#
#
# @pytest.mark.asyncio
# async def test_exchange_currency_invalid_amount(
#     client: httpx.AsyncClient,
# ):
#     request = CurrencyExchangeSchema(from_currency="USD", to_currency="EUR", amount=0)
#
#     response = await client.post(
#         settings.API_V1_STR + "/currencies/exchange_currency/", json=request.dict()
#     )
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Invalid amount"}
