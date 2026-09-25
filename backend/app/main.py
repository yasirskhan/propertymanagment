
from fastapi import FastAPI
from app.core.database import Base, engine
from app.routers import properties, tenants, units, leases, addons

Base.metadata.create_all(bind=engine)

app = FastAPI(title="PropertyManagment SaaS - 5%", version="0.05.0")

app.include_router(properties.router, prefix="/api/v1/properties", tags=["properties"])
app.include_router(units.router, prefix="/api/v1/units", tags=["units"])
app.include_router(tenants.router, prefix="/api/v1/tenants", tags=["tenants"])
app.include_router(leases.router, prefix="/api/v1/leases", tags=["leases"])
app.include_router(addons.router, prefix="/api/v1/addons", tags=["addons"])

@app.get("/health")
def health():
    return {"status": "ok", "progress": "5%", "model": "base + addons", "features": 18}

@app.get("/")
def root():
    return {"message": "PropertyManagment SaaS - 5% - Go to /docs"}
