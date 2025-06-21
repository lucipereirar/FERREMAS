from flask import Blueprint, request, jsonify
from models.productomodel import (
    listar_todos_los_productos,
    obtener_producto_por_id,
    crear_producto,
    eliminar_producto, 
    buscar_productos_por_nombre as buscar_productos_por_nombre_model,
    actualizar_producto
    )
    

productos_api = Blueprint('productos_api', __name__)

@productos_api.route("/api/productos", methods=["GET"])
def obtener_lista_productos():
    registros = listar_todos_los_productos()
    datos = [
        {
            "id": item[0],
            "marca": item[1],
            "nombre": item[2],
            "precio": item[3],
            "modelo": item[4],
            "stock": item[5]
        }
        for item in registros
    ]
    return jsonify(datos)

@productos_api.route("/api/productos/<int:producto_id>", methods=["GET"])
def obtener_producto_por_id_route(producto_id):
    producto = obtener_producto_por_id(producto_id)
    if producto:
        datos = {
            "id": producto[0],
            "marca": producto[1],
            "nombre": producto[2],
            "precio": producto[3],
            "modelo": producto[4],
            "stock": producto[5]
        }
        return jsonify(datos)
    else:
        return jsonify({"error": "Producto no encontrado"}), 404
    
@productos_api.route("/api/productos/buscar/<string:nombre>", methods=["GET"])
def buscar_productos_por_nombre(nombre):
    registros = buscar_productos_por_nombre_model(nombre)
    if registros:
        datos = [
            {
                "id": item[0],
                "marca": item[1],
                "nombre": item[2],
                "precio": item[3],
                "modelo": item[4],
                "stock": item[5]
            }
            for item in registros
        ]
        return jsonify(datos)
    else:
        return jsonify({"error": "No se encontraron productos"}), 404
    
@productos_api.route("/api/productos", methods=["POST"])
def crear_producto_route():
    data = request.get_json()
    marca = data.get("marca")
    nombre = data.get("nombre")
    precio = data.get("precio")
    modelo = data.get("modelo")
    stock = data.get("stock")
    
    if not nombre or not precio or not modelo or stock is None:
        return jsonify({"error": "Marca, nombre, precio, modelo y stock son requeridos"}), 400
    
    resultado = crear_producto(marca, nombre, precio, modelo, stock)
    return jsonify({"message": resultado}), 201

@productos_api.route("/api/productos/<int:producto_id>", methods=["PUT"])
def actualizar_producto_route(producto_id):
    data = request.get_json()
    nombre = data.get("nombre")
    precio = data.get("precio")
    
    if not nombre or not precio:
        return jsonify({"error": "Nombre y precio son requeridos"}), 400
    
    resultado = actualizar_producto(producto_id, nombre, precio)
    return jsonify({"message": resultado}), 200

@productos_api.route("/api/productos/<int:producto_id>", methods=["DELETE"])
def eliminar_producto_route(producto_id):
    resultado = eliminar_producto(producto_id)
    return jsonify({"message": resultado}), 200