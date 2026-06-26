import sqlite3
import pandas as pd
import numpy as np
from scipy.stats import ttest_ind


conn = sqlite3.connect("../sql/airbnb.db")

df = pd.read_sql(
"""
SELECT *
FROM fact_listing
""", conn
)

df["number_of_reviews"] = pd.to_numeric(df["number_of_reviews"],errors="coerce")
df = df.dropna()
np.random.seed(42)
df["group"] = np.random.choice(["A", "B"], size=len(df))
median_reviews = (df["number_of_reviews"].median())
df["engagement"] = (df["number_of_reviews"] > median_reviews).astype(int)


control = (df[df["group"] == "A"]["engagement"])
treatment = (df[df["group"] == "B"]["engagement"])
control_rate = (control.mean() * 100)
treatment_rate = (treatment.mean() * 100)
uplift = (treatment_rate - control_rate)
t_stat, p_value = ttest_ind(control, treatment)

if p_value < 0.05:
    decision = "Significant"
else:
    decision = "Not Significant"

print("\n===== A/B TEST =====")
print(f"Control Rate: {control_rate:.2f}%")
print(f"Treatment Rate: {treatment_rate:.2f}%")
print(f"Uplift: {uplift:.2f}%")
print(f"P-value: {p_value:.4f}")
print(f"Decision: {decision}")
conn.close()