import React, { useEffect, useState } from 'react';
import './App.css';
import { fetchProductos } from './api';

function App() {
  const [productos, setProductos] = useState([]);

  useEffect(() => {
    fetchProductos().then(data => {
      console.log("🧪 JSON recibido:", data);
      setProductos(data);
    });
  }, []);

  return (
    <div className="catalogo">
      <h1>Catálogo</h1>
      <div className="grid">
        {productos.map(p => (
          <div key={p.id} className="card">
            <img src={`http://127.0.0.1:8000${p.imagenUrl}`} alt={p.nombre} />
            <h2>{p.nombre}</h2>
            <p>${p.precio}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
