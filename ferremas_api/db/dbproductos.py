import sqlite3

DB_PATH = "ferremas.db"

def conectar_bd():
    return sqlite3.connect(DB_PATH)

def crear_tabla_productos():
    with conectar_bd() as conexion:
        sql = """
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY,
            marca TEXT,
            nombre TEXT,
            precio REAL,
            modelo TEXT,
            stock INTEGER
        )
        """
        conexion.execute(sql)
        conexion.commit()

def crear_tabla_usuarios():
    with conectar_bd() as conexion:
        sql = """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            email TEXT UNIQUE,
            contrasena TEXT
        )
        """
        conexion.execute(sql)
        conexion.commit()

def crear_tabla_ventas():
    with conectar_bd() as conexion:
        sql = """
        CREATE TABLE IF NOT EXISTS ventas (
            id INTEGER PRIMARY KEY,
            producto_id INTEGER,
            usuario_id INTEGER,
            cantidad INTEGER,
            fecha TEXT,
            FOREIGN KEY (producto_id) REFERENCES productos(id),
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        )
        """
        conexion.execute(sql)
        conexion.commit()

def inicializar_bd():
    crear_tabla_productos()
    crear_tabla_usuarios()
    crear_tabla_ventas()
if __name__ == "__main__":
    inicializar_bd()
    print("Base de datos inicializada correctamente.")
