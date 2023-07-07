from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schema
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/new-item")
def create_user(item: schema.Person, db: Session = Depends(get_db)):
    if item.age > 18:
        item.dob = item.dob.isoformat()
        db_item = crud.create_item(db=db, item=item)
        return {"Message": "Voter ID is created Successfully", "Person": db_item}
    else:
        return {"Message": "You are not eligible to apply the Voter Id "}


@app.get("/items")
def get_items(db: Session = Depends(get_db)):
    items = crud.get_users(db)
    return items


@app.put("/update-voter/{item_id}")
def update_voter(voter_id: int, updated_item: schema.Person, db: Session = Depends(get_db)):
    db_item = crud.get_user_by_id(db, voter_id)  # fetching voterid from user
    if db_item:
        updated_values = updated_item.dict(exclude_unset=True)
        crud.update_item_by_id(db, voter_id=voter_id, updated_values=updated_values)
        return {"message": "Item updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/delete_voter_id")
def delete_user_id(voter_id: int, db: Session = Depends(get_db)):
    item = crud.get_user_by_id(db, voter_id)
    if item:
        crud.delete_item_by_id(db, voter_id)
        return {"message": "Item deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="No Item is present with this ID")
