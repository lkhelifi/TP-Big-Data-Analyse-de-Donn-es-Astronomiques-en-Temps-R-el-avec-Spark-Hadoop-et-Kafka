from pyspark.sql import SparkSession

# Initialisation de Spark
spark = SparkSession.builder \
    .appName("BatchAnalysis") \
    .getOrCreate()

# Chargement des données depuis HDFS
batch_df = spark.read.parquet("hdfs://namenode:8020/user/spark/dangerous_objects")

# Agrégation par type d'objet céleste
aggregated_df = batch_df.groupBy("type").agg({"vitesse": "avg"})

# Afficher les 5 objets les plus rapides détectés
fastest_objects_df = aggregated_df.orderBy("avg(vitesse)", ascending=False).limit(5)

# Affichage des résultats
fastest_objects_df.show()

# Écrire les résultats dans HDFS sous un répertoire dédié
fastest_objects_df.write \
    .mode("overwrite") \
    .parquet("hdfs://namenode:8020/user/spark/fastest_objects_results")
