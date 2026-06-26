import sqlite3

conn = sqlite3.connect("../sql/airbnb.db")
cur = conn.cursor()
cur.execute(
"""
CREATE TABLE IF NOT EXISTS experiments(
id INTEGER PRIMARY KEY,
control_rate REAL,
treatment_rate REAL,
uplift REAL,
p_value REAL,
decision TEXT)
"""
)

conn.commit()
conn.close()
print("Experiment Table Created")