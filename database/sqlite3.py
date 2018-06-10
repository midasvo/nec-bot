import sqlite3
import config

db = config.db_path
con = ""


def create_database(conn):
    conn.cursor().execute('''
        CREATE TABLE IF NOT EXISTS article(id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp TEXT, title TEXT,
                           url TEXT, content TEXT, source TEXT)
    ''')
    conn.commit()
    return conn


def set_conn():
    print("Setting connection")
    global conn
    conn = sqlite3.connect(db)
    create_database(conn)


def get_conn():
    print("Getting connection")
    global conn
    this_conn = conn
    return this_conn
