import os
from flask import Flask, send_from_directory
from app.app import app  # ahora sí apunta correctamente
from routes.productos import productos_api
from routes.contacto import contacto_api
from db.dbproductos import crear_tabla_productos, conectar_bd

crear_tabla_productos()

app.register_blueprint(productos_api)
app.register_blueprint(contacto_api)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_FOLDER = os.path.abspath(os.path.join(BASE_DIR, '..', 'frontend'))

if __name__ == "__main__":
    app.run(debug=True)