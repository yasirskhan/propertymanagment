
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime

class Property(Base):
    __tablename__ = "properties"
    id = Column(Integer, primary_key=True, index=True)
    org_id = Column(String, index=True, default="org_test")
    name = Column(String, nullable=False)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    property_type = Column(String, default="multifamily")
    created_at = Column(DateTime, default=datetime.utcnow)
    units = relationship("Unit", back_populates="property", cascade="all, delete-orphan")

class Unit(Base):
    __tablename__ = "units"
    id = Column(Integer, primary_key=True, index=True)
    property_id = Column(Integer, ForeignKey("properties.id"))
    org_id = Column(String, index=True, default="org_test")
    unit_number = Column(String, nullable=False)
    bedrooms = Column(Integer, default=1)
    bathrooms = Column(Float, default=1.0)
    sqft = Column(Integer)
    rent_amount = Column(Float, default=0.0)
    status = Column(String, default="vacant")  # vacant, occupied, notice
    property = relationship("Property", back_populates="units")
