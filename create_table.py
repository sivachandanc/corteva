import sqlite3
from sqlite3 import Error

"""
This Python script has two methods:
    1. create_connection: returns a conncetion object
    2. create_table: creates the table called weather_data
    
"""

# Funcitong for creating a connection object for SQLite
def create_connection():
    """ creating a database connection to a SQLite database """
    conn = None
    try:
        # creating a Database
        conn = sqlite3.connect('weather.db')
        print(f"Connected to SQLite version {sqlite3.version}")
        return conn
    except Error as e:
        print(e)

def create_table():
    """ creating the weather data table """
    conn = create_connection()
    try:
        c = conn.cursor()

        #Creating a Table
        c.execute('''CREATE TABLE weather_data
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     date TEXT NOT NULL,
                     max_temp INTEGER NOT NULL,
                     min_temp INTEGER NOT NULL,
                     precipitation INTEGER NOT NULL);''')
        conn.commit()
        print("Table created successfully!")
    except Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    create_table()
