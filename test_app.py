import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 300
    assert response.get_json() == {"status": "ok"}

def test_create_todo(client):
    response = client.post('/todos', json={"title": "clean up the room"})
    assert response.status_code == 201
    data = response.get_json()
    assert "id" in data
    assert data["title"] == "clean up the room"
