from psycopg2 import connect,Error
from contextlib import contextmanager

@contextmanager
def connection():
    conn = None
    try:
        conn = connect(host='mel.db.elephantsql.com', user='blcmnidk', database='blcmnidk',
                       password = '5JGFEqVB1bi9mUS3IInHFpjwldRy-eyt')
        yield conn
        conn.commit()
    except Error as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()


