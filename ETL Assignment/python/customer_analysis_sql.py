import sqlite3
import csv
import yaml
from pathlib import Path

current_dir = Path(__file__).parent
sql_file_path = current_dir.parent/'config'/'sql_queries.yaml'

# Load SQL queries from YAML file
with open(sql_file_path, 'r') as file:
    config = yaml.safe_load(file)

# Get the SQL query from the configuration
query = config['queries']['get_customer_purchases']

# Connect to the SQLite3 databases
sqliteConnection = sqlite3.connect(current_dir.parent/'databases'/"S30 ETL Assignment.db")
cursor = sqliteConnection.cursor()

# Execute the query from the YAML configuration
data = cursor.execute(query)
results = cursor.fetchall()

# Write results to a CSV file with semicolon delimiter
with open(current_dir.parent/'output_file'/'output_sql.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(['Customer', 'Age', 'Item', 'Quantity'])  # Header
    for row in results:
        writer.writerow(row)

# Close the databases connection
sqliteConnection.close()
