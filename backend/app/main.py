from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import product_router
import os

print("🚀 main.py arrancando")

app = FastAPI()

# Rutas
app.include_router(product_router.router, prefix="/productos", tags=["Productos"])

@app.get("/")
def root():
    return {"estado": "Servidor funcionando"}

# Archivos estáticos (imágenes, etc.)
static_dir = os.path.join(os.path.dirname(__file__), "..", "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")
