import sqlite3
from sqlite3 import Error


def create_connection():
    conn = None

    try:
        conn = sqlite3.connect("database/database.db")
    except Error as e:
        print("Error connecting to database: " + str(e))
    return conn
