from unittest.mock import patch

import httpx
import pytest

from app.api.v1.currency.services.currency_helper import CurrencyHelper
from app.config import settings


@pytest.mark.asyncio
@patch.object(CurrencyHelper, "last_update_dates")
async def test_last_update_dates_success(
    mock_last_update_dates,
    ac: httpx.AsyncClient,
):
    mock_last_update_dates.return_value = {"USD": "2023-11-19"}

    response = await ac.get(settings.API_V1_STR + "/currencies/last_update_dates")
    assert response.status_code == 200
    assert response.json() == {"data": {"USD": "2023-11-19"}}


@pytest.mark.asyncio
@patch.object(CurrencyHelper, "last_update_dates")
async def test_last_update_dates_error(
    mock_last_update_dates,
    ac: httpx.AsyncClient,
):
    mock_last_update_dates.return_value = None

    response = await ac.get(settings.API_V1_STR + "/currencies/last_update_dates")
    assert response.status_code == 503
    assert response.json() == {"detail": "Couldn't get any data."}
