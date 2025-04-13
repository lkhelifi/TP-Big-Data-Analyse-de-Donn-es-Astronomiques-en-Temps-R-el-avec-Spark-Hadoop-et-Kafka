import json
import random
import time
from kafka import KafkaProducer

# Configuration du producteur Kafka
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Liste de types d'objets célestes
types = ['astéroïde', 'comète', 'météore', 'débris spatial']

# Fonction pour générer un objet aléatoire
def generate_space_object():
    return {
        "id": f"obj_{random.randint(10000, 99999)}",
        "timestamp": int(time.time()),
        "position": {
            "x": round(random.uniform(-500, 500), 2),
            "y": round(random.uniform(-500, 500), 2),
            "z": round(random.uniform(100, 1000), 2)
        },
        "vitesse": round(random.uniform(5, 35), 1),  # km/s
        "taille": round(random.uniform(1, 50), 1),   # mètre
        "type": random.choice(types)
    }

while True:
    obj = generate_space_object()
    print(f"[INFO] Envoi: {obj}")
    producer.send('space_date', obj)  
    time.sleep(2)  
