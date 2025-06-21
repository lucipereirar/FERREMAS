from app.app import app  # ahora sí apunta correctamente
from routes.productos import productos_api
from routes.contacto import contacto_api
from db.dbproductos import crear_tabla_productos, conectar_bd

crear_tabla_productos()

app.register_blueprint(productos_api)
app.register_blueprint(contacto_api)

if __name__ == "__main__":

    from db.dbproductos import conectar_bd

    def poblar_si_vacio():
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM productos")
        count = cursor.fetchone()[0]
        if count == 0:
            cursor.execute("""
                INSERT INTO productos (codigo, marca, nombre, precio, modelo, stock)
                VALUES (?, ?, ?, ?, ?, ?)
            """, ("P001", "Stanley", "Martillo", 5990, "S-21", 15))
            conexion.commit()
        conexion.close()
    poblar_si_vacio()
    app.run(debug=True)