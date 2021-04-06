from get_weather_data import get_brooklyn_weather_from_api
from write_json_to_db import commit_weather_data_to_db


def main():
    print('Starting job...')
    get_brooklyn_weather_from_api()
    commit_weather_data_to_db()
    print("Job complete.")


if __name__ == '__main__':
    main()