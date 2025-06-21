from flask import Blueprint, request, jsonify


productos_api = Blueprint('productos_api', __name__)

@productos_api.route("/api/productos", methods=["GET"])
def obtener_lista_productos():
    registros = listar_todos_los_productos()
    datos = [
        {
            "id": item[0],
            "codigo": item[1],
            "marca": item[2],
            "nombre": item[3],
            "precio": item[4],
            "modelo": item[5],
            "stock": item[6]
        }
        for item in registros
    ]
    return jsonify(datos)

@productos_api.route("/api/productos/<int:producto_id>", methods=["GET"])
def obtener_producto_por_id(producto_id):
    producto = obtener_producto_por_id(producto_id)
    if producto:
        datos = {
            "id": producto[0],
            "codigo": producto[1],
            "marca": producto[2],
            "nombre": producto[3],
            "precio": producto[4],
            "modelo": producto[5],
            "stock": producto[6]
        }
        return jsonify(datos)
    else:
        return jsonify({"error": "Producto no encontrado"}), 404
    
@productos_api.route("/api/productos/buscar/<string:nombre>", methods=["GET"])
def buscar_productos_por_nombre(nombre):
    registros = buscar_productos_por_nombre(nombre)
    if registros:
        datos = [
            {
                "id": item[0],
                "codigo": item[1],
                "marca": item[2],
                "nombre": item[3],
                "precio": item[4],
                "modelo": item[5],
                "stock": item[6]
            }
            for item in registros
        ]
        return jsonify(datos)
    else:
        return jsonify({"error": "No se encontraron productos"}), 404
    
@productos_api.route("/api/productos", methods=["POST"])
def crear_producto():
    data = request.get_json()
    nombre = data.get("nombre")
    precio = data.get("precio")
    descripcion = data.get("descripcion")
    
    if not nombre or not precio:
        return jsonify({"error": "Nombre y precio son requeridos"}), 400
    
    resultado = crear_producto(nombre, precio, descripcion)
    return jsonify({"message": resultado}), 201

@productos_api.route("/api/productos/<int:producto_id>", methods=["PUT"])
def actualizar_producto(producto_id):
    data = request.get_json()
    nombre = data.get("nombre")
    precio = data.get("precio")
    descripcion = data.get("descripcion")
    
    if not nombre or not precio:
        return jsonify({"error": "Nombre y precio son requeridos"}), 400
    
    resultado = actualizar_producto(producto_id, nombre, precio, descripcion)
    return jsonify({"message": resultado}), 200

@productos_api.route("/api/productos/<int:producto_id>", methods=["DELETE"])
def eliminar_producto(producto_id):
    resultado = eliminar_producto(producto_id)
    return jsonify({"message": resultado}), 200

from models import (
    listar_todos_los_productos,
    obtener_producto_por_id,
    crear_producto,
    actualizar_producto,
    eliminar_producto,
    buscar_productos_por_nombre
)
    
    
     