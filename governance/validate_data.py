import sqlite3
import pandas as pd

conn = sqlite3.connect("../sql/airbnb.db")
df = pd.read_sql(
"""
SELECT *
FROM fact_listing
""", conn
)

print("\n===== DATA VALIDATION =====")
numeric_cols = ["price", "minimum_nights", "number_of_reviews", "availability_365"]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    
print("\nNull Values")
print(df.isnull().sum())
print("\nDuplicates")
print(df.duplicated().sum())
negative = (df[df["price"] < 0])
print("\nNegative Prices")
print(len(negative))
high = (df[df["price"] > 1000])
print("\nListings > 1000")
print(len(high))
invalid = (df[df["availability_365"] < 0])
print("\nInvalid Availability")
print(len(invalid))
conn.close()