import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoping


DB_PORT=os.environ.get('DB_PORT')
if not DB_PORT: DB_PORT = 5432

db_uri = f'postgres://postgres:postgres@localhost:{DB_PORT}/postgres'
engine = create_engine(db_uri)
db = scoping.scoped_session(
            sessionmaker(bind = engine,
                         autocommit = False))
