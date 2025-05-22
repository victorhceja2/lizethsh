from pydantic import BaseModel, Field

class ProductoConProveedor(BaseModel):
    id: int
    nombre: str = Field(..., description="Nombre del producto")
    descripcion: str = Field(..., description="Descripción del producto")
    precio: float = Field(..., ge=0, description="Precio en pesos mexicanos")
    talla: str = Field(..., description="Talla estándar mexicana")
    color: str = Field(..., description="Color principal del producto")
    imagenUrl: str = Field(..., description="Ruta relativa a /static/img/")
    proveedor: str = Field(..., description="Nombre del proveedor asociado")