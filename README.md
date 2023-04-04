
# Weather Data Analysis

This project provides a data model for weather data records for weather stations in Nebraska, Iowa, Illinois, Indiana, or Ohio, and performs analysis on the data to calculate the average maximum and minimum temperature, and total precipitation for each year.


## Data Model
The data model is designed using SQLite and includes one table to store the weather data records, and one table to store the analysis results. The `weather_data` table has the following schema:

| Column         | Type    | Description                                           |
|----------------|---------|-------------------------------------------------------|
| id             | INTEGER | Unique identifier for the weather data record.         |
| date           | TEXT    | Date of the weather data record (YYYYMMDD format).     |
| max_temp       | INTEGER | Maximum temperature for that day (in tenths of a degree Celsius). |
| min_temp       | INTEGER | Minimum temperature for that day (in tenths of a degree Celsius). |
| precipitation  | INTEGER | Amount of precipitation for that day (in tenths of a millimeter). |

The `analysis_results` table has the following schema:

| Column              | Type    | Description                                           |
|---------------------|---------|-------------------------------------------------------|
| id                  | INTEGER | Unique identifier for the analysis result.            |
| year                | INTEGER | Year of the analysis result.                           |
| avg_max_temp        | REAL    | Average maximum temperature for that year (in degrees Celsius). |
| avg_min_temp        | REAL    | Average minimum temperature for that year (in degrees Celsius). |
| total_precipitation | REAL    | Total accumulated precipitation for that year (in centimeters). |


## Ingestion
The `ingest_data()` function ingests the weather data from the raw text files supplied into the `weather_data` table. The function checks for duplicates by using date and max_temp and does not insert duplicate rows into the table. The function also produces log output indicating start and end times and number of records ingested.
## Data Analysis
The `analyze_data()` function analyzes the weather data and calculates the average maximum and minimum temperature, and total precipitation for each year. The function stores the results in the `analysis_results` table. The function ignores missing data when calculating these statistics. The `create_new_table()` function creates the `analysis_results table`.
## EndPoints
Since I had little experinec on creating REST API EndPoints. I have used `streamlit` to create a web app to see the analytical results.

## Usage
To use the project, first create the `weather_data` and `analysis_results` tables by running the `create_tables()` function in the `create_tables.py` file.

To ingest the `weather data` into the weather_data table, run the `ingest_data()` function in the `ingest_data.py` file.

To analyze the weather data and store the results in the `analysis_results` table, run the `analyze_data()` function in the `analyze_data.py` file.

To view the analysis results, you can run the Streamlit app by running the `streamlit run streamlit_app.py` command in your terminal. The app will display the average maximum and minimum temperature, and total precipitation for each year.
## Bonus - AWS Deployment
For the Database I would used 
1. `AWS RDS` to deploy a MySQL databse instance. 
2. I would have used `AWS lambda` to ingest files along with `s3 event notification` to trigger the AWS Lambda


## Checkout the Streamlit app

I have deployed this project on AWS EC2. Streamlit web app is running in this EC2 and you can acess the on 8501 port whihc I exposed.

To us the app go to : ``