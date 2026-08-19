import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

df = pd.read_csv("data/processed/chocolate_shipments_cleaned.csv")

df["Shipdate"] = pd.to_datetime(df["Shipdate"]).dt.date

# Connect to PostgreSQL
connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

cursor = connection.cursor()

insert_query = """
    INSERT INTO shipments (
        ShipmentID,
        SPID,
        PID,
        GID,
        Shipdate,
        Amount,
        Boxes,
        Order_Status,
        Revenue_per_box,
        Profit,
        Cost_price,
        "Profit_Margin%%",
        Sales_Person,
        Team,
        Product,
        Category,
        Country,
        Region,
        Cost_per_box,
        cancelled
    )
    VALUES (
        %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s
    )
"""

for row in df.itertuples(index=False, name=None):
    cursor.execute(insert_query, row)

connection.commit()

print(f"{len(df)} rows inserted successfully!")

cursor.close()
connection.close()