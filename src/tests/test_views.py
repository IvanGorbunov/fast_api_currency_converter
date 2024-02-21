from fastapi.testclient import TestClient
from app.main import app
from app.config import settings


def test_status() -> None:
    client = TestClient(app)
    result = client.get(settings.API_V1_STR + "/currencies/")
    assert result.status_code == 200
    # assert result.json(), {'status': 'ok'}
