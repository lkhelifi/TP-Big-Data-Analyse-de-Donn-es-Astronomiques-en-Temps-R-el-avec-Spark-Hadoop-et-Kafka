FROM python:3.9-slim

RUN apt-get update && apt-get install -y python3-pip curl && \
    pip install --no-cache-dir pyspark==3.5.0 py4j==0.10.9.7 requests


WORKDIR /app
COPY producer.py .

RUN pip install kafka-python

CMD ["python", "producer.py"]
