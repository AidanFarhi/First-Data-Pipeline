from db_credentials_server import serve_credentials
from operator import itemgetter
import psycopg2

def test_connection():
    conn = None
    print('Attempting to connect to database...')
    try:
        # First get database credentials
        dbname, user, password = itemgetter('dbname', 'user', 'password')(serve_credentials())
        # Then connect to database
        conn = psycopg2.connect(f'dbname={dbname} user={user} password={password}')
        cur = conn.cursor()  # Get a cursor to execute commands
        cur.execute('SELECT VERSION()')
        row = cur.fetchone()
        print(row)
        cur.close()  # Close cursor connection to DB
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            print('Closing connection to DB...')
            conn.close()


if __name__ == '__main__':
    test_connection()