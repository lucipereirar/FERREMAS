from flask import Flask
from routes import productos_api
import db as database

def crear_aplicacion():
    app = Flask(__name__)
    app.register_blueprint(productos_api)
    return app

if __name__ == "__main__":
    database.crear_tabla_productos()
    servidor = crear_aplicacion()
    servidor.run(debug=True)