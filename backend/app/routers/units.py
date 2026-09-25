
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.property import Unit
from app.schemas.property import UnitCreate, UnitResponse
from typing import List

router = APIRouter()

@router.post("/{property_id}/units", response_model=UnitResponse)
def create_unit(property_id: int, payload: UnitCreate, db: Session = Depends(get_db)):
    unit = Unit(property_id=property_id, **payload.model_dump())
    db.add(unit)
    db.commit()
    db.refresh(unit)
    return unit

@router.get("/property/{property_id}", response_model=List[UnitResponse])
def list_units(property_id: int, db: Session = Depends(get_db)):
    return db.query(Unit).filter(Unit.property_id == property_id).all()
