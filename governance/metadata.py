import sqlite3

conn = sqlite3.connect("../sql/airbnb.db")
cur = conn.cursor()
cur.execute(
"""
CREATE TABLE IF NOT EXISTS metadata(table_name TEXT, owner TEXT, version TEXT)
"""
)

records=[("fact_listing", "analytics_team", "v1"), ("dim_host", "analytics_team", "v1"),
            ("dim_location", "analytics_team","v1"), ("dim_room", "analytics_team", "v1")]

cur.executemany(
"""
INSERT INTO metadata
VALUES(?, ?, ?)
""", records
)

conn.commit()
conn.close()
print("Metadata Created")