import pytest
from fastapi.testclient import TestClient

from src.app import app


@pytest.fixture
def api_client() -> TestClient:
    return TestClient(app)


def test_tokenization_success_with_valid_data(api_client: TestClient) -> None:
    response = api_client.post(
        "/tokens",
        json={
            "cardholder_name": "Joe Bloggs",
            "card_number": "4111111111111111",
            "cvv": "123",
            "expiry_year": "2023",
            "expiry_month": "1",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["token"], str)
