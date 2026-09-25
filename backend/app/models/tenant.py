
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime

class Tenant(Base):
    __tablename__ = "tenants"
    id = Column(Integer, primary_key=True, index=True)
    org_id = Column(String, index=True, default="org_test")
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String)
    phone = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class Lease(Base):
    __tablename__ = "leases"
    id = Column(Integer, primary_key=True, index=True)
    org_id = Column(String, index=True, default="org_test")
    unit_id = Column(Integer, ForeignKey("units.id"))
    tenant_id = Column(Integer, ForeignKey("tenants.id"))
    start_date = Column(Date)
    end_date = Column(Date)
    rent_amount = Column(Float)
    deposit = Column(Float, default=0.0)
    status = Column(String, default="active")  # active, expired, terminated
    stripe_subscription = Column(String, default="sub_xxx")  # only sub_xxx
