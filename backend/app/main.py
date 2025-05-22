from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.routers import product_router
import os

print("🚀 main.py arrancando")

app = FastAPI()

# ✅ CORS para que React pueda conectarse
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes limitar a "http://localhost:5173" si quieres
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Ruta estática para servir imágenes desde /static/img/
static_dir = os.path.join(os.path.dirname(__file__), 'static')
if not os.path.exists(static_dir):
    os.makedirs(os.path.join(static_dir, 'img'))  # crea static/img si no existe

app.mount("/static", StaticFiles(directory=static_dir), name="static")

# ✅ Rutas API
app.include_router(product_router.router, prefix="/productos", tags=["Productos"])

# ✅ Ruta raíz
@app.get("/")
def root():
    return {"estado": "Servidor funcionando"}