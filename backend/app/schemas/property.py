
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class UnitCreate(BaseModel):
    unit_number: str
    bedrooms: int = 1
    bathrooms: float = 1.0
    sqft: Optional[int] = None
    rent_amount: float = 0.0
    status: str = "vacant"

class UnitResponse(UnitCreate):
    id: int
    property_id: int
    class Config:
        from_attributes = True

class PropertyCreate(BaseModel):
    name: str
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    property_type: str = "multifamily"
    org_id: str = "org_test"

class PropertyResponse(PropertyCreate):
    id: int
    created_at: datetime
    units: List[UnitResponse] = []
    class Config:
        from_attributes = True
