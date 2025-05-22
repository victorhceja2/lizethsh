# 👠 Lizeth SH – Backend API

Proyecto de backend para el sistema de ventas de calzado "Lizeth SH", diseñado para gestionar productos, proveedores y pedidos. Este backend expone endpoints RESTful utilizando **FastAPI**, y se conecta a una base de datos **SQL Server**.

---

## 🚀 Tecnologías

- 🐍 Python 3.13
- ⚡ FastAPI
- 🐘 SQL Server (con PyODBC)
- 📦 Uvicorn (servidor ASGI)
- 🌐 Git + GitHub
- 🖼️ Archivos estáticos (imágenes de productos)

---

## 📂 Estructura del proyecto

```
lizethsh/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── routers/
│   │   └── schemas/
│   └── static/
│       └── img/
├── sql/             # Scripts SQL de base de datos
├── env/             # Entorno virtual (no se sube al repo)
├── requirements.txt
└── README.md
```

---

## ⚙️ Configuración del entorno

1. Clona el repositorio:

```bash
git clone https://github.com/tuusuario/lizethsh.git
cd lizethsh/backend
```

2. Crea y activa el entorno:

```bash
python3 -m venv env
source env/bin/activate
```

3. Instala dependencias:

```bash
pip install -r requirements.txt
```

4. Crea un archivo `.env` en `/backend/app` con el siguiente contenido:

```env
DB_SERVER=66.179.95.14
DB_PORT=1433
DB_NAME=LizethSH
DB_USER=sa
DB_PASSWORD=Vic1973
```

---

## ▶️ Correr el proyecto

Desde `/backend`:

```bash
uvicorn app.main:app --reload
```

Abre en tu navegador:
```
http://127.0.0.1:8000/docs
```

---

## 📦 Endpoints disponibles

- `GET /productos/` → Listar todos los productos con proveedor
- Más endpoints próximamente...

---

## ✨ Créditos

Desarrollado por: **Victor H. Ceja**  
Inspirado y gestionado por: **Cinthia y el equipo de Lizeth SH**

---

## 🧙‍♂️ Roadmap (siguiente fase)

- Módulo de pedidos
- Alta de productos desde panel
- Frontend web visual
- App móvil Flutter
- Sincronización con Shopify
