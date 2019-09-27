# from app import api
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoping

db_uri = 'postgres://postgres:postgres@localhost:5432/postgres'
engine = create_engine(db_uri)
db = scoping.scoped_session(
            sessionmaker(bind = engine,
                         autocommit = False))
