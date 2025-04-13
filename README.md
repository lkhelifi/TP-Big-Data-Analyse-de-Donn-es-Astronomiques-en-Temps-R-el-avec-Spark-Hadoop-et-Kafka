# Pipeline de détection d'objets célestes dangereux

## Description

Ce projet met en place un pipeline de traitement en temps réel qui :

- **Consomme des données** depuis Kafka 
- **Analyse les objets célestes** avec Spark Streaming 
- **Stocke les résultats** dans HDFS en format Parquet
- **Diffuse les alertes** d'objets dangereux via une API REST

---

## Lancer le projet

### 1. Cloner le repo
```bash
git clone <repo>
cd <repo>
```

### 2. Lancer tous les services
```bash
docker-compose up --build
```

---

## Services exposés

| Service     | URL                                  |
|-------------|--------------------------------------|
| Flask API   | [http://localhost:5000](http://localhost:5000) |
| Kafka       | kafka:9092 (interne uniquement)     |
| Spark UI    | [http://localhost:8080](http://localhost:8080) |
| HDFS        | Accès via la ligne de commande HDFS  |

---

## Fonctionnalités

### 1. **Consommation des données via Kafka**
   Le pipeline consomme des messages depuis le topic Kafka `space_data`.

### 2. **Traitement des données avec Spark**
   - Les données sont analysées en temps réel avec **Spark Streaming**.
   - Les objets célestes dangereux sont filtrés (taille > 10m et vitesse > 25 km/s).
   
### 3. **Stockage des objets dangereux dans HDFS**
   Les objets dangereux sont stockés dans HDFS sous le chemin `/user/spark/dangerous_objects` en format **Parquet**.
   
   **Note** : L'API est encore en développement et peut ne pas être entièrement fonctionnelle.

---

## Exemple de flux de données

1. **Kafka** reçoit des données d'objets célestes.
2. **Spark Streaming** analyse ces données en temps réel et filtre les objets dangereux.
3. Les objets filtrés sont **stockés dans HDFS** (en format Parquet).
4. Les alertes sont envoyées via l'**API Flask** et peuvent être affichées via une interface **React** (fonctionnalité à venir).

---

## Organisation des dossiers

```
.
.
├── docker-compose.yml              # Configuration des services Docker pour Kafka, Spark, et Flask
├── app/                            
│   ├── consumer/                   # Répertoire pour la consommation des messages depuis Kafka
│   │   ├── consumer.py             # Fichier responsable de la consommation des messages Kafka (données d'objets célestes)
│   │   └── Dockerfile              # Dockerfile pour le service de consommation de Kafka
│   ├── producer/                   # Répertoire pour la production des messages Kafka
│   │   ├── producer.py             # Fichier responsable de l'envoi de messages Kafka (simulation des objets célestes)
│   │   └── Dockerfile              # Dockerfile pour le service de production de Kafka
│   ├── analysis/                   # Répertoire pour le traitement Spark des objets célestes
│   └──  └── batch_analysis.py       # Code Spark pour analyser les objets célestes (filtrage des objets dangereux)        
├── space-api/                     
│   ├── space-api.py                # Serveur Flask avec les endpoints /objects et /alerts
│   ├── Dockerfile                  # Dockerfile de l'API Flask
│   └── requirements.txt            # Dépendances Python pour l'API Flask
├── space-objects/                  
│   ├── space-objects.js           # Code principal du frontend
│   └── Dockerfile                  # Dockerfile du frontend JS
└── README.md                     
     

```


---

## TODO

- Finaliser l'**API Flask** pour une meilleure gestion des objets et alertes.
- Développer l'**interface React** pour afficher les objets et alertes.

--- 

## Auteur

- **Lidia KHELIFI**
