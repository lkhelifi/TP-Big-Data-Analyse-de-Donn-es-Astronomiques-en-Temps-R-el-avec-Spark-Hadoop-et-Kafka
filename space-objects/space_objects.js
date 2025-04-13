import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import L from 'leaflet';

function App() {
  const [objects, setObjects] = useState([]);
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    // Récupérer les objets célestes et les alertes depuis l'API
    axios.get('http://localhost:5000/objects')
      .then(response => setObjects(response.data));

    axios.get('http://localhost:5000/alerts')
      .then(response => setAlerts(response.data));
  }, []);

  return (
    <div>
      <h1>Objets Célestes</h1>
      <ul>
        {objects.map(obj => (
          <li key={obj.id}>{obj.id} - {obj.type}</li>
        ))}
      </ul>

      <h2>Alertes</h2>
      <ul>
        {alerts.map(alert => (
          <li key={alert.id}>{alert.message}</li>
        ))}
      </ul>

      <h2>Carte Interactive</h2>
      <MapContainer center={[0, 0]} zoom={2} style={{ height: "400px", width: "100%" }}>
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        {objects.map(obj => (
          <Marker key={obj.id} position={[obj.position.x, obj.position.y]}>
            <Popup>
              {obj.id} - {obj.type}
            </Popup>
          </Marker>
        ))}
      </MapContainer>
    </div>
  );
}

export default App;
