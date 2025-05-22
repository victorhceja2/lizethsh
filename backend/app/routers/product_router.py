from fastapi import APIRouter, HTTPException
from app.database import get_connection
from app.schemas.product_schema import ProductoConProveedor

router = APIRouter()

@router.get("/", response_model=list[ProductoConProveedor])
def listar_productos():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM vw_ProductosConProveedor")
        rows = cursor.fetchall()
        conn.close()
    except Exception as e:
        print("❌ Error al consultar productos:", e)
        raise HTTPException(status_code=500, detail="Error al obtener productos")

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