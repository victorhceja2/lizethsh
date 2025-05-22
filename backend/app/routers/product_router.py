from fastapi import APIRouter
from app.database import get_connection
from app.schemas.product_schema import ProductoConProveedor

router = APIRouter()

@router.get("/", response_model=list[ProductoConProveedor])
def listar_productos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vw_ProductosConProveedor")
    rows = cursor.fetchall()
    conn.close()

    productos = []
    for row in rows:
        productos.append(ProductoConProveedor(
            id=row.Id,
            nombre=row.Nombre,
            descripcion=row.Descripcion,
            precio=float(row.Precio),
            talla=row.Talla,
            color=row.Color,
            imagenUrl=row.ImagenUrl,
            proveedor=row.Proveedor
        ))

    return productos