from sqlalchemy import Column, Integer, String, Text, Numeric, TIMESTAMP
from .database import Base

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    location = Column(String(255))
    price = Column(Numeric(10,2))
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
