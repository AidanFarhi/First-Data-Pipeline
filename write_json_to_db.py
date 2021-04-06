import os
import json
import psycopg2
from db_credentials_server import serve_credentials
from operator import itemgetter


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
        if data.get('rain') is None: precip = 0
        else: precip = data['rain']['1h']
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
        dbname, user, password, port, host = itemgetter('dbname', 'user', 'password', 'port', 'uri')(serve_credentials())
        # Then connect to database
        conn = psycopg2.connect(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')
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
