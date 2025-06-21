from db.dbproductos import conectar_bd

def listar_todos_los_productos():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conexion.close()

    resultados = []
    for p in productos:
        producto = {
            "id": p[0],
            "marca": p[1],
            "nombre": p[2],
            "precio": p[3],
            "modelo": p[4],
            "stock": p[5]
        }
        resultados.append(producto)
    return resultados

def obtener_producto_por_id(producto_id):
    conexion = conectar_bd()
    consulta = conexion.cursor()
    consulta.execute("SELECT * FROM productos WHERE id = ?", (producto_id,))
    resultado = consulta.fetchone()
    conexion.close()
    return resultado

def crear_producto(marca, nombre, precio, modelo, stock):
    conexion = conectar_bd()
    consulta = conexion.cursor()
    consulta.execute("INSERT INTO productos (marca, nombre, precio, modelo, stock) VALUES (?, ?, ?, ?, ?)", 
                     (marca, nombre, precio, modelo, stock))
    conexion.commit()
    conexion.close()
    return "Producto creado exitosamente"

def actualizar_producto(producto_id, nombre, precio):
    conexion = conectar_bd()
    consulta = conexion.cursor()
    consulta.execute("UPDATE productos SET nombre = ?, precio = ?, WHERE id = ?", 
                     (nombre, precio, producto_id))
    conexion.commit()
    conexion.close()
    return "Producto actualizado exitosamente"

def eliminar_producto(producto_id):
    conexion = conectar_bd()
    consulta = conexion.cursor()
    consulta.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
    conexion.commit()
    conexion.close()
    return "Producto eliminado exitosamente"

def buscar_productos_por_nombre(nombre):
    conexion = conectar_bd()
    consulta = conexion.cursor()
    consulta.execute("SELECT * FROM productos WHERE nombre LIKE ?", ('%' + nombre + '%',))
    resultados = consulta.fetchall()
    conexion.close()
    return resultados
