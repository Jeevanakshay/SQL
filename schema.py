from datetime import date
from pydantic import BaseModel


class Person(BaseModel):
    name: str
    gender: str
    dob: date
    age: int


class voter(BaseModel):
    voter_id: int
