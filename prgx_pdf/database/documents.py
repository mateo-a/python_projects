import sqlite3
from sqlite3 import Error

from .connection import create_connection


def insert_document(data):
    conn = create_connection()

    sql = """INSERT INTO EXTRACTION(Vendor_Name, Fiscal_Number, \
        Contract, Start_Date, End_Date, Comments)
        VALUES(?,?,?,?,?,?)"""

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(f"Error inserting document: {str(e)}")
        return False

    finally:
        if conn:
            cur.close()
            conn.close()


def select_all_documents(table):
    conn = create_connection()

    sql = "SELECT rowid as id, * FROM " + table + " ORDER BY id DESC;"
    try:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(sql)
        document_rows = cur.fetchall()
        documents = [dict(row) for row in document_rows]
        return documents
    except Error as e:
        print(f"Error retrieving all documents: {str(e)}")
        return False
    finally:
        if conn:
            cur.close()
            conn.close()
