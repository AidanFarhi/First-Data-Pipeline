import psycopg2
import os
from dotenv import load_dotenv


def create_weather_table():
    conn = None
    print('attempting to connect to database...')
    try:
        load_dotenv()
        dbname = os.getenv('dbname')
        user = os.getenv('user')
        password = os.getenv('password')
        conn = psycopg2.connect(f'dbname={dbname} user={user} password={password}')
        cur = conn.cursor()
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            print('closing db connection...')
            conn.close()


if __name__ == '__main__':
    create_weather_table()