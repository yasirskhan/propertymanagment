
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.property import Property
from app.schemas.property import PropertyCreate, PropertyResponse
from typing import List

router = APIRouter()

@router.post("/", response_model=PropertyResponse)
def create_property(payload: PropertyCreate, db: Session = Depends(get_db)):
    prop = Property(**payload.model_dump())
    db.add(prop)
    db.commit()
    db.refresh(prop)
    return prop

@router.get("/", response_model=List[PropertyResponse])
def list_properties(org_id: str = "org_test", db: Session = Depends(get_db)):
    return db.query(Property).filter(Property.org_id == org_id).all()

@router.get("/{property_id}", response_model=PropertyResponse)
def get_property(property_id: int, db: Session = Depends(get_db)):
    prop = db.query(Property).filter(Property.id == property_id).first()
    if not prop:
        raise HTTPException(404, "Property not found")
    return prop

@router.delete("/{property_id}")
def delete_property(property_id: int, db: Session = Depends(get_db)):
    prop = db.query(Property).filter(Property.id == property_id).first()
    if not prop:
        raise HTTPException(404, "Property not found")
    db.delete(prop)
    db.commit()
    return {"deleted": property_id}
