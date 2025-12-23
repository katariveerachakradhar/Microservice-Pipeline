import pytest
from app.main import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello from Microservice!" in response.data
