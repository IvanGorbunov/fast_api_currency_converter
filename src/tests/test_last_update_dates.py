from unittest.mock import patch

import httpx
import pytest
import pytest_asyncio
from typing import AsyncIterator

from app.api.v1.currency.services.currency_helper import CurrencyHelper
from app.main import app
from app.config import settings


# @pytest_asyncio.fixture
# async def client() -> AsyncIterator[httpx.AsyncClient]:
#     async with httpx.AsyncClient(app=app, base_url="http://testserver") as client:
#         yield client


@pytest.mark.asyncio
async def test_last_update_dates_empty(ac: httpx.AsyncClient):
    # Test the last_update_dates endpoint
    response = await ac.get(settings.API_V1_STR + "/currencies/last_update_dates")
    assert response.status_code == 200
    assert "data" in response.json()


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
