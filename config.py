import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoping


DB_PORT=os.environ.get('DB_PORT')
if not DB_PORT: DB_PORT = 5432

DB_NAME=os.environ.get('DB_NAME')
if not DB_NAME: DB_NAME = 'bxdoan_falcon'

db_uri = f'postgres://postgres:postgres@localhost:{DB_PORT}/{DB_NAME}'
engine = create_engine(db_uri)
db = scoping.scoped_session(
            sessionmaker(bind = engine,
                         autocommit = False))
