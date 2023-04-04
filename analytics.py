import create_table as ct
import time
from sqlite3 import Error

def create_new_table():
    """ create a new table to store the analysis results """
    conn = ct.create_connection()
    try:
        c = conn.cursor()
        c.execute('''CREATE TABLE analysis_results
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     year INTEGER NOT NULL,
                     avg_max_temp REAL,
                     avg_min_temp REAL,
                     total_precipitation REAL);''')
        conn.commit()
        print("New table created successfully!")
    except Error as e:
        print(e)
    finally:
        conn.close()

def analyze_data():
    """ analyze the weather data and store the results in the analysis_results table """
    start_time = time.time()
    conn = ct.create_connection()
    c = conn.cursor()
    c.execute("SELECT DISTINCT SUBSTR(date, 1, 4) FROM weather_data")
    years = c.fetchall()
    for year in years:
        c.execute(f"SELECT AVG(max_temp)/10, AVG(min_temp)/10, SUM(precipitation)/10 FROM weather_data WHERE SUBSTR(date, 1, 4) = '{year[0]}' AND max_temp > -9999 AND min_temp > -9999 AND precipitation > -9999")
        result = c.fetchone()
        avg_max_temp = result[0] if result[0] is not None else None
        avg_min_temp = result[1] if result[1] is not None else None
        total_precipitation = result[2] if result[2] is not None else None
        c.execute(f"INSERT INTO analysis_results (year, avg_max_temp, avg_min_temp, total_precipitation) VALUES ({year[0]}, {avg_max_temp}, {avg_min_temp}, {total_precipitation})")
    conn.commit()
    conn.close()
    end_time = time.time()
    print(f"Data analysis completed in {end_time - start_time} seconds")

if __name__ == '__main__':
    create_new_table()
    analyze_data()
    
