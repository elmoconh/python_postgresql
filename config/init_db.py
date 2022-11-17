import psycopg2
from decouple import config
from urllib.parse import urlparse

def connect():
    url = urlparse(config('DB_URL'))
    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
    return conn

def init_db():
    conn = connect()
    cur = conn.cursor()
    with open('config/schema.sql', 'r') as f:
        cur.execute(f.read())
    conn.commit()
    cur.close()
    conn.close()