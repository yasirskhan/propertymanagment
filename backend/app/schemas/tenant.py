
from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class TenantCreate(BaseModel):
    first_name: str
    last_name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    org_id: str = "org_test"

class TenantResponse(TenantCreate):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

class LeaseCreate(BaseModel):
    unit_id: int
    tenant_id: int
    start_date: date
    end_date: date
    rent_amount: float
    deposit: float = 0.0
    status: str = "active"
    org_id: str = "org_test"

class LeaseResponse(LeaseCreate):
    id: int
    stripe_subscription: str = "sub_xxx"
    class Config:
        from_attributes = True
