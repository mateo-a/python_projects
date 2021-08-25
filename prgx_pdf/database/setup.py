import sqlite3
from sqlite3 import Error

from .connection import create_connection


def read_file(path):
    """ Function to read a file"""

    with open(path, 'r') as sql_file:
        return sql_file.read()


def create_tables():
    """ Function that opens a connection to database and invokes the SQL to
    create tables into it """

    conn = create_connection()

    path = 'database/sql/tables.sql'

    sql = read_file(path)

    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        return True
    except Error as e:
        print(f"Error creating tables: {str(e)}")
        return False
    finally:
        if conn:
            cur.close()
            conn.close()
