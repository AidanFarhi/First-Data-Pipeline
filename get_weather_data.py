from dotenv import load_dotenv  # So we can use environment variables in a .env file
import os
import requests
import json


def write_to_json_file(json_data):
    file_name = 'json_data.json'
    with open(file_name, 'w') as file:
        json.dump(json_data, file)
    print("JSON data dumped successfully.")


def get_brooklyn_weather_from_api():
    load_dotenv()                   # Loads .env variables
    key = os.environ.get('api-key') # Get api-key from .env file
    data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?zip=11225,us&units=imperial&appid={key}').json()
    write_to_json_file(data)


if __name__ == '__main__':
    data = get_brooklyn_weather_from_api()
    write_to_json_file(data)
