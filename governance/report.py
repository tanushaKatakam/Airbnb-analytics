import sqlite3
import pandas as pd

conn = sqlite3.connect("../sql/airbnb.db")
print("\n===== AUDIT =====")
print(pd.read_sql(
"""
SELECT *
FROM audit_log
""", conn)
)

print("\n===== METADATA =====")
print(pd.read_sql(
"""
SELECT *
FROM metadata
""", conn)
)

conn.close()