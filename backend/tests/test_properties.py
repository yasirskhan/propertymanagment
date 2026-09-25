
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["progress"] == "5%"

def test_create_property():
    r = client.post("/api/v1/properties/", json={"name": "Test Property 5%", "org_id": "org_test"})
    assert r.status_code == 200
    assert r.json()["name"] == "Test Property 5%"

def test_list_properties():
    r = client.get("/api/v1/properties/?org_id=org_test")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
