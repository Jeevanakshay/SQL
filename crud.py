import uuid
from sqlalchemy.orm import Session
import models

item_id = str(uuid.uuid4().int % 10000)  # Generate a unique item_id


def create_item(db: Session, item):
    db_item = models.User(name=item.name, gender=item.gender, dob=item.dob, age=item.age, voter_id=item_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_user_by_id(db: Session, user_id: int):  # accessing the particular  voter id
    try:
        return db.query(models.User).filter(models.User.voter_id == user_id).first()
    except Exception as e:
        return "Error", str(e)


def get_users(db: Session):
    try:
        return db.query(models.User).all()
    except Exception as e:
        return "Error", str(e)


def update_item_by_id(db: Session, voter_id: int, updated_values: dict):
    try:
        item = db.query(models.User).get(voter_id)
        if item:
            for key, value in updated_values.items():
                setattr(item, key, value)
            db.commit()
            return True
        return False
    except Exception as e:
        return "Error", str(e)


def delete_item_by_id(db: Session, voter_id: int):
    try:
        item = db.query(models.User).get(voter_id)
        if item:
            db.delete(item)
            db.commit()
            return True
        return False
    except Exception as e:
        return "Error", str(e)
