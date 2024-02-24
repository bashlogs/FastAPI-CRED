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
cd app
uvicorn main:app --reload
```

Docker Run command
```bash
docker pull bashlogs/fastapi

docker run -d -p 8000:8000 `
 -e DB_USERNAME=YOUR_USERNAME `
 -e DB_PASSWORD=YOUR_PASSWORD `
 -e DB_HOSTNAME=YOUR_HOST_NAME `
 -e DB_PORT=5432 `
 -e DB_DATABASE_NAME='python_db' bashlogs/fastapi:1.0
 ```

Images

![image](https://github.com/bashlogs/FastAPI-CRED/assets/102829101/dbb92c43-9a1f-4df7-8817-16f29eea193d)

![image](https://github.com/bashlogs/FastAPI-CRED/assets/102829101/1bb080c9-f4df-4867-b225-ad204d071d42)

