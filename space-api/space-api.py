from flask import Flask, jsonify
import os

app = Flask(__name__)

# Liste des objets célestes (données simulées ou issues de HDFS)
objects = [
    {"id": "obj_1", "type": "Astéroïde", "taille": 5, "vitesse": 30, "position": {"x": 0.1, "y": 0.2, "z": 0.3}},
    {"id": "obj_2", "type": "Comète", "taille": 10, "vitesse": 40, "position": {"x": 1.1, "y": 2.2, "z": 3.3}},
    {"id": "obj_3", "type": "Météorite", "taille": 3, "vitesse": 50, "position": {"x": 3.1, "y": 4.2, "z": 5.3}}
]

# Liste des objets dangereux
alerts = [
    {"id": "obj_2", "type": "Comète", "vitesse": 40, "taille": 10, "message": "Objet dangereux détecté !"}
]

# Route pour récupérer les objets célestes détectés
@app.route('/objects', methods=['GET'])
def get_objects():
    return jsonify(objects), 200

# Route pour récupérer les alertes d'objets dangereux
@app.route('/alerts', methods=['GET'])
def get_alerts():
    return jsonify(alerts), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
