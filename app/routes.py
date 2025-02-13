from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from .models import Property
from .schemas import PropertyUpdate

router = APIRouter()

@router.put("/update/{property_id}")
def update_property(property_id: int, property_data: PropertyUpdate, db: Session = Depends(get_db)):
    # Buscar la propiedad en la base de datos
    property_record = db.query(Property).filter(Property.id == property_id).first()
    
    if not property_record:
        raise HTTPException(status_code=404, detail="Property not found")
    
    # Actualizar solo los campos proporcionados
    for key, value in property_data.dict(exclude_unset=True).items():
        setattr(property_record, key, value)
    
    db.commit()
    db.refresh(property_record)
    
    return {"message": "Property updated successfully", "property": property_record}
