from unittest.mock import patch

import httpx
import pytest
import pytest_asyncio
from typing import AsyncIterator

from app.api.v1.currency.services.currency_helper import CurrencyHelper
from app.main import app
from app.config import settings


@pytest_asyncio.fixture
async def client() -> AsyncIterator[httpx.AsyncClient]:
    async with httpx.AsyncClient(app=app, base_url="http://testserver") as client:
        yield client


@pytest.mark.asyncio
@patch.object(CurrencyHelper, "update_exchange_rates")
async def test_update_exchange_rates_success(
    mock_update_exchange_rates,
    client: httpx.AsyncClient,
):
    mock_update_exchange_rates.return_value = "Exchange rates updated successfully"

    response = await client.post(
        settings.API_V1_STR + "/currencies/update_exchange_rates/", json={}
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Exchange rates updated successfully"}


@pytest.mark.asyncio
@patch.object(CurrencyHelper, "update_exchange_rates")
async def test_update_exchange_rates_error(
    mock_update_exchange_rates,
    client: httpx.AsyncClient,
):
    mock_update_exchange_rates.return_value = None

    response = await client.post(
        settings.API_V1_STR + "/currencies/update_exchange_rates/", json={}
    )

    assert response.status_code == 503
    assert response.json() == {"detail": "Couldn't get any data."}
