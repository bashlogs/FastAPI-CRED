# FastAPI-CRED

## API Development and Cloud Infrastructure

### How to run the project

Install all the requirements

```bash
pip install -r app/requirements.txt
```

Update the ```app/config.py``` file with your own database credentials.

```bash
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

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)
Base = declarative_base()
```

Run the project

```bash
uvicorn main:app --reload
```