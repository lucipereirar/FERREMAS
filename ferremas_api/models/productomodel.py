from db.db import conectar_bd

def listar_todos_los_productos():
    conexion = conectar_bd()
    consulta = conexion.cursor()
    consulta.execute("SELECT * FROM productos")
    resultados = consulta.fetchall()
    conexion.close()
    return resultados

def obtener_producto_por_id(producto_id):
    conexion = conectar_bd()
    consulta = conexion.cursor()
    consulta.execute("SELECT * FROM productos WHERE id = ?", (producto_id,))
    resultado = consulta.fetchone()
    conexion.close()
    return resultado

def crear_producto(nombre, precio, descripcion):
    conexion = conectar_bd()
    consulta = conexion.cursor()
    consulta.execute("INSERT INTO productos (nombre, precio, descripcion) VALUES (?, ?, ?)", 
                     (nombre, precio, descripcion))
    conexion.commit()
    conexion.close()
    return "Producto creado exitosamente"

def actualizar_producto(producto_id, nombre, precio, descripcion):
    conexion = conectar_bd()
    consulta = conexion.cursor()
    consulta.execute("UPDATE productos SET nombre = ?, precio = ?, descripcion = ? WHERE id = ?", 
                     (nombre, precio, descripcion, producto_id))
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

