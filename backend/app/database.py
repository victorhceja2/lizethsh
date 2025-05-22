import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    try:
        conn_str = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={os.getenv('DB_SERVER')},{os.getenv('DB_PORT')};"
            f"DATABASE={os.getenv('DB_NAME')};"
            f"UID={os.getenv('DB_USER')};"
            f"PWD={os.getenv('DB_PASSWORD')}"
        )
        connection = pyodbc.connect(conn_str)
        print("✅ Conexión a SQL Server establecida correctamente.")
        return connection
    except pyodbc.Error as e:
        print("❌ Error de conexión a SQL Server:", e)
        raise