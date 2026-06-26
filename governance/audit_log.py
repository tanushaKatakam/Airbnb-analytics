import sqlite3
from datetime import datetime

conn = sqlite3.connect("../sql/airbnb.db")
cur = conn.cursor()
cur.execute(
"""
CREATE TABLE IF NOT EXISTS audit_log(
id INTEGER PRIMARY KEY,
table_name TEXT,
rows_loaded INTEGER,
loaded_at TEXT)
"""
)

tables = ["dim_host", "dim_location", "dim_room", "fact_listing"]

for table in tables:
    rows = cur.execute(f"""
    SELECT COUNT(*)
    FROM {table}
    """
    ).fetchone()[0]
    cur.execute(
"""
INSERT INTO audit_log(table_name, rows_loaded, loaded_at)
VALUES(?, ?, ?)
""",(table, rows, str(datetime.now()))
)

conn.commit()
conn.close()
print("Audit Log Created")