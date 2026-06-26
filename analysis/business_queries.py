import sqlite3
import pandas as pd

conn = sqlite3.connect("../sql/airbnb.db")
queries = {
"Average Price":"""

SELECT
AVG(price)
AS avg_price

FROM fact_listing
""",

"Top Hosts":"""
SELECT
host_id,
COUNT(*) AS listings
FROM fact_listing
GROUP BY host_id
ORDER BY listings DESC
LIMIT 10

""",

"Average Reviews":"""
SELECT
AVG(number_of_reviews)
AS avg_reviews
FROM fact_listing
""",

"Top Locations":"""

SELECT
COUNT(*) listings,
price
FROM fact_listing
GROUP BY price
ORDER BY listings DESC
LIMIT 10
"""
}

for name,query in queries.items():
    print("\n==========")
    print(name)
    print(
        pd.read_sql(query,conn)
    )

conn.close()