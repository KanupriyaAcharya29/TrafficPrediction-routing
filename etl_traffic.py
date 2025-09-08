from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, avg
from pyspark.sql.types import StructType, StringType, DoubleType, LongType

spark = SparkSession.builder \
    .appName("TrafficETL") \
    .getOrCreate()

schema = StructType() \
    .add("vehicle_id", StringType()) \
    .add("lat", DoubleType()) \
    .add("lon", DoubleType()) \
    .add("speed", DoubleType()) \
    .add("timestamp", LongType())

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "traffic_data") \
    .load()

json_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Feature: average speed per minute
features = json_df.groupBy("vehicle_id").agg(avg("speed").alias("avg_speed"))

query = features.writeStream.outputMode("complete").format("console").start()
query.awaitTermination()