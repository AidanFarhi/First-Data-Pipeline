import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
dbname = os.getenv('dbname')
user = os.getenv('user')
password = os.getenv('password')
conn = psycopg2.connect(f'dbname={dbname} user={user} password={password}')
print(conn)
conn.close()
