from sqlalchemy import Column, Integer, TIMESTAMP, String, Date
from model import BaseModel
from datetime import datetime

class User(BaseModel):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(64))
    password = Column(String(64))
    dob = Column(Date)
