import os
from flask import Flask, send_from_directory

# Ruta absoluta a la carpeta frontend
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_FOLDER = os.path.abspath(os.path.join(BASE_DIR, '..', 'frontend'))

# Crear instancia de Flask con carpeta estática definida
app = Flask(__name__, static_folder=STATIC_FOLDER, static_url_path='')

# Ruta principal que sirve index.html
@app.route("/")
def root():
    return send_from_directory(STATIC_FOLDER, "index.html")

# Ruta para archivos estáticos (JS, CSS, etc.)
@app.route("/<path:filename>")
def serve_static(filename):
    return send_from_directory(STATIC_FOLDER, filename)