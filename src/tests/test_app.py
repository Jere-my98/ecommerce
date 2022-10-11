from app import app, fakeDatabase
import pytest
import json

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_get_items(client):
    items = client.get('/')
    assert json.dumps(fakeDatabase) == json.dumps(items.get_json())
    