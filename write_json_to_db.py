import psycopg2
import os
import json
from dotenv import load_dotenv


def create_db_commit_string():
    dt = temp = temp_min = temp_max = pressure = humidity = wind_spd = precip =  0
    desc = ''
    with open('json_data.json') as f:
        data = json.load(f)
        dt = data['dt']
        desc = data['weather'][0]['description']
        temp = data['main']['temp']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        wind_spd = data['wind']['speed']
        precip = data['rain']['1h']
    commit_string = f"""
        INSERT INTO weather_data 
        (dt, description, temp, temp_min, temp_max, pressure, humidity, wind_spd, precip) 
        VALUES (
            {dt}, '{desc}', {temp}, {temp_min}, {temp_max},
            {pressure}, {humidity}, {wind_spd}, {precip}
        );
    """
    os.remove('json_data.json')  # remove json file when done
    return commit_string
        

def commit_weather_data_to_db():
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
        cur.execute(create_db_commit_string())  # insert vals into db
        cur.close()  # Close cursor connection to DB
        conn.commit()  # Commit changes to DB
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            print('Closing connection to DB...')
            conn.close()


if __name__ == '__main__':
    commit_weather_data_to_db()