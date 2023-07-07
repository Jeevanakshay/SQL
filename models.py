from sqlalchemy import Column, Integer, String
# from datetime import date
from database import Base


class User(Base):
    __tablename__ = "jeevan_user3"

    voter_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    gender = Column(String)
    dob = Column(String)
    age = Column(Integer)

    class Config:
        orm_mode = True
