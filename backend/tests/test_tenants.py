
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_tenant():
    r = client.post("/api/v1/tenants/", json={"first_name": "John", "last_name": "Doe", "org_id": "org_test"})
    assert r.status_code == 200
    assert r.json()["first_name"] == "John"

def test_create_lease():
    # Create property, unit, tenant first
    prop = client.post("/api/v1/properties/", json={"name": "Lease Test Prop", "org_id": "org_test"}).json()
    unit = client.post(f"/api/v1/units/{prop['id']}/units", json={"unit_number": "101", "rent_amount": 1200}).json()
    tenant = client.post("/api/v1/tenants/", json={"first_name": "Jane", "last_name": "Doe", "org_id": "org_test"}).json()
    lease = client.post("/api/v1/leases/", json={
        "unit_id": unit["id"],
        "tenant_id": tenant["id"],
        "start_date": "2024-01-01",
        "end_date": "2025-01-01",
        "rent_amount": 1200,
        "org_id": "org_test"
    })
    assert lease.status_code == 200
    assert lease.json()["rent_amount"] == 1200
