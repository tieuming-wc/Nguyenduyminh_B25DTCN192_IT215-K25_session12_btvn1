from sqlalchemy.orm import Session
from model import ParkingSlotModel

def create_parking_slot(db: Session, slot_data):
    new_slot = ParkingSlotModel(**slot_data.dict())
    db.add(new_slot)
    db.commit()
    db.refresh(new_slot)
    return new_slot

def get_all_slots(db: Session):
    return db.query(ParkingSlotModel).all()