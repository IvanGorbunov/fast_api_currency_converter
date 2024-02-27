from unittest.mock import patch

import httpx
import pytest

from app.api.v1.currency.services.currency_helper import CurrencyHelper
from app.config import settings


@pytest.mark.asyncio
@patch.object(CurrencyHelper, "update_exchange_rates")
async def test_update_exchange_rates_success(
    mock_update_exchange_rates,
    ac: httpx.AsyncClient,
):
    mock_update_exchange_rates.return_value = "Exchange rates updated successfully"

    response = await ac.post(
        settings.API_V1_STR + "/currencies/update_exchange_rates/", json={}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Exchange rates updated successfully"}


@pytest.mark.asyncio
@patch.object(CurrencyHelper, "update_exchange_rates")
async def test_update_exchange_rates_error(
    mock_update_exchange_rates,
    ac: httpx.AsyncClient,
):
    mock_update_exchange_rates.return_value = None

    response = await ac.post(
        settings.API_V1_STR + "/currencies/update_exchange_rates/", json={}
    )
    assert response.status_code == 503
    assert response.json() == {"detail": "Couldn't get any data."}
