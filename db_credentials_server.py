from dotenv import load_dotenv  # So we can use environment variables in a .env file
import os


def serve_credentials():
    load_dotenv()
    credentials = {
        "dbname": "",
        "user": "",
        "password": "",
        "port": "",
        "uri": ""
    }
    credentials['dbname'] = os.getenv('dbname')
    credentials['user'] = os.getenv('user')
    credentials['password'] = os.getenv('password')
    credentials['port'] = os.getenv('port')
    credentials['uri'] = os.getenv('uri')
    return credentials