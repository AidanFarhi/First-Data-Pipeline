from dotenv import load_dotenv  # So we can use environment variables in a .env file
import os
import requests
import json


def get_brooklyn_weather_from_api():
    load_dotenv()                   # Loads .env variables
    key = os.environ.get('api-key') # Get api-key from .env file
    data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?zip=11225,us&units=imperial&appid={key}').json()
    return data




if __name__ == '__main__':
    main()