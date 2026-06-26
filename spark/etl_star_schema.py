from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id

spark = (
    SparkSession
    .builder
    .master("local[*]")
    .appName("AirbnbAnalytics")
    .config("spark.hadoop.fs.defaultFS","file:///")
    .getOrCreate()
)

df=(
spark
.read.csv("file:///Users/tanushak/airbnb-analytics/data/AB_NYC_2019.csv", header=True, inferSchema=True)
)

df=df.dropDuplicates()
df=df.fillna({
"reviews_per_month":0
})

host=(df.select("host_id", "host_name").dropDuplicates())
location=(df.select("neighbourhood_group", "neighbourhood").dropDuplicates()
.withColumn("location_id",monotonically_increasing_id())
)

room=(df.select("room_type").dropDuplicates().withColumn(monotonically_increasing_id()))
host.write.mode("overwrite").parquet("../data/host")
location.write.mode("overwrite").parquet("../data/location")
room.write.mode("overwrite").parquet("../data/room")

print("Dimensions Created")
spark.stop()