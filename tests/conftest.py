import pytest
from src.app import app

@pytest.fixture(scope="module")
def test_client():
    with app.test_client() as client:
        yield client