from dotenv import load_dotenv  # So we can use environment variables in a .env file
import os


def serve_credentials():
    load_dotenv()
    credentials = {
        "dbname": "",
        "user": "",
        "password": ""
    }
    credentials['dbname'] = os.getenv('dbname')
    credentials['user'] = os.getenv('user')
    credentials['password'] = os.getenv('password')
    return credentials