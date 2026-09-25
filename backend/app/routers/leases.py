
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.tenant import Lease
from app.schemas.tenant import LeaseCreate, LeaseResponse
from typing import List

router = APIRouter()

@router.post("/", response_model=LeaseResponse)
def create_lease(payload: LeaseCreate, db: Session = Depends(get_db)):
    lease = Lease(**payload.model_dump())
    db.add(lease)
    db.commit()
    db.refresh(lease)
    return lease

@router.get("/", response_model=List[LeaseResponse])
def list_leases(org_id: str = "org_test", db: Session = Depends(get_db)):
    return db.query(Lease).filter(Lease.org_id == org_id).all()
