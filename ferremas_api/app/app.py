import os
from flask import Flask, send_from_directory

# Ruta absoluta a la carpeta frontend
static_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend'))

app = Flask(__name__, static_folder=static_folder_path, static_url_path='')

# Ruta raíz para servir index.html
@app.route("/")
def home():
    print("Entró a /")
    print("Ruta index:", os.path.join(static_folder_path, "index.html"))
    return send_from_directory(static_folder_path, "index.html")

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(static_folder_path, filename)