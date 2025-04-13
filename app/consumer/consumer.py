from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, FloatType, LongType, StructField

# Initialisation de SparkSession
spark = SparkSession.builder \
    .appName("KafkaSparkConsumer") \
    .getOrCreate()

# Schéma de l'objet envoyé
schema = StructType([
    StructField("id", StringType()),
    StructField("timestamp", LongType()),
    StructField("position", StructType([
        StructField("x", FloatType()),
        StructField("y", FloatType()),
        StructField("z", FloatType())
    ])),
    StructField("vitesse", FloatType()),
    StructField("taille", FloatType()),
    StructField("type", StringType())
])

# Lecture des données depuis Kafka
df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "space_data") \
    .load()

# Parsing du message JSON
parsed_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Filtrer les objets dangereux
dangerous_objects_df = parsed_df.filter((col("taille") > 10) & (col("vitesse") > 25))

# Stockage des objets dangereux dans HDFS 
dangerous_objects_df.writeStream \
    .outputMode("append") \
    .format("parquet") \
    .option("path", "hdfs://namenode:8020/user/spark/dangerous_objects") \
    .option("checkpointLocation", "hdfs://namenode:8020/user/spark/checkpoints/dangerous_objects") \
    .start()

dangerous_objects_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

# Attendre que le flux se termine
dangerous_objects_df.awaitTermination()
