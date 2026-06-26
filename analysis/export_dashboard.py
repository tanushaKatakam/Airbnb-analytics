import sqlite3
import pandas as pd


conn = sqlite3.connect(
"../sql/airbnb.db"
)


query = """
SELECT
listing_id,
price,
number_of_reviews,
availability_365
FROM fact_listing
"""

df = pd.read_sql(query,conn)

# Convert numbers
cols = [
"price",
"number_of_reviews",
"availability_365"
]

for col in cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

df = df.dropna()
df.to_csv("../dashboard/tableau_data.csv", index=False)

print("Dashboard Exported")


conn.close()