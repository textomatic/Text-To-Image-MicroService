from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_image_endpoint():
    response = client.get("/vector_image/panda eating ice cream")
    assert response.status_code == 200
    #assert response.json() == {"msg": "Hello World"}