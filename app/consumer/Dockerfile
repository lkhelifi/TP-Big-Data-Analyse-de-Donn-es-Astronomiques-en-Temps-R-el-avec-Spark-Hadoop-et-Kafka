FROM bitnami/spark:3.5.0

USER root

RUN apt-get update && \
    apt-get install -y python3-pip curl && \
    pip install --no-cache-dir pyspark==3.5.0 py4j==0.10.9.7 requests

COPY consumer.py /app/consumer/consumer.py

CMD ["spark-submit", "--packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0", "/app/consumer/consumer.py"]
