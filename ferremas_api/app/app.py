from flask import Flask
from routes.productos import productos_bp
import db as database

def crear_aplicacion():
    app = Flask(__name__)
    app.register_blueprint(productos_bp)
    return app

if __name__ == "__main__":
    database.crear_tabla_productos()
    servidor = crear_aplicacion()
    servidor.run(debug=True)