from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from service import create_parking_slot, get_all_slots

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.post("/parking-slots")
def add_slot(slot_data, db: Session = Depends(get_db)):
    return create_parking_slot(db, slot_data)

@app.get("/parking-slots")
def list_slots(db: Session = Depends(get_db)):
    return get_all_slots(db)