import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()


#DB Configurations
user = os.environ.get('user')
password = os.environ.get('password')
host = os.environ.get('host')
port = os.environ.get('port')
database = os.environ.get('database')

connection_str = f'postgresql://{user}:{password}@{host}:{port}/{database}'
engine  = create_engine(connection_str)

try:
    conn = engine.connect()
except Exception as ex:
    print("Something's wrong. Please try again", ex)