FROM bitnami/spark:latest

USER root

RUN apt-get update && apt-get install -y python3-pip curl && \
    pip install --no-cache-dir pyspark==3.5.0 py4j==0.10.9.7 requests

ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=python3