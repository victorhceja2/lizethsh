
import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()  # Carga las variables desde el .env si existe

def get_connection():
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={os.getenv('DB_SERVER', '66.179.95.14')},{os.getenv('DB_PORT', '1433')};"
        f"DATABASE={os.getenv('DB_NAME', 'LizethSH')};"
        f"UID={os.getenv('DB_USER', 'sa')};"
        f"PWD={os.getenv('DB_PASSWORD', 'Vic1973')}"
    )
    return pyodbc.connect(conn_str)
