from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import get_settings # imported for containing all env config

engine = create_engine( # engine is required to interact with db from ORM
    get_settings().db_url, connect_args={"check_same_thread" : False} # it needs db_url always
)

SessionLocal = sessionmaker( # used for a single transac betwn db and ORM
    autocommit=False, autoflush=False, bind=engine # requires bind=engine 
)

Base = declarative_base() # used for defining db models and schema