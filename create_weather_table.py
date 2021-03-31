import psycopg2
import os
from dotenv import load_dotenv


def generate_create_table_string():
    create_table_string = """
        CREATE TABLE IF NOT EXISTS weather_data (
            id INTEGER PRIMARY KEY,
            dt INTEGER NOT NULL,
            description VARCHAR(255),
            temp DECIMAL NOT NULL,
            temp_min DECIMAL NOT NULL,
            temp_max DECIMAL NOT NULL,
            pressure DECIMAL NOT NULL,
            humidity DECIMAL NOT NULL,
            wind_spd DECIMAL NOT NULL 
        );
    """
    return create_table_string

def create_weather_table():
    conn = None
    print('Attempting to connect to database...')
    try:
        # First get database credentials
        load_dotenv()
        dbname = os.getenv('dbname')
        user = os.getenv('user')
        password = os.getenv('password')
        # Then connect to database
        conn = psycopg2.connect(f'dbname={dbname} user={user} password={password}')
        cur = conn.cursor()  # Get a cursor to execute commands
        cur.execute(generate_create_table_string())  # Now execute create table command
        cur.close()  # Close cursor connection to DB
        conn.commit()  # Commit changes to DB
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            print('Closing connection to DB...')
            conn.close()


if __name__ == '__main__':
    create_weather_table()