from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import urllib.parse

username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'
hostname = 'YOUR_HOST_NAME'
port = '5432'
database_name = 'python_db'
quoted_password = urllib.parse.quote_plus(password)

DATABASE_URL = f'postgresql://{username}:{quoted_password}@{hostname}:{port}/{database_name}'

# For local postgresql server
# DATABASE_URL = 'postgresql://postgres:khadde@localhost:5432/python_db'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)
Base = declarative_base()
