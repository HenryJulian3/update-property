from pydantic import BaseModel
from typing import Optional

class PropertyUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    price: Optional[float] = None
