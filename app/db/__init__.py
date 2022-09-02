from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g # global variable

load_dotenv()

# connect to db using env variable
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()

def init_db(app):
  Base.metadata.create_all(engine)

  app.teardown_appcontext(close_db)

def get_db():
  if 'db' not in g: 
    # store db connection in app context
    g.db = Session()

  return g.db # return session wrapped in global object, instead of creating a new session each time

def close_db(e=None):
  db = g.pop('db', None) # attempts to find and remove db from global object

  if db is not None:
    db.close()