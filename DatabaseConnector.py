#   Student Name:   Anthony Cox
#   Student ID:     C00162988
#   Date:           9th February 2015
#   Purpose:        This file manages the connection, committing of new details and closure of connections to the database.

import mysql.connector

class DatabaseConnection:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.passwd = '' 
        self.db = 'proto2'

    # This code executes before the body of the with statement - connects to the database and returns a cursor
    def __enter__(self):
        self.conn = mysql.connector.connect(host = self.host,
                                            user = self.user,
                                            password = self.passwd,
                                            database = self.db, )
        self.cursor = self.conn.cursor()
        return self.cursor

    # Tear down the connections, commit - all processed after the with statement
    def __exit__(self, exc_type, exv_value, exc_traceback):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()


