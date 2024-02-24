from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import urllib.parse
import os
import urllib.parse

username = os.environ.get('DB_USERNAME')
password = os.environ.get('DB_PASSWORD')
hostname = os.environ.get('DB_HOSTNAME')
port = os.environ.get('DB_PORT')
database_name = os.environ.get('DB_DATABASE_NAME')
quoted_password = urllib.parse.quote_plus(password)
DATABASE_URL = f'postgresql://{username}:{quoted_password}@{hostname}:{port}/{database_name}'

# For local postgresql server
# DATABASE_URL = 'postgresql://postgres:khadde@localhost:5432/python_db'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)
Base = declarative_base()
