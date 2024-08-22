import requests
from sqlalchemy import create_engine
import pandas as pd

# Fetch data from the API
response = requests.get('http://127.0.0.1:5000/extract-data')
data = response.json()

# Convert JSON data to DataFrame
df = pd.DataFrame(data)

# Load data into SQLite (or any other database)
engine = create_engine('sqlite:///sales_data.db')
df.to_sql('sales', con=engine, if_exists='replace', index=False)

print("Data has been loaded into the database.")
