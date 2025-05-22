from pydantic import BaseModel

class Product(BaseModel):
    id: int
    nombre: str
    descripcion: str
    precio: float
    imagenUrl: str
    talla: str
    color: str
class ProductoConProveedor(BaseModel):
    id: int
    nombre: str
    descripcion: str
    precio: float
    talla: str
    color: str
    imagenUrl: str
    proveedor: str