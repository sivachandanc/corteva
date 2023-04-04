import os
import time
import create_table as ct
import os

def insert_data():
    """ insert data from files into the weather_data table """
    conn = ct.create_connection()
    c = conn.cursor()
    path = "wx_data/"
    for file_name in os.listdir(path):
        if file_name.endswith(".txt"):
            with open(os.path.join(path, file_name), "r") as file:
                for line in file:
                    date, max_temp, min_temp, precipitation = line.strip().split("\t")
                    c.execute(f"INSERT INTO weather_data (date, max_temp, min_temp, precipitation) VALUES ('{date}', {max_temp}, {min_temp}, {precipitation})")
    conn.commit()
    print("Data inserted successfully!")
    conn.close()

def ingest_data():
    """ ingest the weather data from the raw text files into the database """
    start_time = time.time()
    conn = ct.create_connection()
    c = conn.cursor()
    path = "wx_data/"
    total_records = 0
    for file_name in os.listdir(path):
        # Ingesting the files in 'wx_data' folder
        if file_name.endswith(".txt"):
            with open(os.path.join(path, file_name), "r") as file:
                for line in file:
                    date, max_temp, min_temp, precipitation = line.strip().split("\t")
                    # Chekcing for Duplicates 
                    c.execute(f"SELECT COUNT(*) FROM weather_data WHERE date = '{date}' AND max_temp = {max_temp} AND min_temp = {min_temp} AND precipitation = {precipitation}")
                    result = c.fetchone()[0]
                    
                    if result == 0:
                        c.execute(f"INSERT INTO weather_data (date, max_temp, min_temp, precipitation) VALUES ('{date}', {max_temp}, {min_temp}, {precipitation})")
                        total_records += 1
    conn.commit()
    conn.close()
    end_time = time.time()
    print(f"{total_records} records ingested in {end_time - start_time} seconds")

if __name__ == '__main__':
    insert_data()
