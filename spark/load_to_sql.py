from pyspark.sql import SparkSession
import sqlite3

spark = (
    SparkSession
    .builder
    .master("local[*]")
    .appName("LoadWarehouse")
    .config("spark.hadoop.fs.defaultFS","file:///")
    .getOrCreate()
)

df = (spark.read.csv("file:///Users/tanushak/airbnb-analytics/data/AB_NYC_2019.csv", header=True, inferSchema=True))

conn = sqlite3.connect("../sql/airbnb.db")

# ---------- DIM HOST ----------

host = (df.select("host_id", "host_name").dropDuplicates())
host_pd = (host.toPandas())
host_pd.to_sql("dim_host", conn, if_exists="replace", index=False)

# ---------- DIM LOCATION ----------

location = (df.select("neighbourhood_group", "neighbourhood").dropDuplicates())
location_pd = (location.toPandas())
location_pd.insert(0, "location_id",range(1,len(location_pd)+1))
location_pd.to_sql("dim_location", conn, if_exists="replace", index=False)

# ---------- DIM ROOM ----------

room = (df.select("room_type").dropDuplicates())
room_pd = (room.toPandas())
room_pd.insert(0, "room_id",range(1,len(room_pd)+1))
room_pd.to_sql("dim_room", conn, if_exists="replace", index=False)

# ---------- FACT ----------

fact = (df[
["id", "host_id", "price", "minimum_nights", "number_of_reviews", "availability_365"]]
)

fact_pd = (fact.toPandas())
fact_pd.columns = ["listing_id","host_id","price","minimum_nights","number_of_reviews",
                    "availability_365"]

fact_pd.to_sql("fact_listing", conn, if_exists = "replace", index=False)
conn.close()
spark.stop()
print("Warehouse Loaded")