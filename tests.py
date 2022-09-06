import pytest
from main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_read_main(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
    
def test_read_user(client):
    response = client.get("/user")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello User"}
    
def test_read_user_id(client):
    response = client.get("/user/1")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello User 1"}
    
def test_read_user_id_incorrect(client):
    response = client.get("/user/a")
    assert response.status_code == 422
    assert response.json() == {"detail": [{"loc": ["path", "user_id"], "msg": "value is not a valid integer", "type": "type_error.integer"}]}
    
def test_read_user_id_not_found(client):
    response = client.get("/user/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}
    
def test_read_user_id_put(client):
    response = client.put("/user/1")
    assert response.status_code == 405
    assert response.json() == {"detail": "Method Not Allowed"}
    
def test_read_user_id_delete(client):
    response = client.delete("/user/1")
    assert response.status_code == 405
    assert response.json() == {"detail": "Method Not Allowed"}
    
def test_read_user_post(client):
    response = client.post("/user", json={"name": "FastAPI", "email": "     "})
    assert response.status_code == 422
    assert response.json() == {"detail": [{"loc": ["body", "email"], "msg": "field required", "type": "value_error.missing"}]}
