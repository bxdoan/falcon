from config import engine
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()
BaseModel.metadata.create_all(engine)
from model.User import User
from model.Customer import Customer

__all__ = [
    BaseModel,
    User,
    Customer
]
